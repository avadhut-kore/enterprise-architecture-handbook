# Global E-Commerce Platform Reference Architecture

This reference architecture models a global, multi-region digital commerce platform engineered for high-concurrency flash sales, sub-second checkout, and resilient event-driven order fulfillment.

## 1. Business Context & Architectural Drivers
* **Throughput Target**: Sustained 15,000 requests/sec with peak flash-sale bursts up to 80,000 requests/sec.
* **Latency SLA**: p99 checkout response time $\le 350$ms globally.
* **Availability**: 99.99% availability (less than 52 minutes of downtime per year).
* **Consistency Model**: Eventual consistency for search catalogs and inventory reservations; strong serializable consistency for payment authorization and ledger balance.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph Users ["Shoppers & Operations"]
        Shopper["Online Shopper<br/>[Person]<br/>Browses products and places orders"]
        CSR["Customer Support Rep<br/>[Person]<br/>Manages refunds and order status"]
    end

    subgraph CorePlatformBoundary ["Global E-Commerce Platform"]
        EComPlatform["E-Commerce System<br/>[Software System]<br/>Provides catalog browsing, shopping cart, checkout, and order tracking"]
    end

    subgraph ExternalSystems ["External Enterprise Systems"]
        StripePay["Payment Gateway (Stripe/Adyen)<br/>[External System]<br/>Credit card auth & fraud checks"]
        FedEx["Logistics & Carrier API (FedEx/UPS)<br/>[External System]<br/>Shipping rates & label generation"]
        ERP["Corporate ERP (SAP S/4HANA)<br/>[External System]<br/>Inventory replenishment & ledger"]
    end

    Shopper -->|"Browses & Buys via HTTPS"| EComPlatform
    CSR -->|"Manages orders via Web Portal"| EComPlatform
    EComPlatform -->|"Authorizes payments"| StripePay
    EComPlatform -->|"Generates shipping labels"| FedEx
    EComPlatform -->|"Syncs financial batches"| ERP
```

## 3. C4 Level 2: Container Architecture

```mermaid
graph TB
    Shopper["Shopper [Person]"]

    subgraph IngressBoundary ["Cloudflare Edge Network"]
        CDN["Cloudflare CDN & WAF<br/>[Container: Edge Cache]<br/>Static assets, DDoS scrubbing, SSL termination"]
    end

    subgraph EKSCluster ["Core Application Cluster (AWS EKS)"]
        APIGW["Kong API Gateway<br/>[Container: Go/Envoy]<br/>Routing, JWT validation, rate limiting"]
        
        CatalogSvc["Catalog Service<br/>[Container: Go]<br/>Product search & recommendations"]
        CartSvc["Cart Service<br/>[Container: Node.js]<br/>High-speed session cart management"]
        OrderSvc["Order Service<br/>[Container: Java Spring Boot]<br/>Order state machine & transactional checkout"]
        PaymentSvc["Payment Service<br/>[Container: Java Spring Boot]<br/>Payment gateway integration"]
    end

    subgraph PersistenceAndEvents ["Persistence & Event Tier"]
        Elasticsearch[("Product Search Index<br/>[Elasticsearch Cluster]")]
        RedisCart[("Cart In-Memory Store<br/>[Redis Cluster]")]
        AuroraOrders[("Order Database<br/>[Amazon Aurora PostgreSQL Multi-AZ]")]
        KafkaBus["Event Streaming Broker<br/>[Apache Kafka MSK]"]
    end

    Shopper --> CDN
    CDN --> APIGW
    APIGW --> CatalogSvc
    APIGW --> CartSvc
    APIGW --> OrderSvc
    OrderSvc --> PaymentSvc

    CatalogSvc --> Elasticsearch
    CartSvc --> RedisCart
    OrderSvc --> AuroraOrders
    OrderSvc -->|"Publish orders.created.v1"| KafkaBus
```

## 4. Checkout Sequence Flow with Fallback

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Shopper (Browser)
    participant GW as Kong API Gateway
    participant OrderSvc as Order Service
    participant PaySvc as Payment Service
    participant Stripe as Stripe API
    participant Kafka as Kafka Event Bus

    Customer->>GW: POST /checkout (CartID, PaymentToken, IdempotencyKey)
    GW->>OrderSvc: Forward Request (User Claims Validated)
    OrderSvc->>OrderSvc: Validate Price & Lock Inventory
    OrderSvc->>PaySvc: Process Payment ($149.99)
    
    critical Stripe Authorization
        PaySvc->>Stripe: POST /v1/charges (IdempotencyKey)
        Stripe-->>PaySvc: 200 OK (Charge ID: ch_9102)
    option Network Timeout (Retry with Backoff)
        PaySvc->>Stripe: POST /v1/charges (Retry 1)
        Stripe-->>PaySvc: 200 OK (Charge ID: ch_9102)
    option Card Declined
        PaySvc-->>OrderSvc: Payment Rejected (Insufficient Funds)
        OrderSvc-->>GW: 402 Payment Required
        GW-->>Customer: Show Payment Declined UI
    end

    PaySvc-->>OrderSvc: Payment Success
    OrderSvc->>OrderSvc: Commit Order Record (Aurora)
    OrderSvc->>Kafka: Publish Event (Topic: orders.placed.v1)
    OrderSvc-->>GW: 201 Created (Order #ORD-8841)
    GW-->>Customer: Render Order Confirmation
```

## 5. Physical Deployment & Multi-Region Topology

```mermaid
graph TB
    subgraph GlobalDNS ["Global Traffic Routing"]
        R53["Amazon Route 53 (Latency & Geo DNS)"]
    end

    subgraph RegionUS ["Primary Region: US-East-1 (Active)"]
        ALBUS["ALB US-East"]
        EKSUS["EKS Worker Nodes (AZ 1a, 1b, 1c)"]
        AuroraPrimary[("Aurora PostgreSQL (Writer Instance)")]
        ALBUS --> EKSUS
        EKSUS --> AuroraPrimary
    end

    subgraph RegionEU ["Secondary Region: EU-West-1 (Active-Read)"]
        ALBEU["ALB EU-West"]
        EKSEU["EKS Worker Nodes (AZ 1a, 1b, 1c)"]
        AuroraReplica[("Aurora Global Database (Read Replica)")]
        ALBEU --> EKSEU
        EKSEU --> AuroraReplica
    end

    R53 -->|"US Traffic"| ALBUS
    R53 -->|"EU Traffic"| ALBEU
    AuroraPrimary -.->|"Cross-Region Storage Replication (<1s lag)"| AuroraReplica
```

## 6. Key Architecture Decision Records (ADRs)
* **ADR-01: Microservices vs Modular Monolith**: Decomposed into 6 bounded microservices due to distinct scaling profiles (Catalog: 95% reads; Checkout: 100% ACID writes).
* **ADR-02: Inventory Reservation Strategy**: Implemented Redis distributed locks with 10-minute TTL for flash-sale cart reservations to protect relational databases.
* **ADR-03: Eventual Consistency for Fulfillment**: Order placement succeeds immediately upon payment authorization; warehouse allocation is handled asynchronously via Kafka consumers.
