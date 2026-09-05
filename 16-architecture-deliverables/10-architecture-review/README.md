# 10-ARCHITECTURE-REVIEW: Architecture Review Board (ARB) Governance

## 1. Overview & Purpose
This directory provides the operational charter, intake templates, agendas, checklists, and decision records for conducting formal **Architecture Review Board (ARB)** evaluations.

The ARB provides architectural governance across the enterprise. It ensures alignment with corporate technology strategy, enforces security and compliance guardrails, mitigates cross-system risks, and prevents uncoordinated technical debt accumulation.

> [!NOTE]
> **Existing Reviews Ledger**: This repository maintains an established archive of review guides in [../architecture-review/](../architecture-review/README.md). This directory (`10-architecture-review/`) provides the **standardized intake packets, decision record schemas, and domain review rubrics**.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master ARB Review Intake & Evaluation Packet.
* **[architecture-review-agenda.md](architecture-review-agenda.md)**: Standard 60-minute ARB session agenda.
* **[architecture-review-checklist.md](architecture-review-checklist.md)**: Comprehensive ARB evaluation checklist.
* **Specialized Review Rubrics**:
  - [decision-review.md](decision-review.md) — Evaluating critical ADRs and architectural trade-offs.
  - [security-review.md](security-review.md) — Reviewing threat models and cryptographic controls.
  - [performance-review.md](performance-review.md) — Latency, throughput, and benchmarking reviews.
  - [scalability-review.md](scalability-review.md) — Horizontal scaling limits and capacity headroom.
  - [reliability-review.md](reliability-review.md) — SPOF elimination, failover, and fault tolerance.
  - [cloud-review.md](cloud-review.md) — Cloud architecture, landing zones, and FinOps TCO.
  - [data-review.md](data-review.md) — Data models, consistency, and compliance reviews.
  - [integration-review.md](integration-review.md) — System boundaries and event schema compatibility.
  - [ai-review.md](ai-review.md) — LLM architectures, safety, and operational costs.
  - [production-readiness-review.md](production-readiness-review.md) — Operational handoff to SRE.
* **Governance**:
  - [examples/sample-arb-review-packet.md](examples/sample-arb-review-packet.md) — Completed ARB review packet and decision record.
