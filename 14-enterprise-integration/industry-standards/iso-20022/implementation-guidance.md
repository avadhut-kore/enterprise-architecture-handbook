# Practical Implementation Guidance for Integration Architects

## 1. Golden Rules for Implementation
1. **Never Hand-Craft XML**: Use official JAXB or XMLBeans bindings generated directly from ISO 20022 XSD schemas.
2. **Preserve EndToEndId and UETR**: These tracking identifiers must never be truncated or regenerated.
3. **UTC Timestamps Only**: Normalize all date-time fields to UTC with explicit time zone offsets (`2026-09-05T12:00:00Z`).

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
