# CDC Architecture: CDC for Search Indexing (Elasticsearch) & Cache Invalidation

## 1. Architectural Purpose & Problem Context
Asynchronous search index synchronization and distributed cache eviction driven by database mutations with sub-second propagation latency.

---

## 2. Structural Architecture & Pipeline Topology

```mermaid
flowchart LR
    App[Application Writes] --> DB[(Primary Database: PostgreSQL/MySQL)]
    DB -->|Write-Ahead Log WAL| Engine[Log-Based CDC Engine: Debezium]
    Engine -->|Publish Mutation Events| Kafka[(Kafka Topic: Partitioned by PK)]
    Kafka --> Cache[Cache Invalidator]
    Kafka --> Search[Search Index Sync: OpenSearch]
    Kafka --> Lake[Lakehouse Ingestion: Apache Iceberg]
```

---

## 3. Production Invariants
- Never use application dual-writes to sync databases and caches/search; always use log-based CDC or transactional outbox.
- Key CDC events strictly by primary key to ensure mutations for the same entity arrive on the same Kafka partition in order.
- Retain database transaction logs (WAL) long enough to survive connector outages without triggering full snapshot re-reads.
