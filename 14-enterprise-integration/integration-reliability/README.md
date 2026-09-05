# Enterprise Integration Reliability & Fault Tolerance

## 1. Overview
In enterprise systems, partial failure is inevitable. Integration reliability engineering designs systems to isolate faults, eliminate cascading failures, and guarantee eventual consistency across unreliable networks.

---

## 2. Directory Contents
* **[timeouts.md](timeouts.md)** — Connect, read, and execution timeout budgets.
* **[retries.md](retries.md)** — Transient vs permanent error classification.
* **[backoff.md](backoff.md)** — Exponential backoff with decorrelated full jitter.
* **[circuit-breaker.md](circuit-breaker.md)** — Fail-fast mechanisms and circuit state transitions.
* **[idempotency.md](idempotency.md)** — `Idempotency-Key` headers, token storage, and deduplication windows.
* **[duplicate-detection.md](duplicate-detection.md)** — Bloom filters and database unique constraints.
* **[ordering.md](ordering.md)** — Partition key design, sequencing, and out-of-order tolerance.
* **[delivery-semantics.md](delivery-semantics.md)** — At-most-once vs At-least-once vs "Effectively-once".
* **[dead-letter.md](dead-letter.md)** — Dead-Letter Queue (DLQ) routing, triage, and redrive workflows.
* **[replay.md](replay.md)** — Offset rewinding, message re-ingestion, and state recovery.
* **[poison-messages.md](poison-messages.md)** — Isolating corrupt payloads to prevent queue starvation.
* **[partial-failure.md](partial-failure.md)** — Graceful degradation and fallback responses.
* **[reconciliation.md](reconciliation.md)** — Bridging asynchronous drift via reconciliation.
* **[disaster-recovery.md](disaster-recovery.md)** — Multi-region active-active messaging and DNS failover.
* **[checklist.md](checklist.md)** — 20-Point Integration Reliability Review Checklist.
