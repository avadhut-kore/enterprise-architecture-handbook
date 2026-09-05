# Data Architecture: Silo vs. Pool vs. Bridge Models

## 1. Tenancy Model Comparison

| Tenancy Model | Data Isolation | Cost Per Tenant | Operational Complexity | Target Tenant Tier |
| :--- | :--- | :--- | :--- | :--- |
| **Pooled (Shared DB + RLS)**| Logical (Row-Level Security) | Very Low | Low | Free / Starter / Pro |
| **Bridge (Shared Engine, Schema per Tenant)**| Medium (Schema Isolation) | Medium | Moderate | Business Tier |
| **Silo (Dedicated DB Instance)**| Physical Hardware Isolation | High | High | Enterprise Tier ($100k+/yr) |

---

## 2. PostgreSQL Row-Level Security (RLS) Implementation
```sql
-- Enable RLS on core domain table
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Create Tenant Isolation Policy
CREATE POLICY tenant_isolation_policy ON documents
    AS RESTRICTIVE
    USING (tenant_id = current_setting('app.current_tenant_id', true));

-- Application sets session variable upon connection checkout:
-- SET LOCAL app.current_tenant_id = 'tenant_acme_corp';
```
