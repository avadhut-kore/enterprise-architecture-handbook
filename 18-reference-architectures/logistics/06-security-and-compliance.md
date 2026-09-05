# Security & Regulatory Compliance: Logistics Platform

## 1. Regulatory Frameworks
- **DOT Hours of Service (HOS)**: Electronic Logging Device (ELD) compliance tracking driver driving hours, on-duty hours, and mandatory rest periods.
- **FDA Food Safety Modernization Act (FSMA)**: Refrigerated shipments (cold-chain) record continuous temperature logs. If temperature exceeds $4^\circ	ext{C}$ for $> 15\text{ minutes}$, an automated alert quarantines the load.

## 2. Zero-Trust Security & Identity Enforcement
- **Identity & Access Management (IAM)**: Fine-grained RBAC and ABAC policies mapped to OAuth 2.0 / OIDC claims with short-lived tokens (15-minute expiry).
- **Data Protection & Encryption**: Strict TLS 1.3 in transit with mandated PFS cipher suites; AES-256-GCM envelope encryption at rest.
- **Audit Logging**: Immutable WORM logging of all administrative access, data exports, and permission mutations.
