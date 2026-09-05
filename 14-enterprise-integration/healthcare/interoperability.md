# Healthcare Interoperability: ONC Cures Act, TEFCA, and USCDI

## 1. US Regulatory Mandates
- **ONC 21st Century Cures Act**: Prohibits "information blocking" and mandates certified EHRs to expose standardized FHIR R4 APIs.
- **USCDI (United States Core Data for Interoperability)**: Standardized set of health data classes required for nationwide interoperability.
- **TEFCA (Trusted Exchange Framework and Common Agreement)**: Establishes Qualified Health Information Networks (QHINs) for nationwide clinical exchange.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
