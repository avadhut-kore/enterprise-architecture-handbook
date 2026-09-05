# Production Kubernetes Multi-AZ Deployment Topology

Illustrates an enterprise-grade Kubernetes cluster topology deployed across three Availability Zones with separated system and application node pools.

```mermaid
flowchart TD
    subgraph Internet["Public Internet"]
        Users["Global End Users"]
        Route53["Route 53 / Cloudflare DNS"]
    end

    subgraph AWS_VPC["VPC: 10.100.0.0/16 (Production)"]
        subgraph PublicSubnets["Public Ingress Subnets (Multi-AZ)"]
            NLB["Network Load Balancer (AWS NLB)"]
        end

        subgraph PrivateSubnets["Private Compute Subnets (Multi-AZ)"]
            subgraph EKS["Amazon EKS 1.30 Managed Cluster"]
                subgraph AZ_A["Availability Zone A (us-east-1a)"]
                    IngressA["Ingress Controller Pod (Nginx/Envoy)"]
                    AppA1["Order API Pod (Replica 1)"]
                    AppA2["Payment Pod (Replica 1)"]
                end

                subgraph AZ_B["Availability Zone B (us-east-1b)"]
                    IngressB["Ingress Controller Pod (Nginx/Envoy)"]
                    AppB1["Order API Pod (Replica 2)"]
                    AppB2["Payment Pod (Replica 2)"]
                end

                subgraph AZ_C["Availability Zone C (us-east-1c)"]
                    IngressC["Ingress Controller Pod (Nginx/Envoy)"]
                    AppC1["Order API Pod (Replica 3)"]
                    AppC2["Payment Pod (Replica 3)"]
                end
            end
        end

        subgraph DataSubnets["Isolated Data Subnets (Multi-AZ)"]
            AuroraPrimary["Amazon Aurora PostgreSQL
[Primary Writer - AZ-a]"]
            AuroraReplica1["Amazon Aurora PostgreSQL
[Read Replica - AZ-b]"]
            AuroraReplica2["Amazon Aurora PostgreSQL
[Read Replica - AZ-c]"]
            RedisCluster["ElastiCache Redis Cluster
[6 Nodes - Multi-AZ]"]
        end
    end

    Users --> Route53 --> NLB
    NLB --> IngressA
    NLB --> IngressB
    NLB --> IngressC

    IngressA --> AppA1
    IngressB --> AppB1
    IngressC --> AppC1

    AppA1 --> AuroraPrimary
    AppB1 --> AuroraPrimary
    AppC1 --> AuroraReplica1

    AppA1 --> RedisCluster
    AppB1 --> RedisCluster
    AppC1 --> RedisCluster
```
