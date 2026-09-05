# Exception Management and Break Triage

## 1. Break Classification
- **Timing Break**: Temporary delay due to bank processing windows. Resolves automatically within 24 hours.
- **Fee Variance Break**: Discrepancy caused by unforeseen bank wire fees. Auto-adjusted to fee expense account.
- **Missing Leg Break**: Critical error. Transaction debited from customer but never reached destination. Requires immediate human escalation.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
