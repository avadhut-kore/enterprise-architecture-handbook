# 14 — Messaging & Event-Driven Architecture Strategy

## Purpose

Messaging and Event-Driven Architecture (EDA) Strategy defines the communication models, transport topologies, broker technologies, and delivery semantics used to exchange asynchronous messages and state-change events across distributed system components.

It achieves **extreme temporal and spatial decoupling**, enabling microservices to operate autonomously without blocking on the availability or latency of downstream systems.

---

## Problem It Solves

- **Cascading Outages**: Prevents a slow or offline third-party dependency (e.g., payment gateway or email vendor) from exhausting thread pools in upstream caller services.
- **Traffic Spikes & Surge Overload**: Acts as a massive shock absorber, flattening a spike of 50,000 requests/second into a smooth, steady stream that backend workers can process at a controlled rate.
- **Tight Coupling & Monolithic Release Trains**: Allows new business services to subscribe to existing event streams without requiring changes or redeployment of producer services.

---

## Inputs

- **Domain Events & Commands**: Domain boundaries and state transitions from Step 09.
- **Throughput & Retention Requirements**: Sizing numbers from Step 07.
- **Delivery Guarantee Requirements**: At-least-once vs. Exactly-once semantics.

---

## Decision Process: Queue vs. Stream Broker Selection

```mermaid
graph TD
    BrokerChoice{What is the primary message lifecycle and consumption pattern?}
    
    BrokerChoice -->|Discrete task workers, individual message ACKs, complex routing| QueueChoice["Adopt Message Queue (RabbitMQ / AWS SQS)<br/>Messages are EPHEMERAL; deleted immediately upon consumer ACK"]
    
    BrokerChoice -->|Immutable audit log, multi-consumer fanout, temporal event replay| StreamChoice["Adopt Event Stream (Apache Kafka / AWS Kinesis)<br/>Messages are PERSISTED on append-only disk log; consumers track offsets"]
    
    BrokerChoice -->|Ultra-low latency, ephemeral in-memory pub/sub, notifications| RedisChoice["Adopt Redis Pub/Sub<br/>Fire-and-forget; zero persistence; sub-millisecond dispatch"]
```

---

## The 3 Message Delivery Semantics

```mermaid
flowchart TD
    subgraph AtMostOnce["1. At-Most-Once Delivery (Best Effort)"]
        A1["Producer sends message once; does not wait for ACK"]
        A2["Consumer acknowledges BEFORE processing"]
        A3["Risk: Messages may be LOST during crashes; never duplicated!"]
        A4["Best For: High-volume telemetry, metrics, IoT sensor data"]
    end

    subgraph AtLeastOnce["2. At-Least-Once Delivery (Production Standard)"]
        B1["Producer retries until broker sends durable ACK"]
        B2["Consumer acknowledges AFTER processing completes"]
        B3["Consequence: ZERO message loss; but DUPLICATES CAN OCCUR!"]
        B4["Mandate: Requires IDEMPOTENT consumers to handle duplicates safely!"]
    end

    subgraph ExactlyOnce["3. Exactly-Once Processing (Transactional Coordination)"]
        C1["Kafka Transactions (Read-Process-Write) + Idempotent Producers"]
        C2["High coordination overhead; limited to bounded stream-to-stream topologies"]
        C3["Best For: Financial stream processing pipelines"]
    end
```

---

## Ensuring Zero Message Loss: The Transactional Outbox Pattern

A classic distributed systems failure occurs when an application commits a state change to its database, but crashes before publishing the event to Kafka ("Dual-Write Failure"):

```mermaid
sequenceDiagram
    autonumber
    participant App as Order Application Service
    participant DB as PostgreSQL Database
    participant CDC as Debezium CDC Relay
    participant Kafka as Apache Kafka Broker

    rect rgb(235, 245, 255)
    Note over App,DB: ATOMIC LOCAL DATABASE TRANSACTION
    App->>DB: 1. INSERT INTO orders (id, total, status) VALUES (...)
    App->>DB: 2. INSERT INTO outbox_table (event_type, payload) VALUES (...)
    App->>DB: 3. COMMIT TRANSACTION (Both succeed or both fail!)
    end

    CDC->>DB: 4. Poll / Read PostgreSQL Write-Ahead Log (WAL)
    CDC->>Kafka: 5. Publish OrderPlacedEvent to 'orders.v1' topic
    CDC->>DB: 6. Mark outbox row as processed (or delete)
```

---

## Consumer Error Handling: Dead Letter Queues (DLQ) & Retry Topics

Never let a malformed message ("poison pill") crash a consumer worker repeatedly, blocking the entire queue:

```mermaid
flowchart LR
    Topic["Primary Topic<br/>(orders.v1)"] --> Worker["Consumer Worker"]
    Worker -->|Exception: Network Timeout| Retry1["Retry Topic 1<br/>(Delay: 30s)"]
    Retry1 --> WorkerRetry["Retry Worker"]
    WorkerRetry -->|Exception: Deserialization / Syntax Error| DLQ["Dead Letter Queue (DLQ)<br/>(Quarantined for SRE Triage)"]
    DLQ --> Alert["PagerDuty Alert / SRE Admin UI"]
```

---

## Important Probing Questions

- *What happens if messages arrive out of order? Can consumers tolerate reordering, or is strict partition-key ordering mandatory?*
- *How are message schemas governed across teams? Are we using an Avro / Protobuf Schema Registry?*
- *What is the message retention policy on the broker (e.g., 7 days vs. 30 days vs. infinite)?*
- *What is the maximum acceptable consumer lag before alerting fires?*

---

## Common Mistakes

- **Assuming "Exactly-Once" is Magic**: Believing that setting `enable.idempotence=true` in Kafka eliminates the need to write idempotent consumer business logic. (End-to-end exactly-once requires idempotency keys at the application database layer).
- **Unbounded Queue Buildup**: Allowing queues to grow indefinitely without dead-letter limits, eventually exhausting broker disk space and causing total messaging collapse.
- **Mega-Payloads in Messages**: Sending 20 MB files through Kafka topics instead of uploading the binary to S3 and passing an S3 URI in the event payload (**Claim-Check Pattern**).

---

## Trade-offs

| Messaging Strategy | Advantage | Trade-Off / Cost |
|:---|:---|:---|
| **Event Streaming (Kafka)** | Immutable audit log; multi-consumer replay; extreme throughput. | High operational complexity (Zookeeper/KRaft, partition sizing, consumer lag). |
| **Simple Managed Queues (SQS)**| Zero server maintenance; simple pay-per-message pricing; auto-scaling. | Cannot replay historical messages; lacks multi-subscriber non-destructive reads. |

---

## Production Considerations

- Monitor **Consumer Lag**: Alert when the difference between the latest partition offset and the consumer group's committed offset exceeds defined thresholds.
- Enforce **Schema Compatibility Modes (BACKWARD / FULL)** in the Schema Registry to prevent producer deployments from breaking downstream consumers.
