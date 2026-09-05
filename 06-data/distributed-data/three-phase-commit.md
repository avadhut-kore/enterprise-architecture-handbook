# Three-Phase Commit Protocol (3PC)

## 1. Architectural Motivation
Three-Phase Commit (3PC) was designed to eliminate the indefinite blocking flaw of 2PC by introducing an intermediate state (**Pre-Commit**) and distributed timeouts.

```mermaid
flowchart LR
    P1[Phase 1: Can-Commit?] --> P2[Phase 2: Pre-Commit]
    P2 --> P3[Phase 3: Do-Commit]
```

---

## 2. Why 3PC Fails in Real-World Distributed Networks
While 3PC eliminates blocking under crash-stop assumptions on reliable networks, it **completely fails under network partitions**:
* If a network partition divides the coordinator and participants during the Pre-Commit phase, one partition times out and aborts, while the other times out and commits.
* **Result: Data Corruption / Split-Brain**.
* *Modern Standard*: Real-world enterprise systems bypass 3PC entirely in favor of quorum consensus protocols (**Raft** and **Paxos**).
