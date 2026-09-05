# Database Selection: Comprehensive Database Decision Criteria Matrix

## 1. Architectural Purpose & Problem Context
Side-by-side comparative rubric across Relational, Distributed SQL, Key-Value, Document, Wide-Column, Graph, and Time-Series paradigms.

---

## 2. Decision Tree Topology

```mermaid
flowchart TD
    Start{"Does the workload require strict ACID transactions across multiple entities?"}
    Start -->|Yes| Relational{"Is single-node capacity exceeded by write volume?"}
    Relational -->|No| RDBMS[(Standard Relational RDBMS: PostgreSQL / SQL Server)]
    Relational -->|Yes| DistSQL[(Distributed SQL: CockroachDB / YugabyteDB)]
    Start -->|No| Access{"What is the primary access pattern?"}
    Access -->|Simple Key Point Lookups| KV[(Key-Value Store: Redis / DynamoDB)]
    Access -->|Hierarchical Semi-Structured JSON| Doc[(Document Store: MongoDB)]
    Access -->|Append-Heavy High-Throughput Writes| WideCol[(Wide-Column: Cassandra / ScyllaDB)]
    Access -->|Deep Many-to-Many Relationship Traversals| Graph[(Graph DB: Neo4j)]
    Access -->|Timestamped Metrics / Telemetry| TS[(Time-Series DB: TimescaleDB)]
```

---

## 3. Production Invariants
- Default to standard relational databases (e.g., PostgreSQL) unless explicit scale or data-model requirements justify alternative engines.
- Never adopt NoSQL solely for "scalability" without verifying that read/write access patterns align with the engine's query capabilities.
