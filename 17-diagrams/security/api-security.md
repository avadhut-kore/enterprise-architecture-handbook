# Enterprise API Security Architecture & Defense-in-Depth

Multi-layered API threat mitigation architecture covering L7 API gateway enforcement, schema validation, rate throttling, and mTLS.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph PublicInternet ["External Zone"]
        Consumer["Third-Party Partner / Mobile Client"]
    end

    subgraph EdgePerimeter ["Edge Security Perimeter"]
        DDoS["Cloudflare / Akamai DDoS Scrubbing"]
        WAF["Web Application Firewall (OWASP Rules)"]
        Consumer -->|"TLS 1.3"| DDoS
        DDoS --> WAF
    end

    subgraph APIGatewayZone ["DMZ / Ingress Gateway Layer"]
        APIGW["Enterprise API Gateway (Kong / Apigee)"]
        TokenVal["JWT / OAuth2 Signature Validator"]
        RateLimit["Distributed Token Bucket Rate Limiter"]
        SchemaVal["OpenAPI JSON Schema Validator"]

        WAF -->|"Sanitized Traffic"| APIGW
        APIGW --> TokenVal
        APIGW --> RateLimit
        APIGW --> SchemaVal
    end

    subgraph InternalMesh ["Internal Zero-Trust Mesh"]
        MeshIngress["Service Mesh Ingress (Envoy)"]
        ServiceA["Core Billing Service"]
        ServiceB["Account Balance Service"]

        SchemaVal -->|"mTLS (SPIFFE/SPIRE)"| MeshIngress
        MeshIngress --> ServiceA
        ServiceA -->|"East-West mTLS"| ServiceB
    end

    classDef edge fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef gw fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef internal fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class DDoS,WAF edge;
    class APIGW,TokenVal,RateLimit,SchemaVal gw;
    class MeshIngress,ServiceA,ServiceB internal;
```

## PlantUML Specification

```plantuml
@startuml
actor Client
participant "DDoS & WAF Shield" as edge
participant "API Gateway" as gw
participant "OAuth2 Authorization Server" as auth
participant "Internal Microservice" as svc

Client -> edge : HTTPS API Request
edge -> edge : Inspect for SQLi, XSS, Bot Patterns
edge -> gw : Forward Cleaned Traffic
gw -> auth : Validate Token / Introspect
auth -> gw : Token Active + Claims
gw -> gw : Enforce Rate Limits & Payload Schema
gw -> svc : Forward with Mutual TLS (mTLS)
svc -> gw : 200 OK
gw -> Client : Filtered Response
@enduml
```

## Architectural Design Considerations

* **OWASP API Security Top 10**: Mitigate Broken Object Level Authorization (BOLA) and Broken Authentication directly at the gateway and domain layers.
* **Strict Schema Enforcement**: Block malformed JSON bodies and unexpected parameters before requests reach backend application code.
* **Mutual TLS (mTLS)**: Enforce mTLS for all B2B partner integrations and internal microservice-to-microservice communication.

## Related Documentation & Patterns

* [OAuth 2.0](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/oauth2.md)
* [WAF & DDoS](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/waf.md)
* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
