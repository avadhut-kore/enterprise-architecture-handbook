# Enterprise Security Anti-Patterns (`security-anti-patterns/`)

## Executive Summary

Security anti-patterns are recurring design flaws that appear expedient during development but introduce catastrophic systemic vulnerabilities, breach liabilities, and operational paralysis in production.

---

## Index of 20 Lethal Security Anti-Patterns

| Anti-Pattern | Core Vulnerability | Primary Architectural Refactoring |
| :--- | :--- | :--- |
| [`security-as-an-afterthought.md`](security-as-an-afterthought.md) | Bolting security on before launch | Shift-left STRIDE threat modeling at Architecture Inception Gate |
| [`shared-production-credentials.md`](shared-production-credentials.md) | Single shared admin password | Individual SSO with Just-in-Time (JIT) role elevation |
| [`long-lived-static-access-keys.md`](long-lived-static-access-keys.md) | Hardcoded cloud IAM access keys | Workload Identity Federation (OIDC) with ephemeral 15-min tokens |
| [`secrets-in-version-control.md`](secrets-in-version-control.md) | Committing `.env` or API keys to Git | Pre-commit secret scanning (Gitleaks) + External Secrets Operator |
| [`over-permissioned-iam-wildcards.md`](over-permissioned-iam-wildcards.md) | `Action: "*"` and `Resource: "*"` | Scoped least-privilege IAM with SCP permission boundaries |
| [`publicly-accessible-databases.md`](publicly-accessible-databases.md) | Database with public IP address | Isolated private subnets, PrivateLink, zero public IPs |
| [`implicit-trust-of-internal-networks.md`](implicit-trust-of-internal-networks.md) | Flat internal corporate networks | Zero Trust architecture: mutual TLS (mTLS) and token verification |
| [`skipping-threat-modeling.md`](skipping-threat-modeling.md) | Relying solely on vulnerability scans | Mandatory STRIDE threat modeling on all HLD/LLD designs |
| [`purely-manual-security-gates.md`](purely-manual-security-gates.md) | Manual CAB / CISO spreadsheets | Automated DevSecOps CI/CD security gating (SAST/SCA/Trivy) |
| [`missing-audit-logs-on-critical-paths.md`](missing-audit-logs-on-critical-paths.md) | Zero forensic record of transactions | Tamper-proof WORM audit logging to S3 Object Lock |
| [`logging-sensitive-pii-passwords.md`](logging-sensitive-pii-passwords.md) | Plaintext credentials in log files | Automated log forwarder regex masking and scrubbing |
| [`inactive-or-ignored-key-rotation.md`](inactive-or-ignored-key-rotation.md) | 5-year-old KMS keys or TLS certs | Automated 365-day KMS rotation and ACME/Cert-Manager automation |
| [`unchecked-third-party-dependencies.md`](unchecked-third-party-dependencies.md) | Arbitrary npm/PyPI package pulls | Private enterprise package mirror (Artifactory) + SCA gating |
| [`blind-faith-in-vendor-zero-trust.md`](blind-faith-in-vendor-zero-trust.md) | Buying a single "Zero Trust" tool | Holistic Zero Trust architecture (Identity, Device, App, Data) |
| [`compliance-checkbox-architecture.md`](compliance-checkbox-architecture.md) | Passing audits without real security | Threat-model driven security controls exceeding compliance minimums |
| [`fragile-certificate-pinning.md`](fragile-certificate-pinning.md) | Hardcoded leaf certificate in mobile | Public Key Pinning (SPKI) with mandatory backup pins |
| [`ubiquitous-jwt-without-tradeoffs.md`](ubiquitous-jwt-without-tradeoffs.md) | JWTs used for revocable sessions | Opaque reference tokens in Redis for public browser sessions |
| [`hardcoded-secrets-in-docker-images.md`](hardcoded-secrets-in-docker-images.md) | Baked-in API keys in Docker layers | Multi-stage builds + runtime secret mounting via tmpfs |
| [`unrestricted-outbound-egress.md`](unrestricted-outbound-egress.md) | Open `0.0.0.0/0` outbound internet | Egress firewalls with TLS SNI domain allowlisting |
| [`single-account-multi-tenant-sprawl.md`](single-account-multi-tenant-sprawl.md) | Staging and Prod in one cloud account | Multi-account landing zone with strict blast radius isolation |
