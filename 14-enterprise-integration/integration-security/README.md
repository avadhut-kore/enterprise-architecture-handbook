# Enterprise Integration Security

## 1. Overview
Enterprise integration security operates under the **Zero Trust Principle: Never Trust, Always Verify**. Integrations frequently traverse high-risk perimeters: public clouds, partner B2B connections, on-premises data centers, and third-party SaaS applications.

---

## 2. Directory Contents
* **[trust-boundaries.md](trust-boundaries.md)** — Network perimeters, DMZ, VPC peering, and data classification boundaries.
* **[identity.md](identity.md)** — Machine-to-machine (M2M) identity, service principals, and SPIFFE/SPIRE.
* **[authentication.md](authentication.md)** — mTLS, API keys, and client credential exchanges.
* **[authorization.md](authorization.md)** — Fine-grained scopes, ABAC claim verification, and tenant isolation.
* **[oauth2.md](oauth2.md)** — OAuth 2.0 Client Credentials Grant, JWT assertions, and token caching.
* **[oidc.md](oidc.md)** — OpenID Connect token validation via JSON Web Key Sets (JWKS).
* **[mTLS.md](mTLS.md)** — Mutual TLS 1.3 architecture, handshake mechanics, and cipher suites.
* **[certificates.md](certificates.md)** — Automated X.509 PKI certificate rotation (Let's Encrypt / Vault / ACM).
* **[encryption.md](encryption.md)** — End-to-end payload encryption (JWE / PGP) vs transport encryption.
* **[secrets.md](secrets.md)** — Dynamic secret generation, rotation, and elimination of static tokens.
* **[tokenization.md](tokenization.md)** — Credit card (PCI) and SSN tokenization at ingress boundaries.
* **[data-minimization.md](data-minimization.md)** — Payload trimming to prevent unnecessary data exposure.
* **[pii.md](pii.md)** — GDPR/CCPA privacy redaction and masking in transit.
* **[financial-data.md](financial-data.md)** — Banking and payment transaction payload confidentiality.
* **[healthcare-data.md](healthcare-data.md)** — HIPAA Business Associate Agreement (BAA) and PHI security.
* **[audit.md](audit.md)** — Tamper-evident SIEM security event logging.
* **[checklist.md](checklist.md)** — 20-Point Integration Security Review Checklist.
