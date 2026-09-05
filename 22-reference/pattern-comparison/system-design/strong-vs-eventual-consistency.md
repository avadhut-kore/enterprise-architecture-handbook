# Architecture Comparison: Strong vs Eventual Consistency

## 1. Architectural Trade-Off Matrix

```
+--------------------------+---------------------------------+---------------------------------+
| Architectural Dimension  | Strong Consistency (Linearizab.)| Eventual Consistency (BASE)     |
+--------------------------+---------------------------------+---------------------------------+
| Read Invariant           | Always returns latest committed | May return stale data for a time|
| Write Latency            | High (Must reach consensus/lock)| Low (Writes return immediately) |
| System Availability      | Reduced under network partition | High (Partitions accept writes) |
| Conflict Reconciliation  | Not needed (Serialized)         | Required (LWW, Vector Clocks, C)|
| Protocol Complexity      | Raft, Paxos, 2PC                | Gossip, Merkle Trees, Read Rep  |
| Hardware Requirement     | Strict bounds, low jitter       | Heterogeneous commodity hardware|
| Best Use Case            | Ledger, Inventory reservation   | Social feeds, DNS, Caches       |
+--------------------------+---------------------------------+---------------------------------+
```

---

## 2. PACELC Theorem Application

```
If there is a Partition (P):
  Trade-off between Availability (A) and Consistency (C).
Else (E) under normal operation:
  Trade-off between Latency (L) and Consistency (C).
```

- **PC/EC Systems (e.g., Spanner, CockroachDB)**: Prioritize consistency at all times; pay higher latency.
- **PA/EL Systems (e.g., DynamoDB, Cassandra)**: Prioritize availability during partitions and ultra-low latency during normal operation; accept eventual consistency.
