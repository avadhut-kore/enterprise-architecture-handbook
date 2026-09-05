# Event-Driven Architecture: Events vs Commands vs Messages: Core Architectural Taxonomy

## 1. Architectural Purpose & Problem Context
Disambiguating intent: Commands (targeted intent to mutate state), Events (immutable historical fact published to anyone), and Messages (envelope wrapper).

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
