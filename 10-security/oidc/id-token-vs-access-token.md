# ID Token vs Access Token: Architectural Semantics

## Executive Summary

Confusing ID Tokens with Access Tokens is a primary source of authorization vulnerabilities. They serve completely different audiences and possess fundamentally distinct lifecycles.

---

## 1. Comprehensive Comparison Matrix

| Property | ID Token | Access Token |
| :--- | :--- | :--- |
| **Intended Audience (`aud`)**| The **Client Application (Relying Party)** | The **Resource Server (Protected API)** |
| **Primary Purpose** | **Authentication**: Proves that the user authenticated, when they authenticated, and who they are. | **Authorization**: Grants delegated permission to access specific backend API endpoints. |
| **Format** | Strictly a signed **JSON Web Token (JWT)** | Opaque string OR signed JWT |
| **Who Validates It?** | The Client Application frontend / backend | The API Gateway / Backend Microservices |
| **Can it be passed to APIs?** | **NO (Anti-Pattern)**. APIs must reject ID tokens presented in the `Authorization` header. | **YES**. Presented as `Authorization: Bearer <token>`. |
| **Typical Lifetime** | Short (5–15 minutes, used to establish client session) | Short (15–60 minutes) |
| **Key Claims** | `sub`, `iss`, `aud`, `auth_time`, `nonce`, `email` | `sub`, `iss`, `aud`, `client_id`, `scope`, `permissions` |
