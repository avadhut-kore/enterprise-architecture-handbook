# OpenID Connect Architecture & Protocol Flows

## Executive Summary

OpenID Connect extends OAuth 2.0 by introducing a standardized identity artifact: the **ID Token** (a signed JSON Web Token), along with standard endpoints for discovery and user attributes.

---

## 1. OIDC Architectural Roles

```mermaid
flowchart LR
    EU["End User"]
    RP["Relying Party (Client App)"]
    OP["OpenID Provider (IdP)"]

    EU -->|Logs in & Consents| OP
    RP -->|Redirects User for Auth| OP
    OP -->|Issues ID Token + Access Token| RP
    RP -->|Validates ID Token (Establishes Session)| RP
```

- **OpenID Provider (OP)**: The OAuth 2.0 Authorization Server capable of authenticating the End User and issuing claims via ID Tokens (e.g., Microsoft Entra ID, Okta, Google Cloud Identity).
- **Relying Party (RP)**: The client application that relies on the OpenID Provider for asserting the authenticated identity of the End User.
