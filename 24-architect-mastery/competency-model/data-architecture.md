# Competency Deep Dive: Data Architecture & Persistence

> **"Code is temporary; data is permanent. Systems will be rewritten 5 times, but their underlying data models and storage paradigms will outlast every framework and programming language."**

---

## 1. Definition & Core Essence

**Data Architecture & Persistence** is the discipline of structuring, storing, processing, and governing data across its entire corporate lifecycle. It encompasses:
* Polyglot persistence: Relational (PostgreSQL), Document (MongoDB), Key-Value (DynamoDB/Redis), Wide-Column (Cassandra), and Search (Elasticsearch/OpenSearch).
* Analytical architectures: Data Warehouses (Snowflake, BigQuery), Data Lakes (S3/Parquet), and Lakehouse open table formats (Apache Iceberg, Delta Lake).
* Streaming & data integration: Change Data Capture (CDC via Debezium), ETL/ELT pipelines, and stream processing (Flink, Spark).
* Data governance & strategy: Data Mesh (domain-owned data products), Master Data Management (MDM), data lineage, and data cataloging.

---

## 2. Why It Matters for Modern Architects

* **Solution Architects**: Prevents selecting inappropriate database engines (e.g., using NoSQL for complex relational joins or Relational for petabyte-scale append logs).
* **Technical Architects**: Governs the enterprise analytical data backbone, CDC replication pipelines, and centralized vector/search indexing infrastructure.
* **Enterprise Architects**: Shapes corporate Data Mesh strategy, global data governance, master data integration, and compliance with data residency laws (GDPR/CCPA).

---

## 3. 5-Tier Behavioral Capability Progression

| Level | Behavioral Capability Anchor |
| :--- | :--- |
| **L1 (Practitioner)** | Writes standard SQL queries, joins, and basic CRUD database interactions. |
| **L2 (Independent)** | Designs normalized database schemas; creates composite and partial indexes; tunes connection pools; resolves lock contention. |
| **L3 (Advanced)** | Selects polyglot persistence based on access patterns; designs CQRS read models and cache invalidation strategies; handles data sharding and partitioning. |
| **L4 (Architect)** | Architects enterprise Lakehouses (Apache Iceberg, Delta Lake); designs real-time CDC replication backbones (Debezium); implements hybrid vector search (Lucene BM25 + HNSW). |
| **L5 (Strategic)** | Formulates corporate Data Mesh strategy; establishes global data governance frameworks; designs multi-region data sovereignty architecture and master data management. |

---

## 4. Practical Experiences & Apprenticeship Exercises

1. **Design a CQRS Data Pipeline with CDC**: Architect an event-driven data pipeline capturing PostgreSQL row mutations via Debezium CDC and streaming them into OpenSearch for full-text search and Snowflake for analytics.
2. **Benchmark Open Table Formats**: Conduct an experiment in [`99-experiments/`](../../99-experiments/) testing Apache Iceberg vs Delta Lake compaction, partitioning, and query performance over 100M rows.
3. **Resolve Write Lock Contention**: Diagnose an incident involving row lock contention on an order counter table; refactor using optimistic concurrency or distributed counter sharding.

---

## 5. Objective Evidence of Capability (What to Inspect in Git)

- [ ] Complete Data Architecture Document detailing Entity Relationship Diagrams (ERD), polyglot data choices, and data flow topologies.
- [ ] Documented ADR justifying the selection of a specific persistence engine over competing alternatives.
- [ ] Database migration and zero-downtime rollback runbook for a high-traffic production table.

---

## 6. Common Cognitive Gaps & Blind Spots

* **Query Pattern Blindness in NoSQL**: Adopting DynamoDB or Cassandra before fully defining all read query access patterns, resulting in unscalable full-table scans.
* **Dual-Write Data Desynchronization**: Updating a database and pushing to a cache/search index in separate uncoordinated application code blocks without CDC or Outbox guarantees.
* **Over-Normalization in Analytical Systems**: Attempting to run real-time analytical reporting directly against a highly normalized 3NF transactional OLTP database.

---

## 7. Authoritative Repository Links

* Data Architecture Core: [`06-data/`](../../06-data/README.md)
* Multi-Tier Caching: [`06-data/caching/`](../../06-data/caching/README.md)
* Modern Lakehouse Architecture: [`06-data/data-lakes/`](../../06-data/data-lakes/README.md)
* Search & Vector Indexing: [`06-data/search/`](../../06-data/search/README.md)
* Data Governance: [`06-data/data-governance/`](../../06-data/data-governance/README.md)

---

## 8. Diagnostic Assessment Questions

1. *Why is Apache Iceberg increasingly preferred over raw Parquet files in modern enterprise data lakehouse architectures?*
2. *How do you solve the dual-write problem when updating a primary database and updating a search index or cache?*
3. *What are the trade-offs between schema-on-write (Relational) and schema-on-read (Data Lake) for an evolving business domain?*
