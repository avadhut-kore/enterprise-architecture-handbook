# Architecture Overview & C4 Model Specification

## 1. System Context View (C4 Level 1)
Details the software system within the enterprise environment, identifying external users, third-party systems, and institutional boundaries.

```mermaid
C4Context
    title C4 Level 1: System Context Diagram
    Enterprise_Boundary(b0, "Enterprise Corporate Network") {
        Person(user, "Enterprise Operator", "Submits and manages orders")
        System(core, "Order Management System", "Orchestrates order validation, reservation, and fulfillment")
    }
    System_Ext(payment, "Stripe Payment Gateway", "Processes credit card captures")
    System_Ext(erp, "SAP S/4HANA", "Inventory and GL ledger updates")
    
    Rel(user, core, "Submits orders via", "HTTPS / Web Portal")
    Rel(core, payment, "Authorizes payment", "HTTPS / REST API")
    Rel(core, erp, "Posts transactions", "Kafka Event / mTLS")
```

---

## 2. Container View (C4 Level 2)
Decomposes the system into high-level deployable containers (applications, databases, message queues).

```mermaid
C4Container
    title C4 Level 2: Container Diagram
    Container(spa, "Single Page App", "React / TypeScript", "Web UI for operators")
    Container(gateway, "API Gateway", "Envoy / Kong", "Rate limiting, TLS termination, OIDC auth")
    Container(order_svc, "Order Service", "Java / Spring Boot", "Order domain logic and state machine")
    Container(payment_svc, "Payment Service", "Go", "Payment capture and idempotent retries")
    ContainerDb(order_db, "Order Database", "PostgreSQL", "Stores order aggregates and outbox events")
    ContainerQueue(broker, "Event Broker", "Apache Kafka", "Order lifecycle event streaming")

    Rel(spa, gateway, "API requests", "HTTPS / JSON")
    Rel(gateway, order_svc, "Routes /orders", "gRPC / mTLS")
    Rel(gateway, payment_svc, "Routes /payments", "gRPC / mTLS")
    Rel(order_svc, order_db, "Persists orders", "JDBC / TLS")
    Rel(order_svc, broker, "Publishes OrderPlacedEvent", "Kafka Protocol")
    Rel(payment_svc, broker, "Consumes OrderPlacedEvent", "Kafka Protocol")
```
