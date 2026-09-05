# Distributed Design Principle: Event-Driven Architecture (EDA)

## 1. Core Principle Definition

Event-Driven Architecture is a design paradigm where system components communicate by publishing and reacting to immutable occurrences known as **events** (significant changes in state).

Producers emit events without knowledge of who consumes them, and consumers process events asynchronously without blocking the producer.

---

## 2. Orchestration vs Choreography

```
Orchestration (Synchronous Controller):
[ Orchestrator ] ──► Call Service A ──► Call Service B ──► Call Service C
(Centralized control, high coupling, cascading timeouts)

Choreography (Decoupled Event Fabric):
[ Service A ] ──► Emits Event: OrderCreated
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
  [ Service B (Billing) ]    [ Service C (Inventory) ]
```

---

## 3. Core Structural Benefits

- **Temporal Decoupling**: The producer and consumer do not need to be online at the same time. If the billing service is undergoing maintenance, events accumulate safely in Kafka topics and are processed when the consumer returns.
- **Extensibility**: Adding a new feature (e.g., Fraud Analytics or Audit Logging) requires creating a new consumer on existing topics with zero code changes to the upstream producer.
