# HLD Deployment & Infrastructure Overview

## 1. Runtime Topology

```mermaid
flowchart TD
    subgraph CloudVPC["Cloud VPC (10.100.0.0/16)"]
        subgraph PublicSubnet["Public Subnets (Multi-AZ)"]
            ALB["Application Load Balancer (HTTPS / TLS 1.3)"]
        end
        
        subgraph PrivateSubnet["Private App Subnets (Multi-AZ)"]
            INGRESS["Kong Ingress Controller"]
            POD1["Pod Replica 1 (AZ-a)"]
            POD2["Pod Replica 2 (AZ-b)"]
            POD3["Pod Replica 3 (AZ-c)"]
        end
        
        subgraph DataSubnet["Isolated Database Subnets"]
            PG_PRIMARY[("PostgreSQL Primary (AZ-a)")]
            PG_REPLICA[("PostgreSQL Standby (AZ-b)")]
            REDIS[("Redis Cluster")]
        end
    end
    
    ALB --> INGRESS
    INGRESS --> POD1 & POD2 & POD3
    POD1 & POD2 & POD3 --> PG_PRIMARY
    PG_PRIMARY -. Synchronous Replication .-> PG_REPLICA
    POD1 & POD2 & POD3 --> REDIS
```

## 2. Resource Specifications
* **CPU Requests / Limits**: 500m / 2000m.
* **Memory Requests / Limits**: 1024Mi / 2048Mi.
* **Horizontal Pod Autoscaler (HPA)**: Min 3 replicas, Max 30 replicas; target average CPU 70%.
