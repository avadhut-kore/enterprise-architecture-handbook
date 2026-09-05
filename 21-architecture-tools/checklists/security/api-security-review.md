# Checklist: API Security Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Ingress secured via centralized API Gateway chokepoint.
- [ ] Distributed sliding-window rate limiting enforced per client.
- [ ] Strict OpenAPI 3.1 request schema validation active.
- [ ] OAuth 2.0 Authorization Code with PKCE enforced for all apps.
- [ ] High-value financial transactions require HMAC-SHA256 signatures.
