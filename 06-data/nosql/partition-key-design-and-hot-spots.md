# NoSQL Architecture: Partition Key Design & Hot Partition Mitigation

## 1. Architectural Purpose & Problem Context
Designing uniform hash distributions: salt keys, composite keys, avoiding sequential timestamps, and detecting write/read throttle throttles.

---

## 2. Distributed Storage & Topology Model

```mermaid
flowchart LR
    subgraph Client Application
        App[Application Client / SDK]
    end
    subgraph Distributed Cluster Ring
        NodeA[Storage Node A: Partition Hash 0-33%]
        NodeB[Storage Node B: Partition Hash 34-66%]
        NodeC[Storage Node C: Partition Hash 67-100%]
    end

    App -->|Hash(PartitionKey)| NodeA
    NodeA -.->|Replicate R+W>N| NodeB
    NodeB -.->|Replicate| NodeC
```

---

## 3. Production Invariants & Operational Rules
- Model schemas around specific query access patterns; NoSQL databases do not perform efficient ad-hoc table joins.
- Always monitor for hot partitions caused by monotonically increasing or poorly distributed partition keys.
- Understand write concern and read consistency levels: strong consistency reduces availability during network partitions.
