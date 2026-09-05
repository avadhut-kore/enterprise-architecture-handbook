# Reference Architecture 05: Enterprise B2B Multi-Tenant SaaS Observability

## 1. System Context & Overview
Multi-tenant enterprise SaaS applications host thousands of corporate clients on shared infrastructure. Platform engineers require deep visibility to detect **"noisy neighbors"** (a single customer exhausting database pools or CPU quotas) and calculate exact **FinOps Cost-to-Serve per tenant**.

---

## 2. Architecture Diagram

```mermaid
flowchart LR
    User["Tenant Requests\n(Tenant: Acme Corp)"] --> Gateway["API Gateway / Edge Router"]
    
    Gateway -->|Inject Attribute:\ntenant_id=acme_corp| App["Application Workloads"]
    
    subgraph Telemetry_Extraction ["Tenant-Aware Telemetry Pipeline"]
        App -->|Spans tagged with tenant_id| OTel["OTel Collector (Tenant Processor)"]
        OTel --> Splitter{"Routing Engine"}
        
        Splitter -->|Aggregation| Metrics["Tenant-Segmented Metrics\n- QPS by Tenant\n- Error Rate by Tenant\n- CPU/Memory Cost Attribution"]
        Splitter -->|Trace Isolation| Traces["Tenant Tracing (RBAC Isolated)"]
    end

    subgraph FinOps_Engine ["FinOps & SRE Governance"]
        Metrics --> Noisy["Noisy Neighbor Alert Engine"]
        Metrics --> Billing["Per-Tenant Cost Accounting Engine"]
    end
```

---

## 3. Key Architectural Decisions
1. **Cardinality Boundary**: `tenant_id` is emitted on distributed traces and low-volume billing metrics, but **strictly excluded** from high-frequency system metrics to prevent metric cardinality explosions.
2. **Automated Noisy-Neighbor Mitigation**: When a specific `tenant_id` consumes more than 40% of the database connection pool, the alerting engine automatically triggers API rate-limiting against that tenant's API keys.
3. **Tenant RBAC Isolation**: Multi-tenant trace stores enforce tenant-based access control, ensuring enterprise customers viewing embedded dashboards can never see trace data from other organizations.
