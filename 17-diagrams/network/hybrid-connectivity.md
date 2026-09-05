# Enterprise Hybrid Cloud Connectivity Architecture (DirectConnect & IPsec)

Resilient hybrid connectivity topology linking corporate private data centers with public cloud infrastructure using redundant dedicated circuits and automated IPsec VPN failover.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph CorporateDatacenter ["On-Premises Data Center (AS 65000)"]
        EdgeRouterA["Border Router A (BGP)"]
        EdgeRouterB["Border Router B (BGP)"]
        InternalCore["Core Enterprise Workloads (192.168.0.0/16)"]
        InternalCore --- EdgeRouterA
        InternalCore --- EdgeRouterB
    end

    subgraph HybridInterconnect ["Hybrid Transport Layer"]
        DirectConnect["Primary: Dedicated 100Gbps DirectConnect / ExpressRoute"]
        IPsecVPN["Secondary Fallback: Redundant IPsec VPN Tunnels (BGP Active)"]
        EdgeRouterA <-->|"BGP Weight 200"| DirectConnect
        EdgeRouterB <-->|"BGP Weight 100 (AS Prepend)"| IPsecVPN
    end

    subgraph CloudNetworkEstate ["AWS Cloud Estate (AS 64512)"]
        DXGW["Direct Connect Gateway"]
        TransitGW["AWS Transit Gateway (TGW)"]
        WorkloadVPC["Production Workload VPC (10.100.0.0/16)"]

        DirectConnect <--> DXGW
        IPsecVPN <--> TransitGW
        DXGW <--> TransitGW
        TransitGW <--> WorkloadVPC
    end

    classDef onprem fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef conn fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef cloud fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    class EdgeRouterA,EdgeRouterB,InternalCore onprem;
    class DirectConnect,IPsecVPN conn;
    class DXGW,TransitGW,WorkloadVPC cloud;
```

## PlantUML Specification

```plantuml
@startuml
node "On-Premises Data Center" as onprem {
  [Core Routers]
}
node "Hybrid Transport" as transport {
  [Direct Connect (Primary 100G)] as dx
  [IPsec VPN (Backup 1.25G)] as vpn
}
node "AWS Cloud" as aws {
  [Transit Gateway] as tgw
  [Workload VPC] as vpc
}

[Core Routers] <--> dx : Primary BGP Path
[Core Routers] <--> vpn : Fallback BGP Path
dx <--> tgw
vpn <--> tgw
tgw <--> vpc
@enduml
```

## Architectural Design Considerations
* **Dynamic BGP Failover**: Enforce BGP dynamic routing with BFD (Bidirectional Forwarding Detection) to detect link degradation and trigger sub-second route failover.
* **AS Path Prepending**: Prepend autonomous system numbers on the backup IPsec VPN connection to ensure return traffic exclusively uses the high-bandwidth DirectConnect path during normal operation.
* **MTU Size Management**: Account for IPsec encapsulation overhead by clamping TCP MSS or configuring Jumbo Frames (9001 MTU) on DirectConnect circuits.

## Related Documentation & Patterns
* [Transit Network](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/transit-network.md)
* [Hub and Spoke](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/network/hub-spoke.md)
* [Cloud: Multi-Cloud](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/cloud/multi-cloud.md)
