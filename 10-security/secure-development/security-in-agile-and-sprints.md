# Security in Agile & Sprint Cadences

## Executive Summary

Treating security as a standalone project creates friction. Security requirements must be decomposed into **Security User Stories** and enforced via the **Definition of Done (DoD)**.

---

## 1. Security in the Definition of Done (DoD)
A story cannot be marked "Done" unless:
- [ ] No secrets or credentials are hardcoded.
- [ ] Automated SAST scanner (Semgrep) reports 0 new security alerts.
- [ ] Any new third-party dependency passes SCA with 0 Critical/High CVEs.
- [ ] Database queries use parameterized statements.
- [ ] Authorization checks are covered by unit tests.
