# Modular Monolith Architecture (In-Process Bounded Contexts)

Clean in-process modular monolith enforcing strict module boundaries, explicit public APIs, and zero out-of-process network latency.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph MonolithProcess ["Single OS Process / Single Deployment Unit"]
        Host["Monolith Host Runtime (JVM / .NET Runtime)"]

        subgraph OrderModule ["Module: Orders"]
            OrderAPI["Order Public API Interface"]
            OrderInternal["Order Internal Service & Entities"]
            OrderAPI --> OrderInternal
        end

        subgraph CustomerModule ["Module: Customers"]
            CustAPI["Customer Public API Interface"]
            CustInternal["Customer Internal Service & Entities"]
            CustAPI --> CustInternal
        end

        subgraph InventoryModule ["Module: Inventory"]
            InvAPI["Inventory Public API Interface"]
            InvInternal["Inventory Internal Service & Entities"]
            InvAPI --> InvInternal
        end

        InProcBus["In-Memory Event Dispatcher (Spring ApplicationEvent / MediatR)"]

        OrderInternal -->|"In-Memory Method Call"| CustAPI
        OrderInternal -->|"In-Process Event"| InProcBus
        InProcBus --> InvAPI
    end

    subgraph RelationalStore ["Single Database with Schema Isolation"]
        DB[("PostgreSQL Database<br/>- schema: orders<br/>- schema: customers<br/>- schema: inventory")]
    end

    OrderInternal --> DB
    CustInternal --> DB
    InvInternal --> DB
```

## PlantUML Specification

```plantuml
@startuml
package "Modular Monolith Process" {
  component "Orders Module" as orders {
    [Order Public API]
    [Order Internals]
  }
  component "Customers Module" as customers {
    [Customer Public API]
    [Customer Internals]
  }
  component "In-Memory Event Bus" as bus
}
database "Isolated DB Schemas" as db

[Order Internals] --> [Customer Public API] : Direct In-Memory Call
[Order Internals] --> bus : Emit In-Process Event
bus --> [Customers Module]
orders --> db : orders schema
customers --> db : customers schema
@enduml
```

## Architectural Design Considerations

* **Zero Distributed System Overhead**: Eliminates network serialization, distributed transactions, and complex Kubernetes orchestration during early organizational stages.
* **Enforced Package Boundaries**: Leverage architectural unit tests (e.g., ArchUnit) to prevent Module A from importing internal classes of Module B.
* **Migration Stepping Stone**: A well-structured modular monolith can be decomposed into standalone microservices when team scale demands it.

## Related Documentation & Patterns

* [Microservices](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/microservices.md)
* [Layered Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/layered.md)
* [Hexagonal Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/hexagonal.md)
