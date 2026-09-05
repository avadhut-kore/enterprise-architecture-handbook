# Industry Integration Standards Library

## 1. Overview
Enterprise integration in regulated and mature industries requires strict adherence to standardized data schemas, interaction protocols, and semantic dictionaries.

## 2. Industry Standards Catalog
- [iso-20022/](iso-20022/README.md): ISO 20022 Financial Services messaging (pacs, pain, camt, remt).
- [fhir/](fhir/README.md): HL7 Fast Healthcare Interoperability Resources (FHIR R4 / R5).
- [hl7/](hl7/README.md): Health Level Seven version 2 (HL7 v2.x) clinical messaging.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
