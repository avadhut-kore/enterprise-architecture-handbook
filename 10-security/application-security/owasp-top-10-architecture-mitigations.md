# OWASP Top 10: Architectural Prevention

## Executive Summary

| OWASP Category | Vulnerability | Primary Architectural Prevention |
| :--- | :--- | :--- |
| **A01: Broken Access Control** | Unauthorized vertical/horizontal data access | Enforce Policy-as-Code (OPA) at Gateway + Row-Level Security in Database |
| **A02: Cryptographic Failures**| Plaintext data exposure, weak ciphers | Enforce TLS 1.3 only; AES-256-GCM envelope encryption with KMS CMKs |
| **A03: Injection** | SQL, Command, LDAP injection | Strictly mandate compile-time type-safe ORMs / Parameterized Queries |
| **A04: Insecure Design** | Missing threat models, business logic flaws | Mandatory STRIDE threat modeling at Architecture Inception Gate |
| **A05: Security Misconfiguration**| Default passwords, open cloud storage | Policy-as-Code (Checkov) in CI/CD blocking non-compliant Terraform |
| **A06: Vulnerable Components** | Vulnerable open-source packages | Automated SCA (Dependabot/Snyk) blocking builds on Critical/High CVEs |
| **A07: Identification & Auth** | Weak passwords, missing MFA | Mandate FIDO2 passwordless or OIDC SSO with adaptive risk scoring |
| **A08: Software & Data Integrity**| Malicious dependency tampering | Cryptographic container image signing (Cosign) and verified SBOMs |
| **A09: Security Logging Failures**| Missing audit trails, log tampering | Streaming logs directly to immutable WORM storage (S3 Object Lock) |
| **A10: SSRF** | Attacker probes cloud metadata service | Dedicated forward egress proxy + IMDSv2 enforced across all cloud VMs |
