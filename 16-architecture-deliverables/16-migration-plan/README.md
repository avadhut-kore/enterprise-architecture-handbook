# 16-MIGRATION-PLAN: System, Database & Cloud Migration Architecture

## 1. Overview & Purpose
A **Migration Plan** defines the step-by-step strategy for transitioning applications, databases, integrations, and infrastructure from a current state to a target state with minimal downtime and zero data loss.

Every migration plan must define:
* Current State vs Target State architectures.
* Intermediate Transition Architectures (coexistence states).
* Phased rollout waves and dependency graphs.
* Data migration, CDC synchronization, and dual-writing.
* Automated and manual cutover runbooks.
* Instant rollback triggers and procedures.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Enterprise Migration Plan template.
* **Core Migration Artifacts**:
  - [current-state.md](current-state.md) — As-Is architecture baseline and inventory.
  - [target-state.md](target-state.md) — To-Be architecture target.
  - [transition-state.md](transition-state.md) — Intermediate coexistence architectures.
  - [migration-strategy.md](migration-strategy.md) — Big Bang vs Phased vs Parallel Run.
  - [data-migration.md](data-migration.md) — Dual-writing, CDC, and reconciliation.
  - [application-migration.md](application-migration.md) — Workload shifting and traffic routing.
  - [integration-migration.md](integration-migration.md) — Legacy facade and API proxy routing.
  - [rollout.md](rollout.md) — Hour-by-hour cutover schedule and war room operations.
  - [rollback.md](rollback.md) — Rollback triggers, decision thresholds, and back-out runbooks.
  - [validation.md](validation.md) — Smoke tests, data parity checks, and acceptance criteria.
  - [risks.md](risks.md) — Migration risk register and contingencies.
  - [checklist.md](checklist.md) — 20-Point Migration Readiness Checklist.
