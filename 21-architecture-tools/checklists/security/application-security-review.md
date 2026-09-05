# Checklist: Application Security Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Parameterized SQL queries enforced (zero string concatenation).
- [ ] Strict Content Security Policy (CSP) nonces active on frontend.
- [ ] BOLA/IDOR prevented via server-side tenant ID verification.
- [ ] SSRF mitigated via forward egress proxy blocking RFC 1918 ranges.
- [ ] Banned native serialization formats (no Java pickle).
