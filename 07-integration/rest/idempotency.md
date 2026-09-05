# API Idempotency & IETF Standards

## 1. The IETF Idempotency-Key Specification
Under the IETF Draft standard, mutating HTTP methods (`POST`, `PATCH`) achieve idempotency through client-supplied unique tokens in the request header:
```http
POST /v1/payments HTTP/1.1
Host: api.enterprise.com
Idempotency-Key: 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d
```

---

## 2. Server-Side Idempotency Processing Lifecycle

```mermaid
sequenceDiagram
    autonumber
    Client->>Gateway: POST /v1/payments (Idempotency-Key: X)
    Gateway->>Cache: SETNX idemp:X "IN_PROGRESS" EX 120
    alt Key already exists and status == "IN_PROGRESS"
        Gateway-->>Client: HTTP 409 Conflict (Concurrent Request In-Flight)
    else Key already exists and status == "COMPLETED"
        Gateway-->>Client: Return Cached Response (HTTP 200/201)
    else Key does not exist (First Time)
        Gateway->>Service: Execute Payment Logic
        Service->>DB: Persist Transaction
        Service-->>Gateway: Execution Success
        Gateway->>Cache: SET idemp:X "{status: COMPLETED, body: ...}" EX 86400
        Gateway-->>Client: Return Fresh Response
    end
```
