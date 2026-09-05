# API Design Review Checklist

Use this 20-point checklist before approving an API specification for client consumption.

---

## 1. Resource Modeling & REST Semantics
- [ ] URIs use plural nouns with lowercase letters and hyphens (no camelCase or snake_case in URIs).
- [ ] Proper HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) are strictly adhered to.
- [ ] State-changing `POST` requests support `Idempotency-Key` headers.

## 2. Data Contract & Validation
- [ ] Complete JSON Schemas / OpenAPI 3.1 definitions are provided for all payloads.
- [ ] Field constraints (min/max length, regex, valid enum values) are explicitly documented.
- [ ] Error responses strictly conform to the RFC 7807 Problem Details standard.

## 3. Security & Performance
- [ ] Authentication mechanism (OAuth2 / mTLS) and required scopes are documented.
- [ ] Keyset/cursor-based pagination is implemented for all unbounded collection queries.
- [ ] Rate limits and burst quotas are defined along with IETF rate limit headers.
- [ ] PII fields are identified and marked for audit masking.
