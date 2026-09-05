# Enterprise Multi-Tenant B2B SaaS Architecture

This reference architecture models a modern, highly scalable multi-tenant B2B SaaS application supporting hybrid tenant isolation models (Pooled vs Siloed), dynamic database routing, custom tenant domain branding, and tenant quota metering.

## 1. Business Context & Architectural Drivers
* **Isolation Models**: Support Free/Standard tiers on cost-efficient shared pooled infrastructure while offering Enterprise tiers dedicated isolated databases (Silo).
* **Tenant Noisy-Neighbor Mitigation**: Hard rate-limiting and compute throttling per tenant to ensure no single tenant degrades global platform performance.
* **Custom Domains**: Dynamic SSL certificate provisioning and routing for enterprise customer vanity domains (e.g., `app.customer.com`).

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph EnterpriseTenants ["B2B SaaS Customers"]
        StdTenant["Standard Tier Customer<br/>[Company A - 50 Seats]"]
        EntTenant["Enterprise Tier Customer<br/>[Company B - 5,000 Seats]"]
    end

    subgraph SaaSPlatformCore ["Cloud B2B SaaS Platform"]
        CoreApp["Enterprise SaaS Application<br/>- Multi-Tenant Identity & RBAC<br/>- Dynamic Tenant Context Routing<br/>- Business Workflows & Reporting<br/>- Metering & Usage Billing Engine"]
    end

    subgraph ExternalIntegrations ["Platform Integrations"]
        StripeBilling["Stripe Billing & Subscriptions"]
        CustomerIdP["Enterprise Customer IdP (Okta / Entra ID)"]
    end

    StdTenant -->|"Accesses app via shared domain"| CoreApp
    EntTenant -->|"Accesses app via vanity domain"| CoreApp
    CoreApp <-->|"Federated SAML / OIDC SSO"| CustomerIdP
    CoreApp -->|"Usage metering & credit card charges"| StripeBilling
```

## 3. C4 Level 2: Hybrid Tenant Isolation Topology (Pool vs Silo)

```mermaid
graph TD
    subgraph TenantIngress ["Dynamic Tenant Ingress Layer"]
        CustomDNS["Cloudflare SSL for SaaS (Custom Domains)"]
        IngressProxy["Tenant Routing Reverse Proxy (Envoy / OpenResty)<br/>[Extracts Tenant ID from Hostname / JWT]"]
        CustomDNS --> IngressProxy
    end

    subgraph StatelessCompute ["Pooled Application Services (Shared EKS Cluster)"]
        AppPod1["saas-core-app Pod 1 (Tenant Context Interceptor)"]
        AppPod2["saas-core-app Pod 2 (Tenant Context Interceptor)"]
        DynamicPool["Dynamic Database Connection Router (HikariCP)"]
        
        IngressProxy --> AppPod1
        IngressProxy --> AppPod2
        AppPod1 --> DynamicPool
        AppPod2 --> DynamicPool
    end

    subgraph StorageIsolationTiers ["Multi-Tenant Storage Architectures"]
        subgraph PooledTier ["Tier 1: Shared Pooled Database (Standard Tier)"]
            SharedDB[("PostgreSQL Multi-Tenant DB<br/>[Row-Level Security: tenant_id]")]
        end

        subgraph SiloedTier ["Tier 2: Dedicated Siloed Database (Enterprise Tier)"]
            EnterpriseDB[("Enterprise Customer Dedicated DB<br/>[Isolated Aurora Cluster - Customer Managed KMS]")]
        end

        DynamicPool -->|"Tenant A (Standard)"| SharedDB
        DynamicPool -->|"Tenant B (Enterprise)"| EnterpriseDB
    end
```

## 4. Tenant Request Lifecycle & Dynamic Routing Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Enterprise Employee
    participant Proxy as Ingress Proxy
    participant App as SaaS Core Application
    participant Router as Dynamic DB Router
    participant SiloDB as Dedicated Enterprise DB
    participant Meter as Usage Metering Engine

    User->>Proxy: GET https://acme.saasplatform.com/api/v1/projects
    Proxy->>Proxy: Lookup Hostname -> Tenant ID = "ten_acme_99"
    Proxy->>App: Forward with Header: X-Tenant-ID: ten_acme_99
    
    App->>App: Interceptor establishes TenantSecurityContext in ThreadLocal
    App->>Router: Request Database Connection for "ten_acme_99"
    Router->>Router: Query Tenant Registry: Type = SILOED
    Router-->>App: Return Dedicated Connection Pool (Aurora DB-Acme)
    
    App->>SiloDB: SELECT * FROM projects (Zero cross-tenant leakage risk)
    SiloDB-->>App: Return Project Records
    App->>Meter: Increment Monthly API Call Counter (+1)
    App-->>User: 200 OK (JSON Payload)
```

## 5. Architectural Decisions
* **PostgreSQL Row-Level Security (RLS)**: In pooled tiers, RLS policies enforce `WHERE tenant_id = current_setting('app.current_tenant_id')` on every table to prevent coding errors from leaking data.
* **Tenant-Aware Rate Limiting**: Redis Token Bucket rate limiters keyed by `tenant_id` guarantee that an aggressive script from Tenant A cannot exhaust API Gateway capacity for Tenant B.
