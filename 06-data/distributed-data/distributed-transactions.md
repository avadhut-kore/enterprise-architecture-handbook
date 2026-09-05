# Distributed Transactions Architecture

## 1. The Distributed Transactions Dilemma
When microservices decouple databases into private persistence stores, business workflows span multiple independent datastores. Coordinating ACID guarantees across network boundaries introduces severe latency and availability penalties.

```mermaid
flowchart LR
    OrderSvc[Order Service: PostgreSQL] --> PaymentSvc[Payment Service: Stripe]
    PaymentSvc --> InventorySvc[Inventory Service: MySQL]
    InventorySvc --> ShippingSvc[Shipping Service: DynamoDB]
```

---

## 2. The FLP Impossibility Theorem
Formulated by Fischer, Lynch, and Paterson (1985), the **FLP Theorem** mathematically proves that in an asynchronous network, **no deterministic consensus protocol can guarantee both safety and liveness in the presence of even a single unannounced fail-stop process crash**.

---

## 3. Evolutionary Path of Distributed Transactions

| Paradigm | Consistency Model | Locking Model | Availability | Production Fit |
| :--- | :--- | :--- | :--- | :--- |
| **Two-Phase Commit (2PC)** | Strict ACID | Pessimistic distributed locks | Very Low (Blocks on coordinator failure) | Legacy banking, single-DC RDBMS. |
| **Saga Pattern** | BASE (Eventual) | Optimistic / Compensating transactions | High (Autonomous microservices) | Modern enterprise microservices. |
| **Outbox + CDC** | At-Least-Once Delivery | Local DB ACID + Event stream | High | Event-driven domain architectures. |
