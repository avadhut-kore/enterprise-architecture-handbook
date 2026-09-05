# Change Data Capture (CDC) Architecture (Debezium & Kafka Connect)

Non-intrusive log-based CDC architecture capturing row-level database mutations directly from the database write-ahead log (WAL) without querying source tables.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph SourceDB ["Source Database Engine"]
        App["App Transactions"]
        Tables[("Customer Tables")]
        WAL["Write-Ahead Log (WAL)<br/>[PostgreSQL pgoutput / MySQL binlog]"]

        App -->|"INSERT / UPDATE / DELETE"| Tables
        Tables -.->|"Append to Log"| WAL
    end

    subgraph CDCPipeline ["Debezium CDC Infrastructure"]
        Connector["Debezium PostgreSQL Connector<br/>[Kafka Connect Cluster]"]
        Kafka["Apache Kafka Topic<br/>(schema.customers.mutations)"]
        
        WAL -->|"Stream Logical Replication Stream"| Connector
        Connector -->|"Produce JSON/Avro Event with Before/After State"| Kafka
    end

    subgraph DownstreamConsumers ["Real-Time Replicas & Sinks"]
        CacheSync["Redis Invalidation Consumer"]
        DWLoader["Snowflake Streaming Ingest"]
        AuditLog["Security Compliance Audit Sink"]

        Kafka --> CacheSync
        Kafka --> DWLoader
        Kafka --> AuditLog
    end

    classDef src fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef cdc fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef snk fill:#edf7ed,stroke:#2e7d32,stroke-width:2px;
    class App,Tables,WAL src;
    class Connector,Kafka cdc;
    class CacheSync,DWLoader,AuditLog snk;
```

## PlantUML Specification

```plantuml
@startuml
database "Postgres Tables" as tbl
database "Write-Ahead Log (WAL)" as wal
component "Debezium (Kafka Connect)" as debezium
queue "Kafka Topic (mutations)" as kafka
database "Elasticsearch" as es
database "Snowflake" as sf

tbl -> wal : Transaction committed
wal -> debezium : Read changes directly from WAL
debezium -> kafka : Emit mutation payload (before, after, op)
kafka -> es : Update search cache in real time
kafka -> sf : Stream to analytical warehouse
@enduml
```

## Architectural Design Considerations

* **Zero Database Impact**: Reading from transaction logs avoids executing expensive `SELECT ... WHERE updated_at > ?` polling queries against active production databases.
* **Payload Richness**: Debezium captures full operational metadata: operation type (`c`, `u`, `d`), transaction timestamp, and both `before` and `after` row states.
* **Schema Evolution**: Integrate with Schema Registry to automatically detect and handle upstream column additions or type migrations without crashing consumers.

## Related Documentation & Patterns

* [Event-Driven Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/event-driven.md)
* [Streaming Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/streaming.md)
* [Data Migration](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-migration.md)
