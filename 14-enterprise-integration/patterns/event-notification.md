# Event Notification Pattern

## 1. Thin Events vs. Rich Payloads
An **Event Notification** carries minimal data (just the entity ID and status change):
```json
{ "eventType": "ORDER_SHIPPED", "orderId": "ORD-99182" }
```
The consumer receives the notification and makes a synchronous callback to the producer's REST API to fetch full order details. Prevents sensitive data leakage across public brokers.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
