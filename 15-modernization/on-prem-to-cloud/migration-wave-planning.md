# Migration Wave Planning & Scheduling

## 1. Wave Design Methodology
1. **Wave 0 (Pilot)**: Low-criticality internal tool or stateless dev/test environment. Validates network connectivity, deployment pipelines, and operational readiness.
2. **Wave 1 (Edge Applications)**: Web frontends and stateless microservices with low database coupling.
3. **Wave 2 (Line-of-Business)**: Core departmental applications and associated database read-replicas.
4. **Wave 3 (Mission-Critical Core)**: Primary OLTP databases, payment backends, and ERP integrations.
5. **Wave 4 (Legacy Long-Tail / Decommission)**: Decommissioned archives and cold data vaults.
