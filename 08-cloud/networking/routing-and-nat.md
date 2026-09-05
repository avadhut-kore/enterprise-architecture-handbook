# Cloud Routing Architecture & NAT Gateways

## Executive Summary

Routing tables govern packet flow across subnets and gateways. Managing outbound internet egress for thousands of private compute instances requires designing **scalable, cost-optimized NAT architectures**.

---

## 1. Multi-AZ NAT Gateway Architecture

```mermaid
graph TD
    subgraph Public Subnet AZ1
        NAT1[NAT Gateway AZ1] --> IGW[Internet Gateway]
    end
    subgraph Public Subnet AZ2
        NAT2[NAT Gateway AZ2] --> IGW
    end

    subgraph Private Subnet AZ1
        App1[Compute Fleet AZ1] -->|Route 0.0.0.0/0| NAT1
    end
    subgraph Private Subnet AZ2
        App2[Compute Fleet AZ2] -->|Route 0.0.0.0/0| NAT2
    end
```

---

## 2. The NAT Single-Point-of-Failure Trap

- **Anti-Pattern (Single Shared NAT)**: Deploying one NAT Gateway in AZ1 and routing private subnets from AZ2 and AZ3 through it saves $\$32/\text{month}$ per gateway, but:
  1. If AZ1 suffers an outage, **all outbound internet connectivity for the entire region collapses**.
  2. Incurs cross-AZ data transfer fees ($\$0.01/\text{GB}$) for all traffic originating in AZ2/AZ3.
- **Rule**: In production, **deploy exactly one NAT Gateway per Availability Zone** and route each private subnet exclusively to its local AZ NAT Gateway.

---

## 3. Centralized Egress Inspection VPC

At scale (dozens of VPCs), deploying NAT Gateways in every VPC is financially unsustainable. Deploy a **Centralized Egress VPC** attached to AWS Transit Gateway or Azure Virtual WAN, routing all outbound internet traffic through an autoscaling fleet of Next-Gen Firewalls.
