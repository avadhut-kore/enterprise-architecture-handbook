# PACELC Theorem

## 1. Beyond CAP: What Happens in the Normal State?
The CAP theorem only analyzes system behavior **during an active network partition**. However, systems operate in normal, healthy state $99.9\%$ of the time. Daniel Abadi formulated the **PACELC Theorem** to capture the complete trade-off spectrum:

$$\text{If } \mathbf{P} \text{ (Partition)} \rightarrow \text{Choose } \mathbf{A} \text{ or } \mathbf{C}; \quad \text{Else } \mathbf{E} \rightarrow \text{Choose } \mathbf{L} \text{ (Latency) or } \mathbf{C} \text{ (Consistency)}.$$

```mermaid
flowchart TD
    Start{Network Partition Present?}
    Start -->|Yes: P| PartitionChoice{Choose A or C}
    PartitionChoice -->|A| AP[Available under Partition: e.g. Dynamo / Cassandra]
    PartitionChoice -->|C| CP[Consistent under Partition: e.g. Spanner / ZooKeeper]
    
    Start -->|No: E (Normal State)| NormalChoice{Choose L or C}
    NormalChoice -->|L| EL[Low Latency: Asynchronous Replicas]
    NormalChoice -->|C| EC[Strong Consistency: Synchronous Consensus round-trips]
```

---

## 2. Distributed Database Classification Matrix

| System | Classification | Normal State Trade-off | Partition State Trade-off |
| :--- | :--- | :--- | :--- |
| **Apache Cassandra** | **PA/EL** | Sacrifices consistency for sub-millisecond write latency ($L$). | Continues operating locally ($A$). |
| **Amazon DynamoDB** (Default) | **PA/EL** | Async replication optimizes read latency ($L$). | Local partition availability ($A$). |
| **Google Cloud Spanner** | **PC/EC** | Enforces Paxos consensus; pays latency penalty ($C$). | Rejects writes if quorum unreachable ($C$). |
| **PostgreSQL (Sync Replica)**| **PC/EC** | Blocks commit until replica flushes ($C$). | Master freezes writes if replica dies ($C$). |
| **MongoDB** (Configurable) | **PA/EC** or **PC/EC** | Depends on `ReadConcern` and `WriteConcern`. | Depends on primary election quorum. |
