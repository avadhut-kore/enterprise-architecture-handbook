# ADR-0070: Standardization on Error Budgets and Multi-Window Multi-Burn-Rate Alerting

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Simple threshold alerts create extreme on-call alarm fatigue during transient spikes and fail to catch slow, catastrophic error budget drains.

---

## Decision Outcome
**Chosen Option**: Adopt Google SRE Error Budget policies with multi-window multi-burn-rate alerting in Prometheus/PagerDuty; ban raw CPU-only threshold paging alerts.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Zero false-positive wake-up pages; mathematically rigorous alerting on genuine user pain; feature releases automatically paused if error budget is exhausted.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
