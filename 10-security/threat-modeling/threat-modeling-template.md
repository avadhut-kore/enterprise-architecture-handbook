# Reusable Enterprise Threat Model Specification Template

```markdown
# Threat Model: [System Name]

## 1. System Context & Criticality
- **System Owner**: [Team Name / Lead Architect]
- **Business Criticality**: [Tier 1 Mission-Critical / Tier 2 / Tier 3]
- **Data Classification**: [Public / Internal / Confidential / Restricted PII]
- **Regulatory Scope**: [GDPR / PCI-DSS / HIPAA / SOC 2 / None]

---

## 2. Architecture & Trust Boundaries
[Insert Level 1 Data Flow Diagram highlighting Trust Boundaries]

---

## 3. Threat Identification & Mitigation Matrix (STRIDE)

| Threat ID | Element | STRIDE Category | Threat Description | Architectural Mitigation | Status | Jira Epic |
|:---|:---|:---:|:---|:---|:---:|:---|
| **TH-01** | Login API | Spoofing | Replay of stolen user bearer token | Enforce 15-min token TTL and DPoP / mTLS sender-constrained tokens | Mitigated | SEC-101 |
| **TH-02** | Wire Transfer | Tampering | Modification of recipient IBAN in flight | Enforce TLS 1.3 + HMAC message payload signature | Mitigated | SEC-102 |
| **TH-03** | Audit Log | Repudiation | SRE modifies audit logs to hide changes | Ship logs via Kinesis Firehose directly to S3 WORM Object Lock | Mitigated | SEC-103 |
| **TH-04** | Order DB | Info Disclosure | Unencrypted database backups stolen | Enforce KMS CMK envelope encryption + deny cross-account restore | Mitigated | SEC-104 |
| **TH-05** | Search API | DoS | High-cardinality regex search saturating CPU | Enforce Redis query caching + WAF rate-limiting rules (100 req/min) | Mitigated | SEC-105 |
| **TH-06** | Admin API | Elevation | Regular user guesses tenant admin endpoint | Enforce Open Policy Agent (OPA) fine-grained authorization | Mitigated | SEC-106 |

---

## 4. Residual Risk Assessment
- **Identified Residual Risks**: [Document any known risks remaining post-mitigation]
- **Business Risk Acceptance**: [Sign-off from CISO / Business Owner if residual risk > Medium]
```
