# Mermaid Flowcharts & Subgraph Clustering

Flowcharts are the most versatile diagram type for modeling system top-level architectures, network segments, and procedural workflows.

## Production Microservice Flowchart

```mermaid
graph TB
    subgraph PublicZone ["Public Ingress"]
        Client["Browser Client"]
        DNS["Route53 DNS"]
        WAF["AWS WAF & CloudFront"]
        Client --> DNS
        DNS --> WAF
    end

    subgraph VPCZone ["Production VPC (10.0.0.0/16)"]
        subgraph IngressSubnet ["Public Subnet"]
            ALB["Application Load Balancer"]
            WAF --> ALB
        end

        subgraph AppSubnet ["Private Application Subnet"]
            App1["order-service Pod"]
            App2["inventory-service Pod"]
            ALB --> App1
            App1 --> App2
        end

        subgraph DataSubnet ["Restricted Database Subnet"]
            DB[(PostgreSQL Primary)]
            Cache[("Redis Cluster")]
            App1 --> DB
            App2 --> Cache
        end
    end

    classDef pub fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef app fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef db fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    class Client,DNS,WAF pub;
    class ALB,App1,App2 app;
    class DB,Cache db;
```

## Subgraph Best Practices
1. **Explicit ID**: Always specify both a unique subgraph ID and a display name: `subgraph SubnetA ["Display Name"]`.
2. **Class Assignments**: Apply distinct CSS styles to subgraphs using `classDef` and `class` statements.
