# Event Streaming & Distributed Logs

## 1. The Append-Only Commit Log
Unlike traditional message queues, **Event Streaming platforms (Apache Kafka, Apache Pulsar)** treat events as an immutable, ordered, append-only log persisted durably on disk.

```mermaid
flowchart LR
    subgraph Kafka Partition Log
        M0[Offset 0] --> M1[Offset 1] --> M2[Offset 2] --> M3[Offset 3] --> M4[Offset 4]
    end
    
    Consumer1[Real-Time Fraud Consumer: At Offset 4]
    Consumer2[Batch Hadoop Importer: At Offset 1 - Replaying History!]
```

---

## 2. Architectural Distinctions of Event Streams
* **Durability & Replayability**: Events are not deleted upon consumption. Consumers can reset their offset to timestamp $T_0$ and replay years of historical business events.
* **Extreme Throughput**: Employs sequential disk writes and Linux kernel `sendfile` zero-copy network transfer, sustaining gigabytes per second per broker.
