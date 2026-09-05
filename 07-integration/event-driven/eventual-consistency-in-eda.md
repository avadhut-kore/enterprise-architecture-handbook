# Event-Driven Architecture: Eventual Consistency & Business Compensations in EDA

## 1. Architectural Purpose & Problem Context
Managing temporal divergence: designing idempotent consumers, outbox-driven delivery, and handling edge cases where compensations fail.

---

## 2. Event-Driven Interaction Model

```mermaid
flowchart LR
    Producer[Order Service] -->|Publish Fact: OrderPlaced| Broker[(Enterprise Event Bus)]
    Broker --> Inventory[Inventory Service: Reserve Stock]
    Broker --> Billing[Billing Service: Authorize Charge]
    Broker --> Notifications[Notification Service: Send Email]
```

---

## 3. Production Invariants
- Events must represent past facts (past-tense naming, e.g., `OrderPlaced`, `PaymentFailed`).
- Event consumers must be strictly idempotent.
- Distributed trace contexts must be forwarded across all asynchronous event message envelopes.
