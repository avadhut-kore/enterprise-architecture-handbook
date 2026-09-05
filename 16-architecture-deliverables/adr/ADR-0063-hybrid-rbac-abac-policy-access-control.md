# ADR-0063: Hybrid RBAC and ABAC Policy-Based Access Control via Open Policy Agent

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Pure RBAC leads to severe role explosion (thousands of ad-hoc roles), while pure ABAC is computationally expensive and difficult to audit.

---

## Decision Outcome
**Chosen Option**: Adopt a hybrid authorization model: coarse-grained Role-Based Access Control (RBAC) combined with Attribute-Based Access Control (ABAC) evaluated via Open Policy Agent (OPA) sidecars.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Decoupled authorization policy from application code; sub-millisecond local policy evaluation; clear auditability of Rego policy rules.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
