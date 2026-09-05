# 17-MODERNIZATION-PLAN: Legacy System Modernization Framework

## 1. Overview & Purpose
A **Modernization Plan** defines the multi-year architecture roadmap for decomposing, re-architecting, or replacing legacy monolithic systems and technical debt.

> [!IMPORTANT]
> **Modernization Does NOT Automatically Mean Microservices.**
> True enterprise modernization assesses each legacy component against the industry-standard **7R Framework**:
> 1. **Retain**: Keep as-is (low business value, low maintenance cost).
> 2. **Retire**: Decommission completely (redundant capability).
> 3. **Rehost**: Lift-and-shift to cloud VM with zero code changes.
> 4. **Replatform**: Move to managed platform (e.g., self-hosted DB $ightarrow$ RDS).
> 5. **Refactor**: Optimize internal code without changing external architecture.
> 6. **Rearchitect**: Decompose into modular monolith or microservices (Strangler Fig).
> 7. **Rebuild**: Rewrite greenfield from scratch.
> *(Optional 8th R: **Replace** with commercial SaaS).*

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Legacy Modernization Plan template.
* **Assessment & Options**:
  - [current-state.md](current-state.md) — Legacy codebase assessment and technical debt audit.
  - [assessment.md](assessment.md) — Business value vs Technical health portfolio mapping.
  - [modernization-drivers.md](modernization-drivers.md) — Business velocity, licensing, and talent constraints.
  - [options.md](options.md) — The 7R Modernization Decision Matrix.
  - [target-state.md](target-state.md) — Target domain-driven modern architecture.
* **Modernization Patterns**:
  - [strangler-pattern.md](strangler-pattern.md) — Strangler Fig interception and incremental decomposition.
  - [replatform.md](replatform.md) — Containerization and cloud migration guidelines.
  - [refactor.md](refactor.md) — Clean code, modular encapsulation, and tech debt reduction.
  - [rearchitect.md](rearchitect.md) — Event-driven and microservices decomposition.
  - [rebuild.md](rebuild.md) — Greenfield rewrite governance.
  - [retire.md](retire.md) — Legacy system decommissioning and data legal hold.
* **Roadmap & Governance**:
  - [migration-roadmap.md](migration-roadmap.md) — Multi-wave modernization schedule.
  - [risk.md](risk.md) — Organizational and operational modernization risks.
  - [checklist.md](checklist.md) — 20-Point Modernization Plan Review Checklist.
