# API Gateway Architecture & Patterns

## 1. Overview & Architectural Role
The API Gateway is the single point of ingress and policy enforcement sitting between external clients (web, mobile, IoT, third-party partners) and internal microservice clusters. It encapsulates system architecture, shields internal network topologies, and centralizes cross-cutting concerns (authentication, TLS termination, rate limiting, and observability).

```mermaid
flowchart TD
    Clients[External Clients: Web, iOS, Android, Partners] -->|Public Internet / HTTPS| Gateway[API Gateway Layer]
    
    subgraph Gateway Cross-Cutting Policies
        Auth[Authentication & JWT Validate]
        Rate[Token-Bucket Rate Limiting]
        TLS[TLS 1.3 Termination]
        Route[Dynamic Weighted Routing]
    end
    
    Gateway --> Auth --> Rate --> TLS --> Route
    
    Route -->|gRPC / Internal HTTP| SvcA[Order Microservice]
    Route -->|gRPC / Internal HTTP| SvcB[Customer Microservice]
    Route -->|gRPC / Internal HTTP| SvcC[Payment Microservice]
```

---

## 2. Directory Structure
* [API Gateway Pattern](api-gateway-pattern.md)
* [Reverse Proxy Architecture](reverse-proxy.md)
* [Dynamic Routing & Traffic Splitting](routing.md)
* [Edge Authentication (JWT & OAuth2)](authentication.md)
* [Edge Authorization & Policy Enforcement (OPA)](authorization.md)
* [Distributed Rate Limiting](rate-limiting.md)
* [Request Transformation & gRPC Transcoding](request-transformation.md)
* [SSL/TLS Termination](ssl-termination.md)
* [Backend-for-Frontend (BFF) Pattern](bff-pattern.md)
* [Envoy vs. Kong vs. AWS API Gateway](envoy-vs-kong-vs-api-gateway.md)
