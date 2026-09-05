# Quorum Systems & Split-Brain Mitigation

## Executive Summary

When a network partition isolates distributed nodes, a **Split-Brain** condition occurs if multiple sub-clusters simultaneously believe they are the authoritative leader, accepting conflicting writes and corrupting data.

---

## 1. Split-Brain Disaster Scenario

```mermaid
graph TD
    subgraph Network Partition Cuts WAN Link
        NodeA[(Cluster Node A: In Zone 1)] <.- -X- -.> NodeB[(Cluster Node B: In Zone 2)]
        NodeA -->|Believes Node B is Dead: Elects Itself Leader!| WriteA[Accepts Write: Balance = $100]
        NodeB -->|Believes Node A is Dead: Elects Itself Leader!| WriteB[Accepts Write: Balance = $50]
    end
    WriteA & WriteB --> Diverge[IRRECONCILABLE DATABASE CORRUPTION!]
```

---

## 2. Mathematical Mitigation: Majority Quorum & Fencing Tokens

1. **Strict Majority Quorum ($Q = \lfloor N/2 \rfloor + 1$)**:
   - A cluster of $N=5$ nodes requires at least 3 nodes to agree on a leader. If the cluster partitions into 2 nodes and 3 nodes, only the 3-node partition can form a quorum; the 2-node partition shuts down safely.
2. **Fencing Tokens**:
   - Every newly elected leader receives a monotonically increasing token (e.g., Token 42). When writing to shared storage, the storage engine rejects any write carrying a token lower than the latest seen token, neutralizing zombie former leaders.
