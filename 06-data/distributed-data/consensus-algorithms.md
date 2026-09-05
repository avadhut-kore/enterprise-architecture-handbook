# Distributed Consensus Algorithms

## 1. The Consensus Problem
Distributed consensus requires a cluster of independent nodes to agree on a state value or log sequence, even when network links drop messages and nodes crash.

### Quorum Majority Requirement
To tolerate $F$ node failures, a cluster must contain at least:
$$N = 2F + 1\text{ nodes}$$
A quorum consists of:
$$\text{Quorum Size} = \left\lfloor \frac{N}{2} \right\rfloor + 1$$
* A 3-node cluster tolerates $F=1$ failure (Quorum = 2).
* A 5-node cluster tolerates $F=2$ failures (Quorum = 3).
* An even node count (e.g., 4 nodes) still only tolerates $F=1$ failure while increasing failure probability! Always deploy **odd cluster node sizes**.

---

## 2. CFT vs. BFT Consensus
* **Crash Fault Tolerant (CFT - Raft / Paxos)**: Assumes nodes are honest but may crash or experience network delays. Standard for internal enterprise data centers.
* **Byzantine Fault Tolerant (BFT - PBFT / Tendermint)**: Tolerates malicious, compromised, or lying nodes. Requires $N \ge 3F + 1$ nodes. Standard for public decentralized blockchains.
