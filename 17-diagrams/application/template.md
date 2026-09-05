# Application Architecture Starter Template

Production-ready boilerplate template for modeling domain aggregates, application services, driving/driven adapters, and database connections.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph InboundLayer ["Inbound Adapters"]
        API["Web REST Controller"]
        Consumer["Event Bus Consumer"]
    end

    subgraph ApplicationBoundary ["Application Core"]
        AppSvc["Application Service Orchestrator"]
        DomainModel["Domain Aggregates & Business Rules"]
        AppSvc --> DomainModel
    end

    subgraph OutboundLayer ["Outbound Adapters"]
        RepoAdapter["Database Persistence Adapter"]
        MsgAdapter["Message Publisher Adapter"]
    end

    subgraph ExternalInfrastructure ["External Infrastructure"]
        DB[(PostgreSQL Store)]
        Queue["Kafka Event Bus"]
    end

    API --> AppSvc
    Consumer --> AppSvc
    AppSvc --> RepoAdapter
    AppSvc --> MsgAdapter
    RepoAdapter --> DB
    MsgAdapter --> Queue
```

## PlantUML Specification

```plantuml
@startuml
package "Inbound Adapters" {
  [REST API]
  [Queue Consumer]
}
package "Application Domain" {
  [Application Service] --> [Domain Entity]
}
package "Outbound Adapters" {
  [Repository Adapter]
  [Publisher Adapter]
}
[REST API] --> [Application Service]
[Queue Consumer] --> [Application Service]
[Application Service] --> [Repository Adapter]
[Application Service] --> [Publisher Adapter]
@enduml
```

## Architectural Design Considerations

* **Standard Starter**: Use this template when documenting new microservices or bounded contexts.
* **Explicit Boundaries**: Separate adapters from pure business rules to maximize long-term maintainability.
* **Symmetrical Layout**: Inbound on top/left, core in center, outbound on bottom/right.

## Related Documentation & Patterns

* [Clean Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/clean.md)
* [Hexagonal Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/hexagonal.md)
* [Application Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/checklists.md)
