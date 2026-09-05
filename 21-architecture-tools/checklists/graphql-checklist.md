# Architecture Checklist: GraphQL Production Architecture Checklist

## Purpose & Scope
Query depth limiting, complexity budgets, DataLoader batching, and production introspection disabling.

---

## Architectural Review Criteria

### 1. Functional & Structural Integrity
- [ ] Are boundaries, contracts, and schema ownership explicitly defined and documented?
- [ ] Are data types, precision, and serialization formats strictly validated at integration boundaries?
- [ ] Is accidental data duplication eliminated across independent service domains?

### 2. Resilience, Error Handling & Failure Modes
- [ ] Are all external network dependencies protected by explicit timeouts, retries with jitter, and circuit breakers?
- [ ] Are state-changing mutations protected by unique client idempotency keys?
- [ ] Are unprocessable or schema-violating messages routed to auditable Dead-Letter Queues (DLQs)?

### 3. Performance, Capacity & Operational Readiness
- [ ] Are storage capacity, partition sizing, and throughput requirements calculated and validated?
- [ ] Are distributed trace contexts (`traceparent`) propagated across all synchronous and asynchronous boundaries?
- [ ] Are automated data quality assertions or reconciliation matching jobs running continuously?

---

## Sign-off Matrix
| Reviewer Role | Name | Status | Date | Notes |
|---|---|---|---|---|
| Enterprise Architect | | [ ] Approved [ ] Blocked | | |
| Lead Solution Architect | | [ ] Approved [ ] Blocked | | |
| Data / Security Architect | | [ ] Approved [ ] Blocked | | |
