# Idempotency Architecture & Distributed Deduplication

## 1. Mathematical Definition
An operation is **idempotent** if executing it multiple times produces the exact same side-effects and outcome as executing it once:
$$f(f(x)) = f(x)$$

In distributed systems where network drops force clients to retry requests, idempotency is **mandatory** to prevent duplicate credit card charges, duplicate bank transfers, or duplicate inventory deductions.

```mermaid
sequenceDiagram
    autonumber
    Client->>Gateway: POST /payments (Idempotency-Key: 9b1deb4d-3b7d-4bad)
    Gateway->>DB: INSERT key INTO idempotency_keys (Status: PROCESSING)
    Gateway->>Stripe: Charge Card $100
    Gateway->>DB: UPDATE idempotency_keys (Status: COMPLETED, Response: {id: tx_123})
    Gateway-->>Client: HTTP 200 OK
    
    Note over Client,Gateway: Network Glitch! Client Never Receives 200 OK!
    
    Client->>Gateway: RETRY: POST /payments (Idempotency-Key: 9b1deb4d-3b7d-4bad)
    Gateway->>DB: SELECT status, response FROM idempotency_keys
    Note over Gateway: Status COMPLETED detected! DO NOT RE-CHARGE CARD!
    Gateway-->>Client: Return Cached HTTP 200 OK ({id: tx_123})
```

---

## 2. Implementation with Redis / Distributed Locks
* Use atomic `SET key value NX EX 86400` (set if not exists with 24-hour TTL).
* If key exists and status is `PROCESSING`: return `HTTP 409 Conflict` (request currently in flight).
* If key exists and status is `COMPLETED`: return stored response payload immediately.
