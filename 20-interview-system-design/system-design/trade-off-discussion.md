# System Design Interview: Navigating Trade-Offs

## 1. The Core Philosophy of Senior Interviews

> **There are no solutions in software architecture; there are only trade-offs.**

An architect who claims their design has "no downsides" fails the interview. Strong candidates proactively voice the negative consequences of every choice and explain why the trade-off is acceptable for the business.

---

## 2. Common Trade-Off Dimensions

```
+--------------------------+-----------------------+-----------------------+
| Architectural Decision   | Benefits Gained       | Costs / Risks Paid    |
+--------------------------+-----------------------+-----------------------+
| Eventual Consistency     | High availability,    | Potential stale reads,|
| (NoSQL / AP)             | low write latency     | complex conflict logic|
| In-Memory Caching        | Sub-millisecond reads,| Cache invalidation,   |
| (Redis / Memcached)      | database offload      | memory cost, stampedes|
| Microservices            | Team independence,    | Distributed tracing,  |
|                          | decoupled deployments | network hops, sagas   |
| Message Queues (Kafka)   | Asynchronous buffer,  | Eventual consistency, |
|                          | load leveling         | consumer lag, ordering|
+--------------------------+-----------------------+-----------------------+
```
