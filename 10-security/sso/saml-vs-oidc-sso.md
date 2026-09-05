# SAML 2.0 vs OpenID Connect (OIDC) for Enterprise SSO

## Executive Summary

| Dimension | SAML 2.0 (Security Assertion Markup Language) | OpenID Connect (OIDC) |
| :--- | :--- | :--- |
| **Payload Encoding** | Verbose XML with XMLDSIG signatures | Compact JSON Web Tokens (JWT) |
| **Transport Mechanism**| Browser redirects via HTTP POST binding | HTTP GET/POST with RESTful JSON endpoints |
| **Mobile & API Fit** | Terrible (Difficult to parse XML on mobile/SPAs) | **Native** (First-class support in iOS, Android, SPAs) |
| **Adoption Scope** | Legacy enterprise on-prem software & older SaaS | Cloud-native microservices, mobile apps, modern SaaS |
| **XML Security Risks** | Vulnerable to XML Signature Wrapping & XXE attacks | Simpler, hardened JSON cryptographic validation |
