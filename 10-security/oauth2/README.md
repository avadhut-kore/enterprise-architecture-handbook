# OAuth 2.0 Framework Architecture (`oauth2/`)

## Executive Summary

OAuth 2.0 (RFC 6749) is the industry-standard delegated authorization framework. It allows a third-party client application to obtain limited access to a protected HTTP resource on behalf of a resource owner, without requiring the user to share their credentials with the client.

---

## Key Guides in this Directory

| Guide | Core Topic | Architectural Impact |
| :--- | :--- | :--- |
| [`oauth2-architecture.md`](oauth2-architecture.md) | Protocol Roles & Flows | Resource Owner, Client, Authorization Server, Resource Server |
| [`authorization-code-with-pkce.md`](authorization-code-with-pkce.md) | PKCE Standard | Mandatory flow for SPAs, Mobile, and Web Clients (RFC 7636) |
| [`client-credentials-flow.md`](client-credentials-flow.md) | Machine-to-Machine | Inter-service microservice authentication |
| [`refresh-token-rotation.md`](refresh-token-rotation.md) | Refresh Governance | Single-use rotation, token family tracking, breach invalidation |
| [`token-scopes-and-consent.md`](token-scopes-and-consent.md) | Scopes & Permissions | Designing granular, resource-oriented permission namespaces |
| [`token-validation-and-introspection.md`](token-validation-and-introspection.md) | Validation Strategies | Local cryptographic validation (JWKS) vs RFC 7662 Introspection |
| [`oauth-vs-authentication.md`](oauth-vs-authentication.md) | Architecture Reality | Why OAuth 2.0 is NOT an authentication protocol |
