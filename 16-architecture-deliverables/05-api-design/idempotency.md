# API Idempotency Specification

## 1. Idempotency Key Semantics
* Clients MUST supply an `Idempotency-Key` header with a unique UUID v4 on all mutating `POST` requests.
* Server stores the request key in Redis with a 24-hour TTL:
  - State 1: `PROCESSING` (Prevents concurrent duplicate executions).
  - State 2: `COMPLETED` (Caches HTTP response status and body; subsequent identical calls return cached response).
