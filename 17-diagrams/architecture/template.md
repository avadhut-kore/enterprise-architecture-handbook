# Architecture Blueprint Starter Template

Standardized enterprise architecture blueprint starter template covering ingress, application services, messaging integration, and storage.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph ClientPerimeter ["1. Client & Ingress Zone"]
        ClientApp["Browser / Mobile Client"]
        Gateway["API Gateway / Reverse Proxy"]
        ClientApp -->|"HTTPS / TLS 1.3"| Gateway
    end

    subgraph ApplicationPerimeter ["2. Core Application Domain"]
        ServiceA["Domain Service A (Primary API)"]
        ServiceB["Domain Service B (Worker/Processor)"]
        Gateway --> ServiceA
        ServiceA -->|"Internal Call"| ServiceB
    end

    subgraph MessagingTier ["3. Event & Messaging Bus"]
        MessageBroker["Event Broker / Queue (Kafka / SQS)"]
        ServiceA -->|"Publish Domain Events"| MessageBroker
        MessageBroker -->|"Consume"| ServiceB
    end

    subgraph DataStoragePerimeter ["4. Persistence Tier"]
        MainDB[("Primary Database (PostgreSQL)")]
        CacheStore[("In-Memory Cache (Redis)")]
        ServiceA --> MainDB
        ServiceA --> CacheStore
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Client Ingress" {
  [Client] --> [Gateway]
}
package "Application Services" {
  [Gateway] --> [Service A]
  [Service A] --> [Service B]
}
package "Data & Events" {
  database "PostgreSQL" as db
  queue "Kafka" as kafka
  [Service A] --> db
  [Service A] --> kafka
}
@enduml
```

## Architectural Design Considerations

* **Reusable Baseline**: Copy and adapt this template when beginning new high-level architectural proposals.
* **Distinct Tiers**: Maintain clear separation between presentation, application logic, messaging, and persistence tiers.
* **Explicit Flow Direction**: Enforce top-to-bottom or left-to-right flow directionality for visual consistency.

## Related Documentation & Patterns

* [High-Level Design](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/high-level-design.md)
* [Diagramming Standard](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/diagramming-standard.md)
* [Architecture Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/checklists.md)
