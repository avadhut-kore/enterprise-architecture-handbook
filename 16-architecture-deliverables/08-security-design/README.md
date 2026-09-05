# 08-SECURITY-DESIGN: Enterprise Security Architecture & Threat Modeling

## 1. Overview & Purpose
This directory provides production standards, master templates, and audit checklists for designing end-to-end security architecture, STRIDE threat models, identity perimeters, cryptographic controls, and compliance frameworks.

Security is not a downstream checkbox; it is a foundational architectural quality attribute. Every system must satisfy the Zero Trust principle: **Never Trust, Always Verify**.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Enterprise Security Design template.
* **Threat Modeling & Identity**:
  - [threat-model.md](threat-model.md) — STRIDE threat modeling methodology and risk rating.
  - [trust-boundaries.md](trust-boundaries.md) — Network segmentation and trust boundary mapping.
  - [identity.md](identity.md) — Enterprise identity federation, Okta/Azure AD integration.
  - [authentication.md](authentication.md) — Multi-Factor Authentication (MFA) and token standards.
  - [authorization.md](authorization.md) — Role-Based (RBAC) and Attribute-Based (ABAC) access control.
  - [oauth2.md](oauth2.md) — OAuth 2.0 grant types and client security.
  - [oidc.md](oidc.md) — OpenID Connect identity assertion validation.
* **Data, Network & Cryptography**:
  - [api-security.md](api-security.md) — OWASP API Security Top 10 mitigations.
  - [network-security.md](network-security.md) — Microsegmentation, WAF, and DDoS mitigation.
  - [encryption.md](encryption.md) — Cryptographic standards (AES-256-GCM, TLS 1.3).
  - [key-management.md](key-management.md) — AWS KMS / HashiCorp Vault key rotation lifecycles.
  - [secrets.md](secrets.md) — Dynamic secrets injection and rotation.
  - [data-protection.md](data-protection.md) — Data classification, tokenization, and DLP.
  - [privacy.md](privacy.md) — GDPR, CCPA, and right-to-be-forgotten erasure workflows.
* **Governance & Operations**:
  - [audit-logging.md](audit-logging.md) — Immutable security event logging (SIEM / Splunk).
  - [vulnerability-management.md](vulnerability-management.md) — SAST, DAST, and dependency scanning.
  - [supply-chain-security.md](supply-chain-security.md) — Software Bill of Materials (SBOM) and SLSA levels.
  - [ai-security.md](ai-security.md) — Prompt injection, model stealing, and data leakage guards.
  - [compliance.md](compliance.md) — SOC 2, ISO 27001, PCI-DSS, and HIPAA mapping.
  - [review-checklist.md](review-checklist.md) — 25-Point Security Architecture Review Checklist.
  - [examples/fintech-security-design.md](examples/fintech-security-design.md) — Complete Banking Enclave Security Design.
