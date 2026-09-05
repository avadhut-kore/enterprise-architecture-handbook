# Security Exceptions & Risk Acceptance Framework

## Executive Summary

Security exceptions occur when technical constraints, legacy dependencies, or urgent business requirements prevent compliance with established standards. A rigorous exception framework prevents exceptions from becoming permanent vulnerabilities.

---

## 1. Non-Negotiable Exception Governance Rules

1. **Mandatory Expiration**: All security exceptions expire automatically in **90 days**. Zero permanent exceptions permitted.
2. **Executive Ownership**: Exceptions for Tier-1 mission-critical systems require written sign-off from the Business Unit Vice President and the CISO.
3. **Mandatory Compensating Controls**: An exception cannot be approved without active compensating controls (e.g., if TLS 1.0 must remain enabled for a legacy client, the endpoint must be isolated to a dedicated WAF rule with IP whitelisting).
4. **Enterprise Risk Register Entry**: Every active exception is tracked in the central risk register and presented quarterly to the Board Audit Committee.
