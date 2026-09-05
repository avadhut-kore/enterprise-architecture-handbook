# C4 Comprehensive Enterprise Example: Retail Digital Banking

This document illustrates a complete end-to-end C4 model progression for a modern, multi-tier Digital Retail Banking Platform.

---

## Level 1: System Context

```mermaid
flowchart TD
    Customer["Retail Banking Customer
[Person]
Manages checking accounts, pays bills, and transfers funds."]
    SupportAgent["Customer Support Representative
[Person]
Assists customers with account inquiries and fraud alerts."]

    subgraph BankSystem["Digital Core Banking System"]
        BankingPlatform["Retail Digital Banking Platform
[Software System]
Provides omnichannel digital banking services to consumers."]
    end

    subgraph ExternalSystems["External Banking Ecosystem"]
        PaymentNetwork["Visa / Mastercard Payment Rails
[External Network]
Processes merchant card authorizations and clearing."]
        CreditBureau["Experian / Equifax Credit Bureau
[External API]
Provides credit history and credit score lookups."]
        CoreLedger["Mainframe Core Ledger
[External System]
Maintains primary bank balance records and general ledger."]
        FraudEngine["Falcon AI Fraud Detection
[External System]
Real-time fraud scoring for payment transactions."]
    end

    Customer -->|Manages accounts & executes transfers| BankingPlatform
    SupportAgent -->|Reviews customer activity & overrides holds| BankingPlatform
    BankingPlatform -->|Authorizes debit/credit card charges| PaymentNetwork
    BankingPlatform -->|Fetches credit scores for overdrafts| CreditBureau
    BankingPlatform -->|Debits/Credits deposit accounts| CoreLedger
    BankingPlatform -->|Scores transaction risk in real-time| FraudEngine
```

---

## Level 2: Container Topology

```mermaid
flowchart TD
    subgraph Channels["Customer Channels"]
        WebSPA["Web Banking SPA
[React / TypeScript]"]
        MobileApp["Mobile Banking App
[React Native / iOS & Android]"]
    end

    subgraph CloudVPC["Digital Banking Platform (AWS)"]
        EdgeGateway["API Edge Gateway
[Kong Enterprise Gateway]"]
        AuthService["Authentication & OIDC Service
[Go / Ory Hydra]"]
        AccountService["Account & Balance Service
[Java 21 / Spring Boot]"]
        TransferService["Money Transfer Service
[.NET 8 / C#]"]
        
        AccountDB[("Account Database
[PostgreSQL 16 Multi-AZ]")]
        TransferDB[("Transfer Ledger DB
[Amazon Aurora PostgreSQL]")]
        RedisCache[("Session & Account Cache
[Redis 7 Cluster]")]
        KafkaBus["Banking Event Mesh
[Apache Kafka Cluster]"]
    end

    subgraph CoreBackend["On-Premises Data Center"]
        CoreMainframe["Mainframe Settlement Core
[IBM z16]"]
    end

    WebSPA -->|HTTPS / JSON| EdgeGateway
    MobileApp -->|HTTPS / JSON| EdgeGateway

    EdgeGateway -->|Validates Tokens| AuthService
    EdgeGateway -->|gRPC / mTLS| AccountService
    EdgeGateway -->|gRPC / mTLS| TransferService

    AccountService --> RedisCache
    AccountService --> AccountDB
    TransferService --> TransferDB
    TransferService -.->|Emits TransferInitiated| KafkaBus
    KafkaBus -.->|Pulls Transfer Events| TransferService
    TransferService -->|DirectConnect MQ / TCP| CoreMainframe
```
