# Multi-Level Caching (L1/L2) Architecture

## 1. Multi-Tiered Latency Hierarchy
Multi-level caching combines the microsecond speed of in-process local memory with the centralized capacity of a distributed cluster:

```mermaid
flowchart LR
    Client[Request] --> L1{L1: Local In-Process Cache}
    L1 -->|Hit: 90% in <1 microsecond| Return[Fast Response]
    L1 -.->|Miss: 10%| L2{L2: Distributed Redis Cluster}
    L2 -->|Hit: 9% in 1ms| PopulateL1[Populate L1]
    L2 -.->|Miss: 1%| DB[(Primary Database: 20ms)]
    DB --> PopulateL2[Populate L2]
```

---

## 2. The L1 Cache Invalidation Challenge
When Pod A mutates data, Pod B's local in-process cache becomes stale.
* **Redis Pub/Sub Invalidation Bus**: When Pod A writes to DB, it publishes an invalidation event (`DEL user:123`) to a shared Redis Pub/Sub channel.
* All microservice pods subscribe to the channel and immediately evict the key from their local L1 memory.
