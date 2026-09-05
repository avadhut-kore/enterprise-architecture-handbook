# Database Modernization & Schema Splitting Playbook

## 1. Overview
Database modernization is the most perilous frontier of enterprise architecture. While stateless application containers can be replaced in seconds, databases represent state, transactional history, and legal compliance. 

This playbook provides actionable patterns for decomposing monolithic shared databases, breaking cross-schema dependencies, achieving zero-downtime data migration, and guaranteeing data integrity.

## 2. Directory Structure
- [shared-database-problems.md](shared-database-problems.md): The structural perils of shared enterprise databases.
- [schema-splitting-playbook.md](schema-splitting-playbook.md): The 15-stage database schema splitting playbook.
- [database-per-service-vs-schema.md](database-per-service-vs-schema.md): Physical database splitting vs. logical schema isolation.
- [foreign-keys-and-stored-procedures.md](foreign-keys-and-stored-procedures.md): Decoupling cross-domain foreign keys, triggers, and procedures.
- [cdc-and-synchronization.md](cdc-and-synchronization.md): Log-based Change Data Capture (Debezium / GoldenGate) synchronization.
- [dual-writes-vs-transactional-outbox.md](dual-writes-vs-transactional-outbox.md): Why dual-writes fail and outbox pattern implementation.
- [dual-reads-and-shadow-validation.md](dual-reads-and-shadow-validation.md): Shadow verification of query equivalence before write cutover.
- [data-backfill-and-historical-hydration.md](data-backfill-and-historical-hydration.md): High-volume zero-downtime historical backfills.
- [reporting-and-bi-decoupling.md](reporting-and-bi-decoupling.md): Decoupling ad-hoc queries, ETL, and analytical data warehouses.
- [reconciliation-and-drift-repair.md](reconciliation-and-drift-repair.md): Automated data parity verification and drift repair.
- [database-rollback-and-forward-fix.md](database-rollback-and-forward-fix.md): Managing rollbacks when database rollback is non-trivial.
