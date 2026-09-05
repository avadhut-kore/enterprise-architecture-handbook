# Hybrid Connectivity: Dedicated Fiber vs Redundant IPsec VPNs

## Executive Summary

Designing enterprise hybrid connectivity requires balancing bandwidth, deterministic latency, high-availability SLAs, and deployment lead times.

---

## 1. Resilient Hybrid Transit Blueprint

```mermaid
graph TD
    subgraph Corporate Data Center Edge
        Cisco1[Data Center Core Router 1]
        Cisco2[Data Center Core Router 2]
    end

    subgraph Cloud Edge Meet-Me Facility
        DX1[Direct Connect Location A: Primary 10G]
        DX2[Direct Connect Location B: Secondary 10G]
    end

    subgraph Cloud Transit Network
        TGW[AWS Transit Gateway / Azure vWAN]
    end

    Cisco1 ==>|Dedicated Fiber Cross-Connect| DX1 ==> TGW
    Cisco2 ==>|Dedicated Fiber Cross-Connect| DX2 ==> TGW
    Cisco1 -.->|Auto-Failover IPsec BGP VPN| TGW
    Cisco2 -.->|Auto-Failover IPsec BGP VPN| TGW
```

---

## 2. BGP Routing Architecture & Failover Mechanics

- **Border Gateway Protocol (BGP)**: Mandate dynamic BGP (Autonomous System Number - ASN) peering over hybrid circuits. Static routing over hybrid links is prohibited because it cannot detect remote fiber conduit breaks.
- **AS-Path Prepending**: Configure the enterprise on-premises routers to prepend their BGP ASN 3 times on the secondary Direct Connect path. Cloud routers will preferentially select the primary circuit and automatically shift traffic to the secondary circuit within sub-second detection windows via **Bidirectional Forwarding Detection (BFD)**.
