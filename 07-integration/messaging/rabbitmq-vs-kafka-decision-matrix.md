# Technology Comparison: RabbitMQ vs Apache Kafka

## 1. Architectural Context & Paradigm Differences
RabbitMQ is a traditional message broker optimized for complex routing, flexible queuing, and transient message distribution. Apache Kafka is an append-only distributed commit log optimized for high-throughput stream processing, long-term retention, and replayability.

---

## 2. Comprehensive Decision Criteria Matrix

| Evaluation Dimension | RabbitMQ (AMQP) | Apache Kafka | Architectural Recommendation |
|---|---|---|---|
| **Primary Architectural Pattern** | Message Queuing / Smart Broker | Event Streaming / Dumb Broker, Smart Consumer | Choose RabbitMQ for task queues; Kafka for event logs |
| **Message Consumption Model** | Destructive read (acknowledged messages deleted) | Non-destructive read (offset advancement, messages retained) | Kafka when multiple independent consumers need replay |
| **Routing Flexibility** | Extreme (Direct, Topic, Fanout, Headers, Dead-Letter) | Fixed (Key-based partition routing) | RabbitMQ for dynamic routing rules |
| **Throughput Ceiling** | Moderate (10k - 80k msgs/sec per node) | Planetary (500k - 2M+ msgs/sec per cluster) | Kafka for high-volume telemetry & clickstreams |
| **Latency Profile** | Sub-millisecond (very low) | Low (2 - 15ms batching latency) | RabbitMQ for instant RPC / real-time commands |
| **Message Ordering** | Per-queue FIFO (degraded with multiple consumers) | Strict per-partition ordering | Kafka for strict partition-keyed order |
| **Replayability** | None (unless manually archived) | Full deterministic replay from beginning or offset | Kafka for event sourcing & audit streams |
| **Operational Complexity** | Low - Moderate (Erlang runtime, clustering) | Moderate - High (JVM tuning, partition planning, KRaft) | RabbitMQ for smaller teams & lower TCO |

---

## 3. Decision Guidelines
- **Choose RabbitMQ when**: Workload requires point-to-point task queues, complex topic/header routing, individual message acknowledgements, or immediate destruction upon completion.
- **Choose Kafka when**: Workload requires high-throughput streaming, historical replay, multiple independent consumer groups reading the same event log, or log compaction.
