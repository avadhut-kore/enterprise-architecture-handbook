# API Gateway Security Patterns: Token Exchange & Boundaries

## Executive Summary

The API Gateway acts as the security translation boundary between the public internet and internal microservices.

---

## 1. Token Exchange Pattern (Opaque to JWT)

```mermaid
sequenceDiagram
    autonumber
    actor Client as Browser Client
    participant GW as API Gateway (Edge)
    participant Redis as Session Cache
    participant Svc as Internal Microservice

    Client->>GW: GET /orders (Cookie: session_id=uuid_8942)
    Note over GW: 1. Validates Session Cookie against Redis
    GW->>Redis: GET session:uuid_8942
    Redis-->>GW: Returns User Claims {id: 101, roles: ["User"], tenant: "T-99"}
    Note over GW: 2. Mints short-lived internal JWT (1-min TTL)
    GW->>Svc: GET /orders (Authorization: Bearer <Internal_JWT>)
    Note over Svc: 3. Validates Internal JWT locally via JWKS; processes request
    Svc-->>GW: 200 OK (Orders Data)
    GW-->>Client: 200 OK
```
- **Architectural Benefit**: Frontend clients never see or store internal JWTs containing microservice claims; internal microservices never make expensive database calls to validate sessions.
