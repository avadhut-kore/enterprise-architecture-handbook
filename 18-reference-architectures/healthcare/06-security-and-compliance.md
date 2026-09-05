# Security, Privacy & HIPAA Compliance: Healthcare Platform

## 1. HIPAA Security Rule & BAA
- **Encryption at Rest & In Transit**: AES-256-GCM for all clinical databases and disk volumes; TLS 1.3 enforced on all API connections.
- **Business Associate Agreements (BAAs)**: Executed with cloud hyperscalers covering all infrastructure resources touching Protected Health Information (PHI).
- **Audit Logging**: Immutable WORM logging of every read, write, and export access to patient records, retaining logs for a minimum of 6 years.

## 2. Zero-Trust Security & Identity Enforcement
- **Identity & Access Management (IAM)**: Fine-grained RBAC and ABAC policies mapped to OAuth 2.0 / OIDC claims with short-lived tokens (15-minute expiry).
- **Data Protection & Encryption**: Strict TLS 1.3 in transit with mandated PFS cipher suites; AES-256-GCM envelope encryption at rest.
- **Audit Logging**: Immutable WORM logging of all administrative access, data exports, and permission mutations.
