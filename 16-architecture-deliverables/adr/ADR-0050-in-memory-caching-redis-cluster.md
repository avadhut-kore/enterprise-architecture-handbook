# ADR-0050: Standardization on Redis Cluster (ElastiCache) for Distributed Caching

## Metadata
```yaml
id: ADR-0050
title: Standardization on Redis Cluster (ElastiCache) for Distributed Caching
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
High-throughput read queries were hammering primary relational databases, causing connection pool exhaustion during traffic spikes.

---

## 2. Decision
We mandate a distributed caching tier using Amazon ElastiCache for Redis (Cluster Mode Enabled) implementing the Cache-Aside pattern with explicit TTLs.

---

## 3. Positive Consequences
- Offloads 90% of read traffic from the relational database.
- Delivers sub-millisecond query response times.
- Scales write throughput horizontally across up to 500 shards.

---

## 4. Negative Consequences & Trade-offs
- Introduces cache invalidation complexity.
- Requires application logic to handle thundering herd and cache stampede scenarios.

---

## 5. Alternatives Considered & Rejected
- **Memcached**: Rejected due to lack of replication and data persistence capabilities.
- **In-Process Local Memory Caches**: Rejected due to memory inconsistency across horizontally scaled pods.
