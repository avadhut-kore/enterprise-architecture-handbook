# OpenID Connect (OIDC) Federated Identity Architecture

Identity layer on top of OAuth 2.0 enabling clients to verify end-user identity based on authentication performed by an Authorization Server.

## Mermaid Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    actor User as Enterprise User
    participant RP as Relying Party (Web Application)
    participant OP as OpenID Provider (IdP)
    participant UserInfo as OIDC UserInfo Endpoint

    RP->>OP: GET /.well-known/openid-configuration (Discovery)
    OP-->>RP: Return JSON Metadata (jwks_uri, issuer, endpoints)
    
    User->>RP: Access Protected Resource
    RP->>User: Redirect to OP (/auth?scope=openid email profile)
    User->>OP: Authenticate & Authorize Scopes
    OP-->>RP: 302 Redirect with Auth Code
    
    RP->>OP: POST /token (code, client_secret, redirect_uri)
    OP-->>RP: 200 OK (id_token [JWT], access_token)
    
    Note over RP: Validate id_token (iss, aud, exp, signature via JWKS)
    RP->>UserInfo: GET /userinfo (Authorization: Bearer <access_token>)
    UserInfo-->>RP: Return Claims JSON (sub, email, name, groups)
    RP-->>User: Set Application Session Cookie & Display Dashboard
```

## PlantUML Specification

```plantuml
@startuml
actor User
participant "Relying Party (App)" as RP
participant "OpenID Provider" as OP

RP -> OP : Read /.well-known/openid-configuration
User -> RP : Access Request
RP -> OP : Redirect with scope=openid profile email
User -> OP : Enter Credentials + MFA
OP -> RP : Return Auth Code
RP -> OP : Exchange Code for ID Token + Access Token
RP -> RP : Validate ID Token JWT signature & claims
RP -> User : Authenticated App Session Established
@enduml
```

## Architectural Design Considerations

* **Discovery Endpoint**: Relying parties must dynamically fetch OpenID metadata from `/.well-known/openid-configuration` rather than hardcoding endpoints.
* **Claims Validation**: The `iss` (issuer) must match the OP URL, `aud` (audience) must match the Client ID, and `nonce` must be verified against replay attacks.
* **Logout Specifications**: Implement OIDC Back-Channel Logout or RP-Initiated Logout for enterprise-wide single sign-out.

## Related Documentation & Patterns

* [OAuth 2.0](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/oauth2.md)
* [JWT Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/jwt.md)
* [Authentication](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/authentication.md)
