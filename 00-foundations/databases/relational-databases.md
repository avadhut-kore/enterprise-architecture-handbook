# Relational Databases (RDBMS): Internals & Architecture

> **Domain**: `00-foundations/databases`  
> **Status**: Approved  
> **Target Audience**: Solution Architects, Data Architects, Principal Engineers

---

## 1. Simple Explanation

A **Relational Database Management System (RDBMS)** stores structured data in strict tabular relations (tables with rows and columns) governed by a formal schema. It enforces relational integrity through primary and foreign keys and provides mathematical ACID guarantees (Atomicity, Consistency, Isolation, Durability) via SQL (Structured Query Language).

---

## 2. Architect-Level Deep Dive: Internal Storage Engines

Why are enterprise relational databases (PostgreSQL, MySQL InnoDB, Oracle, Microsoft SQL Server) capable of sustaining thousands of concurrent read/write queries without losing data on sudden power failure?

```mermaid
flowchart TD
    SQL["Incoming SQL Mutation: UPDATE accounts SET balance = balance - 100"] --> Engine["SQL Parser & Query Optimizer"]
    Engine --> BufferPool["Shared Buffer Pool (In-Memory RAM Cache)"]

    subgraph Memory ["RAM (Volatile)"]
        BufferPool
        WAL_Buffer["WAL Buffer (In-Memory Log)"]
    end

    subgraph Disk ["Persistent Storage (Non-Volatile)"]
        WAL_Disk["Write-Ahead Log (WAL / Redo Log)\nSequential Append-Only Write (Fast fsync!)"]
        DataFiles["Data Pages (8KB or 16KB Pages)\nB+ Tree On-Disk Table Storage"]
    end

    BufferPool -->|1. Mark page Dirty in RAM| BufferPool
    Engine -->|2. Append transaction record| WAL_Buffer
    WAL_Buffer -->|3. Synchronous fsync before returning 200 OK| WAL_Disk
    BufferPool -. 4. Asynchronous Background Checkpoint Writer .-> DataFiles
```

### 2.1 The Write-Ahead Log (WAL)
Modifying data in a B+ Tree directly on disk requires random disk I/O, which is slow.
* **The WAL Breakthrough**: Before any dirty page in memory is written to disk tables, a sequential, append-only log entry is flushed to the **Write-Ahead Log (WAL)**.
* Sequential disk writes on modern SSDs execute in microseconds. Once the WAL entry is safely synced (`fsync`), the database confirms the transaction to the client.
* If the power fails 1 millisecond later, the database reboots, reads the WAL, and **replays the unwritten transactions into the B+ Tree**, guaranteeing Durability!

### 2.2 Multi-Version Concurrency Control (MVCC)
In modern databases (PostgreSQL, MySQL InnoDB), **readers do not lock writers, and writers do not lock readers.**
* How? Every time a row is updated, the database does not overwrite the row in place. Instead, it writes a new version of the row tagged with a transaction ID (`xmin`, `xmax`).
* A concurrent `SELECT` query reads the historical snapshot of the row that was committed prior to the query's start time.
* *The Penalty*: **Database Bloat**. Dead tuple versions must be periodically cleaned up by background processes (PostgreSQL `VACUUM`).

---

## 3. When to Choose Relational Databases

* **Complex Multi-Table Joins**: Your access patterns require flexible ad-hoc querying across multiple normalized entities.
* **Financial & Audit Invariants**: Strict ACID transactions where balances, debits, and credits must balance to zero.
* **Structured, Schema-Enforced Domain Models**: High business risk associated with corrupted or missing fields.

---

## 4. When NOT to Choose Relational Databases

* **Massive Unstructured / Dynamic Schemas**: Storing arbitrary IoT JSON payloads with thousands of varying telemetry tags.
* **Extreme Write Volumes Beyond Scale-Up Limits**: Single-node write saturation exceeding 50,000 writes/second where sharding overhead is too complex.
* **Graph Traversals**: Evaluating social network relationships (friends of friends of friends), which requires recursive joins that degrade RDBMS performance exponentially.
