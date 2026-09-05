# Integration Architecture Starter Template

Standardized template for modeling multi-system integration topologies across API gateways, message buses, and external partners.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph ProducerZone ["System Producers"]
        SourceA["Internal Core Application"]
        SourceB["External B2B Partner"]
    end

    subgraph IntegrationBus ["Enterprise Integration Layer"]
        Gateway["Enterprise API Gateway"]
        Broker["Distributed Message Broker (Kafka / MQ)"]
        SourceA --> Gateway
        SourceB --> Gateway
        Gateway -->|"Async Events"| Broker
    end

    subgraph ConsumerZone ["Target Consumers & Sinks"]
        ConsumerA["Fulfillment Service"]
        ConsumerB["Analytics Lakehouse"]
        Gateway -->|"Sync RPC"| ConsumerA
        Broker -->|"Consume"| ConsumerA
        Broker -->|"Ingest"| ConsumerB
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Producers" {
  [System A]
  [System B]
}
package "Integration Layer" {
  [API Gateway]
  queue "Event Bus" as bus
}
package "Consumers" {
  [Target App]
  [Data Warehouse]
}
[System A] --> [API Gateway]
[System B] --> [API Gateway]
[API Gateway] --> bus
bus --> [Target App]
bus --> [Data Warehouse]
@enduml
```

## Architectural Design Considerations

* **Standard Starter**: Copy and adapt this template when mapping integration touchpoints between disparate systems.
* **Protocol Annotations**: Clearly label protocols (REST, gRPC, SFTP, Kafka) directly on connections.
* **Separation of Concerns**: Differentiate real-time synchronous APIs from asynchronous event queues.

## Related Documentation & Patterns

* [Modern API Gateway](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/api-gateway.md)
* [Event-Driven Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/eda.md)
* [Integration Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/checklists.md)
