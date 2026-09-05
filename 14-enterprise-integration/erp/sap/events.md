# SAP Event Mesh and CloudEvents Integration

## 1. Native Eventing in S/4HANA
S/4HANA emits standardized CloudEvents when business entities change:
```json
{
  "specversion": "1.0",
  "type": "sap.s4.beh.businesspartner.v1.BusinessPartner.Created.v1",
  "source": "/default/sap.s4.beh/S4H_100",
  "id": "e81928-1234-4567-89ab-cdef01234567",
  "time": "2026-09-05T12:00:00Z",
  "data": {
    "BusinessPartner": "1000029"
  }
}
```

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
