# Cache-Aside Pattern (Lazy Loading)

## 1. Principles of Cache-Aside
Cache-Aside is the most widely deployed caching architecture. The application code sits between the cache and the primary datastore, orchestrating both reads and writes.

```mermaid
sequenceDiagram
    autonumber
    participant App as Application
    participant Cache as Redis
    participant DB as Database
    
    Note over App,DB: Read Path
    App->>Cache: GET key
    alt Cache Hit
        Cache-->>App: Return Cached Value
    else Cache Miss
        Cache-->>App: null
        App->>DB: SELECT data WHERE id = key
        DB-->>App: Return Data
        App->>Cache: SET key value (TTL=3600)
    end
    
    Note over App,DB: Write Path (Mutation)
    App->>DB: UPDATE table SET value WHERE id = key
    App->>Cache: DEL key (Invalidate Cache)
```

---

## 2. Why Invalidate (DEL) Instead of Update (SET)?
When modifying data in the database, **always delete the key from cache rather than updating it**:
* **Prevents Race Conditions**: If two concurrent threads execute writes out of order ($W_1$ then $W_2$), updating cache directly can result in $W_1$ overwriting $W_2$'s cache entry, leaving stale data indefinitely.
* Deleting the key forces the next reader to atomically reload the freshest database state.
