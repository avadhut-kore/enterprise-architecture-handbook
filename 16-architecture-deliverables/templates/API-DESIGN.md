# API Design Specification: [API NAME]

---
**Metadata**:
* **API ID**: API-[NAME]-001
* **Protocol**: REST | gRPC | GraphQL | Webhook
---

## 1. Endpoint Definitions
| Method | Path | Summary | Idempotent | Auth Scope |
|---|---|---|---|---|
| POST | /v1/[resource] | Create resource | Yes (Keyed) | [resource]:write |

## 2. Request & Response Payload Schemas
[Complete JSON schemas with field validation rules.]

## 3. Error Handling (RFC 7807)
[Standard Problem Details JSON payload and error codes.]
