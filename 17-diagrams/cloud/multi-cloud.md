# Multi-Cloud & Hybrid Enterprise Topology

High-resilience enterprise architecture interconnecting on-premises private data centers, AWS, and Azure via redundant colocation transit centers (Equinix / Megaport).

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph OnPremEstate ["On-Premises Corporate DC"]
        DCRouters["Edge Border Routers (BGP)"]
        DCWorkloads["Core Legacy Banking Systems"]
        DCRouters --- DCWorkloads
    end

    subgraph CarrierEquinix ["Colocation Cloud Transit Hub (Equinix / Megaport)"]
        TransitRouter1["Redundant Transit Router A"]
        TransitRouter2["Redundant Transit Router B"]
        DCRouters <-->|"MACsec Fiber 100Gbps"| TransitRouter1
        DCRouters <-->|"MACsec Fiber 100Gbps"| TransitRouter2
    end

    subgraph AWSCloudEstate ["AWS Cloud Estate (us-east-1)"]
        DXGW["AWS Direct Connect Gateway"]
        TGW["AWS Transit Gateway"]
        VPCWorkload["Production VPCs"]
        TransitRouter1 <-->|"AWS Direct Connect"| DXGW
        DXGW <--> TGW
        TGW <--> VPCWorkload
    end

    subgraph AzureCloudEstate ["Azure Cloud Estate (East US)"]
        ExpressRoute["Azure ExpressRoute Gateway"]
        VirtualWAN["Azure Virtual WAN Hub"]
        AzureSpokes["Production Spoke VNets"]
        TransitRouter2 <-->|"ExpressRoute Circuit"| ExpressRoute
        ExpressRoute <--> VirtualWAN
        VirtualWAN <--> AzureSpokes
    end
```

## PlantUML Specification

```plantuml
@startuml
node "On-Premises Data Center" as onprem
node "Equinix Cloud Exchange Fabric" as colo
node "AWS Cloud (Direct Connect)" as aws
node "Azure Cloud (ExpressRoute)" as azure

onprem <--> colo : Dedicated Dual 100G Links
colo <--> aws : Direct Connect Virtual Interface
colo <--> azure : ExpressRoute Cross-Connection
aws <..> azure : Cross-Cloud BGP Failover
@enduml
```

## Architectural Design Considerations

* **BGP Dynamic Routing**: Deploy redundant BGP peering across carrier exchange hubs with autonomous system (AS) path prepending to guarantee deterministic failover paths.
* **Data Egress Cost Awareness**: Minimize high-volume inter-cloud data transfer; locate interdependent data processing pipelines within the same cloud provider where possible.
* **Unified Security Policy**: Standardize Kubernetes (EKS/AKS) and infrastructure-as-code (Terraform) across clouds to avoid duplicate engineering skill requirements.

## Related Documentation & Patterns

* [AWS Well-Architected](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/aws-well-architected.md)
* [Azure Enterprise Landing Zone](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/azure-enterprise-landing-zone.md)
* [Network: DirectConnect](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/hybrid-connectivity.md)
