# SAD-SAAS-001: Enterprise Multi-Tenant Platform Architecture
* **Tenant Isolation**: Shared compute with PostgreSQL row-level security (RLS) enforcing `tenant_id` on all queries.
