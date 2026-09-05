# CQRS and Event Sourcing (CQRS/ES) Architectural Model

Complete CQRS and Event Sourcing architecture detailing immutable event store journals, domain aggregates, projection workers, and read models.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph CommandTier ["Command Side (Writes)"]
        ClientCmd["Client POST /orders"]
        CmdHandler["CreateOrderCommandHandler"]
        Aggregate["OrderAggregate Root"]
        EventStore[("Immutable Event Store<br/>(EventStoreDB / PostgreSQL)<br/>- OrderCreated<br/>- ItemAdded<br/>- OrderPaid")]

        ClientCmd --> CmdHandler
        CmdHandler --> Aggregate
        Aggregate -->|"Append Uncommitted Events"| EventStore
    end

    subgraph EventStreamProjectors ["Projection & Materialization"]
        Projector["Async Read Model Projector (Worker Pod)"]
        EventStore -->|"Stream Committed Events"| Projector
    end

    subgraph QueryTier ["Query Side (Reads)"]
        ReadDB[("Read-Optimized Store<br/>(Elasticsearch / Read Replica)")]
        QueryHandler["OrderQueryService"]
        ClientQuery["Client GET /orders/summary"]

        Projector -->|"Materialize View"| ReadDB
        ClientQuery --> QueryHandler
        QueryHandler -->|"Fast Query"| ReadDB
    end
```

## PlantUML Specification

```plantuml
@startuml
actor Client
participant "Command API" as cmd
participant "Domain Aggregate" as agg
database "Event Store (Append Only)" as es
participant "Read Projector" as proj
database "Read Model (Elasticsearch)" as readDB
participant "Query API" as qry

Client -> cmd : Submit Command
cmd -> agg : Execute Business Invariant
agg -> es : Append Event (e.g. OrderCreated)
es -> proj : Stream New Event
proj -> readDB : Update Materialized View
Client -> qry : Query View
qry -> readDB : Fast Search
readDB -> Client : View Payload
@enduml
```

## Architectural Design Considerations

* **Complete Audit Trail**: The Event Store contains an immutable, complete history of every change that has ever occurred in the domain.
* **Temporal Replay**: Historical state can be replayed to regenerate broken read models or build brand-new projections retrospectively.
* **Eventual Consistency Window**: Clients must be architected to handle the brief latency between command commit and read model materialization.

## Related Documentation & Patterns

* [Event-Driven Application](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/event-driven.md)
* [Data-Flow: Event-Driven](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/event-driven.md)
* [Hexagonal Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/hexagonal.md)
