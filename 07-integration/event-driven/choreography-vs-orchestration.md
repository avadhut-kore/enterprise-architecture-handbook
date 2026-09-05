# Event-Driven Architecture: Choreography vs Orchestration in Event-Driven Systems

## 1. Architectural Purpose & Problem Context
Evaluating loose coupling of reactive choreography vs central visibility and auditability of orchestrated state machine sagas.

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
