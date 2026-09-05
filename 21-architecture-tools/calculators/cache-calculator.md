# Architectural Calculator: Cache Capacity & Working Set Sizing

## 1. Mathematical Formulation: The Pareto Principle (80/20 Rule)

In most consumer and enterprise platforms:
**20% of catalog items generate 80% of read traffic.**

$$\text{Cache Working Set} = \text{Daily Active Working Data} \cdot 0.20 \cdot \text{Memory Safety Buffer (1.4)}$$

---

## 2. In-Memory Sizing Model

```
Parameters:
- Total Daily Read Requests: 100,000,000 (100M)
- Unique Entities Read Daily: 10,000,000 (10M)
- Average Serialized Entity Size: 1,500 Bytes
- Redis Overhead per Key (dictEntry, robj): ~250 Bytes
- Effective Size per Entry: 1,750 Bytes

Calculations:
- 20% Working Set Count: 10M * 0.20 = 2,000,000 Keys
- Raw Memory Required: 2,000,000 * 1,750 Bytes = 3.5 GB
- Production Headroom Multiplier: 1.5x (Accounts for maxmemory fragmentation & pubsub)
- Total RAM Allocation: 3.5 GB * 1.5 = 5.25 GB
```

---

## 3. Cache Eviction Configuration

- Set `maxmemory-policy: allkeys-lru` or `volatile-lfu` to automatically discard cold keys when memory hits limits.
