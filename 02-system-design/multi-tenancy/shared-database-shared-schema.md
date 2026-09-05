# Shared Database, Shared Schema Architecture

## 1. Principles & Row-Level Security (RLS)
All tenants share the identical database tables. Every table includes a `tenant_id` column:
```sql
CREATE TABLE orders (
    tenant_id   UUID NOT NULL,
    order_id    UUID NOT NULL,
    total       DECIMAL(12,2),
    PRIMARY KEY (tenant_id, order_id)
);
```

---

## 2. PostgreSQL Row-Level Security (RLS) Defense
To prevent cross-tenant data leaks caused by application developer bugs (forgetting `WHERE tenant_id = ?` in SQL):
```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON orders
    FOR ALL
    USING (tenant_id = CURRENT_SETTING('app.current_tenant_id')::UUID);
```
* The database engine automatically enforces the filter at the kernel level for every single query!
