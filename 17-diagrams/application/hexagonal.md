# Hexagonal Architecture (Ports and Adapters)

Alistair Cockburn's Ports and Adapters architecture isolating pure business domain logic from external drivers and driven infrastructure.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph DrivingAdapters ["Driving / Inbound Adapters (Primary)"]
        REST["REST API Controller Adapter"]
        CLI["CLI Tool Adapter"]
        KafkaIn["Kafka Event Consumer Adapter"]
    end

    subgraph HexagonCore ["Domain Core (The Hexagon)"]
        subgraph InboundPorts ["Inbound Ports (API)"]
            OrderPort["OrderManagementUseCase (Port Interface)"]
        end

        subgraph PureDomain ["Pure Business Domain (Zero External Dependencies)"]
            OrderEntity["Order Aggregate Root"]
            TaxCalc["Domain Policy / Invariants"]
            OrderEntity --- TaxCalc
        end

        subgraph OutboundPorts ["Outbound Ports (SPI)"]
            DBPort["OrderRepositoryPort (Port Interface)"]
            PayPort["PaymentGatewayPort (Port Interface)"]
        end

        OrderPort --> OrderEntity
        OrderEntity --> DBPort
        OrderEntity --> PayPort
    end

    subgraph DrivenAdapters ["Driven / Outbound Adapters (Secondary)"]
        PostgresAdapter["PostgreSQL JPA Repository Adapter"]
        StripeAdapter["Stripe Payment Gateway Client Adapter"]
    end

    REST --> OrderPort
    CLI --> OrderPort
    KafkaIn --> OrderPort

    DBPort --> PostgresAdapter
    PayPort --> StripeAdapter
```

## PlantUML Specification

```plantuml
@startuml
package "Driving Adapters" {
  [REST Controller]
  [Kafka Consumer]
}
node "Hexagon Core" {
  portin "OrderUseCase Port" as inPort
  component "Pure Domain Model" as domain
  portout "OrderRepo Port" as outPort1
  portout "Payment Port" as outPort2
}
package "Driven Adapters" {
  [Postgres Adapter]
  [Stripe Adapter]
}

[REST Controller] --> inPort
inPort --> domain
domain --> outPort1
domain --> outPort2
outPort1 --> [Postgres Adapter]
outPort2 --> [Stripe Adapter]
@enduml
```

## Architectural Design Considerations

* **Dependency Inversion**: The core domain defines interfaces (ports); infrastructure adapters implement them, pointing dependencies inward.
* **Technology Independence**: External libraries (Spring, JPA, AWS SDK) never leak into the domain core.
* **Testability Without Infrastructure**: The entire application core can be tested using in-memory mock adapters without spinning up databases or networks.

## Related Documentation & Patterns

* [Clean Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/clean.md)
* [Layered Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/layered.md)
* [Modular Monolith](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/modular-monolith.md)
