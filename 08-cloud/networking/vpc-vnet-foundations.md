# VPC & VNet Foundations: CIDR Planning & Subnet Architecture

## Executive Summary

IP address exhaustion and overlapping CIDR blocks are among the most expensive and difficult technical debts to remediate in enterprise cloud architecture. Enterprise networking mandates a **globally planned, non-overlapping IP address schema**.

---

## 1. Enterprise RFC 1918 CIDR Allocation Plan

```mermaid
graph TD
    Enterprise[Corporate Enterprise IP Block: 10.0.0.0/8]
    Enterprise --> OnPrem[10.0.0.0/12: On-Premises Data Centers]
    Enterprise --> AWS[10.16.0.0/12: AWS Global Estate]
    Enterprise --> Azure[10.32.0.0/12: Azure Global Estate]
    Enterprise --> GCP[10.48.0.0/12: GCP Global Estate]
    Enterprise --> Reserve[10.64.0.0/10: Reserved for Mergers & Acquisitions]
```

---

## 2. Standard 3-Tier Multi-AZ Subnet Blueprint

Every production VPC/VNet must span a minimum of three Availability Zones with strictly isolated functional tiers:

```mermaid
graph TD
    subgraph Availability Zone A
        PubA[Public Subnet: 10.16.1.0/24 - Ingress ALB]
        PrivA[Private App Subnet: 10.16.10.0/22 - EKS / ECS]
        DBA[Isolated DB Subnet: 10.16.20.0/24 - Aurora / RDS]
    end
    subgraph Availability Zone B
        PubB[Public Subnet: 10.16.2.0/24 - Ingress ALB]
        PrivB[Private App Subnet: 10.16.14.0/22 - EKS / ECS]
        DBB[Isolated DB Subnet: 10.16.21.0/24 - Aurora / RDS]
    end
    subgraph Availability Zone C
        PubC[Public Subnet: 10.16.3.0/24 - Ingress ALB]
        PrivC[Private App Subnet: 10.16.18.0/22 - EKS / ECS]
        DBC[Isolated DB Subnet: 10.16.22.0/24 - Aurora / RDS]
    end
```

### Architectural Subnet Rules
1. **Size for Container Density**: Private application subnets must be allocated at least a `/22` (1,022 usable IPs) to accommodate Kubernetes pod churn and prefix delegation without IP starvation.
2. **Zero Route to Internet in Database Tier**: Isolated database subnets must **never contain a default route (`0.0.0.0/0`)** to an Internet Gateway or NAT Gateway.
