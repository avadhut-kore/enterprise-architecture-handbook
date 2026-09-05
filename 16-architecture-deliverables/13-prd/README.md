# 13-PRD: Product Requirements Document Hand-off to Architecture

## 1. Overview & Purpose
The **Product Requirements Document (PRD)** establishes the business vision, user personas, user stories, success metrics, and functional boundaries defined by Product Management.

> [!IMPORTANT]
> **The PRD is Product-Oriented, NOT an Architecture Document.**
> The PRD specifies **WHAT** problem must be solved and for **WHOM**. Architecture deliverables (SAD, HLD, LLD) specify **HOW** the system solves it.

```text
Product Vision & Market Problem
              ↓
  [13-prd/ (PRD)]
              ↓
  [14-requirements/ & 15-nfr/]
              ↓
  [02-sad/ & 03-hld/ (Architecture Design)]
```

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Product Requirements Document template.
* **Core Product Artifacts**:
  - [product-vision.md](product-vision.md) — Strategic positioning and value proposition.
  - [problem-statement.md](problem-statement.md) — Quantitative friction and customer pain points.
  - [personas.md](personas.md) — Target user archetypes, roles, and workflows.
  - [user-stories.md](user-stories.md) — Epics, user stories, and Gherkin scenarios.
  - [functional-requirements.md](functional-requirements.md) — System capabilities and business logic rules.
  - [non-functional-requirements.md](non-functional-requirements.md) — Product-level expectations (speed, uptime).
  - [success-metrics.md](success-metrics.md) — North Star KPIs and OKR targets.
  - [scope.md](scope.md) — MVP vs Phase 2 vs Phase 3 scope delineation.
  - [assumptions.md](assumptions.md) — Market and organizational assumptions.
  - [dependencies.md](dependencies.md) — Upstream business initiatives and partner readiness.
  - [risks.md](risks.md) — Product adoption, regulatory, and commercial risks.
  - [checklist.md](checklist.md) — 15-Point PRD-to-Architecture Hand-off Checklist.
