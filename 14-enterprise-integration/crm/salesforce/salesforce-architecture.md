# Salesforce Platform Architecture & Governor Limits

## 1. Multi-Tenant Resource Governance
Because Salesforce shares compute and database resources across tenants, it enforces strict Governor Limits:
- Max 24-hour API call quotas based on license tiers.
- Max 10 concurrent long-running Apex requests ($> 5	ext{s}$).
- Integration architectures must utilize bulk APIs and asynchronous event streaming to stay within limits.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
