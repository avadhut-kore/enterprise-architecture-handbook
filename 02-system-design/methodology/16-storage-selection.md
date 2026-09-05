# 16 — Storage Engine Selection Architecture

## Purpose

Storage Engine Selection Architecture provides the formal engineering criteria and decision trees used to select the optimal persistence engines (Relational, Document, Key-Value, Wide-Column, Graph, Search, Time-Series, Object Storage) for specific enterprise bounded contexts.

It operationalizes the principle of **Polyglot Persistence**, rejecting the anti-pattern of forcing an entire enterprise platform to store all data in a single monolithic database engine.

---

## Problem It Solves

- **The Database Mismatch Trap**: Prevents choosing a relational database for high-velocity unstructured IoT telemetry (where writes stall) or choosing a NoSQL document database for financial double-entry ledgers (where atomic multi-row ACID invariants fail).
- **Unbounded Licensing Costs**: Prevents deploying expensive proprietary database licenses (Oracle, SQL Server Enterprise) for simple key-value lookups that open-source PostgreSQL or Redis handle natively.
- **Operational Sprawl**: Prevents adopting 8 different exotic database engines across a small team that lacks the operational capability to back up, monitor, and patch them.

---

## Inputs

- **Data Model & Relationships**: Entities and cardinality from Step 11.
- **Access Patterns & Query Types**: Point lookups vs. full-text search vs. graph traversals from Step 12.
- **Throughput & Storage Projections**: Sizing calculations from Step 07.
- **Consistency & Durability Requirements**: ACID vs. BASE requirements from Step 04.

---

## Decision Process: The Polyglot Storage Decision Tree

```mermaid
graph TD
    DataNature{What is the primary data structure, consistency invariant, and query model?}
    
    DataNature -->|Complex relations, financial accounting, multi-row ACID transactions| RDBMS["Relational Database (RDBMS)<br/>PostgreSQL / MySQL / Aurora<br/>Default for 80% of business domains"]
    
    DataNature -->|Sub-millisecond latency, transient state, sessions, rate limits| InMem["In-Memory Key-Value Store<br/>Redis / Memcached<br/>RAM-based ultra-fast operations"]
    
    DataNature -->|Massive write throughput (> 50k TPS), append-only, high availability| WideCol["Wide-Column Store<br/>Apache Cassandra / ScyllaDB<br/>LSM-tree commit logs; masterless replication"]
    
    DataNature -->|Hierarchical documents, polymorphic schema, rapid prototyping| DocStore["Document Store<br/>MongoDB / Amazon DocumentDB<br/>JSON/BSON document structures"]
    
    DataNature -->|Full-text fuzzy search, inverted indexing, log analytics| SearchEngine["Search Engine<br/>Elasticsearch / OpenSearch<br/>Lucene inverted indexes and tokenizers"]
    
    DataNature -->|Deep relationship traversals (social networks, fraud rings)| GraphDB["Graph Database<br/>Neo4j / Amazon Neptune<br/>Nodes, edges, and index-free adjacency"]
    
    DataNature -->|Timestamp-ordered metrics, continuous sensor data, aggregations| TimeSeries["Time-Series Database<br/>TimescaleDB / InfluxDB<br/>Optimized for hypertable time-range scans"]
    
    DataNature -->|Unstructured binaries, images, videos, large backups, reports| ObjectStore["Cloud Object Storage<br/>Amazon S3 / Azure Blob Storage<br/>Virtually infinite capacity; lowest cost per GB"]
```

---

## Comparative Storage Engines Matrix

| Storage Category | Technology Examples | Write Scalability | Read Latency | Consistency Model | Query Capability | Primary Anti-Pattern |
|:---|:---|:---:|:---:|:---|:---|:---|
| **Relational (RDBMS)** | PostgreSQL, MySQL | Medium (Vertical + Read Replicas) | 5 – 20ms | Strict **ACID** | Complex SQL `JOIN`s, aggregations | High-frequency IoT sensor telemetry |
| **In-Memory Key-Value**| Redis, KeyDB | High | **< 1ms** | In-Memory (Optional AOF persistence)| Point lookups, sorted sets, hashes | Using as primary storage without backups |
| **Wide-Column** | Cassandra, ScyllaDB | **Ultra-High (LSM)** | 5 – 15ms | **BASE** (Tunable eventual consistency) | Partition-key lookups only (No joins) | Relational accounting ledgers |
| **Document Store** | MongoDB, Couchbase | High | 5 – 15ms | Configurable (Single-document ACID) | Document queries, aggregation pipelines | Highly normalized relational networks |
| **Search Engine** | Elasticsearch, OpenSearch | Medium | 10 – 30ms | Near real-time (Refresh lag) | Inverted index full-text fuzzy search | Primary system of record for mutations |
| **Graph Database** | Neo4j, Neptune | Low-Medium | 5 – 20ms | ACID (Graph-native) | Cypher graph pattern traversals | High-throughput batch streaming writes |
| **Object Storage** | AWS S3, Cloudflare R2 | Virtually Infinite | 50 – 200ms | Strong Consistency (Put-after-create) | Key-based blob fetch / Range requests | Storing small, high-frequency mutable records |

---

## Important Probing Questions

- *Is this database the primary source of truth, or is it a derived read model materialized via CDC from an upstream database?*
- *Can our team reliably operate, back up, tune, and patch this database engine in production?*
- *What is the cost per GB and cost per million IOPS for this storage tier at 3-year projected scale?*
- *Does the database support native automated multi-AZ failover and point-in-time recovery (PITR)?*

---

## Common Mistakes

- **Using Elasticsearch as a Primary Database**: Treating Elasticsearch as the transactional system of record. Elasticsearch can drop records during split-brain events and does not support multi-document transactions. (Elasticsearch should always be a derived read model powered by CDC from PostgreSQL).
- **Over-Adopting Niche NoSQL Engines**: Introducing 5 different NoSQL databases across a small team. (PostgreSQL with `JSONB`, TimescaleDB extensions, and pgvector can often handle documents, time-series, and vector search in a single operable engine).
- **Ignoring Write Amplification**: Sizing wide-column databases without accounting for SSTable compaction disk space overhead (which requires keeping 50% free disk space available for compactions).

---

## Trade-offs

| Strategy | Advantage | Trade-Off / Cost |
|:---|:---|:---|
| **Consolidated PostgreSQL (Swiss Army Knife)**| Single database engine to operate, back up, and monitor; unified ACID transactions. | Reaches hardware limits earlier than specialized distributed engines under massive scale. |
| **Extreme Polyglot Specialization** | Maximizes performance for every specific workload (Search, Graph, Timeseries). | High operational tax; data synchronization complexity; multi-database backup management. |

---

## Production Considerations

- Always verify that the selected database supports **Automated WAL Archival to WORM Object Storage** for disaster recovery.
- Maintain strict database connection limits and deploy **Connection Poolers (PgBouncer/ProxySQL)** in front of relational engines.
