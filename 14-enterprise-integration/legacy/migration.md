# Legacy Data Migration and Cutover Runbooks

## 1. Cutover Weekend Execution Plan
- **T-48h**: Initial bulk database snapshot and hydration.
- **T-0**: Freeze legacy OLTP transactions; drain in-flight MQ queues.
- **T+2h**: Catch up incremental CDC delta logs.
- **T+4h**: Run automated reconciliation checks.
- **T+6h**: Switch DNS / API Gateway routing to modern cloud platform.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
