# Tenant Migration & Resharding

## 1. Migrating a Growing Tenant to Dedicated Hardware
When a startup tenant expands into a Fortune 500 enterprise, it must be migrated from a shared multi-tenant database to a dedicated database cluster without downtime.

```mermaid
flowchart TD
    Shared[(Shared DB)] -->|1. Initial Snapshot Copy| Dedicated[(Dedicated DB)]
    Shared == 2. Change Data Capture (CDC) Continuous Sync ==> Dedicated
    App[App Gateway] -->|3. 50ms Cutover: Route Tenant to Dedicated| Dedicated
```
