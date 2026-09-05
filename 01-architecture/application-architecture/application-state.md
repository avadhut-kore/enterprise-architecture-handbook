# Application State Management

## 1. Stateless vs Stateful Application Tiers

```
+--------------------------+---------------------------------+---------------------------------+
| Dimension                | Stateless Compute               | Stateful Compute                |
+--------------------------+---------------------------------+---------------------------------+
| Session Storage          | In-Memory Cache (Redis) / JWT   | Local Server RAM / Sticky Sess. |
| Scaling Vector           | Instant Horizontal Autoscaling  | Complex Partitioning / Sharding |
| Pod Crash Impact         | Zero user impact; retry request | Active user session dropped     |
| Deployment Model         | Rolling zero-downtime cutover   | Drain connections slowly        |
| Architecture Fit         | Standard Web APIs & Microserv.  | Multiplayer Gaming, Real-Time WS|
+--------------------------+---------------------------------+---------------------------------+
```

---

## 2. Managing In-Process State Safely

When in-process caching or state machines are required:
- Use thread-safe data structures (`ConcurrentDictionary` in .NET, `ConcurrentHashMap` in Java).
- Enforce size bounds and eviction policies (LRU/LFU) to prevent Out-Of-Memory (OOM) crashes.
