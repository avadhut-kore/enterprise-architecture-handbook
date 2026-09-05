# Enterprise Architecture Diagram Starter Template

Production-ready boilerplate template for authoring enterprise-level capability mappings, application portfolios, and cross-enterprise system landscapes.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph BusinessLayer ["1. Business Architecture Layer"]
        B1["Business Capability: Customer Management"]
        B2["Business Process: Order Fulfillment Workflow"]
        B1 --- B2
    end

    subgraph ApplicationLayer ["2. Application Architecture Layer"]
        A1["Application Service: CRM SaaS"]
        A2["Application Service: Custom Order Engine"]
        B1 -.-> A1
        B2 -.-> A2
    end

    subgraph TechnologyLayer ["3. Technology & Infrastructure Layer"]
        T1["PaaS Container Runtime (Kubernetes)"]
        T2["Relational Database Storage (Postgres)"]
        A2 --> T1
        A2 --> T2
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Business Architecture" {
  [Business Capability]
}
package "Application Architecture" {
  [Application Component]
}
package "Technology Architecture" {
  node "Hosting Infrastructure" as infra
}
[Business Capability] ..> [Application Component] : Realized by
[Application Component] --> infra : Hosted on
@enduml
```

## Architectural Design Considerations

* **TOGAF Alignment**: Standardizes the tripartite alignment between Business Architecture, Application Architecture, and Technology Architecture.
* **Traceable Value**: Shows how technical infrastructure investments directly support core business capabilities.
* **Consistent Layout**: Business layer on top, application layer in the middle, technology layer at the bottom.

## Related Documentation & Patterns

* [Business Capability Map](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/business-capability-map.md)
* [Application Portfolio](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/application-portfolio.md)
* [Enterprise Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/checklists.md)
