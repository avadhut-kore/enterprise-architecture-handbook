# JWT Architecture, Token Lifecycle & Cryptographic Rotation

Stateless token lifecycle architecture detailing asymmetric signing, JSON Web Key Sets (JWKS) cache/invalidation, claims validation, and blacklist strategies.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph TokenIssuance ["Token Issuance (IdP)"]
        KMS["Cloud KMS / HSM<br/>[Private Key (RS256/ES256)]"]
        IdP["Identity Provider"]
        IdP -->|"Sign Token"| KMS
        JWKS_EP["Public JWKS Endpoint<br/>[/.well-known/jwks.json]"]
        IdP -.->|"Publish Public Key (kid)"| JWKS_EP
    end

    subgraph TokenStructure ["JWT Payload Anatomy"]
        Header["Header: alg, typ, kid"]
        Payload["Claims: iss, sub, aud, exp, nbf, roles"]
        Signature["Signature: HMAC / RSA / ECDSA"]
        Header --- Payload --- Signature
    end

    subgraph GatewayValidation ["Resource Gateway / Microservice"]
        GW["API Gateway / Service Mesh"]
        KeyCache["Local JWKS Memory Cache<br/>[TTL: 60m]"]
        RevokeStore["Token Revocation Blacklist<br/>[Redis Cluster]"]
        Backend["Protected Microservice"]

        GW -->|"1. Extract Bearer Token"| TokenStructure
        GW -->|"2. Verify Signature"| KeyCache
        KeyCache -.->|"Fetch if kid missing"| JWKS_EP
        GW -->|"3. Check Token JTI"| RevokeStore
        GW -->|"4. Validated Request"| Backend
    end

    classDef iss fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef val fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class KMS,IdP,JWKS_EP iss;
    class GW,KeyCache,RevokeStore,Backend val;
```

## PlantUML Specification

```plantuml
@startuml
component "Identity Provider" as idp
component "KMS Private Key" as privKey
component "Public JWKS Endpoint" as jwks
component "API Gateway" as gw
database "Redis Revocation List" as redis
component "Downstream Service" as svc

idp -> privKey : Sign JWT with active Key ID (kid)
idp -> jwks : Expose Public Keys
gw -> jwks : Cache Public Keys
gw -> redis : Verify Token JTI not blacklisted
gw -> gw : Verify Signature, exp, iss, aud
gw -> svc : Forward with Trusted Headers
@enduml
```

## Architectural Design Considerations

* **Algorithm Whitelisting**: Explicitly reject `alg: "none"` and enforce strict asymmetric verification algorithms (`RS256` or `ES256`).
* **JWKS Key Rotation**: Validate tokens using the `kid` header parameter; allow seamless key rotation without downtime by maintaining previous and next public keys in JWKS.
* **Token Revocation Dilemma**: For stateless tokens requiring immediate revocation, check token `jti` against a distributed in-memory cache (Redis) or use ephemeral token lifetimes.

## Related Documentation & Patterns

* [OAuth 2.0](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/oauth2.md)
* [API Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/api-security.md)
* [Key Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/key-management.md)
