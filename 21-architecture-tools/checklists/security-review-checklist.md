# Enterprise Security & Zero Trust Review Checklist

Ensure applications, APIs, and cloud infrastructure comply with Zero Trust principles, OWASP Top 10 guidelines, and regulatory frameworks.

---

## 1. Authentication & Identity (AuthN)
* [ ] **Modern Protocol**: Is authentication based on modern protocols (OAuth 2.0 / OpenID Connect)? Legacy HTTP Basic or custom token schemes prohibited.
* [ ] **Multi-Factor Authentication (MFA)**: Is MFA enforced on all human administrative access, VPNs, and privileged developer consoles?
* [ ] **Short-Lived Access Tokens**: Do JWT access tokens have an expiration `<= 15 minutes`?
* [ ] **Cryptographic Signature Validation**: Does the resource server validate token signature (RS256/ES256), issuer (`iss`), audience (`aud`), and expiration (`exp`) on every request?

---

## 2. Authorization & Access Control (AuthZ)
* [ ] **Principle of Least Privilege**: Are service accounts and users restricted to the absolute minimum permissions required?
* [ ] **Tenant Isolation Enforced**: Is multi-tenant data segregated with mandatory `tenant_id` validation at the database query or row-level security layer?
* [ ] **Centralized Policy Engine**: Are complex authorization decisions offloaded to Open Policy Agent (OPA) or verified authorization services?
* [ ] **BOLA / IDOR Prevention**: Are object references verified to ensure the authenticated user owns the requested entity (OWASP API #1)?

---

## 3. Cryptography & Secrets Management
* [ ] **TLS 1.3 Mandatory**: Is TLS 1.3 enforced for all inbound and outbound connections? TLS 1.0 and 1.1 disabled; insecure ciphers rejected.
* [ ] **No Hardcoded Secrets**: Has the repository been scanned (via Gitleaks / TruffleHog) with zero exposed keys, certificates, or tokens?
* [ ] **Automated Secret Rotation**: Are secrets stored in HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault with automatic rotation enabled?
* [ ] **Envelope Encryption**: Is sensitive customer data encrypted before storage using data encryption keys (DEK) wrapped by a root key (KEK)?

---

## 4. Application Security & Vulnerability Scanning
* [ ] **Input Sanitization**: Are all client inputs strongly typed, validated, and parameterized to prevent SQL injection, NoSQL injection, and SSRF?
* [ ] **CI/CD SAST & SCA**: Do CI pipelines run static code analysis (Semgrep/SonarQube) and dependency vulnerability scans (Snyk/Trivy) on every pull request?
* [ ] **Container Hardening**: Do containers run as non-root users with read-only root filesystems and minimal distroless base images?
* [ ] **Security Headers**: Does the web ingress emit modern headers (`Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`)?

---

## 5. Security Logging, Auditing & SIEM
* [ ] **Immutable Audit Trail**: Are all authentication attempts, permission changes, and data export events logged to an append-only, tamper-evident SIEM?
* [ ] **No Sensitive Data in Logs**: Are passwords, credit card numbers, JWT tokens, and PII masked or excluded from application log streams?
* [ ] **Real-Time Alerting**: Are anomalies (e.g., 50 failed login attempts in 1 minute, token replay) routed to SOC / PagerDuty immediately?
