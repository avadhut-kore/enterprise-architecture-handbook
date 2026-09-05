# Event-Driven Legacy Modernization Strategy

## 1. Decoupling the Legacy Core via Events

Direct point-to-point database sharing is a legacy anti-pattern that creates rigid technical debt. Event-driven modernization uses **Change Data Capture (CDC)** to extract state changes from legacy databases as real-time event streams:

```mermaid
flowchart LR
    LegacyMonolith["Legacy Monolith\n(Mainframe / Oracle DB)"] -->|Database Log Tailing| CDC["Debezium CDC Connector"]
    CDC --> Kafka["Enterprise Kafka Cluster (Topic: 'account-events')"]
    
    subgraph ModernMicroservices ["Modern Cloud Services"]
        Svc1["AI Fraud Detection Service"]
        Svc2["Real-Time Notifications Service"]
        Svc3["Modern Cloud Read Replica"]
    end

    Kafka --> Svc1 & Svc2 & Svc3
```
