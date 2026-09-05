# OpenID Connect (OIDC) Architecture (`oidc/`)

## Executive Summary

OpenID Connect (OIDC) is an identity layer built directly on top of the OAuth 2.0 framework. It enables clients to verify the identity of the end user based on authentication performed by an Authorization Server, and to obtain basic profile information in an interoperable, REST-like manner.

---

## Key Guides in this Directory

| Guide | Scope | Core Content |
| :--- | :--- | :--- |
| [`oidc-architecture.md`](oidc-architecture.md) | OIDC Foundations | Core actors, OpenID Provider (OP), Relying Party (RP) |
| [`id-token-vs-access-token.md`](id-token-vs-access-token.md) | Token Semantics | Architectural distinction between ID Tokens and Access Tokens |
| [`claims-and-userinfo.md`](claims-and-userinfo.md) | Identity Data | Standard claims (`sub`, `iss`, `aud`, `auth_time`) and UserInfo |
| [`discovery-and-jwks.md`](discovery-and-jwks.md) | Discovery Standard | `.well-known/openid-configuration` and automated JWKS key rolling |
| [`nonce-and-replay-protection.md`](nonce-and-replay-protection.md) | Replay Defenses | Using cryptographically random nonces to stop ID token replay |
| [`oauth2-vs-oidc.md`](oauth2-vs-oidc.md) | Comparison Matrix | Definitive structural comparison between OAuth 2.0 and OIDC |
