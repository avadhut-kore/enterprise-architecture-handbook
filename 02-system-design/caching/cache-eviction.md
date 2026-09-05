# Cache Eviction Policies

## 1. Principles of Memory Eviction
When cache RAM reaches its configured threshold (`maxmemory` in Redis), the system must evict existing keys to accommodate incoming allocations.

```mermaid
flowchart TD
    MemoryFull[Cache Reaches maxmemory Ceiling] --> Policy{Eviction Policy}
    Policy -->|allkeys-lru| LRU[Evict Least Recently Accessed Keys]
    Policy -->|allkeys-lfu| LFU[Evict Least Frequently Used Keys]
    Policy -->|volatile-ttl| TTL[Evict Keys with Shortest TTL Remaining]
    Policy -->|noeviction| Error[Reject Writes: Return OOM Error to Client]
```

---

## 2. Redis Eviction Directives
* `noeviction`: Returns errors on writes when memory limit is reached (preserves all data).
* `allkeys-lru`: Evicts least recently used keys among the entire keyspace.
* `volatile-lru`: Evicts least recently used keys among keys that have an explicit `EXPIRE` set.
* `allkeys-lfu`: Evicts least frequently used keys (tracks access frequency counters).
* `volatile-ttl`: Evicts keys with the shortest time-to-live.
