# Full-Stack Reference Architecture: Angular + Java Spring Boot Corporate Monorepo

## 1. Architectural Vision & End-to-End Context
Large-scale enterprise intranet architecture leveraging Nx monorepo for Angular frontend and Spring Boot microservices with Eureka/Consul discovery.

---

## 2. End-to-End System Diagram

```mermaid
flowchart LR
    subgraph Client Layer
        UI[Web Client / Mobile App]
    end
    subgraph Gateway / BFF Layer
        BFF[BFF Gateway / Reverse Proxy]
    end
    subgraph Backend Services
        App[Backend Application Runtime]
        Cache[(Distributed Cache)]
        DB[(Primary Database)]
    end

    UI -->|HTTPS / OpenAPI / JWT| BFF
    BFF -->|mTLS / Internal gRPC| App
    App --> Cache
    App --> DB
```

---

## 3. Production Invariants & Integration Rules
- Contracts between UI and Backend must be strongly typed and generated from OpenAPI or Protobuf definitions.
- Security tokens (OAuth2/OIDC) must be validated with zero-trust verification at the API boundary.
- Distributed trace contexts (`traceparent` header) must propagate seamlessly from frontend user actions to database queries.
