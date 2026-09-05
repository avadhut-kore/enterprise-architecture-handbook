# Security & PCI-DSS Level 1: Fintech Platform

## 1. Cryptographic Key Hierarchy & Hardware Security
- Master Keys are generated and stored exclusively within FIPS 140-2 Level 3 validated CloudHSM clusters.
- PIN blocks are translated from Zone Encryption Keys (ZEK) to Local Storage Keys (LSK) inside the HSM without ever appearing in plaintext memory.

## 2. Zero-Trust Security & Identity Enforcement
- **Identity & Access Management (IAM)**: Fine-grained RBAC and ABAC policies mapped to OAuth 2.0 / OIDC claims with short-lived tokens (15-minute expiry).
- **Data Protection & Encryption**: Strict TLS 1.3 in transit with mandated PFS cipher suites; AES-256-GCM envelope encryption at rest.
- **Audit Logging**: Immutable WORM logging of all administrative access, data exports, and permission mutations.
