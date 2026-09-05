# ADR-0068: Automated DevSecOps Security Gates in CI/CD Pipelines

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Manual security review boards create deployment bottlenecks and fail to detect known CVEs before production release.

---

## Decision Outcome
**Chosen Option**: Enforce non-bypassable CI/CD security gates: pre-commit secret scanning (Gitleaks), SAST (Semgrep), SCA (Snyk), container scanning (Trivy), and IaC linting (Checkov).

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Vulnerabilities caught before code is merged; eliminated late-stage security rework; requires strict false-positive tuning to maintain developer velocity.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
