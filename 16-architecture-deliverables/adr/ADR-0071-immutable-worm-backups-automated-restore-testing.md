# ADR-0071: Immutable WORM Backups and Automated Continuous Restore Testing

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Ransomware actively targets and encrypts standard cloud backups; untested backups frequently fail during real disaster recovery scenarios.

---

## Decision Outcome
**Chosen Option**: Enforce AWS S3 Object Lock in Compliance Mode (WORM) for all backups, paired with automated monthly CI/CD restore drills to ephemeral staging environments.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Mathematical immunity to ransomware deletion; verified recovery capability with measured RTO/RPO; storage cost increases managed by lifecycle tiering.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
