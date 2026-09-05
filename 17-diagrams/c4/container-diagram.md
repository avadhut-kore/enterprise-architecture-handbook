# C4 Model: Level 2 — Container Diagram

## Overview

A **Container Diagram (Level 2)** zooms inside the central software system boundary established in Level 1. It illustrates the high-level technical architecture by showing the deployable and runnable software units—known as **Containers**—that compose the system, along with how they communicate and where data is stored.

This diagram is the most frequently authored and reviewed artifact in Solution Architecture. It provides software engineers, architects, DevOps, and operations teams with a clear roadmap of system responsibilities, technical stacks, and integration protocols.

---

## What is a "Container" in the C4 Model?

> [!IMPORTANT]
> In the C4 model, a **"Container" is NOT synonymous with a Docker container**. 
> A Container is defined as **any independently deployable or runnable software artifact or data store that executes code or holds data**.

### Examples of C4 Containers
- **Client Applications**: Single-Page Applications (React, Angular), Mobile Apps (iOS/Android), CLI tools.
- **Server Applications**: REST API applications (Spring Boot, ASP.NET Core), background worker daemons, serverless functions (AWS Lambda).
- **Data Stores**: Relational databases (PostgreSQL), NoSQL stores (DynamoDB, MongoDB), in-memory caches (Redis).
- **Messaging Infrastructure**: Event streaming clusters (Apache Kafka), message brokers (RabbitMQ).
- **File & Object Storage**: S3 buckets, network-attached storage (NAS).

---

## Production Enterprise Example: Internet Banking System Containers

```mermaid
flowchart TD
    Customer["Customer<br/>[Person]"]
    
    subgraph SystemBoundary["Internet Banking System [Boundary]"]
        SPA["Single-Page Web App<br/>[Container: TypeScript / React]<br/>Provides banking features to customers via their web browser."]
        MobileApp["Mobile Banking App<br/>[Container: Swift / Kotlin]<br/>Provides retail banking features via native mobile UI."]
        
        APIGW["API Gateway / Reverse Proxy<br/>[Container: Envoy / Kong]<br/>Handles TLS termination, routing, and rate limiting."]
        
        APIApp["Backend API Application<br/>[Container: Java / Spring Boot]<br/>Provides banking business logic via RESTful API."]
        
        Cache[("Session & Read Cache<br/>[Container: Redis]<br/>Caches customer sessions and user profiles.")]
        
        PrimaryDB[("Primary Relational Database<br/>[Container: PostgreSQL]<br/>Stores customer accounts, transactions, and balances.")]
        
        EventBus[("Event Streaming Broker<br/>[Container: Apache Kafka]<br/>Streams real-time transaction events for fraud detection.")]
    end

    CoreBanking["Mainframe Core Banking<br/>[External System]"]
    EmailSvc["SendGrid Email API<br/>[External SaaS]"]

    Customer -->|Interacts via browser HTTPS| SPA
    Customer -->|Interacts via mobile OS| MobileApp
    
    SPA -->|JSON/HTTPS requests| APIGW
    MobileApp -->|JSON/HTTPS requests| APIGW
    
    APIGW -->|Routes API calls via HTTP/2| APIApp
    
    APIApp -->|Reads/writes sessions via RESP| Cache
    APIApp -->|Reads/writes ACID data via JDBC/SQL| PrimaryDB
    APIApp -->|Publishes transaction events via TCP| EventBus
    
    APIApp -->|Queries account data via SOAP/XML| CoreBanking
    APIApp -->|Dispatches notification emails via REST/HTTPS| EmailSvc
```

---

## Authoring Guidelines for Level 2

1. **Explicit Technologies**: Every container box must explicitly declare its technology runtime in brackets (e.g., `[Container: Go / Gin]`, `[Container: Redis 7.2]`).
2. **Responsibilities over Descriptions**: State clearly what the container does, not how it works internally (e.g., `Handles payment authorizations and idempotency verification`).
3. **Specify Communication Protocols**: Every connection arrow must identify the transport protocol and serialization format (e.g., `JSON/HTTPS`, `gRPC/HTTP/2`, `JDBC/TCP`, `AMQP`).
4. **Boundary Isolation**: Group internal containers inside a clear visual boundary box representing the software system, leaving external third-party systems outside the perimeter.
