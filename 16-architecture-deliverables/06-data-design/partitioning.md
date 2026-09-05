# Data Partitioning & Sharding Standards

## 1. Partitioning Strategies
* **Range Partitioning**: Time-series and transactional ledger data partitioned by month (`created_at`).
* **Hash Partitioning**: High-cardinality multitenant data partitioned by `tenant_id`.
