# Event-Driven Architecture: EDA Observability, Distributed Tracing & Correlation IDs

## 1. Architectural Purpose & Problem Context
Tracing asynchronous workflows: injecting OpenTelemetry W3C traceparent headers into message envelopes, visualizing event flows, and lag alerting.

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
