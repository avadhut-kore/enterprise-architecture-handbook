# SQL Architecture: Query Optimization & Execution Plan Analysis

## 1. Architectural Purpose & Problem Context
Cost-based optimizers (CBO), index seeks vs table scans, nested loop vs hash joins, statistics freshness, and diagnosing query plan regressions.

---

## 2. Structural Architecture & Engine Mechanics

```mermaid
flowchart TD
    Client[Application Client] --> Pool[Connection Pool]
    Pool --> Parser[SQL Parser & Query Optimizer]
    Parser --> Engine[Execution Engine]
    Engine --> BufferPool[(Buffer Pool / Memory Cache)]
    Engine --> WAL[(Write-Ahead Log / Redo Log)]
    BufferPool -.->|Async Checkpoint Flush| Disk[(Primary Data Files on Disk)]
```

---

## 3. Production Invariants & Best Practices
- Every production table must have an explicit primary key.
- Never execute DDL migrations that acquire exclusive table locks during peak production traffic; use the Expand/Contract pattern.
- Always monitor replication lag when routing read queries to secondary replicas.
- Size database connection pools conservatively; oversized pools degrade database throughput due to CPU context switching.
