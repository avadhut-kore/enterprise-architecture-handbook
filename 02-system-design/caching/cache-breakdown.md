# Cache Breakdown Defense

## 1. Breakdown vs. Avalanche
* **Cache Avalanche**: Thousands of disparate keys expiring simultaneously.
* **Cache Breakdown**: A **single ultra-hot key** (e.g., breaking news, viral discount) expiring, unleashing a thundering herd.

---

## 2. Defensive Architectures

### 1. Singleflight / Mutex Locking Pattern
When a cache miss occurs, the thread must acquire a distributed lock before querying the database. All other concurrent threads wait for the lock or poll the cache:

```mermaid
sequenceDiagram
    autonumber
    participant T1 as Thread 1
    participant T2 as Thread 2
    participant Cache as Redis
    participant DB as PostgreSQL
    
    T1->>Cache: GET hot_deal (MISS)
    T2->>Cache: GET hot_deal (MISS)
    T1->>Cache: SETNX lock:hot_deal (SUCCESS)
    T2->>Cache: SETNX lock:hot_deal (FAILED - Sleep & Retry)
    T1->>DB: Query Heavy SQL (Execute once!)
    T1->>Cache: SET hot_deal value EX 3600
    T1->>Cache: DEL lock:hot_deal
    T2->>Cache: GET hot_deal (HIT from T1's work!)
```

### 2. Logical Expiration (Never Expire in Cache)
Store data with a logical expiration timestamp in the payload, without setting a Redis physical TTL. A background worker periodically re-populates the key before the logical timestamp lapses.
