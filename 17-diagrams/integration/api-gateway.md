# Modern API Gateway Integration Architecture

Lightweight, cloud-native API Gateway pattern providing perimeter security, SSL termination, traffic management, and rate limiting.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph ExternalClients ["External Consumers"]
        WebSPA["Single Page App (Browser)"]
        Mobile["Mobile Apps (iOS/Android)"]
        Partner["Third-Party B2B Partner"]
    end

    subgraph APIGatewayCluster ["Enterprise API Gateway (Kong / Apigee / Envoy)"]
        TLS["TLS 1.3 Termination & WAF"]
        AuthN["OAuth2 / OIDC Token Verification"]
        RateLimit["Distributed Rate Limiting (Token Bucket)"]
        Router["Path & Method Routing Engine"]
        Cache["Response Cache (Redis backed)"]

        TLS --> AuthN
        AuthN --> RateLimit
        RateLimit --> Cache
        Cache --> Router
    end

    subgraph InternalServices ["Internal Private Mesh (mTLS)"]
        SvcOrder["Order Microservice"]
        SvcPayment["Payment Microservice"]
        SvcCustomer["Customer Microservice"]

        Router -->|"Route: /api/v1/orders"| SvcOrder
        Router -->|"Route: /api/v1/payments"| SvcPayment
        Router -->|"Route: /api/v1/customers"| SvcCustomer
    end

    WebSPA --> TLS
    Mobile --> TLS
    Partner --> TLS
```

## PlantUML Specification

```plantuml
@startuml
actor Client
participant "API Gateway" as gw
database "OAuth IdP" as idp
participant "Order Service" as svc1
participant "Payment Service" as svc2

Client -> gw : HTTPS Request with Bearer Token
gw -> idp : Validate JWT Signature
idp -> gw : Valid Token & Claims
gw -> gw : Enforce Rate Limits
gw -> svc1 : Forward via mTLS (/orders)
svc1 -> gw : Response
gw -> Client : Filtered JSON Response
@enduml
```

## Architectural Design Considerations

* **Dumb Pipes Principle**: Unlike an ESB, an API Gateway focuses strictly on edge routing, authentication, and traffic policy without performing heavy business transformations.
* **BFF (Backend for Frontend)**: Implement distinct API gateways tailored to specific client form factors (Mobile BFF vs Web BFF vs Partner Gateway).
* **High Availability**: Deploy gateways across multiple availability zones backed by auto-scaling groups to sustain high-volume traffic bursts.

## Related Documentation & Patterns

* [Security: API Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/api-security.md)
* [ESB](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/esb.md)
* [Event Mesh](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/event-mesh.md)
