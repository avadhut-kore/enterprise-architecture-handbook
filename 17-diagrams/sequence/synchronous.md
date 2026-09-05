# Synchronous Request-Reply Sequence Diagram

Synchronous interactions block the calling client until the receiving server processes the request and returns a response.

```mermaid
sequenceDiagram
    autonumber
    actor Client as Web Browser
    participant Gateway as API Gateway (Kong)
    participant Auth as Auth Service (OIDC)
    participant Svc as Product Catalog Service
    participant Cache as Redis Cache
    participant DB as PostgreSQL Database

    Client->>Gateway: GET /v1/products/123 (Bearer Token)
    activate Gateway
    Gateway->>Auth: Validate JWT Signature & Claims
    activate Auth
    Auth-->>Gateway: 200 OK (Claims: role=user, tenant=42)
    deactivate Auth

    Gateway->>Svc: GET /products/123 (X-Tenant-ID: 42)
    activate Svc

    Svc->>Cache: GET product:123
    activate Cache
    Cache-->>Svc: null (Cache Miss)
    deactivate Cache

    Svc->>DB: SELECT * FROM products WHERE id = 123
    activate DB
    DB-->>Svc: Product Row (JSON payload)
    deactivate DB

    Svc->>Cache: SETEX product:123 3600 (Payload)
    Svc-->>Gateway: 200 OK (Product JSON)
    deactivate Svc

    Gateway-->>Client: 200 OK (Cache-Control: public, max-age=300)
    deactivate Gateway
```

## Architectural Considerations
- **Blocking Latency**: End-to-end latency is the sum of all serial calls.
- **Cascading Exhaustion**: Thread starvation in upstream callers if downstream databases lock.
