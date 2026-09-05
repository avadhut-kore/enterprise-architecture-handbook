# Network Segmentation & Microsegmentation

## Executive Summary

Network segmentation partitions enterprise networks into isolated subnet tiers. Microsegmentation applies granular, workload-level firewall rules directly to virtual interfaces or container network namespaces.

---

## 1. Subnet Tiering Architecture

```mermaid
flowchart TD
    subgraph PublicSubnet ["Public Tier (DMZ)"]
        ALB["Application Load Balancer"]
        NAT["NAT Gateway"]
    end
    subgraph PrivateSubnet ["Private Compute Tier"]
        K8s["Kubernetes Worker Pods"]
    end
    subgraph IsolatedSubnet ["Isolated Database Tier (No Internet)"]
        DB["Aurora Primary"]
        Cache["Redis Cluster"]
    end

    Internet["Internet"] -->|Port 443| ALB
    ALB -->|Internal Port 8080| K8s
    K8s -->|Internal Port 5432| DB
    K8s -->|Internal Port 6379| Cache
    K8s -->|Outbound HTTPS via NAT| NAT
    NAT --> Internet
```
