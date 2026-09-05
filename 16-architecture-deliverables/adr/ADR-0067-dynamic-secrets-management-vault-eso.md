# ADR-0067: Dynamic Secrets Management via HashiCorp Vault and External Secrets Operator

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Static database connection strings shared across multiple instances create severe audit blind spots and credential rotation outages.

---

## Decision Outcome
**Chosen Option**: Deploy HashiCorp Vault with dynamic database credential generation, synchronized to Kubernetes workloads via the External Secrets Operator (ESO).

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Unique, ephemeral credentials per pod lease; automated revocation on lease expiry; GitOps manifests contain zero secret material.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
