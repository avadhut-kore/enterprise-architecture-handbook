# Reference Architecture 03: Event-Driven & Streaming Observability

## 1. System Context & Overview
Asynchronous event-driven systems (built on Apache Kafka, Apache Pulsar, and Apache Flink) decouple producers and consumers across time. Standard HTTP distributed trace propagation breaks because events sit in topics for seconds, minutes, or hours before being processed.

This reference architecture implements **W3C Trace Context Record Header Propagation** and **Consumer Lag Telemetry**.

See visual modeling in [`../../17-diagrams/sequence/event-driven.md`](../../17-diagrams/sequence/event-driven.md).

---

## 2. Architecture Diagram

```mermaid
flowchart LR
    subgraph Producer_Service ["Order Producer Service"]
        P_App["Order API Service"]
        P_SDK["OTel Tracing SDK"]
        P_App -->|Create Order| P_SDK
    end

    subgraph Kafka_Cluster ["Apache Kafka Streaming Cluster"]
        Topic["Kafka Topic: 'orders.v1'\n[Record 101]\n- Key: order_123\n- Header 'traceparent': 00-4bf92f35...-01\n- Header 'tracestate': enterprise=prod\n- Payload: { ... }"]
    end

    subgraph Consumer_Services ["Consumer Ecosystem"]
        subgraph Payments ["Payment Consumer"]
            C1_SDK["OTel SDK (Extracts Header)"]
            C1_App["Process Charge"]
            C1_SDK --> C1_App
        end

        subgraph Inventory ["Inventory Consumer"]
            C2_SDK["OTel SDK (Extracts Header)"]
            C2_App["Reserve Stock"]
            C2_SDK --> C2_App
        end
    end

    P_SDK -->|Produce Event + Inject Header| Topic
    Topic -->|Consume Record| C1_SDK
    Topic -->|Consume Record| C2_SDK

    subgraph Monitoring ["Streaming Health Monitoring"]
        Burrow["Kafka Exporter / Burrow\n- Consumer Group Lag\n- Partition Offset Drift"]
        Grafana["Streaming Lag Dashboard"]
        Burrow --> Grafana
    end
```

---

## 3. Key Architectural Decisions
1. **Trace Context in Record Headers**: The OpenTelemetry Kafka interceptor automatically serializes the active W3C `traceparent` string into binary record headers during `producer.send()`. Consumers extract the header to establish a `ChildOf` or `FollowsFrom` trace span.
2. **FollowsFrom vs ChildOf Spans**: High-latency batch consumers use OpenTelemetry `FollowsFrom` span links rather than direct child spans, ensuring long queue wait times do not distort the producer's synchronous latency metrics.
3. **Consumer Lag SLIs**: Alerting rules evaluate **Consumer Lag Time (seconds behind head)** rather than raw message count, ensuring low-volume slow partitions trigger pages before queue saturation.
