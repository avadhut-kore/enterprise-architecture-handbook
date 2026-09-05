# Macro Enterprise Integration Landscape

High-level enterprise system landscape mapping macro integration channels across core operational platforms, digital customer channels, and cloud data lakes.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph DigitalChannels ["1. Digital Customer Channels"]
        Web["Customer Web Portal"]
        Mobile["Mobile Banking App"]
        PartnerAPI["B2B Open Banking APIs"]
    end

    subgraph IntegrationBackbone ["2. Enterprise Integration Fabric"]
        APIM["Azure API Management Gateway"]
        EventMesh["Kafka Enterprise Event Mesh"]
        ETLHub["Batch Integration Hub (Informatica / Airflow)"]
    end

    subgraph CorePlatforms ["3. Core Business Record Platforms"]
        CoreBanking[("Mainframe Core Banking<br/>(System of Record)")]
        CRM["Salesforce CRM<br/>(System of Engagement)"]
        ERP["SAP S/4HANA<br/>(General Ledger & ERP)"]
    end

    subgraph AnalyticalEcosystem ["4. Enterprise Data & AI Platform"]
        Lakehouse[("Snowflake Data Lakehouse")]
        BI["PowerBI Executive Dashboards"]
        Lakehouse --> BI
    end

    DigitalChannels --> APIM
    APIM --> CorePlatforms
    CorePlatforms --> EventMesh
    EventMesh --> CorePlatforms
    CorePlatforms --> ETLHub
    ETLHub --> Lakehouse
    EventMesh --> Lakehouse
```

## PlantUML Specification

```plantuml
@startuml
package "Digital Channels" {
  [Web Portal]
  [Mobile App]
}
package "Integration Fabric" {
  component "API Management" as apim
  queue "Kafka Event Mesh" as bus
}
package "Core Systems" {
  database "Core Banking Mainframe" as core
  [Salesforce CRM] as crm
  [SAP ERP] as erp
}
package "Analytics" {
  database "Data Lakehouse" as dw
}

[Web Portal] --> apim
apim --> core
apim --> crm
core --> bus
crm --> bus
bus --> dw
erp --> dw
@enduml
```

## Architectural Design Considerations

* **Holistic View**: Provides executive stakeholders and ARB with a single comprehensive picture of enterprise data flows and system couplings.
* **System of Record vs Engagement**: Clearly separate systems of record (mainframes, ERPs) from agile systems of engagement (mobile apps, customer portals).
* **Modernization Roadmap**: Use this landscape to highlight legacy point-to-point connections targeted for decommissioning.

## Related Documentation & Patterns

* [Business Capability Map](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/business-capability-map.md)
* [Application Portfolio](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/enterprise/application-portfolio.md)
* [Integration: Point-to-Point](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/point-to-point.md)
