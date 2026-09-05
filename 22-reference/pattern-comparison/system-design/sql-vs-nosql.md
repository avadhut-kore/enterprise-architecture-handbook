# Architecture Comparison: SQL (RDBMS) vs NoSQL

## 1. Architectural Trade-Off Matrix

```
+--------------------------+---------------------------------+---------------------------------+
| Architectural Dimension  | SQL Relational (Postgres, MySQL)| NoSQL (Cassandra, Dynamo, Mongo)|
+--------------------------+---------------------------------+---------------------------------+
| Data Model               | Structured Tables & Relations   | Key-Value, Document, Wide-Column|
| Schema Nature            | Rigid, Strongly Typed (DDL)     | Dynamic / Schema-on-Read        |
| Transactional Model      | Strict ACID                     | BASE (Eventual Consistency)     |
| Scaling Vector           | Primarily Vertical (Read replica| Horizontal Partitioning (Scale- |
|                          | scaling, sharding complex)      | out across commodity nodes)     |
| Complex Joins            | Native, declarative multi-table | Application-side or Denormalized|
| Query Language           | Declarative SQL Standard        | Proprietary APIs / Query specs  |
| Best Use Case            | Financials, ERP, Core Relational| High-Velocity Ingest, Big Data  |
+--------------------------+---------------------------------+---------------------------------+
```

---

## 2. Decision Tree

```
Does the domain require strict multi-record ACID transactions and complex joins?
├── YES ──► Choose SQL (PostgreSQL, MySQL) or Distributed SQL (CockroachDB/Spanner)
└── NO  ──► Does the workload exceed single-node write capacity (> 20,000 writes/sec)?
              ├── YES ──► Choose Wide-Column / Key-Value NoSQL (Cassandra, DynamoDB)
              └── NO  ──► Does the data consist of deeply nested, polymorphic JSON documents?
                            ├── YES ──► Choose Document NoSQL (MongoDB) or Postgres JSONB
                            └── NO  ──► Choose SQL (Default pragmatic choice)
```

---

## 3. Enterprise Takeaway

Do not view SQL vs NoSQL as an ideological binary. Modern enterprise architecture embraces **Polyglot Persistence**: using relational databases for core financial transactions and NoSQL/caching stores for telemetry, session tracking, and catalog search.
