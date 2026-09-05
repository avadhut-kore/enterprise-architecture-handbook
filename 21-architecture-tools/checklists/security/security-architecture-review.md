# Checklist: Security Architecture Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Comprehensive STRIDE threat model approved by ARB.
- [ ] Zero standing administrative access; JIT elevation required.
- [ ] All inter-service communications encrypted via mTLS.
- [ ] Multi-AZ blast radius isolation enforced.
- [ ] Immutable audit logging active to WORM storage.
