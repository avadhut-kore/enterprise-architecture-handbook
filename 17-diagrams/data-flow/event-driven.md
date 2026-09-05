# Event-Driven Data Architecture & CQRS Pattern

Command Query Responsibility Segregation (CQRS) and event-driven data flow synchronizing write-side commands with read-optimized materialized views.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph CommandSide ["Write Side (Command Processing)"]
        UserCmd["Client POST /orders"]
        CommandAPI["Order Command Service"]
        WriteDB[("Relational Write Store<br/>(PostgreSQL - Bounded Context)")]
        OutboxTable["Transactional Outbox Table"]

        UserCmd --> CommandAPI
        CommandAPI -->|"ACID Transaction"| WriteDB
        CommandAPI -->|"Insert Outbox Record"| OutboxTable
    end

    subgraph EventRelay ["Reliable Event Relay"]
        Debezium["Debezium CDC Engine"]
        EventBroker["Kafka Event Broker<br/>[Topic: order-lifecycle.v1]"]

        OutboxTable -->|"Log-Based Tail"| Debezium
        Debezium -->|"Publish OrderCreated Event"| EventBroker
    end

    subgraph QuerySide ["Read Side (Materialized Views)"]
        EventConsumer["Read Model Projector"]
        Elasticsearch[("Elasticsearch Cluster<br/>(Search Optimized View)")]
        QueryAPI["Order Query Service"]
        UserQuery["Client GET /orders/search"]

        EventBroker -->|"Consume Events"| EventConsumer
        EventConsumer -->|"Index Enriched Document"| Elasticsearch
        UserQuery --> QueryAPI
        QueryAPI -->|"Fast Search Query"| Elasticsearch
    end

    classDef cmd fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef rly fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef qry fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class UserCmd,CommandAPI,WriteDB,OutboxTable cmd;
    class Debezium,EventBroker rly;
    class EventConsumer,Elasticsearch,QueryAPI,UserQuery qry;
```

## PlantUML Specification

```plantuml
@startuml
actor Client
participant "Order Command API" as cmd
database "PostgreSQL (Write DB)" as db
participant "Transactional Outbox" as outbox
queue "Kafka Event Bus" as bus
participant "Read Model Projector" as proj
database "Elasticsearch (Read DB)" as readDB
participant "Order Query API" as qry

Client -> cmd : POST /orders
cmd -> db : Insert Order
cmd -> outbox : Insert Outbox Event (Atomic Tx)
outbox -> bus : Publish Event via CDC
bus -> proj : OrderCreated Event
proj -> readDB : Update Search Index
Client -> qry : GET /orders/search
qry -> readDB : Query Index
readDB -> Client : Fast Response (<20ms)
@enduml
```

## Architectural Design Considerations

* **Transactional Outbox Pattern**: Prevent dual-write anomalies by writing entity mutations and event messages within a single database transaction.
* **Eventual Consistency**: Acknowledge that the read model may lag slightly behind the write model (typically tens of milliseconds).
* **Consumer Idempotency**: Consumers must record processed message identifiers to safely discard duplicate events during rebalances.

## Related Documentation & Patterns

* [Change Data Capture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/cdc.md)
* [Streaming Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/streaming.md)
* [Logical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/logical-data-flow.md)
