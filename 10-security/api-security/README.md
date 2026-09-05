# API Security Architecture (`api-security/`)

## Executive Summary

APIs are the primary entry point and attack surface for modern enterprise systems. Securing APIs requires an architectural defense combining edge WAFs, API gateways, cryptographic token validation, fine-grained object-level authorization, strict schema parsing, and distributed rate limiting.

---

## Key Guides in this Directory

| Guide | Scope | Core Content |
| :--- | :--- | :--- |
| [`api-security-architecture.md`](api-security-architecture.md) | End-to-End Design | Architectural layers, mTLS, gateway chokepoints, token verification |
| [`owasp-api-security-top-10.md`](owasp-api-security-top-10.md) | Vulnerability Mitigations | BOLA, broken auth, BOPLA, resource consumption, BFLA, SSRF |
| [`rate-limiting-and-throttling.md`](rate-limiting-and-throttling.md) | Traffic Defense | Token bucket, sliding window, Redis distributed counters |
| [`api-input-and-schema-validation.md`](api-input-and-schema-validation.md) | Ingress Sanitization | OpenAPI / JSON schema validation, preventing mass assignment |
| [`request-signing-and-replay-protection.md`](request-signing-and-replay-protection.md) | Non-Repudiation | HMAC-SHA256, timestamps, nonces, and idempotent requests |
| [`api-gateway-security-patterns.md`](api-gateway-security-patterns.md) | Gateway Architecture | Token exchange (Opaque to JWT), perimeter vs internal gateways |
