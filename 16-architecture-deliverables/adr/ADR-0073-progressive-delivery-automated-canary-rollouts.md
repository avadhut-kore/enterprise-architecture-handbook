# ADR-0073: Progressive Delivery with Automated Canary Analysis via Argo Rollouts

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Big-bang deployments expose 100% of customer traffic to new release bugs, causing catastrophic downtime and manual rollback chaos.

---

## Decision Outcome
**Chosen Option**: Mandate progressive canary deployments (5% -> 25% -> 100%) with automated metric analysis and instant rollback for all production services.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Blast radius of flawed releases limited to < 5% of traffic; automated rollback in < 30 seconds; eliminates human error during deployment triage.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
