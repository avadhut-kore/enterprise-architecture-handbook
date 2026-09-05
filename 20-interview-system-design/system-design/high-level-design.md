# System Design Interview: High-Level Architecture (HLD)

## 1. Constructing the Architectural Topology

Draw a clean, layered architectural diagram with clear separation of responsibilities:

```mermaid
flowchart TB
    Client[Mobile / Web Client] --> CDN[Edge CDN / DNS]
    CDN --> LB[L4 / L7 Load Balancer]
    LB --> Gateway[API Gateway Cluster]

    subgraph ServiceMesh [Microservices Tier]
        Gateway --> AuthSvc[Auth Service]
        Gateway --> CoreSvc[Core Domain Service]
    end

    subgraph StorageMesh [Data & Caching Tier]
        CoreSvc --> Cache[(Redis Cache)]
        CoreSvc --> PrimaryDB[(Primary Database)]
        CoreSvc --> EventBus[Kafka Event Bus]
    end
```

---

## 2. Walking Through the Data Flow

Always narrate the data flow step-by-step:
1. Client resolves DNS and sends HTTPS request to edge load balancer.
2. Load balancer terminates TLS and forwards to API Gateway.
3. Gateway authenticates JWT token and rate-limits request.
4. Gateway routes request to Core Service.
5. Core Service checks cache (cache-aside); on miss, queries database, populates cache, and returns response.
