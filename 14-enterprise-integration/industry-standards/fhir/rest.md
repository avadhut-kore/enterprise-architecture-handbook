# FHIR RESTful API and Search Specifications

## 1. Interaction Verbs
- `GET [base]/[type]/[id]`: Read current resource state.
- `POST [base]/[type]`: Create new resource.
- `PUT [base]/[type]/[id]`: Idempotent update or create.
- `DELETE [base]/[type]/[id]`: Logical deletion.
- `POST [base]`: Execute batch or transaction Bundle.

## 2. Advanced Search Modifiers
`GET /Observation?subject=Patient/101&code=883-9&date=ge2026-01-01&_include=Observation:patient`

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
