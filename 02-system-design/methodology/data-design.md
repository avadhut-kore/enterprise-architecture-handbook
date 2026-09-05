# Data Design & Modeling in System Design

## Overview

Data Design is the process of selecting appropriate storage paradigms, defining database schemas, optimizing access patterns, and partitioning data to satisfy system throughput, latency, and consistency requirements. In modern distributed systems, the myth of the "one-size-fits-all database" is dead. Architects practice **Polyglot Persistence**—matching specific domain data models and access patterns to the optimal underlying storage engine.

---

## The Database Selection Decision Matrix

```mermaid
graph TD
    Storage{What is the primary access pattern and data structure?}
    
    Storage -->|Complex relational joins, ACID transactions, strict schema| Relational["Relational (RDBMS)<br/>PostgreSQL / MySQL / Oracle<br/>Best for: Financial ledgers, ERP, user accounts"]
    
    Storage -->|High write volume, simple key lookup, horizontal partitioning| KeyValue["Key-Value / Document<br/>Redis / AWS DynamoDB / MongoDB<br/>Best for: Session cache, user profiles, shopping carts"]
    
    Storage -->|Massive write scale, append-only, multi-datacenter replication| WideColumn["Wide-Column Store<br/>Apache Cassandra / ScyllaDB<br/>Best for: IoT sensor metrics, audit logs, messaging"]
    
    Storage -->|Complex relationship traversal, highly interconnected entities| Graph["Graph Database<br/>Neo4j / Amazon Neptune<br/>Best for: Social networks, fraud detection, recommendation graphs"]
    
    Storage -->|Full-text fuzzy search, log analytics, inverted indexes| Search["Search Engine<br/>Elasticsearch / OpenSearch<br/>Best for: Product catalog search, APM log indexing"]
    
    Storage -->|Timestamp-ordered telemetry, high ingestion, time-window aggregations| TimeSeries["Time-Series Database<br/>TimescaleDB / InfluxDB<br/>Best for: Server metrics, financial tick data"]
```

---

## 1. Relational vs. NoSQL Schema Design

```mermaid
flowchart TD
    subgraph RelationalDesign["Relational Design (Query-Agnostic / Normalized)"]
        R1["1. Design around entities and business relationships (3NF)"]
        R2["2. Eliminate redundancy; enforce foreign key integrity"]
        R3["3. Assemble queries dynamically at runtime via JOINs"]
        R4["Trade-off: High write consistency, but JOINs become unscalable at petabyte volume"]
    end

    subgraph NoSQLDesign["NoSQL Design (Query-First / Denormalized)"]
        N1["1. List all required application queries and access patterns first"]
        N2["2. Design tables specifically to satisfy those exact queries in 1 single read"]
        N3["3. Duplicate data intentionally across documents/tables to avoid JOINs"]
        N4["Trade-off: Blazing fast single-key reads, but updates require updating multiple records"]
    end
```

---

## 2. Choosing the Optimal Partition / Shard Key

When data exceeds the capacity of a single physical database instance, the dataset must be partitioned. The choice of **Shard Key (Partition Key)** is the single most important decision in distributed data architecture:

### Criteria for an Effective Shard Key
1. **High Cardinality**: The key must have millions of distinct values (e.g., `user_id` or `uuid`) to distribute evenly across dozens of physical nodes. Using `country_code` or `status` is disastrous because 90% of data pools into 2 or 3 hot shards.
2. **Even Write & Read Distribution**: Avoid monotonic sequence keys (e.g., auto-incrementing timestamps `created_at`). Monotonic keys cause 100% of current write traffic to slam the single shard holding the latest time window ("Hot Spotting").
3. **Query Colocation**: Choose a shard key that aligns with the primary read query filter. If 99% of queries filter by `WHERE tenant_id = ?`, sharding by `tenant_id` ensures queries are satisfied by a single physical node (Scatter-Gather queries avoided).

```mermaid
graph LR
    subgraph BadKey["Anti-Pattern: Monotonic Timestamp Key"]
        T1["Writes at 10:00 AM -> Shard A (100% Load / Overheated)"]
        T2["Writes at 10:01 AM -> Shard A (100% Load)"]
        T3["Older Shards B, C, D: 0% Load (Idle Waste)"]
    end

    subgraph GoodKey["Pattern: Hash-Distributed Shard Key (user_id)"]
        U1["user_102 -> MD5 Hash -> Shard A (25% Load)"]
        U2["user_409 -> MD5 Hash -> Shard B (25% Load)"]
        U3["user_891 -> MD5 Hash -> Shard C (25% Load)"]
        U4["user_012 -> MD5 Hash -> Shard D (25% Load)"]
    end
```

---

## 3. Database Indexing Strategies

Indexes trade write latency and disk space for lightning-fast read performance:
- **B-Tree Indexes**: Standard for relational databases; excellent for point lookups (`WHERE id = 42`) and range scans (`WHERE age BETWEEN 20 AND 30`).
- **Hash Indexes**: Extreme $O(1)$ point lookups; cannot support range queries or sorting.
- **Inverted Indexes**: Tokenizes text strings into individual words mapped to document IDs (core of Elasticsearch/Lucene).
- **Covering Indexes**: An index containing all columns requested in the `SELECT` clause (e.g., `INDEX (user_id, status) INCLUDE (email)`), allowing the database engine to satisfy the entire query directly from RAM without touching the underlying physical table pages.

---

## 4. Polyglot Persistence Architecture in Practice

A modern enterprise e-commerce platform utilizes specialized databases across its bounded contexts:

```mermaid
flowchart TD
    User["Web / Mobile User"] --> APIGW["API Gateway"]
    
    APIGW --> Catalog["Product Catalog Service"]
    APIGW --> Order["Order Processing Service"]
    APIGW --> SearchSvc["Catalog Search Service"]
    APIGW --> Analytics["Analytics & BI Engine"]
    
    Catalog --> Cache[("Redis: In-Memory L2 Cache")]
    Catalog --> DocDB[("MongoDB: Product Attribute Documents")]
    
    Order --> SQLDB[("PostgreSQL: Transactional ACID Orders & Payments")]
    
    SearchSvc --> Elastic[("Elasticsearch: Full-Text Inverted Index")]
    
    Order -.->|CDC / Debezium| Kafka[("Kafka Event Stream")]
    Kafka --> Elastic
    Kafka --> Analytics
    Analytics --> Lake[("ClickHouse / Snowflake: Analytical OLAP Columnar Store")]
```
