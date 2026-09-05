# Azure Enterprise Landing Zone (CAF Management Group Hierarchy)

Microsoft Cloud Adoption Framework (CAF) enterprise-scale landing zone detailing Management Groups, Subscriptions, Azure Policy, and Hub-Spoke virtual networks.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph AzureTenant ["Entra ID Tenant (Azure Active Directory)"]
        RootMG["Root Management Group (Tenant Root)"]
    end

    subgraph TopLevelMGs ["Management Group Hierarchy"]
        PlatformMG["Platform Management Group"]
        LandingZonesMG["Landing Zones Management Group"]
        SandboxMG["Sandbox Management Group"]

        RootMG --> PlatformMG
        RootMG --> LandingZonesMG
        RootMG --> SandboxMG
    end

    subgraph PlatformSubs ["Platform Subscriptions"]
        SubNet["Connectivity Subscription<br/>(Virtual WAN / Hub VNet / Azure Firewall)"]
        SubIdentity["Identity Subscription<br/>(Domain Controllers, Key Vault)"]
        SubSec["Management Subscription<br/>(Log Analytics Workspace, Sentinel)"]

        PlatformMG --> SubNet
        PlatformMG --> SubIdentity
        PlatformMG --> SubSec
    end

    subgraph WorkloadSubs ["Workload Subscriptions"]
        subgraph CorpTier ["Corp (Connected)"]
            SubCorpProd["Online Banking Production Sub<br/>(Spoke VNet)"]
        end
        subgraph OnlineTier ["Online (Public Ingress)"]
            SubOnline["E-Commerce Public Sub<br/>(App Gateway / Front Door)"]
        end

        LandingZonesMG --> CorpTier
        LandingZonesMG --> OnlineTier
    end

    SubNet <-->|"VNet Peering"| SubCorpProd
    SubCorpProd -.->|"Diagnostic Metrics"| SubSec
```

## PlantUML Specification

```plantuml
@startuml
package "Azure Tenant Root" {
  node "Platform Management Group" as mgPlat {
    [Connectivity Subscription]
    [Identity Subscription]
    [Management Subscription]
  }
  node "Landing Zones MG" as mgLZ {
    [Production Workload Sub]
    [Non-Prod Workload Sub]
  }
}
[Connectivity Subscription] <--> [Production Workload Sub] : VNet Peering
[Production Workload Sub] --> [Management Subscription] : Azure Monitor Logs
@enduml
```

## Architectural Design Considerations

* **Management Group Inheritance**: Azure Policies and RBAC assignments configured at higher Management Groups automatically inherit downward across all child subscriptions.
* **Dedicated Platform Subscriptions**: Segregate network routing (Connectivity), centralized logging (Management), and authentication (Identity) into separate subscriptions to prevent noisy-neighbor quota exhaustion.
* **Hub-and-Spoke Connectivity**: Force all inter-subscription communication through the Hub VNet's Azure Firewall for inspection and micro-segmentation.

## Related Documentation & Patterns

* [AWS Well-Architected](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/aws-well-architected.md)
* [GCP Enterprise Foundations](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/gcp-enterprise-foundations.md)
* [Network: Hub and Spoke](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/hub-spoke.md)
