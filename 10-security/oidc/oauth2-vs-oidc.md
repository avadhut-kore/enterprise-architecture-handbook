# OAuth 2.0 vs OpenID Connect (OIDC)

## Executive Summary

| Dimension | OAuth 2.0 | OpenID Connect (OIDC) |
| :--- | :--- | :--- |
| **Primary Focus** | **Authorization** (Delegated API Access) | **Authentication** (Federated Identity) |
| **What it answers**| "What resources is this application allowed to access?" | "Who is the currently logged-in user?" |
| **Core Artifact** | Access Token (typically opaque or internal JWT) | ID Token (standard signed JWT) + Access Token |
| **Target Consumer**| Protected Resource Server (API) | Relying Party (Client Application) |
| **Token Standard** | Unspecified by RFC 6749 | Strictly specified by OpenID Connect Core 1.0 |
| **User Profile Endpoint**| Non-standardized (vendor-specific) | Standardized `/userinfo` endpoint |
| **Discovery Mechanism**| Non-standardized | Standardized `/.well-known/openid-configuration` |
