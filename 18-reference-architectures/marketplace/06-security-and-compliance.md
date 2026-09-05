# Security, Trust & Safety: Marketplace Platform

## 1. Review Fraud & Seller Verification
- **Anti-Collusion Review Detection**: Graph analytics detecting cyclical reviews between coordinated buyer and seller accounts.
- **DAC7 EU Compliance**: Automatically exports EU seller transaction volumes and tax identification numbers to European tax authorities.

## 2. Zero-Trust Security & Identity Enforcement
- **Identity & Access Management (IAM)**: Fine-grained RBAC and ABAC policies mapped to OAuth 2.0 / OIDC claims with short-lived tokens (15-minute expiry).
- **Data Protection & Encryption**: Strict TLS 1.3 in transit with mandated PFS cipher suites; AES-256-GCM envelope encryption at rest.
- **Audit Logging**: Immutable WORM logging of all administrative access, data exports, and permission mutations.
