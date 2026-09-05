# API Design Specification: [API / Service Name]

> **API Name**: [e.g., Customer Payments Core API]  
> **Protocol**: [RESTful HTTP/2 / gRPC / GraphQL]  
> **Base URL**: `https://api.enterprise.domain/v1/[resource]`  
> **API Maturity**: Richardson Maturity Level 3 (Hypermedia / HATEOAS where applicable)  
> **Status**: [Draft | Review | Approved | Deprecated]  
> **Version**: [v1.0.0]

---

## 1. API Overview & Resource Hierarchy

*Describe the domain capabilities exposed by this API, consumer personas (Mobile, Web, B2B Partners), and resource model.*

```text
/api/v1/customers
  ├── POST   /                      -> Register new customer
  ├── GET    /{id}                  -> Fetch customer details
  ├── PUT    /{id}                  -> Full update customer profile
  ├── PATCH  /{id}                  -> Partial update customer profile
  └── /api/v1/customers/{id}/wallets
        ├── GET   /                 -> List customer wallets
        └── POST  /                 -> Provision a new wallet
```

---

## 2. Authentication, Authorization & Headers

### 2.1 Security Schemes
* **Auth Scheme**: OAuth2 Bearer Token (`Authorization: Bearer <JWT>`).
* **Token Issuer**: `https://identity.enterprise.domain/oauth2/v1`
* **Audience**: `api://payments-service`

### 2.2 Standard Request Headers

| Header Name | Type | Mandatory? | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `Authorization` | String | Yes | OAuth2 JWT Bearer token | `Bearer eyJhbGciOi...` |
| `X-Correlation-ID` | UUID | Yes | Client-generated request trace ID | `c73a0e19-94b2-4d2a-b67f-94d0b135e89a` |
| `Idempotency-Key` | String | Mutating | Unique UUID for safe mutation retries | `9f3c7b2a-1122-4433-8899-aabbccddeeff` |
| `Content-Type` | String | Body req | MIME type of request body | `application/json` |
| `Accept` | String | Yes | Requested response format | `application/json` |

---

## 3. Endpoints Specification & Contracts

### 3.1 Endpoint: Create Payment Intent
* **Method**: `POST`
* **Path**: `/api/v1/payments/intents`
* **OAuth Scope**: `payments:write`

#### Request Payload Schema (JSON)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["customerId", "amount", "currency", "paymentMethod"],
  "properties": {
    "customerId": { "type": "string", "format": "uuid" },
    "amount": { "type": "number", "minimum": 0.01 },
    "currency": { "type": "string", "pattern": "^[A-Z]{3}$" },
    "paymentMethod": {
      "type": "object",
      "required": ["type", "token"],
      "properties": {
        "type": { "type": "string", "enum": ["CARD", "SEPA", "APPLE_PAY"] },
        "token": { "type": "string" }
      }
    }
  }
}
```

#### Example Response: `201 Created`
```json
{
  "paymentIntentId": "pi_88492048-2849-411a",
  "status": "REQUIRES_ACTION",
  "amount": 150.00,
  "currency": "EUR",
  "createdAt": "2026-09-05T08:30:00Z",
  "_links": {
    "self": { "href": "/api/v1/payments/intents/pi_88492048-2849-411a" },
    "nextAction": { "href": "https://3ds.bank.com/challenge?id=xyz" }
  }
}
```

---

## 4. Standard Error Response Schema (RFC 7807)

All error responses return `application/problem+json` following RFC 7807:

```json
{
  "type": "https://api.enterprise.domain/errors/insufficient-funds",
  "title": "Insufficient Funds",
  "status": 422,
  "detail": "Customer wallet balance (EUR 20.00) is insufficient for transaction amount (EUR 150.00).",
  "instance": "/api/v1/payments/intents/pi_88492048-2849-411a",
  "code": "ERR_PAYMENT_INSUFFICIENT_FUNDS",
  "correlationId": "c73a0e19-94b2-4d2a-b67f-94d0b135e89a",
  "invalidParams": []
}
```

---

## 5. Rate Limiting, Throttling & Caching

* **Rate Limits**:
  * Tier 1 (Standard B2C): 100 requests / second per IP.
  * Tier 2 (Enterprise B2B Partner): 2,000 requests / second per client token.
* **Rate Limit Headers Returned**:
  * `X-RateLimit-Limit`: `100`
  * `X-RateLimit-Remaining`: `42`
  * `X-RateLimit-Reset`: `1757064000` (Unix timestamp)
* **HTTP Caching**: Safe `GET` endpoints emit `Cache-Control: public, max-age=300, must-revalidate` and `ETag` headers for conditional validation (`304 Not Modified`).

---

## 6. Versioning & Deprecation Policy

* **URI Versioning**: Major breaking changes increment the URI path (e.g., `/v1/` to `/v2/`).
* **Non-Breaking Changes**: Adding new optional fields or endpoints does not increment the version.
* **Sunset Window**: Deprecated endpoints return a `Sunset: <date>` HTTP header and remain supported for at least 12 months before final decommission.
