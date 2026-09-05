# JSON Web Token (JWT) Architecture (`jwt/`)

## Executive Summary

JSON Web Tokens (RFC 7519) are compact, URL-safe means of representing claims to be transferred between two parties. In modern enterprise architectures, JWTs serve as the primary vehicle for stateless access tokens and identity assertions.

---

## Key Guides in this Directory

| Guide | Scope | Core Content |
| :--- | :--- | :--- |
| [`jwt-architecture-and-structure.md`](jwt-architecture-and-structure.md) | Format & Encoding | Header, Payload, Signature, Base64URL encoding |
| [`signing-algorithms.md`](signing-algorithms.md) | Cryptographic Ciphers | RS256 vs ES256 vs EdDSA vs HS256 trade-offs |
| [`jwt-validation-algorithm.md`](jwt-validation-algorithm.md) | Verification Checklist | Deterministic 8-step validation algorithm |
| [`token-storage-strategies.md`](token-storage-strategies.md) | Client Storage | HttpOnly SameSite cookies vs LocalStorage vs Memory |
| [`jwt-vs-opaque-tokens.md`](jwt-vs-opaque-tokens.md) | Token Architecture | Stateless JWTs vs Stateful Opaque Tokens trade-off |
| [`common-jwt-security-failures.md`](common-jwt-security-failures.md) | Vulnerability Mitigations| `alg: none`, key confusion, signature stripping |
