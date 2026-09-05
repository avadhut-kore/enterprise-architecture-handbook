# Cloud Architecture Blueprint Starter Template

Standardized enterprise cloud landing zone template covering management accounts, shared networking hubs, and segregated workload environments.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph ManagementTier ["1. Identity & Management"]
        Identity["Enterprise IdP / SSO"]
        ManagementAcc["Central Management & Billing Account"]
        Identity --> ManagementAcc
    end

    subgraph HubNetworkTier ["2. Shared Networking Hub"]
        Firewall["Cloud Next-Gen Firewall / WAF"]
        TransitHub["Transit Gateway / Virtual WAN Hub"]
        ManagementAcc --> TransitHub
        TransitHub <--> Firewall
    end

    subgraph WorkloadTier ["3. Segregated Workload Environments"]
        subgraph ProdSub ["Production Account / VNet"]
            ProdApp["Production Microservices (Private)"]
            ProdDB[(Encrypted Database)]
            ProdApp --> ProdDB
        end
        subgraph NonProdSub ["Non-Production Account / VNet"]
            DevApp["Development Microservices"]
            DevDB[(Dev Database)]
            DevApp --> DevDB
        end

        TransitHub <-->|"Inspected Routes"| ProdApp
        TransitHub <-->|"Inspected Routes"| DevApp
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Management" {
  [Enterprise SSO] --> [Management Account]
}
package "Networking Hub" {
  [Transit Gateway] <--> [Central Firewall]
}
package "Workloads" {
  node "Production" {
    [Prod App] --> [Prod DB]
  }
  node "Non-Production" {
    [Dev App] --> [Dev DB]
  }
}
[Transit Gateway] <--> [Prod App]
[Transit Gateway] <--> [Dev App]
@enduml
```

## Architectural Design Considerations

* **Standard Starter**: Copy and adapt this template when designing multi-account or multi-subscription cloud architectures.
* **Network Isolation**: Ensure production and non-production accounts are strictly isolated at the routing and policy layer.
* **Security Guardrails**: Mandate encryption and logging guardrails across all child accounts.

## Related Documentation & Patterns

* [AWS Well-Architected](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/aws-well-architected.md)
* [Azure Enterprise Landing Zone](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/azure-enterprise-landing-zone.md)
* [Cloud Architecture Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/checklists.md)
