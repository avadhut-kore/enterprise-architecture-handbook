# Security, Segregation of Duties & SOX 404

## 1. Segregation of Duties (SoD) Dual Control
- A user authorized to create a vendor cannot approve payments to that vendor.
- A user authorized to create a purchase order cannot confirm goods receipt or approve the vendor invoice.
- Any attempt to bypass SoD triggers an automated security incident logged to the SIEM.

## 2. Zero-Trust Security & Identity Enforcement
- **Identity & Access Management (IAM)**: Fine-grained RBAC and ABAC policies mapped to OAuth 2.0 / OIDC claims with short-lived tokens (15-minute expiry).
- **Data Protection & Encryption**: Strict TLS 1.3 in transit with mandated PFS cipher suites; AES-256-GCM envelope encryption at rest.
- **Audit Logging**: Immutable WORM logging of all administrative access, data exports, and permission mutations.
