# Application Security (AppSec) Architecture (`application-security/`)

## Executive Summary

Application Security focuses on designing software architectures that are intrinsically resistant to code-level exploits, business logic abuse, and data exfiltration.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`appsec-architecture-principles.md`](appsec-architecture-principles.md) | AppSec Foundations | Memory safety, parameterized queries, context-aware escaping |
| [`owasp-top-10-architecture-mitigations.md`](owasp-top-10-architecture-mitigations.md) | OWASP Mitigations | Structural mitigations for injection, broken auth, XSS, SSRF |
| [`ssrf-defense-architecture.md`](ssrf-defense-architecture.md) | SSRF Protection | Egress proxies, DNS rebinding mitigation, cloud metadata isolation |
| [`injection-defense-patterns.md`](injection-defense-patterns.md) | Injection Defense | Parameterized SQL, ORMs, Command Injection prevention |
| [`insecure-deserialization-defenses.md`](insecure-deserialization-defenses.md) | Deserialization Safety| Banning Java/Python pickle; adopting Protobuf/JSON schema |
| [`business-logic-vulnerability-mitigations.md`](business-logic-vulnerability-mitigations.md) | Logic Flaws | Finite state machines, concurrency locks, distributed idempotency |
