# OIDC Discovery & Automated JWKS Key Rolling

## Executive Summary

The OpenID Connect Discovery specification allows client applications to automatically configure endpoints, supported scopes, and cryptographic signing keys by querying a standardized discovery document:
`https://{issuer}/.well-known/openid-configuration`

---

## 1. Automated JWKS Key Rotation Architecture

```mermaid
sequenceDiagram
    autonumber
    participant Client as Microservice / API Gateway
    participant IdP as Identity Provider (OIDC)

    Note over Client: Startup: Fetches IdP Configuration
    Client->>IdP: GET /.well-known/openid-configuration
    IdP-->>Client: Returns JSON metadata (jwks_uri: "https://idp.com/jwks.json")
    Client->>IdP: GET /jwks.json
    IdP-->>Client: Returns Public Keys {keys: [{kid: "key-2026-A", ...}]}
    Note over Client: Caches public keys in memory (TTL: 24 hours)

    Note over Client,IdP: Rotation Event: IdP begins signing with "key-2026-B"
    Client->>Client: Receives token with unknown kid: "key-2026-B"
    Client->>IdP: Cache-miss bypass: GET /jwks.json (Fetches latest keys)
    IdP-->>Client: Returns {keys: [key-2026-A, key-2026-B]}
    Client->>Client: Updates memory cache and validates token successfully!
```
