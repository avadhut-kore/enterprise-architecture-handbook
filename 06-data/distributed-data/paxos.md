# Paxos Consensus Protocol

## 1. Foundations of Paxos
Formulated by Leslie Lamport (1998), **Paxos** is the foundational consensus protocol proving how distributed state machines can safely reach consensus across asynchronous, unreliable networks.

```mermaid
sequenceDiagram
    autonumber
    participant P as Proposer
    participant A1 as Acceptor 1
    participant A2 as Acceptor 2
    participant A3 as Acceptor 3
    
    Note over P,A3: Phase 1: Prepare Phase
    P->>A1: Prepare(n=101)
    P->>A2: Prepare(n=101)
    A1-->>P: Promise(n=101, max_accepted_val=null)
    A2-->>P: Promise(n=101, max_accepted_val=null)
    
    Note over P,A3: Phase 2: Accept Phase
    P->>A1: Accept(n=101, value="SET X=5")
    P->>A2: Accept(n=101, value="SET X=5")
    A1-->>P: Accepted(n=101)
    A2-->>P: Accepted(n=101)
    Note over P,A3: Consensus Reached on "SET X=5"!
```

---

## 2. Basic Paxos vs. Multi-Paxos
* **Basic Paxos**: Reaches consensus on a single value (single decree). Requires 2 network round-trips per value.
* **Multi-Paxos**: Elects a stable long-term leader, bypassing Phase 1 for subsequent log appends, reducing write latency to **1 network round-trip** ($2\text{ RTT} \rightarrow 1\text{ RTT}$).
