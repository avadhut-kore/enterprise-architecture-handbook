# OAuth 2.0 Authorization Framework & Grant Flows

Industry-standard token-based delegation architecture detailing Authorization Code Flow with PKCE (Proof Key for Code Exchange) and Client Credentials.

## Mermaid Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    actor User as Resource Owner (Browser)
    participant Client as Single Page App / Mobile App
    participant AuthServer as Authorization Server (OAuth2 IdP)
    participant ResourceServer as API Resource Server

    Note over Client: Generate code_verifier & code_challenge (S256)
    Client->>User: Redirect to Authorization Endpoint
    User->>AuthServer: GET /authorize?response_type=code&client_id=...&code_challenge=...
    AuthServer->>User: Render Login & Consent Screen
    User->>AuthServer: Submit Credentials & Consent
    AuthServer-->>Client: Redirect to redirect_uri with Authorization Code (?code=XYZ)
    
    Client->>AuthServer: POST /oauth/token (code=XYZ, code_verifier=ABC, client_id=...)
    Note over AuthServer: Verify code_challenge == SHA256(code_verifier)
    AuthServer-->>Client: Return Tokens (access_token, id_token, refresh_token)
    
    Client->>ResourceServer: GET /api/v1/orders (Authorization: Bearer <access_token>)
    ResourceServer->>ResourceServer: Cryptographically verify JWT via JWKS
    ResourceServer-->>Client: 200 OK + JSON Payload
```

## PlantUML Specification

```plantuml
@startuml
autonumber
actor "User" as user
participant "SPA / Mobile" as client
participant "OAuth2 Auth Server" as auth
participant "Resource API" as api

client -> client : Generate PKCE verifier + challenge
client -> user : Redirect to Auth URL
user -> auth : /authorize?code_challenge=...
auth -> user : Login + Consent
user -> auth : Submit credentials
auth -> client : Redirect with authorization code
client -> auth : POST /token (code + code_verifier)
auth -> client : 200 OK (access_token + refresh_token)
client -> api : GET /resource (Bearer token)
api -> client : 200 OK Response
@enduml
```

## Architectural Design Considerations

* **Mandatory PKCE**: Use PKCE for all authorization code flows, including backend confidential clients and public SPAs, to prevent authorization code injection.
* **Deprecation of Implicit Flow**: Implicit grant (`response_type=token`) and Resource Owner Password Credentials (ROPC) are strictly prohibited.
* **Token Lifetime**: Access tokens should be short-lived (5-15 minutes); refresh tokens must support rotation and replay detection.

## Related Documentation & Patterns

* [OIDC](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/oidc.md)
* [JWT Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/jwt.md)
* [API Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/api-security.md)
