# Real-Time Stream Processing Architecture (Flink & Kafka)

Sub-second streaming analytics pipeline utilizing Apache Kafka for durable message ingestion, Apache Flink for stateful stream computations, and real-time sinks.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph Producers ["Streaming Event Sources"]
        IoT["IoT Telemetry Devices"]
        Clicks["Clickstream Webhook"]
        Orders["Payment Microservice"]
    end

    subgraph IngestionBuffer ["Distributed Event Log"]
        KafkaCluster["Apache Kafka Cluster<br/>[Topics: telemetry, clickstream, orders]<br/>(Replication Factor: 3)"]
        SchemaRegistry["Confluent Schema Registry<br/>[Avro / Protobuf Validation]"]
        
        IoT -->|"MQTT to Kafka Gateway"| KafkaCluster
        Clicks -->|"HTTP Ingestion Proxy"| KafkaCluster
        Orders -->|"Transactional Producer"| KafkaCluster
        KafkaCluster <--> SchemaRegistry
    end

    subgraph StreamCompute ["Stateful Stream Engine (Apache Flink)"]
        FlinkCluster["Flink Streaming JobCluster"]
        RocksDB[("State Store: Embedded RocksDB<br/>(Incremental Checkpoints to S3)")]
        
        KafkaCluster -->|"Consume Partition Streams"| FlinkCluster
        FlinkCluster <--> RocksDB
        
        FlinkCluster --> Window["Tumbling / Sliding Windows (5m aggregation)"]
        Window --> Anomaly["CEP Engine (Fraud & Anomaly Detection)"]
    end

    subgraph RealTimeSinks ["Low-Latency Serving Sinks"]
        RedisCluster[("Redis Real-Time Cache<br/>[Sub-10ms Feature Store]")]
        ClickHouse[("ClickHouse OLAP Database<br/>[High-Throughput Timeseries]")]
        AlertQueue["PagerDuty / Slack Alerting"]

        Anomaly -->|"Real-time Fraud Alerts"| AlertQueue
        Window -->|"Aggregated Metrics"| ClickHouse
        FlinkCluster -->|"User Session State"| RedisCluster
    end

    classDef prod fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef buf fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef stm fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef snk fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class IoT,Clicks,Orders prod;
    class KafkaCluster,SchemaRegistry buf;
    class FlinkCluster,RocksDB,Window,Anomaly stm;
    class RedisCluster,ClickHouse,AlertQueue snk;
```

## PlantUML Specification

```plantuml
@startuml
queue "Kafka Telemetry Topic" as kafka
component "Apache Flink Job" as flink
database "RocksDB State" as state
folder "S3 Checkpoints" as s3
database "ClickHouse OLAP" as ch
database "Redis Cache" as redis

kafka -> flink : Ingest real-time event stream
flink <-> state : Fast local state updates
state -> s3 : Periodic asynchronous checkpoints
flink -> ch : Stream aggregated metrics
flink -> redis : Update user profile counters
@enduml
```

## Architectural Design Considerations

* **Exactly-Once Semantics (EOS)**: Combine Kafka two-phase commit producers with Flink Chandy-Lamport distributed checkpointing to guarantee EOS end-to-end.
* **State Management**: Leverage local RocksDB state storage backed by incremental asynchronous snapshots to cloud object storage (S3).
* **Late Data Handling**: Configure watermarks and allowed lateness windows to correctly handle out-of-order and delayed mobile/IoT events.

## Related Documentation & Patterns

* [Event-Driven Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/event-driven.md)
* [Change Data Capture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/cdc.md)
* [Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md)
