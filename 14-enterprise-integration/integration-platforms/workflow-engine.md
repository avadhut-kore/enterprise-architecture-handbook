# Long-Running Orchestration: Temporal and Camunda

## 1. Durable Execution vs. Stateless Choreography
When a business process takes minutes, hours, or weeks (e.g., loan approval, employee onboarding, physical delivery tracking):
- **Temporal / Cadence**: Code-first durable execution. Automatically persists thread state, local variables, and timers to Cassandra/PostgreSQL; recovers seamlessly across worker crashes.
- **Camunda (BPMN)**: Model-driven orchestration aligning business analysts and engineers.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
