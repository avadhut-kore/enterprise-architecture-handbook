# Sequence Diagrams Architecture Library

Sequence diagrams model **interactions, message exchanges, and temporal ordering** across distributed systems, microservices, and human actors.

## Core Behavioral Perspectives Covered
1. **Synchronous vs Asynchronous Communication**: Request-reply REST/gRPC vs non-blocking Kafka/RabbitMQ events.
2. **Security & Identity Handshakes**: OAuth2 Authorization Code flow with PKCE, JWT validation, and token refresh.
3. **Enterprise Transaction Workflows**: Two-phase payment processing, e-commerce order checkout, and inventory locking.
4. **Distributed Transactions (Sagas)**: Orchestrated and choreographed Sagas with automated compensation rollbacks.
5. **Resilience & Failure Engineering**: Retries with exponential backoff, circuit breaker trip states, timeouts, and dead-letter queues.
6. **Human-in-the-Loop Orchestration**: Multi-stage manual approvals with asynchronous callback webhooks.

---

## Directory Contents
- [`synchronous.md`](./synchronous.md) — Request-Reply HTTP/REST and gRPC lifelines.
- [`asynchronous.md`](./asynchronous.md) — Event-driven decoupling, message queues, and asynchronous workers.
- [`api-request.md`](./api-request.md) — API Gateway routing, rate limiting, and database roundtrips.
- [`authentication.md`](./authentication.md) — OAuth2 / OIDC token issuance and authorization.
- [`payment.md`](./payment.md) — Payment gateway authorization, capture, and settlement rails.
- [`order-processing.md`](./order-processing.md) — Multi-service checkout flow.
- [`event-driven.md`](./event-driven.md) — Transactional outbox pattern and Kafka stream consumption.
- [`saga.md`](./saga.md) — Distributed transaction orchestration with compensation logic.
- [`retry.md`](./retry.md) — Retry policies, jitter, and idempotency key handling.
- [`failure.md`](./failure.md) — Graceful degradation, cascading failure containment, and DLQs.
- [`timeout.md`](./timeout.md) — Distributed timeout budgets and deadline propagation.
- [`circuit-breaker.md`](./circuit-breaker.md) — Closed, Open, and Half-Open circuit breaker state transitions.
- [`human-in-the-loop.md`](./human-in-the-loop.md) — Asynchronous human approval and resume callbacks.
- [`template.md`](./template.md) — Copy-pasteable sequence starter templates.
- [`checklists.md`](./checklists.md) — Review checklist for sequence diagrams.
