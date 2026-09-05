# Enterprise Service Bus (ESB) & Canonical Data Model

Heavyweight enterprise service bus (ESB) integration detailing message mediation, XML/XSLT transformations, and the Canonical Data Model (CDM).

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph SourceApps ["Legacy Producers"]
        Legacy1["Mainframe COBOL (Copybook)"]
        Legacy2["Oracle Financials (SOAP XML)"]
    end

    subgraph ESBRuntime ["Enterprise Service Bus (MuleSoft / TIBCO)"]
        TransformIn["Inbound Protocol Adapter & XSLT Parser"]
        CDM["Canonical Data Model (CDM)<br/>[Enterprise-Standard Common Entity Schema]"]
        Router["Content-Based Message Router"]
        TransformOut["Outbound Protocol Adapter"]

        TransformIn --> CDM
        CDM --> Router
        Router --> TransformOut
    end

    subgraph TargetApps ["Consumer Systems"]
        Target1["Cloud SaaS (REST JSON)"]
        Target2["Data Lakehouse (Parquet S3)"]
    end

    Legacy1 -->|"TCP Socket"| TransformIn
    Legacy2 -->|"HTTP SOAP"| TransformIn
    TransformOut -->|"HTTPS POST"| Target1
    TransformOut -->|"S3 API"| Target2
```

## PlantUML Specification

```plantuml
@startuml
package "Producers" {
  [Mainframe]
  [Oracle DB]
}
package "Enterprise Service Bus" {
  component "Protocol Adapters" as adp1
  component "Canonical Data Model" as cdm
  component "Content-Based Router" as router
  component "Outbound Adapters" as adp2
}
package "Consumers" {
  [Salesforce]
  [Data Lake]
}
[Mainframe] -> adp1
[Oracle DB] -> adp1
adp1 -> cdm : Normalize
cdm -> router
router -> adp2
adp2 -> [Salesforce]
adp2 -> [Data Lake]
@enduml
```

## Architectural Design Considerations

* **Smart Pipes, Dumb Endpoints**: The ESB represents the classic 'smart pipes' philosophy, placing heavy business transformation logic directly inside the integration infrastructure.
* **Architectural Anti-Pattern at Scale**: Can degrade into an unmaintainable monolithic bus where business logic becomes obscured and impossible to test locally.
* **Modern Evolution**: Modern systems replace monolithic ESBs with 'dumb pipes, smart endpoints' (Kafka event streams + microservice consumers).

## Related Documentation & Patterns

* [Hub-and-Spoke](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/hub-and-spoke.md)
* [Modern API Gateway](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/api-gateway.md)
* [Event-Driven Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/eda.md)
