# FHIR Profiles and Implementation Guides (US Core)

## 1. StructureDefinition and Profiling
To make generic FHIR actionable in a specific jurisdiction, national bodies publish **Implementation Guides (IGs)** containing **Profiles** (e.g., US Core Implementation Guide):
- Enforces mandatory elements (e.g., Patient must have an active identifier).
- Constrains terminologies to specific ValueSets (e.g., Race must bind to CDC Race codes).

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
