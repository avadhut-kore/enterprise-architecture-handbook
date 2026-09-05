# SAP Integration Security: Principal Propagation & SNC

## 1. Security Architecture
- **Principal Propagation**: Pass end-user identity securely from edge API gateways to SAP backend services using SAML assertions or X.509 client certificates, ensuring SAP authorization checks reflect the actual human caller.
- **Secure Network Communications (SNC)**: Encrypts all legacy RFC and GUI traffic between on-premise components.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
