# Kafka Architecture: Topics, Partitions & Replication Topology

## 1. Architectural Purpose & Problem Context
Leader and follower replica mechanics, In-Sync Replicas (ISR), `min.insync.replicas`, and partition sizing rules of thumb.

---

## 2. Kafka Cluster Topology & Partition Flow

```mermaid
flowchart TD
    subgraph Producers
        P1[Order Producer]
        P2[Payment Producer]
    end
    subgraph Kafka Cluster KRaft
        Topic[Topic: orders.v1]
        Part0[Partition 0: Leader Broker 1, ISR 1,2]
        Part1[Partition 1: Leader Broker 2, ISR 2,3]
        Part2[Partition 2: Leader Broker 3, ISR 3,1]
    end
    subgraph Consumer Group
        C1[Consumer Instance 1]
        C2[Consumer Instance 2]
    end

    P1 -->|Hash(OrderId)| Part0
    P2 -->|Hash(OrderId)| Part1
    Part0 --> C1
    Part1 --> C2
    Part2 --> C1
```

---

## 3. Production Invariants
- For zero data loss, always configure producers with `acks=all` and topics with `min.insync.replicas=2` (with replication factor 3).
- Kafka alone does not provide end-to-end exactly-once guarantees to external databases; consumer handlers must still be idempotent.
- Never adopt Kafka when simple queue semantics (e.g., RabbitMQ or SQS) are all that is required for transient work distribution.
