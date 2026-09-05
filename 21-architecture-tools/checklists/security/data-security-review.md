# Checklist: Data Security Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Enterprise data classified into Tier 1 to 4 categories.
- [ ] AES-256 envelope encryption enforced with KMS CMKs.
- [ ] Sensitive cardholder/PII fields tokenized at ingress.
- [ ] Automated TTL data retention and cryptographic shredding active.
- [ ] Database row-level security isolates multi-tenant records.
