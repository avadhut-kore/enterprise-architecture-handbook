# 01-ADR: Architecture Decision Records

## 1. Overview & Purpose

An **Architecture Decision Record (ADR)** captures an important architectural decision made on a project along with its context, options evaluated, rationale, consequences, and trade-offs.

ADRs provide the organizational memory of a software system. They prevent recurring circular debates, onboard new engineers effectively, and explain the architectural constraints that shaped the codebase.

> [!NOTE]
> **Active Repository Ledger**: This repository maintains an active ledger of **112+ production ADRs** in [../adr/](../adr/README.md). This directory (`01-adr/`) provides the **governance standard, templates, review checklists, lifecycle rules, and decision case studies** for creating new ADRs.

---

## 2. ADR Governance & Standards

* **Immutable History**: Once an ADR is marked `Accepted`, it is never edited to change historical facts. If architectural direction shifts, author a new ADR that explicitly supersedes the prior one.
* **Decisions Over Descriptions**: An ADR must explain **WHY** a specific path was chosen over viable alternatives, detailing what was sacrificed.
* **Atomic Scope**: Each ADR should address exactly one decision (e.g., choice of message broker, database engine, or authentication mechanism).

---

## 3. Directory Contents

* **[template.md](template.md)**: Production-grade ADR template with 22 structured sections.
* **[adr-index-template.md](adr-index-template.md)**: Standard index ledger template for tracking ADR IDs, statuses, and tags.
* **[adr-review-checklist.md](adr-review-checklist.md)**: 15-Point quality checklist for peer and ARB review.
* **[adr-lifecycle.md](adr-lifecycle.md)**: State transition model (`Proposed` $ightarrow$ `Accepted` / `Rejected` $ightarrow$ `Superseded` / `Deprecated`).
* **[examples/](examples/)**: 7 Comprehensive real-world ADR examples:
  - [database-selection.md](examples/database-selection.md) — Distributed SQL vs Sharded Postgres.
  - [monolith-vs-microservices.md](examples/monolith-vs-microservices.md) — Modular Monolith vs Microservices decomposition.
  - [messaging-selection.md](examples/messaging-selection.md) — Apache Kafka vs RabbitMQ for order events.
  - [synchronous-vs-asynchronous.md](examples/synchronous-vs-asynchronous.md) — Async Event Choreography vs Sync REST orchestration.
  - [sql-vs-nosql.md](examples/sql-vs-nosql.md) — Relational Postgres vs MongoDB Document store.
  - [cloud-selection.md](examples/cloud-selection.md) — Multi-Cloud Abstraction vs Cloud-Native Services.
  - [ai-vs-non-ai.md](examples/ai-vs-non-ai.md) — Deterministic Rule Engine vs LLM Pipeline for compliance.
