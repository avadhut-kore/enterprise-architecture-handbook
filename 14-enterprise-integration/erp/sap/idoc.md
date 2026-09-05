# SAP IDoc Architecture: ALE, EDI, and Asynchronous Ingestion

## 1. Anatomy of an IDoc
An Intermediate Document (IDoc) consists of:
- **Control Record (`EDI_DC40`)**: Metadata, sender/receiver partner numbers, message type (e.g., `ORDERS05`, `INVOIC02`).
- **Data Records (`EDI_DD40`)**: Segment data containing business fields.
- **Status Records (`EDI_DS40`)**: Audit history tracking processing states (e.g., Status `53` = Success, Status `51` = Application Error).

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
