# Payment Settlement and Merchant Payouts

## 1. The Multi-Tier Settlement Hierarchy
1. **Cardholder to Issuer**: Customer pays their monthly credit card balance.
2. **Issuer to Acquirer**: Settled over central banking rails (e.g., Fedwire) via card network net settlement windows.
3. **Acquirer to Merchant**: Merchant receives aggregated batch payouts (gross minus interchange and processing fees) on a $T+1$ or $T+2$ schedule.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
