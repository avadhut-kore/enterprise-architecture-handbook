# Event-Driven Architecture: Event Contracts, Versioning & Backward Compatibility

## 1. Architectural Purpose & Problem Context
Treating event schemas as public contracts: schema registries, semantic versioning, additive evolution, and handling obsolete schema versions.

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
