# Byzantine Fault Tolerance in Distributed Systems

## 1. Problem Definition

A Byzantine fault (named after the Byzantine Generals Problem) is an arbitrary failure mode where a participating node not only stops or crashes, but behaves incorrectly, transmits contradictory data to different peers, or acts maliciously.

In standard enterprise distributed systems, crash-fault-tolerant (CFT) protocols (Raft, Paxos) assume nodes are non-malicious and follow protocol rules. Byzantine Fault Tolerant (BFT) protocols are required when nodes cannot be trusted (e.g., public blockchains, multi-party financial clearing, or mission-critical aerospace fly-by-wire systems).

---

## 2. CFT vs BFT Comparison

```
+---------------------------+------------------------+-----------------------+
| Metric                    | Crash Fault (CFT)      | Byzantine Fault (BFT) |
+---------------------------+------------------------+-----------------------+
| Fault Assumption          | Nodes crash or halt    | Nodes lie or corrupt  |
| Minimum Nodes for $f$ faults| $2f + 1$               | $3f + 1$              |
| Example Protocols         | Raft, Paxos, Zab       | PBFT, Tendermint, Raft-BFT|
| Message Complexity        | $O(N)$ to $O(N^2)$     | $O(N^2)$ to $O(N^3)$  |
| Primary Domain            | Enterprise Datacenters | Blockchains, Avionics |
+---------------------------+------------------------+-----------------------+
```

---

## 3. Practical Enterprise Applications of BFT Concepts

Even in internal enterprise networks, Byzantine-like faults occur due to:
- **Silent Memory Corruption**: Non-ECC memory bit flips altering serialized packets.
- **Firmware / Network Driver Bugs**: Network cards corrupting checksums.
- **Architectural Defense**: Always validate cryptographic HMACs, payload checksums (SHA-256), and schema invariants at service boundaries rather than blindly trusting internal payloads.
