# Split-Brain in Distributed Systems

## 1. Problem Definition

Split-brain occurs when a network partition divides a distributed cluster into two or more disconnected segments, and nodes in multiple segments simultaneously believe they are the authoritative primary (leader).

```
[ Primary A ] <---- NETWORK CUT ----> [ Primary B ]
  Writes Accept                       Writes Accept
  (Divergent Data)                    (Divergent Data)
```

Both partitions accept conflicting writes from clients, leading to catastrophic data corruption and unreconcilable state diverge.

---

## 2. Architectural Root Causes

- **Heartbeat Timeout vs True Crash**: A network switch partition isolates the primary node. Followers observe missed heartbeats, conclude the primary is dead, and elect a new leader while the original primary is still actively serving clients.
- **GC Pauses / Thread Freezes**: A stop-the-world garbage collection pause on the leader causes it to miss heartbeat deadlines. The cluster elects a new leader; when the paused node resumes, it unawarely continues accepting writes.

---

## 3. Engineering Mitigations

### A. Quorum Consensus (Majority Voting)
Require any leader election or write operation to be acknowledged by a strict majority of nodes:
$$\text{Quorum} = \left\lfloor \frac{N}{2} \right\rfloor + 1$$
In a cluster of $N=5$, any partition must have at least 3 nodes to elect a leader or accept writes. A minority partition ($N \le 2$) automatically steps down and refuses writes.

### B. Fencing Tokens
Every elected leader receives a monotonically increasing epoch number (e.g., generation token 42):
- When the leader writes to shared storage, the storage engine verifies that the token $\ge$ the latest seen token.
- If an old "zombie" leader attempts a write with token 41, the storage engine rejects it immediately.

### C. STONITH (Shoot The Other Node In The Head)
Hardware-level fencing via IPMI/PDU where a node power-cycles its rival before declaring leadership.
