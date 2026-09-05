# C4 Level 2: Container Diagram

The **Container Diagram** zooms into the software system, showing the high-level deployable units (containers) that execute code or store data, alongside the protocols connecting them.

> *Note: In C4, a "Container" is NOT just a Docker container—it is any deployable runtime unit such as a Single-Page Application, mobile app, microservice API, serverless function, database, or message broker.*

## When to Use
- Solution Architecture Documents (SADs), High-Level Designs (HLDs), and team architectural alignment.
- Deciding technological choices (frameworks, databases, communication protocols).
- Reviewing system resilience, operational boundaries, and security perimeters.

---

## Architecture Example: Global Wealth Management Containers

```mermaid
flowchart TD
    subgraph Clients["Client Applications"]
        WebSPA["Web Portal
[Container: Next.js / TypeScript]
Responsive investment dashboard rendered in client browser."]
        MobileApp["Mobile App
[Container: React Native]
Native mobile trading app on iOS and Android."]
    end

    subgraph Platform["Wealth Management Platform Boundary"]
        APIGateway["API Gateway & Reverse Proxy
[Container: Envoy / Kong]
Handles TLS termination, rate limiting, and JWT authentication."]
        
        PortfolioSvc["Portfolio Service
[Container: Go 1.22 / Gin]
Calculates real-time PnL, holdings valuation, and allocation drift."]
        TradeOrderSvc["Order Execution Service
[Container: Java 21 / Spring Boot]
Validates trade limits, coordinates with exchanges, and emits trade events."]
        MarketDataSvc["Market Feed Ingestor
[Container: Rust / Tokio]
High-throughput streaming ingestion of tick-by-tick market data."]
        
        KafkaBroker["Event Streaming Mesh
[Container: Apache Kafka Cluster]
Decouples order events, audit logs, and notification triggers."]
        PortfolioDB["Portfolio Store
[Container: PostgreSQL 16]
Stores user holdings, transaction history, and account configurations."]
        MarketCache["Market Data Cache
[Container: Redis 7.2 Cluster]
Sub-millisecond cache for latest asset bid/ask quotes."]
    end

    subgraph External["External Systems"]
        CoreBanking["Core Banking Ledger
[External API]"]
        Exchange["Market Exchange
[External FIX Gateway]"]
    end

    WebSPA -->|HTTPS / GraphQL| APIGateway
    MobileApp -->|HTTPS / REST| APIGateway

    APIGateway -->|gRPC / mTLS| PortfolioSvc
    APIGateway -->|gRPC / mTLS| TradeOrderSvc

    PortfolioSvc -->|SQL| PortfolioDB
    PortfolioSvc -->|TCP| MarketCache
    PortfolioSvc -.->|Publishes ValuationEvents| KafkaBroker

    TradeOrderSvc -->|FIX Protocol| Exchange
    TradeOrderSvc -->|REST / JSON| CoreBanking
    TradeOrderSvc -.->|Publishes TradeExecuted| KafkaBroker

    MarketDataSvc -->|Writes Tick Quotes| MarketCache
```

---

## Related References
- [Container Template](./container-template.md)
- [Level 3 Component Diagram](./component.md)
- [C4 Deployment Topology](./deployment.md)
