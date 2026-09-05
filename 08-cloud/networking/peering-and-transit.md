# Peering vs Transit Networks: Hub-and-Spoke Topologies

## Executive Summary

As cloud deployments scale to dozens or hundreds of VPCs, inter-network routing topologies dictate administrative complexity and network throughput.

---

## 1. Full Mesh Peering vs Hub-and-Spoke Transit Gateway

```mermaid
graph TD
    subgraph Full Mesh Peering [ANTI-PATTERN AT SCALE: N*(N-1)/2 Connections]
        VPC1[VPC 1] <--> VPC2[VPC 2]
        VPC1 <--> VPC3[VPC 3]
        VPC2 <--> VPC3
        VPC1 <--> VPC4[VPC 4]
        VPC2 <--> VPC4
        VPC3 <--> VPC4
    end

    subgraph Hub-and-Spoke Transit Gateway [ENTERPRISE STANDARD]
        TGW[AWS Transit Gateway / Azure Virtual WAN]
        TVPC1[VPC 1] <==> TGW
        TVPC2[VPC 2] <==> TGW
        TVPC3[VPC 3] <==> TGW
        TVPC4[VPC 4] <==> TGW
    end
```

---

## 2. Architectural Trade-Off Analysis

| Feature | VPC / VNet Peering | Transit Gateway / Virtual WAN |
| :--- | :--- | :--- |
| **Topology** | Direct point-to-point connections | Centralized hub-and-spoke router |
| **Transitive Routing** | **Not Supported** (A $\leftrightarrow$ B and B $\leftrightarrow$ C does NOT allow A $\leftrightarrow$ C) | **Supported natively**; acts as a Layer 3 cloud router |
| **Max Connections** | Hard limits (Typically 50–125 peerings per VPC) | Up to 5,000 VPC attachments per transit gateway |
| **Throughput & Bandwidth**| Uncapped; identical to intra-AZ instance bandwidth | Scalable (Up to 50 Gbps per VPC attachment) |
| **Cost** | No hourly fee; standard inter-AZ data transfer fees | Hourly fee per attachment + $\$0.02/\text{GB}$ data processing fee |
| **Best Suited For** | High-throughput data replication between 2 specific VPCs | **Enterprise backbone connecting 10+ VPCs, on-prem, and firewalls** |
