# Network Partitions in Distributed Systems

## 1. Understanding Network Partitions

A network partition is a failure scenario where communication between two or more subnets of a distributed system is severed or severely delayed, even though individual nodes within each partition continue executing normally.

Under the CAP theorem, **Partition Tolerance (P) is non-negotiable** in physical networks: you cannot choose "no partitions" because physical hardware, fiber lines, BGP routing, and switches fail unpredictably. Therefore, during a partition, a system can only choose between **Consistency (CP)** or **Availability (AP)**.

---

## 2. Partition Topologies

```
Symmetric Partition:          Asymmetric / Triangular Partition:
[ Subnet A ] <==CUT==> [ Subnet B ]      [ Node A ] <---OK---> [ Node B ]
(Neither can talk to each other)           \                     /
                                            \==CUT==     ==CUT==/
                                                    [ Node C ]
```

---

## 3. Handling Strategies

```
+-----------------------------------+----------------------------------------+
| Strategy                          | Trade-Off Profile                      |
+-----------------------------------+----------------------------------------+
| CP (Consistency over Availability)| Minority partition rejects writes;     |
|                                   | guarantees zero dirty/divergent state  |
| AP (Availability over Consistency)| All partitions accept writes; relies on|
|                                   | CRDTs, Vector Clocks, or LWW to resolve|
| Circuit-Breaking Partitions       | Rapidly disconnect lagging subnets     |
+-----------------------------------+----------------------------------------+
```

---

## 4. Production Checklist

- Heartbeat thresholds must incorporate expected network jitter (e.g., $3 \times \text{P99.9 latency}$).
- Implement exponential backoff with jitter on inter-node reconnect attempts to prevent network saturation when partitions heal.
