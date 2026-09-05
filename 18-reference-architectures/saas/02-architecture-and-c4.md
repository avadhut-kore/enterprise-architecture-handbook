# C4 Architecture Model & Cloud Mapping: B2B SaaS Platform

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Multi-Tenant Enterprise B2B SaaS Platform
Person(tenant_user, "Tenant Employee", "Uses SaaS web application")
Person(tenant_admin, "Tenant Admin", "Configures SSO and manages seat licenses")
System(saas_platform, "B2B SaaS Platform", "Multi-tenant business software with automated billing and isolation")
System_Ext(tenant_idp, "Customer Corporate IdP", "Okta / Azure AD / Ping via SAML 2.0 / OIDC")
System_Ext(billing_engine, "Subscription Billing", "Stripe Billing / Metronome for usage metering")

Rel(tenant_user, saas_platform, "Interacts with SaaS features", "HTTPS")
Rel(tenant_admin, saas_platform, "Configures SAML SSO & SCIM", "HTTPS")
Rel(saas_platform, tenant_idp, "Authenticates via enterprise federated SSO", "SAML 2.0 / OIDC")
Rel(saas_platform, billing_engine, "Reports monthly active seats & API usage", "REST")
```

---

## 2. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **Tenant Context Gateway**| Envoy Proxy with WASM | AWS API Gateway / Envoy | Azure API Management | Apigee Edge |
| **Pooled Relational DB** | PostgreSQL with RLS | Amazon Aurora PostgreSQL | Azure Database for PostgreSQL | Cloud SQL for PostgreSQL |
| **Silo Enterprise DB** | Isolated RDS Instances | AWS RDS PostgreSQL Silos | Azure SQL Dedicated Instances| Cloud SQL Dedicated Instances |
| **Tenant Secret Store** | HashiCorp Vault | AWS Secrets Manager / KMS | Azure Key Vault | Google Cloud Secret Manager |
