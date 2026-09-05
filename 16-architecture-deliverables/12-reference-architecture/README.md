# 12-REFERENCE-ARCHITECTURE: Enterprise Reference Architecture Framework

## 1. Overview & Purpose
A **Reference Architecture** provides a standardized, reusable architectural blueprint for solving a broad class of problems across an organization.

> [!IMPORTANT]
> **Reference Architecture $
e$ One Mandatory Implementation.**
> A reference architecture defines:
> * Recommended baselines and proven design patterns.
> * Mandatory architectural guardrails and compliance constraints.
> * Allowed variation points and modular extension points.
> * Clear decision criteria for when projects may deviate.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Reference Architecture template (18 structural sections).
* **Core Reference Models**:
  - [principles.md](principles.md) — Guiding architectural principles and trade-off rules.
  - [scope.md](scope.md) — Problem domain boundaries and applicability criteria.
  - [reference-model.md](reference-model.md) — Conceptual layered architecture model.
  - [logical-architecture.md](logical-architecture.md) — Standard subsystem topology.
  - [deployment-model.md](deployment-model.md) — Cloud landing zone, multi-AZ, and VPC blueprints.
  - [security-model.md](security-model.md) — Enterprise Zero Trust, IAM, and KMS standards.
  - [data-model.md](data-model.md) — Data lakehouse, operational databases, and schema standards.
  - [integration-model.md](integration-model.md) — API Gateway, Event Mesh, and messaging baselines.
  - [operational-model.md](operational-model.md) — SRE observability, telemetry, and automated delivery.
* **Technology & Evolution**:
  - [technology-options.md](technology-options.md) — Approved, tolerated, and prohibited technology radars.
  - [adoption-guidance.md](adoption-guidance.md) — Step-by-step project adoption roadmap.
  - [evolution.md](evolution.md) — Governance rules for updating the reference architecture.
  - [governance.md](governance.md) — Exception handling and ARB waiver processes.
  - [review-checklist.md](review-checklist.md) — 20-Point Reference Architecture Quality Checklist.
  - [examples/event-driven-microservices-refarch.md](examples/event-driven-microservices-refarch.md) — Enterprise Event-Driven Microservices Reference Architecture.
