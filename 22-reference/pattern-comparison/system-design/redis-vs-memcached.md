# Architecture Comparison: Redis vs Memcached

## 1. Architectural Trade-Off Matrix

```
+--------------------------+---------------------------------+---------------------------------+
| Architectural Dimension  | Redis                           | Memcached                       |
+--------------------------+---------------------------------+---------------------------------+
| Concurrency Model        | Single-threaded event loop*     | Multi-threaded (Scales on cores)|
| Data Structures          | Strings, Hashes, Lists, Sets,   | Pure String / Byte blobs only   |
|                          | Sorted Sets, Bitmaps, Streams   |                                 |
| Persistence Options      | RDB snapshots & AOF logs        | None (Volatile in-memory only)  |
| High Availability        | Redis Sentinel & Redis Cluster  | Client-side consistent hashing  |
| Memory Efficiency        | Higher overhead per key         | Extremely lightweight memory    |
| Pub/Sub & Lua Scripting  | Native support                  | None                            |
| Best Use Case            | Complex caching, leaderboards,  | High-throughput simple key-value|
|                          | locks, queues, session store    | read caching                    |
+--------------------------+---------------------------------+---------------------------------+
```

---

## 2. Production Recommendation

- **Choose Redis (Default)**: For 90% of enterprise use cases, Redis's rich data structures (Sorted Sets for leaderboards, Hashes for user profiles, atomic locks) and native clustering make it the standard choice.
- **Choose Memcached**: Only when caching simple key-value string blobs where single-instance multi-core vertical throughput is the sole requirement.
