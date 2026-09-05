# Backward Compatibility and Coexistence Strategies

## 1. The Truncation Dilemma
When routing a rich ISO 20022 `pacs.008` message into a legacy core banking system that only understands fixed-width MT103 (35-character address fields):
- **Never Discard Data**: Save the original full ISO 20022 XML in an archival database and pass a correlation pointer to the legacy system.
- **Enrichment on Egress**: When the transaction exits the legacy system, re-hydrate the full structured address from the archival store.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
