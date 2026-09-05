# 06-DATA-DESIGN: Enterprise Data Architecture & Storage Design

## 1. Overview & Purpose
This directory provides production standards, master templates, and audit checklists for designing enterprise data storage, database schemas, access tiers, and lifecycle governance across relational (RDBMS), distributed SQL, NoSQL, and analytical data systems.

Data is the single most durable asset in the enterprise. Applications, frameworks, and cloud providers will be replaced multiple times while underlying data records must persist with mathematical integrity, regulatory auditability, and Zero Trust encryption.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Enterprise Data Design template.
* **Modeling & Storage Architecture**:
  - [logical-data-model.md](logical-data-model.md) — Conceptual and logical domain entities.
  - [physical-data-model.md](physical-data-model.md) — DDL schemas, datatypes, and constraints.
  - [entity-design.md](entity-design.md) — Aggregate roots and entity relationships.
  - [schema-design.md](schema-design.md) — Normalization (3NF) vs denormalization patterns.
* **Access, Indexing & Scaling**:
  - [data-access.md](data-access.md) — Read/write patterns, connection pooling, and ORM guidelines.
  - [indexing.md](indexing.md) — B-Tree, GIN, BRIN, and composite index optimization.
  - [partitioning.md](partitioning.md) — Horizontal sharding, range, hash, and list partitioning.
  - [caching.md](caching.md) — Redis caching tiers, cache-aside, and write-through patterns.
  - [consistency.md](consistency.md) — ACID vs BASE, isolation levels, and eventual consistency.
* **Governance, Privacy & Lifecycle**:
  - [data-retention.md](data-retention.md) — Legal hold policies and time-based retention schedules.
  - [archival.md](archival.md) — Cold storage tiering (S3 Glacier) and automated pruning.
  - [encryption.md](encryption.md) — Transparent Data Encryption (TDE) and column-level crypto.
  - [pii.md](pii.md) — Personally Identifiable Information (PII) redaction and tokenization.
  - [data-quality.md](data-quality.md) — Great Expectations checks and schema drift alerts.
  - [lineage.md](lineage.md) — OpenLineage metadata standards and cataloging.
  - [migration.md](migration.md) — Zero-downtime schema migrations (Flyway / Liquibase).
  - [reconciliation.md](reconciliation.md) — Nightly ledger balancing and discrepancy resolution.
* **Governance**:
  - [review-checklist.md](review-checklist.md) — 25-Point Data Architecture Review Checklist.
  - [examples/ledger-data-design.md](examples/ledger-data-design.md) — Financial Double-Entry Ledger Data Design.
