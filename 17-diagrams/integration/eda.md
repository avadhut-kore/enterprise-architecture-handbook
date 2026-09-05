# Event-Driven Architecture (EDA) Messaging Paradigms

Comprehensive event-driven integration paradigms comparing Simple Event Notification, Event-Carried State Transfer (ECST), and Event Sourcing.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph Pattern1 ["1. Event Notification (Lightweight)"]
        P1["Order Service"]
        E1["Event: OrderCreated {id: 101}<br/>(Consumer must callback for details)"]
        C1["Shipping Service"]
        P1 --> E1
        E1 --> C1
        C1 -.->|"REST GET /orders/101"| P1
    end

    subgraph Pattern2 ["2. Event-Carried State Transfer (ECST)"]
        P2["Order Service"]
        E2["Event: OrderCreated {id: 101, items: [...], customer: {...}, total: $99}"]
        C2["Shipping Service (Zero Callback Needed)"]
        P2 --> E2
        E2 --> C2
    end

    subgraph Pattern3 ["3. Event Sourcing (State as Log)"]
        P3["Account Service"]
        E3["Event Log: AccountOpened -> Deposited($50) -> Withdrawn($20)"]
        C3["Current Balance = $30 (Derived by Fold/Reduce)"]
        P3 --> E3
        E3 --> C3
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Event Notification" {
  [Producer 1] -> [Event: ID Only]
  [Event: ID Only] -> [Consumer 1]
  [Consumer 1] ..> [Producer 1] : Callback for details
}
package "Event-Carried State Transfer" {
  [Producer 2] -> [Event: Full State Snapshot]
  [Event: Full State Snapshot] -> [Consumer 2]
}
package "Event Sourcing" {
  [Events: Delta 1, Delta 2, Delta 3] -> [Materialized State]
}
@enduml
```

## Architectural Design Considerations

* **Event-Carried State Transfer**: Maximizes consumer autonomy and decouples availability, eliminating downstream query storms on producers.
* **Payload Size Constraints**: Avoid bloating events beyond broker message limits (e.g., Kafka default 1MB); use Claim-Check pattern for large media assets.
* **Schema Evolution Discipline**: Changes to event structures must be non-breaking (e.g., additive fields only).

## Related Documentation & Patterns

* [Event Mesh](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/event-mesh.md)
* [RPC vs Events](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/rpc-vs-events.md)
* [CQRS & Event Sourcing](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/cqrs-es.md)
