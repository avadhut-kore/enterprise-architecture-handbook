# ADR-0072: Blameless Post-Incident Review (PIR) and Problem Management Standard

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Blame-oriented incident processes encourage cover-ups, fail to address underlying systemic flaws, and guarantee incident recurrence.

---

## Decision Outcome
**Chosen Option**: Mandate blameless post-incident reviews for all SEV-1 and SEV-2 incidents; track corrective systemic action items in Jira with senior engineering sponsorship.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- High-trust engineering culture; accelerated root cause discovery; continuous systemic hardening against complex distributed failures.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
