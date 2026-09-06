# Competency Deep Dive: Security Architecture & Zero Trust

> **"Security is not a checklist added at the end of a project; it is an architectural property built from first principles. If an architecture is not secure by design, it is fundamentally broken."**

---

## 1. Definition & Core Essence

**Security Architecture & Zero Trust** is the discipline of protecting an enterprise's digital assets, data, and users from compromise, unauthorized access, and cyber threats. It encompasses:
* Zero Trust Principles: "Never trust, always verify" across Identity, Devices, Networks, Applications, and Data.
* Identity & Access Management (IAM): OAuth2, OpenID Connect (OIDC), SAML 2.0, RBAC, ABAC, and Identity Governance & Administration (IGA).
* Threat modeling & vulnerability assessment: STRIDE, DREAD, attack trees, and trust boundary isolation.
* Cryptographic foundations: Asymmetric vs Symmetric encryption, mTLS, PKI, Key Management Services (KMS/HSM), and encryption in transit/rest.
* Application & platform security: OWASP Top 10 mitigation, container image signing, supply chain security (SBOM), and secrets management (HashiCorp Vault).

---

## 2. Why It Matters for Modern Architects

* **Solution Architects**: Prevents catastrophic data breaches, credential leaks, and unauthorized API privilege escalation.
* **Technical Architects**: Establishes enterprise security perimeters, service mesh mTLS policies, and secrets rotation pipelines.
* **Enterprise Architects**: Ensures adherence to global compliance standards (PCI-DSS, HIPAA, SOC 2, ISO 27001, GDPR) and advises the CISO on cyber resilience.

---

## 3. 5-Tier Behavioral Capability Progression

| Level | Behavioral Capability Anchor |
| :--- | :--- |
| **L1 (Practitioner)** | Protects against basic OWASP Top 10 vulnerabilities (SQL injection, XSS); hashes passwords with bcrypt/argon2. |
| **L2 (Independent)** | Implements OAuth2/OIDC JWT token validation; configures IAM roles with least privilege; stores secrets in environment variables or cloud secret managers. |
| **L3 (Advanced)** | Conducts STRIDE threat modeling workshops; designs service-to-service mTLS; integrates HashiCorp Vault for dynamic secrets and automated rotation. |
| **L4 (Architect)** | Architects Zero Trust enterprise perimeters; enforces service mesh authorization policies (Istio AuthorizationPolicy); implements mobile Secure Enclave / Android KeyStore hardware cryptographic storage. |
| **L5 (Strategic)** | Advises the CISO and Board on nation-state threat models, corporate cyber resilience, post-quantum cryptographic transitions, and global privacy compliance. |

---

## 4. Practical Experiences & Apprenticeship Exercises

1. **Perform a STRIDE Threat Model**: Conduct a comprehensive threat model for a new customer-facing payment gateway using [`21-architecture-tools/templates/threat-model-stride-template.md`](../../21-architecture-tools/templates/threat-model-stride-template.md). Document mitigations for Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.
2. **Implement mTLS Across Polyglot Services**: Configure mutual TLS (mTLS) with automatic certificate rotation between a Java service and a Go service within a Kubernetes cluster.
3. **Audit Token Revocation Windows**: Analyze the security trade-offs between short-lived stateless JWT access tokens with refresh tokens versus centralized token revocation lists under high QPS.

---

## 5. Objective Evidence of Capability (What to Inspect in Git)

- [ ] Complete STRIDE Threat Model document identifying trust boundaries and explicit security controls.
- [ ] Documented Security Architecture Specification covering data classification, encryption key rotation, and IAM RBAC/ABAC matrices.
- [ ] Automated security scanning gates (SAST, DAST, Container Scanning, SBOM) integrated into CI/CD pipelines.

---

## 6. Common Cognitive Gaps & Blind Spots

* **Perimeter-Only Security (The Castle-and-Moat Fallacy)**: Assuming that once an attacker breaches the perimeter firewall or VPN, all internal microservice APIs can communicate without authentication or encryption.
* **Hardcoded Credentials & Long-Lived Tokens**: Embedding secrets or static AWS API keys in code repositories instead of utilizing dynamic, temporary IAM role assumption.
* **Client-Side Security Trust**: Trusting parameters, pricing, or authorization claims passed from a mobile app or web frontend without re-validating them authoritatively on the backend.

---

## 7. Authoritative Repository Links

* Security Architecture Core: [`10-security/`](../../10-security/README.md)
* Security Foundations: [`00-foundations/security/`](../../00-foundations/security/README.md)
* Mobile Security (Secure Enclave): [`05-mobile/mobile-security/`](../../05-mobile/mobile-security/README.md)
* STRIDE Threat Model Template: [`21-architecture-tools/templates/threat-model-stride-template.md`](../../21-architecture-tools/templates/threat-model-stride-template.md)

---

## 8. Diagnostic Assessment Questions

1. *What are the core architectural differences between Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC), and when is ABAC required?*
2. *How do you securely handle token revocation in a distributed architecture using stateless JWT access tokens?*
3. *What is the difference between encryption in transit, encryption at rest, and encryption in use (Confidential Computing)?*
