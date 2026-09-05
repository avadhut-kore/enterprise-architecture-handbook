# Database Performance: Lock Contention & Hot Row Mitigation Strategies

## 1. Architectural Purpose & Problem Context
Remediating concurrency bottlenecks on heavily updated singleton rows: batching balance updates, optimistic concurrency, and partitioning queues.

---

## 2. Performance Diagnostic Workflow

```mermaid
flowchart TD
    Alert[High Latency / Database Saturation Alert] --> Digest[Inspect Slow Query Digest]
    Digest --> Explain[Analyze Execution Plan: Seek vs Scan]
    Explain --> RootCause{"Identify Bottleneck"}
    RootCause -->|Missing Index| AddIndex[Add Composite / Partial Index]
    RootCause -->|Lock Contention| TuneLocks[Optimize Transaction Scopes]
    RootCause -->|Query Storm| AddCache[Introduce Cache-Aside with Mutex]
    RootCause -->|IOPS Saturation| ScaleRead[Offload Reads to Replicas]
```

---

## 3. Production Invariants
- No query in the critical customer transaction path should execute an unindexed sequential table scan.
- Transaction scopes must be kept as short as possible to minimize lock holding duration.
- Guard all database read caches with probabilistic early expiration or distributed locks to prevent catastrophic cache stampedes.
