# Regulatory Audit Trails and FFIEC Compliance

## 1. Regulatory Frameworks: FFIEC, SOX, and Basel III
Enterprise banking integrations operate under strict regulatory scrutiny:
- **FFIEC Architecture Guidelines**: Mandates end-to-end transaction accountability, non-repudiation, and separation of duties.
- **SOX 404**: Requires demonstrable financial data integrity between sub-ledgers and the general ledger.
- **BCBS 239**: Basel Committee principles for effective risk data aggregation and reporting.

## 2. Cryptographic Immutability Architecture
All balance modifications, admin overrides, and ledger adjustments must emit an immutable audit envelope:
```json
{
  "audit_version": "1.0",
  "event_id": "AUD-881920",
  "timestamp_utc": "2026-09-05T12:00:00.102Z",
  "actor": {
    "type": "SYSTEM_SERVICE_ACCOUNT",
    "id": "svc-payment-router",
    "cert_thumbprint": "a9b8c7...12"
  },
  "action": "LEDGER_ADJUSTMENT_POSTED",
  "payload_digest_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "previous_event_hash": "8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4"
}
```
