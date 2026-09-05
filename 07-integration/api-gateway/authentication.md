# Edge Authentication Architecture

## 1. Offloading Authentication to the Gateway
Individual microservices should never handle raw password hashing or public OAuth token verification. The API Gateway authenticates the client at the edge perimeter.

```mermaid
sequenceDiagram
    autonumber
    Client->>Gateway: GET /v1/orders (Bearer JWT_Token)
    Gateway->>Gateway: Cryptographically Verify JWT Signature (RS256)
    Gateway->>Gateway: Extract Claims (user_id=42, tenant_id=Acme)
    Gateway->>OrderSvc: Forward GET with Internal Headers: X-User-Id=42, X-Tenant-Id=Acme
    OrderSvc-->>Gateway: 200 OK
    Gateway-->>Client: 200 OK
```

---

## 2. Mutual TLS (mTLS) for Zero Trust
While external traffic authenticates via JWT/OAuth2, internal communication between the API Gateway and backend microservices is secured via **mTLS (Mutual TLS)** using a service mesh (Istio / Linkerd), ensuring cryptographic identity verification for every packet.
