# Distributed Design Principle: Stateless Architecture

## 1. Core Principle Definition

A stateless service architecture dictates that compute instances maintain no persistent client session state, in-memory conversational history, or local disk affinity between successive client requests.

Every inbound request must contain all authorization tokens, credentials, and context required for complete independent evaluation, or state must be retrieved from an external, shared state store (e.g., Redis cluster, distributed database).

---

## 2. Architectural Blueprint

```mermaid
flowchart TB
    Client[Client Device]
    LB[Layer 7 Load Balancer Round-Robin]

    subgraph StatelessComputePool [Stateless Service Cluster]
        Pod1[Service Pod 1]
        Pod2[Service Pod 2]
        Pod3[Service Pod 3]
    end

    subgraph SharedStateTier [Authoritative State Store]
        Redis[(Redis Session / Token Cache)]
        Database[(Distributed SQL / NoSQL DB)]
    end

    Client -->|Req 1 (Any node)| LB
    Client -->|Req 2 (Any node)| LB
    LB --> Pod1
    LB --> Pod2
    LB --> Pod3

    Pod1 <--> Redis
    Pod2 <--> Redis
    Pod3 <--> Redis

    Pod1 <--> Database
    Pod2 <--> Database
    Pod3 <--> Database
```

---

## 3. Benefits & Scaling Mechanics

- **Horizontal Elasticity**: Compute nodes can autoscale up or down dynamically from 10 to 1,000 instances based on CPU/traffic without needing to migrate or replicate active user sessions.
- **Trivial Fault Recovery**: If a physical server dies, the load balancer routes subsequent requests to any surviving instance without user-perceived interruption.
- **Canary & Rolling Deployments**: Pods can be terminated and replaced one-by-one with zero downtime.

---

## 4. Antipatterns & Violations

- **Sticky Sessions (Session Affinity)**: Configuring the load balancer to route a specific IP/cookie always to the same server node. If that node crashes, all pinned user sessions are lost.
- **Local File System Storage**: Saving uploaded files or generated PDFs to local `/tmp` disks rather than object storage (S3/GCS).
