# NoSQL Databases: The 4 Paradigms & Access Patterns

> **Domain**: `00-foundations/databases`  
> **Status**: Approved  
> **Target Audience**: Solution Architects, Data Architects, Principal Engineers

---

## 1. Simple Explanation

**NoSQL ("Not Only SQL")** describes non-relational database management systems designed to address the scale, schema flexibility, and latency limits of traditional RDBMS engines by trading off complex ad-hoc SQL joins and multi-table ACID transactions in favor of horizontal partitionability and high-speed key-based access.

---

## 2. The 4 NoSQL Paradigms

```mermaid
mindmap
  root((NoSQL Paradigms))
    1. Document Store
      MongoDB, Couchbase, DocumentDB
      JSON / BSON hierarchical trees
      Rich secondary indexes
      Access by Document ID or Field
    2. Key-Value Store
      Redis, Memcached, DynamoDB (Simple)
      O(1) Hash Map access
      Ultra-low sub-millisecond latency
      Ephemeral cache or session state
    3. Wide-Column / Columnar
      Apache Cassandra, ScyllaDB, HBase
      LSM-Tree storage engine
      Extreme append-heavy write throughput
      Partition key + Clustering column
    4. Graph Database
      Neo4j, AWS Neptune, ArangoDB
      Nodes, Edges, Properties
      Index-free adjacency
      Relationship traversal algorithms
```

---

## 3. Deep Dive into the 4 Paradigms

### 3.1 Document Databases (e.g., MongoDB)
* **Storage Model**: Data stored as self-describing, nested documents (JSON/BSON).
* **Architectural Advantage**: Natural mapping to Object-Oriented code models (Aggregate Root in DDD). An Order with 10 Order Items is stored in a single document; fetching the order requires **one disk read and zero joins**.
* **Failure Mode**: **Unbounded Document Growth**. MongoDB caps documents at 16MB. Embedding unbounded arrays (e.g., a customer's lifetime activity log) inside a single document causes performance collapse and page reallocation fragmentation.

### 3.2 Key-Value Stores (e.g., Redis)
* **Storage Model**: In-memory hash table mapping an arbitrary string key to an arbitrary value (string, list, set, hash).
* **Architectural Advantage**: Sub-millisecond read and write latencies. Atomic data structure manipulations (`INCR`, `LPUSH`).
* **Fit**: Session management, rate limiting counters, distributed locks, hot caching tiers.

### 3.3 Wide-Column Stores (e.g., Apache Cassandra / ScyllaDB)
* **Storage Model**: Log-Structured Merge-Tree (LSM-Tree) engine.
  * Writes append to in-memory **Memtable** and commit to append-only **CommitLog**.
  * Periodically flushed to immutable disk files (**SSTables**).
* **Architectural Advantage**: **Insane Write Throughput**. A 20-node Cassandra cluster can sustain 500,000 writes/second with zero locks.
* **Architectural Trap**: **Queries must be designed before the schema is created**. In Cassandra, you cannot run arbitrary `WHERE` queries. You must design a dedicated table for every specific query screen in your application!

### 3.4 Graph Databases (e.g., Neo4j)
* **Storage Model**: Graph nodes connected by directional, typed edges with properties. Uses **Index-Free Adjacency** (each node holds direct physical memory pointers to its neighbors).
* **Architectural Advantage**: Constant-time graph traversal ($O(1)$ per hop). Querying "Find all 3rd-degree connections" takes milliseconds, whereas an RDBMS requires recursive self-joins that crash the database engine.
* **Fit**: Fraud detection rings, social networks, knowledge graphs, identity authorization graphs.
