# Strangler Fig Architecture Pattern

## Overview

The Strangler Fig Pattern (originally named the *Strangler Application* pattern by Martin Fowler in 2004, inspired by Australian strangler fig vines that grow around host trees until the host tree dies and rots away) is an architectural migration strategy for incrementally modernizing, replacing, or refactoring legacy monolithic applications. 

Rather than attempting a catastrophic "Big Bang Rewrite" (which historically fails or runs years over budget in 80%+ of enterprise initiatives), the Strangler Fig pattern gradually replaces legacy functionality by carving out discrete domains into modern microservices or modular components behind an intercepting facade until the legacy system can be safely decommissioned.

---

## Architectural Evolution Topology

```mermaid
flowchart TD
    subgraph Phase1["Phase 1: Intercepting Facade Ingress"]
        Client1["Client Traffic"] --> Facade1["Reverse Proxy / API Gateway (Facade)"]
        Facade1 -->|100% Traffic| Legacy1["Monolithic Legacy Application"]
    end

    subgraph Phase2["Phase 2: Incremental Strangulation (Coexistence)"]
        Client2["Client Traffic"] --> Facade2["API Gateway / Dynamic Router"]
        Facade2 -->|Legacy Routes: /billing, /inventory| Legacy2["Monolith"]
        Facade2 -->|Migrated Routes: /users, /orders| NewSvc["Modern Microservices<br/>(Cloud Native / Containers)"]
        Legacy2 <-.->|Data Sync / CDC| NewSvc
    end

    subgraph Phase3["Phase 3: Total Replacement & Decommissioning"]
        Client3["Client Traffic"] --> Facade3["API Gateway"]
        Facade3 -->|100% Traffic| ModernEstate["Modern Architecture Ecosystem"]
        LegacyDead["Legacy Monolith (DECOMMISSIONED & TERMINATED)"]
    end

    Phase1 --> Phase2 --> Phase3
```

---

## The 4 Core Implementation Steps

```mermaid
sequenceDiagram
    autonumber
    participant Client
    participant Facade as Routing Facade (Envoy / API Gateway)
    participant Legacy as Legacy Monolith
    participant Modern as Modern Cloud Microservice

    Note over Client,Facade: Step 1: Deploy Facade without behavior change
    Client->>Facade: GET /api/v1/orders
    Facade->>Legacy: Forward request unchanged

    Note over Facade,Modern: Step 2: Build modern Order Service in parallel
    Note over Facade,Modern: Step 3: Reconfigure Facade to route /orders to Modern
    Client->>Facade: GET /api/v1/orders
    Facade->>Modern: Route to Modern Service!
    
    Note over Legacy: Step 4: Delete old order code in monolith
```

---

## Data Migration & Synchronization Strategies

Migrating application code is straightforward; migrating legacy databases while keeping systems online 24/7 is the true architectural challenge:

```mermaid
flowchart TD
    subgraph DualWrite["Strategy 1: Dual-Write (Application Layer)"]
        D1["New Service writes to Modern DB"] --> D2["New Service synchronously writes to Legacy DB"]
        D3["Risk: High failure risk; distributed rollback nightmare"]
    end

    subgraph CDC["Strategy 2: Change Data Capture (CDC - Recommended)"]
        C1["Legacy DB Transaction Log (WAL / Redo Log)"] --> C2["Debezium / Kafka Connect"]
        C2 --> C3["Kafka Event Stream"]
        C3 --> C4["Modern DB Consumer Updates Read Model"]
        C5["Benefit: Zero impact on legacy code; completely decoupled"]
    end
```

---

## Canary Traffic Shifting & Fallback Mechanics

When strangling a mission-critical domain (e.g., Payment Authorization), never flip 100% of traffic overnight:

```mermaid
graph LR
    subgraph TrafficShift["Gradual Canary Ingress Routing"]
        T1["Day 1: 1% Canary Traffic to Modern Service<br/>(Validate logs & latency)"]
        T2["Day 7: 10% Traffic<br/>(Evaluate load & memory stability)"]
        T3["Day 14: 50% Traffic<br/>(Verify concurrency & locking)"]
        T4["Day 30: 100% Cutover<br/>(Legacy route archived)"]
        T1 --> T2 --> T3 --> T4
    end
```

### Shadow Traffic (Dark Launching)
Prior to routing live user requests to the modern service, duplicate production traffic at the API Gateway:
1. Send the primary request to the legacy monolith and return its response to the user.
2. Asynchronously "shadow" (fork) a duplicate request to the new modern service.
3. Compare the legacy and modern responses via an automated diff analyzer; identify and fix discrepancies with zero customer impact.

---

## Decommissioning and Cleaning Up

The most commonly neglected phase of the Strangler Fig pattern is **Legacy Decommissioning**:
- Teams successfully strangulate 80% of the monolith, but abandon the project, leaving the organization with two architectures to maintain instead of one.
- **Architectural Discipline**: Every strangulation milestone must include a dedicated sprint to delete dead code from the monolith, drop obsolete database tables, revoke unused IAM roles, and reclaim cloud compute.
