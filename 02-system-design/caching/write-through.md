# Write-Through Caching Pattern

## 1. Synchronous Cache-and-Store Mutation
In Write-Through caching, the application writes directly to the cache. The cache synchronously writes through to the persistent datastore before returning success to the client.

```mermaid
sequenceDiagram
    autonumber
    participant App as Application
    participant Cache as Cache Provider
    participant DB as Persistent DB
    
    App->>Cache: WRITE data (key, value)
    Cache->>DB: Synchronous INSERT / UPDATE
    DB-->>Cache: DB Write Success
    Cache->>Cache: Store in In-Memory Map
    Cache-->>App: Acknowledge Success
```

---

## 2. Trade-offs
* **Advantage**: Guaranteed cache freshness; data in cache is never stale.
* **Disadvantage**: High write latency (incurs the round-trip penalty of both cache and persistent disk write).
