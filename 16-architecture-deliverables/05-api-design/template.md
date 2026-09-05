# API Design Specification: [API NAME]

---
**Metadata**:
```yaml
document_id: "API-[NAME]-001"
title: "API Design Specification — [API Name]"
version: "1.0.0"
status: "Draft" # Draft | In Review | Approved | Implemented | Deprecated
protocol: "REST" # REST | GraphQL | gRPC | Webhook | Event
owner: "[API Owner / Architect Name <email>]"
reviewers:
  - "Security Review: [Name]"
  - "Client Platform Lead: [Name]"
created_date: "YYYY-MM-DD"
target_release: "v1.0"
```
---

## 1. Overview & Business Purpose
* Who are the consumers of this API (Internal microservices, Web/Mobile frontends, Third-party partners)?
* What core business capabilities does this interface expose?

## 2. Protocol & Base URLs
* **Production**: `https://api.enterprise.com/v1/[resource]`
* **Staging / Sandbox**: `https://api.sandbox.enterprise.com/v1/[resource]`
* **Protocol**: HTTP/2 over TLS 1.3 | gRPC HTTP/2

## 3. Authentication & Authorization
* Mechanism: OAuth2 Bearer Token (JWT) with mTLS for partner endpoints.
* Required Scopes: `[resource]:read`, `[resource]:write`.

## 4. Endpoints & Resource Design
| Method | Path | Summary | Idempotent | Auth Scope |
|---|---|---|---|---|
| `POST` | `/v1/payments` | Create payment charge | Yes (`Idempotency-Key`) | `payments:write` |
| `GET` | `/v1/payments/{id}` | Retrieve payment status | Yes | `payments:read` |
| `GET` | `/v1/payments` | List payments (cursor paginated) | Yes | `payments:read` |

## 5. Standard Headers
* `Authorization`: `Bearer <jwt>`
* `X-Correlation-ID`: `<uuid>` (propagated across distributed traces)
* `Idempotency-Key`: `<uuid>` (required on all mutating POST requests)

## 6. Request & Response Payloads (OpenAPI / Schema)
Detailed JSON schemas with strict validation rules (max lengths, regex constraints).

## 7. Error Handling (RFC 7807)
Standard Problem Details format. Reference [[error-model.md](error-model.md)].

## 8. Rate Limiting & Quotas
* Tier 1 (Partner): 500 RPS / 5,000 Burst.
* Rate Limit Headers: `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset`.

## 9. Performance & SLA / SLO
* p95 Latency < 100ms; p99 < 250ms under peak load.
* Service Level Objective (SLO): 99.95% successful responses (non-5xx).
