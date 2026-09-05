# OWASP API Security Top 10: Architectural Mitigations

## Executive Summary

| Risk Code | Vulnerability Name | Architectural Root Cause | Architectural Mitigation Standard |
| :--- | :--- | :--- | :--- |
| **API1:2023** | **Broken Object Level Authorization (BOLA)** | Endpoint trusts client-supplied resource ID without verifying tenant context | Inject validated tenant ID from verified JWT; enforce Database Row-Level Security |
| **API2:2023** | **Broken Authentication** | Weak token generation, missing PKCE, unrotated API keys | Mandate OAuth 2.1 Authorization Code with PKCE + FIDO2 passkeys |
| **API3:2023** | **Broken Object Property Level Authorization** | Mass assignment / Over-posting modifies unauthorized internal fields | Strict DTO binding; ignore unmapped JSON fields; compile-time property whitelists |
| **API4:2023** | **Unrestricted Resource Consumption** | Missing rate limits or query pagination limits allow resource exhaustion | Enforce distributed sliding-window rate limiting; mandate pagination (`limit` capped at 100) |
| **API5:2023** | **Broken Function Level Authorization (BFLA)** | Administrative endpoints (`/admin/users`) exposed without role check | Centralized Policy-as-Code (OPA) evaluating RBAC/ABAC at API Gateway before routing |
| **API6:2023** | **Unrestricted Access to Sensitive Business Flows**| Automated bot scalping or credential stuffing | Behavioral bot detection, CAPTCHA on anomalous requests, device fingerprinting |
| **API7:2023** | **Server-Side Request Forgery (SSRF)** | Server fetches user-supplied URL without network egress filtering | Dedicated egress proxy blocking private RFC 1918 CIDR ranges and cloud metadata (169.254.169.254) |
| **API8:2023** | **Security Misconfiguration** | Unhardened default headers, verbose stack traces exposed to client | Automated IaC security scanning (Checkov), global error interceptor hiding stack traces |
| **API9:2023** | **Improper Inventory Management** | Shadow APIs, unversioned deprecated v1 endpoints unmonitored | Automated API cataloging via OpenAPI spec generation in CI/CD; automated v1 deprecation |
| **API10:2023**| **Unsafe Consumption of APIs** | Blindly trusting responses from third-party payment/partner APIs | Treat third-party APIs as untrusted input; validate response schemas; enforce timeouts and circuit breakers |
