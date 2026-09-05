# ADR-0065: Workload Identity Federation for Containerized and Cloud Workloads

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Static cloud IAM credentials leaked in GitHub or stored in container images represent the #1 vector for cloud account takeover and cryptomining attacks.

---

## Decision Outcome
**Chosen Option**: Adopt Workload Identity Federation (EKS Pod Identity / Azure Workload Identity / GCP Workload Identity); ban long-lived static cloud access keys in configuration.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Zero static credentials stored anywhere; automated 15-minute credential rotation; reduced blast radius of container compromise.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
