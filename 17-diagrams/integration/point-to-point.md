# Point-to-Point Integration Anti-Pattern (N*(N-1)/2 Spaghetti)

Point-to-point architectural topology illustrating the quadratic connection explosion and coupling nightmare of direct system-to-system integrations.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph SpaghettiIntegrations ["Point-to-Point Integration Web (6 Systems = 15 Connections)"]
        CRM["Salesforce CRM"]
        ERP["SAP ERP"]
        Billing["Zuora Billing"]
        WMS["Warehouse System"]
        Portal["Customer Web Portal"]
        BI["Analytics DB"]

        CRM <--> ERP
        CRM <--> Billing
        CRM <--> WMS
        CRM <--> Portal
        CRM <--> BI

        ERP <--> Billing
        ERP <--> WMS
        ERP <--> Portal
        ERP <--> BI

        Billing <--> WMS
        Billing <--> Portal
        Billing <--> BI

        WMS <--> Portal
        WMS <--> BI

        Portal <--> BI
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Point-to-Point Architecture" {
  [CRM] <--> [ERP]
  [CRM] <--> [Billing]
  [CRM] <--> [WMS]
  [ERP] <--> [Billing]
  [ERP] <--> [WMS]
  [Billing] <--> [WMS]
}
note right of [CRM] : N*(N-1)/2 Connections: High Coupling
@enduml
```

## Architectural Design Considerations

* **Quadratic Complexity**: For $N$ systems, point-to-point requires $N(N-1)/2$ integrations, causing catastrophic maintenance overhead.
* **Coupling & Fragility**: A change to a single internal schema or API breaks multiple direct consumers simultaneously.
* **Migration Strategy**: Break point-to-point coupling by introducing an intermediate API Gateway, Canonical Data Model, or Event Broker.

## Related Documentation & Patterns

* [Hub-and-Spoke](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/hub-and-spoke.md)
* [Modern API Gateway](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/api-gateway.md)
* [Event Mesh](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/event-mesh.md)
