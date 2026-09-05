# High-Level Design Review Checklist

Use this 20-point checklist before approving an HLD for Low-Level Design (LLD) breakdown.

---

## 1. Scope & System Boundaries
- [ ] Subsystem boundaries are strictly delineated from peer services.
- [ ] Requirements trace cleanly to functional and non-functional specifications.
- [ ] In-Scope and Out-of-Scope lists leave no ambiguity.

## 2. Component Topology & Modeling
- [ ] C4 Component diagram clearly depicts internal architectural layers.
- [ ] Component responsibilities adhere to the Single Responsibility Principle.
- [ ] Synchronous calls are kept to an absolute minimum to avoid distributed deadlock.

## 3. Data & Storage Boundaries
- [ ] Database engine, schemas, and primary/foreign keys are identified.
- [ ] Transactional boundaries (ACID scope) are documented.
- [ ] Dual-write hazards are eliminated (e.g., using Transactional Outbox pattern).

## 4. Resilience & Error Handling
- [ ] Timeouts, circuit breakers, and retries are specified for every network call.
- [ ] Idempotency strategy is defined for state-changing endpoints.
- [ ] Dead-letter queues (DLQ) are configured for asynchronous message consumers.

## 5. Security & Runtime
- [ ] JWT authentication and fine-grained authorization scopes are validated.
- [ ] EKS/Kubernetes pod resource requests and limits are defined.
- [ ] Golden signals (telemetry, metrics, traces) are mapped to dashboards.
