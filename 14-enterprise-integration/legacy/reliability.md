# Throttling, Backpressure, and Mainframe Connection Pools

## 1. Protecting Fragile Legacy Backends
Cloud systems can easily generate 10,000 requests/sec, instantly overwhelming a legacy mainframe designed for 200 TPS:
- **Token Bucket Throttling**: Cap outbound calls to mainframe at strict rate limits.
- **Circuit Breakers**: Trip immediately if mainframe response time degrades $> 2000	ext{ms}$.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
