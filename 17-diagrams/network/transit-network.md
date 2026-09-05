# Enterprise Transit Network & Hub-and-Spoke Routing Architecture

Enterprise transit network topology utilizing cloud Transit Gateways to interconnect hundreds of workload VPCs, on-premises networks, and centralized security inspection appliances.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph CentralTransitHub ["Central Network Transit Hub (AWS / Azure)"]
        TGW["AWS Transit Gateway / Azure Virtual WAN<br/>- Multi-VPC Central Routing Engine<br/>- Supports Route Tables & Propagations"]
        
        subgraph InspectionVPC ["Central Inspection VPC"]
            FirewallPool["Firewall Appliance Fleet (Palo Alto / Fortinet)<br/>[Gateway Load Balancer - GWLB]"]
        end

        TGW <-->|"Appliance Mode"| InspectionVPC
    end

    subgraph SpokeVPCs ["Segregated Spoke VPCs"]
        SpokeProd["Production Workload VPC (10.1.0.0/16)"]
        SpokeShared["Shared Services VPC (10.2.0.0/16)"]
        SpokeDev["Non-Production Dev VPC (10.3.0.0/16)"]

        TGW <-->|"TGW Attachment"| SpokeProd
        TGW <-->|"TGW Attachment"| SpokeShared
        TGW <-->|"TGW Attachment"| SpokeDev
    end

    subgraph OnPremisesHybrid ["On-Premises Connectivity"]
        DirectConnect["Direct Connect Gateway (100Gbps)"]
        DirectConnect <--> TGW
    end

    classDef hub fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef spoke fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef onprem fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    class TGW,InspectionVPC,FirewallPool hub;
    class SpokeProd,SpokeShared,SpokeDev spoke;
    class DirectConnect onprem;
```

## PlantUML Specification

```plantuml
@startuml
node "AWS Transit Gateway (TGW)" as tgw
package "Workload Spokes" {
  node "Production VPC (10.1.0.0/16)" as prod
  node "Shared Services VPC (10.2.0.0/16)" as shared
}
package "Inspection Hub" {
  node "Inspection VPC" as inspect {
    component "Next-Gen Firewall (GWLB)" as fw
  }
}
node "On-Premises Data Center" as dc

prod <--> tgw : Attachment
shared <--> tgw : Attachment
dc <--> tgw : Direct Connect
tgw <--> fw : East-West Inspection
@enduml
```

## Architectural Design Considerations
* **Appliance Mode**: Enable `ApplianceModeSupport` on the Transit Gateway attachment for the inspection VPC to ensure symmetrical return traffic through the same stateful firewall instance.
* **Route Table Segregation**: Create separate TGW route tables for Production and Non-Production to isolate environments at the network layer without permitting cross-environment routing.
* **Scalability**: A single Transit Gateway supports up to 5,000 VPC attachments and up to 50 Gbps of burst bandwidth per attachment.

## Related Documentation & Patterns
* [Hub and Spoke](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/hub-spoke.md)
* [Hybrid Connectivity](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/hybrid-connectivity.md)
* [Multi-Region Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/multi-region-network.md)
