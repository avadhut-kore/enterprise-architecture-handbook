# Technology Comparison: High Availability Trade-Off Matrix

## Executive Summary
This reference matrix evaluates the architectural trade-offs between active-passive vs active-active.

---

## Architectural Comparison Matrix

| Dimension | Active-Passive (Warm Standby) | Active-Active (Bi-Directional) |
| :--- | :--- | :--- |
| **Consistency Model** | Strict ACID (Single primary master) | Eventual Consistency / Paxos consensus |
| **Replication Mechanism** | Asynchronous storage replication | Multi-master bi-directional / CRDTs |
| **Failure Recovery** | DNS failover + Promote standby master | Transparent routing to surviving nodes |
| **Infrastructure Cost** | Moderate (Standby runs at 20% capacity) | High (Both fleets sized for peak traffic) |
