# Security Architecture Review Checklist
- [ ] STRIDE threat model completed and signed off by Security Architect.
- [ ] Trust boundaries and network segmentation explicitly mapped.
- [ ] Authentication enforces MFA and OIDC with PKCE.
- [ ] Authorization enforces fine-grained RBAC/ABAC with zero privilege escalation.
- [ ] Cryptographic algorithms comply with modern enterprise standards (AES-256-GCM, TLS 1.3).
- [ ] Secrets injected dynamically from Vault/KMS; zero hardcoded credentials.
- [ ] Immutable audit logging configured for security monitoring.
