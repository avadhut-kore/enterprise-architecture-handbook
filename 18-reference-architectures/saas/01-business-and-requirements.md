# Business Architecture & Requirements: B2B SaaS Platform

## 1. The Multi-Tenancy Spectrum & Personas
- **Tenant Administrator**: Requires SAML/Okta SSO integration, automated employee onboarding via SCIM, and role-based access management.
- **Tenant Business User**: Requires sub-second response times and continuous availability unaffected by other tenants' heavy workloads.
- **SaaS Platform Operator**: Needs high infrastructure density, low cost-per-tenant, and rapid automated tenant provisioning.

---

## 2. Scale Model & Capacity Assumptions

| Scale Parameter | Growth Stage | Enterprise Scale |
| :--- | :--- | :--- |
| **Total Active Tenants** | 500 organizations | 10,000 organizations |
| **Active User Seats** | 50,000 seats | 1,500,000 seats |
| **Peak Inbound API QPS** | 800 req/sec | 25,000 req/sec |
| **Average DB Storage / Tenant**| 2 GB / tenant | 15 GB / tenant |
| **Total Multi-Tenant Storage** | 1 TB | 150 TB |
