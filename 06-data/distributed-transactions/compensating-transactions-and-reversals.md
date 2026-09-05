# Distributed Transactions: Compensating Transactions & Semantic Reversals

## 1. Architectural Purpose & Problem Context
Designing business compensations: reversing authorization holds, issuing credit notes, restoring stock reservations, and handling non-reversible real-world actions.

---

## 2. Distributed Workflow Architecture

```mermaid
sequenceDiagram
    autonumber
    participant Client
    participant OrderService as Order Service
    participant Outbox as Outbox Relay
    participant Broker as Message Broker
    participant PaymentService as Payment Service

    Client->>OrderService: Create Order
    Note over OrderService: Atomic Local DB Transaction:<br/>Insert Order + Insert Outbox Record
    OrderService-->>Client: 202 Accepted (OrderId)
    Outbox->>Broker: Publish OrderCreated Event
    Broker->>PaymentService: Consume OrderCreated Event
    Note over PaymentService: Check Idempotency Key
    PaymentService->>Broker: Publish PaymentProcessed / PaymentFailed
```

---

## 3. Production Invariants
- Never use Two-Phase Commit (2PC) over wide-area networks or across microservice team boundaries.
- Every state-changing distributed command must support compensating transactions.
- Always implement the Transactional Outbox pattern when publishing events in response to database mutations to eliminate the dual-write hazard.
