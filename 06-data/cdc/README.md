# Change Data Capture (CDC) Architecture

Change Data Capture (CDC) is an architectural pattern that detects, captures, and streams row-level state mutations (INSERT, UPDATE, DELETE) from databases in real-time without introducing application dual-write hazards.

---

## Architectural Index
- [Log-Based Change Data Capture](log-based-cdc.md)
- [Trigger-Based CDC Architecture](trigger-based-cdc.md)
- [Query-Based (Polling) CDC Architecture](query-based-cdc.md)
- [Database Transaction Log Mining](database-log-mining.md)
- [CDC Pipelines with Debezium](cdc-pipelines-debezium.md)
- [CDC to Kafka Event Streaming](cdc-to-kafka.md)
- [CDC to Analytical Data Lakehouse](cdc-to-data-lakehouse.md)
- [CDC to Search Indexes & Cache Invalidation](cdc-to-search-and-cache.md)
- [CDC Event Ordering & Consistency](cdc-event-ordering-and-consistency.md)
- [CDC Schema Evolution Governance](cdc-schema-evolution.md)
- [CDC Failure Recovery, Snapshots & Replay](cdc-failure-recovery-and-replay.md)
