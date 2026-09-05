# 05-API-DESIGN: Enterprise API Design Guidelines & Specifications

## 1. Overview & Purpose
This directory provides production-grade standards, templates, and review checklists for designing enterprise APIs across multiple protocols: REST, GraphQL, gRPC, Webhooks, and Asynchronous Event-Driven APIs.

Enterprise APIs are public, partner, or internal contracts that outlive individual software versions. Backward compatibility, rigorous error models (RFC 7807), standard pagination, deterministic rate limiting, and Zero Trust security are mandatory architectural baselines.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master API specification template (OpenAPI 3.1 & Protocol agnostic).
* **Protocols & Styles**:
  - [rest-api.md](rest-api.md) — RESTful resource modeling, HTTP verbs, and URI design.
  - [graphql.md](graphql.md) — GraphQL schema design, query depth limits, and federation.
  - [grpc.md](grpc.md) — gRPC / Protocol Buffers service definition, streaming, and status codes.
  - [webhook.md](webhook.md) — Outbound webhook dispatch, HMAC signatures, and retry backoff.
  - [event-api.md](event-api.md) — CloudEvents specification, event schemas, and AsyncAPI.
* **Cross-Cutting Standards**:
  - [versioning.md](versioning.md) — Semantic versioning and deprecation timelines.
  - [error-model.md](error-model.md) — RFC 7807 Problem Details and gRPC error models.
  - [authentication.md](authentication.md) — OAuth2, mTLS, and API Key authentication patterns.
  - [authorization.md](authorization.md) — Scopes, claims, and ABAC/RBAC enforcement.
  - [pagination.md](pagination.md) — Keyset/cursor-based vs offset pagination standards.
  - [idempotency.md](idempotency.md) — `Idempotency-Key` headers and deduplication windows.
  - [rate-limiting.md](rate-limiting.md) — Token bucket algorithms and standard IETF rate-limit headers.
  - [compatibility.md](compatibility.md) — Backward compatibility rules and schema evolution.
* **Governance**:
  - [api-review-checklist.md](api-review-checklist.md) — 20-Point API governance checklist.
  - [examples/payment-api-design.md](examples/payment-api-design.md) — Complete Payment Gateway API specification.
