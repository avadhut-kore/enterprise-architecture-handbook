# ISO 20022 Security: Digital Signatures and PKI

## 1. XML Digital Signatures (XML-DSig)
Financial networks enforce non-repudiation using enveloped XML-DSig (W3C standard):
- The `AppHdr` contains the `<Signature>` block.
- An asymmetric private key stored in an HSM signs the cryptographic digest of the `<Document>` payload.
- Any modification of payment amounts or beneficiary accounts invalidates the cryptographic signature immediately.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
