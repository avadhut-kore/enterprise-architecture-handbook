# Idempotency Architecture in Distributed Integration

## 1. The Core Principle
An operation is **idempotent** if performing it multiple times produces the exact same side effects and end state on the server as performing it once:

$$f(f(x)) = f(x)$$

In enterprise networks where packet drops, network timeouts, and load-balancer retries are inevitable, the integration platform cannot guarantee **exactly-once delivery** over the wire. Idempotency is the only architectural mechanism that turns **at-least-once delivery** into **effectively-once processing**.

## 2. Idempotency Key Architecture Pattern

```
[Client] ──(1) POST /transfers (Header: Idempotency-Key: abc-123)──> [API Gateway]
                                                                            │
                                  ┌───(2) Check Key in Redis Cache──────────┘
                                  │
                  ┌───────────────┴────────────────┐
                  ▼ (Key Exists?)                  ▼ (Key New)
             [YES: Cached]                    [NO: Acquire Lock]
                  │                                │
     Return Stored Response Body                   │
     (Status: 201 Created)                         ▼
                                       [Execute Core Ledger Write]
                                                   │
                                       [Save Response to Redis]
                                                   │
                                       Return Response to Client
```

## 3. Production Idempotency Schema (PostgreSQL)
```sql
CREATE TABLE idempotency_records (
    idempotency_key VARCHAR(128) PRIMARY KEY,
    client_id VARCHAR(64) NOT NULL,
    request_hash VARCHAR(64) NOT NULL, -- SHA-256 of request body to detect payload mutation
    status VARCHAR(24) NOT NULL,       -- 'IN_PROGRESS', 'COMPLETED', 'FAILED'
    response_code INT,
    response_body JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL
);

CREATE INDEX idx_idempotency_expiry ON idempotency_records(expires_at);
```

## 4. Critical Edge Cases
- **Concurrent In-Flight Requests**: If a duplicate request arrives while the first request is still `IN_PROGRESS`, return `HTTP 409 Conflict` or block on a distributed lock until the initial request finishes.
- **Payload Mismatch**: If a request arrives with an existing `Idempotency-Key` but a different request body hash, fail immediately with `HTTP 422 Unprocessable Entity`. Never allow key reuse with mismatched parameters.
