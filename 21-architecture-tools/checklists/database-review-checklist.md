# Database Architecture & Review Checklist

Audit database schemas, queries, connection management, and replication topologies before deploying persistence layers to production.

---

## 1. Schema & Data Modeling
* [ ] **Primary Key Strategy**: Are primary keys standard UUIDv7 (time-ordered) or BIGSERIAL? Are random UUIDv4 avoided on clustered indexes to prevent page fragmentation?
* [ ] **Foreign Key Constraints**: Are integrity constraints defined, and are foreign key columns explicitly indexed to avoid full-table locks during cascades?
* [ ] **Data Types Rightsized**: Are data types appropriately sized (`VARCHAR(64)` vs. unbounded `TEXT`, `NUMERIC` for financial balances rather than `FLOAT/DOUBLE`)?
* [ ] **Audit Columns**: Do all mutable tables have `created_at`, `updated_at`, and `version` columns for optimistic concurrency locking?

---

## 2. Indexing & Query Performance
* [ ] **Explain Plan Verified**: Have all critical queries been validated with `EXPLAIN (ANALYZE, BUFFERS)` to confirm index seeks instead of sequential scans?
* [ ] **No Over-Indexing**: Are write-heavy tables protected from excessive indexes (each index adds overhead on `INSERT/UPDATE`)?
* [ ] **Partial & Composite Indexes**: Are composite indexes ordered with equality columns first, followed by range/sort columns?
* [ ] **N+1 Query Prevention**: Are ORMs (EF Core, Hibernate, SQLAlchemy) configured with explicit eager loading or query batching to eliminate N+1 roundtrips?

---

## 3. Connection Management & Pooling
* [ ] **Connection Pooling (PgBouncer/HikariCP)**: Is connection pooling strictly sized to `2 * CPU_cores + effective_spindle_count` rather than allowing thousands of idle connections?
* [ ] **Statement Timeouts**: Is a global `statement_timeout` (e.g., 5,000ms) enforced to terminate runaway queries before they saturate database CPU?
* [ ] **Idle Connection Cleanup**: Are idle connections evicted within 60 seconds to prevent connection leaks?

---

## 4. High Availability & Disaster Recovery
* [ ] **Multi-AZ Replication**: Is the database configured with synchronous or semi-synchronous replication across at least two Availability Zones?
* [ ] **Automated Failover Tested**: Has automatic master failover (via Patroni, Aurora Multi-AZ, or Cloud SQL HA) been chaos-tested under load?
* [ ] **WAL Archiving & PITR**: Are transaction write-ahead logs (WAL) continuously streamed to S3/GCS with Point-In-Time-Recovery tested within the last 30 days?
* [ ] **Read Replicas Configured**: Are analytical queries, BI tools, and heavy read workloads routed to dedicated read replicas?

---

## 5. Security & Access Control
* [ ] **Encrypted at Rest**: Is storage encrypted with customer-managed keys (CMK) via AWS KMS or Azure Key Vault?
* [ ] **Dynamic Credentials**: Do application services authenticate using ephemeral, short-lived database credentials provisioned via HashiCorp Vault?
* [ ] **Network Isolation**: Is the database deployed in private, isolated subnets with zero public IP routing?
