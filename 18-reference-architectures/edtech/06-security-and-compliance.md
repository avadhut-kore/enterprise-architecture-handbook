# Security, Privacy & Compliance: EdTech Platform

## 1. Student Privacy Regulations (FERPA & COPPA)
- **COPPA Compliance**: Strict parental consent verification for students under 13; zero behavioral ad tracking or third-party marketing cookies.
- **FERPA Compliance**: Student educational records are strictly compartmentalized; directory information is masked from unauthorized users.
- **Digital Rights Management (DRM)**: Video streams are encrypted using Apple FairPlay, Google Widevine, and Microsoft PlayReady.

## 2. Zero-Trust Security & Identity Enforcement
- **Identity & Access Management (IAM)**: Fine-grained RBAC and ABAC policies mapped to OAuth 2.0 / OIDC claims with short-lived tokens (15-minute expiry).
- **Data Protection & Encryption**: Strict TLS 1.3 in transit with mandated PFS cipher suites; AES-256-GCM envelope encryption at rest.
- **Audit Logging**: Immutable WORM logging of all administrative access, data exports, and permission mutations.
