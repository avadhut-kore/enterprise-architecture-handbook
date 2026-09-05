# Identity, Multi-Factor Authentication, and Least Privilege

## 1. MFA Requirements (Requirement 8.4.2)
Under PCI-DSS v4.0, Multi-Factor Authentication (MFA) is mandatory for **all access into the CDE**, including console, SSH, VPN, and API administrative access.
- Passwords must be at least 12 characters and changed every 90 days (if MFA is not FIDO2/hardware-bound).
- No shared administrator accounts allowed under any circumstances.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
