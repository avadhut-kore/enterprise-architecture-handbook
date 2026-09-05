# SAP OData Protocol: v2 vs. v4, Batching, and CSRF

## 1. The Two-Step CSRF Token Requirement
SAP OData services reject mutating verbs (`POST`, `PUT`, `DELETE`) without a valid CSRF token:
1. Issue `GET` with header `X-CSRF-Token: Fetch` to obtain token and session cookie.
2. Issue mutating request including returned `X-CSRF-Token` and session cookies.

## 2. OData $batch Operations
To create 100 invoice line items without 100 individual HTTP roundtrips, bundle requests into a single multipart MIME `$batch` POST.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
