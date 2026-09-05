# API Client Architecture: Optimistic UI Updates & Rollback

## 1. Architectural Purpose & Problem Context
Updating UI state immediately before network confirmation; rolling back state on failure.

---

## 2. Structural Workflow

```mermaid
sequenceDiagram
    autonumber
    participant UI as Feature Component
    participant Client as API Client Interceptor
    participant Auth as Token Manager
    participant Network as Remote Backend API

    UI->>Client: Call getUserProfile()
    Client->>Auth: Attach Access Token
    Client->>Network: HTTP GET /v1/users/me
    alt Token Expired (401)
        Network-->>Client: HTTP 401 Unauthorized
        Client->>Auth: Acquire Refresh Lock & Refresh Token
        Auth->>Network: POST /auth/refresh
        Network-->>Auth: New Access Token
        Client->>Network: Replay Original Request with New Token
        Network-->>Client: HTTP 200 OK
    end
    Client-->>UI: Return Typed UserProfileDTO
```

---

## 3. Production Invariants
- Use a distributed mutex / single-flight promise during token refresh so 20 concurrent requests do not trigger 20 refresh calls.
- Never retry non-idempotent POST mutations automatically without an `Idempotency-Key`.
