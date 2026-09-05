# 11-RISK-REGISTER: Architecture Risk Register & Scoring Rubric

## 1. Overview & Purpose
This directory provides production templates, risk categorization taxonomies, quantitative scoring rubrics, and mitigation tracking tools for managing **Architecture and Technical Risks**.

An architecture risk register tracks technical uncertainty, design vulnerabilities, legacy technical debt, external vendor liabilities, and regulatory exposures. It ensures that risks are transparently acknowledged, quantified, owned, and mitigated rather than hidden.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Architecture Risk Register template with full schema.
* **Risk Categorization Guides**:
  - [architecture-risk.md](architecture-risk.md) — System coupling, monolith bottlenecks, and architectural drift.
  - [technical-risk.md](technical-risk.md) — Concurrency bugs, unproven technologies, and code debt.
  - [security-risk.md](security-risk.md) — Zero-day vulnerabilities, credential compromise, and compliance breaches.
  - [data-risk.md](data-risk.md) — Data corruption, split-brain partitions, and GDPR privacy violations.
  - [operational-risk.md](operational-risk.md) — SRE capacity, single point of failure (SPOF), and deployment failures.
  - [vendor-risk.md](vendor-risk.md) — Cloud price increases, vendor lock-in, and SaaS outages.
  - [migration-risk.md](migration-risk.md) — Cutover downtime, data loss during ETL, and rollback failure.
  - [AI-risk.md](AI-risk.md) — LLM hallucination, training data IP contamination, and prompt injection.
* **Scoring & Governance**:
  - [risk-scoring.md](risk-scoring.md) — $5 	imes 5$ Likelihood vs Impact scoring matrix.
  - [mitigation-plan.md](mitigation-plan.md) — Risk treatment plans (Mitigate, Transfer, Accept, Avoid).
  - [review-checklist.md](review-checklist.md) — 15-Point Risk Review Checklist.
  - [examples/enterprise-platform-risk-register.md](examples/enterprise-platform-risk-register.md) — Real-world Enterprise Risk Register.
