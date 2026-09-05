# 15-NFR: Measurable Non-Functional Requirements Framework

## 1. Overview & Purpose
Non-Functional Requirements (NFRs) define **HOW WELL** a system performs its functions. Vague NFRs (*"the system should be fast and resilient"*) are the leading cause of architecture failure.

This directory establishes a **quantifiable, contract-grade NFR framework across 12 engineering dimensions**.

```text
Non-Functional Requirements (NFR)
├── User Experience & Latency
├── Performance & Throughput
├── Scalability & Headroom
├── Availability & Uptime
├── Reliability & Fault Tolerance
├── Security & Cryptography
├── Privacy & Data Residency
├── Maintainability & Code Quality
├── Observability & Telemetry
├── Disaster Recovery (RTO/RPO)
├── Compliance & Audit
└── Total Cost of Ownership (FinOps)
```

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Non-Functional Requirements Specification template.
* **12 Measurable Dimensions**:
  - [availability.md](availability.md) — Uptime SLAs, maintenance windows, and nine-scale formulas.
  - [reliability.md](reliability.md) — MTBF, MTTR, error budgets, and chaos testing limits.
  - [scalability.md](scalability.md) — Peak headroom, burst multipliers, and scale ceilings.
  - [performance.md](performance.md) — Latency percentiles (p50, p95, p99) under defined load.
  - [security.md](security.md) — Cryptographic standards, vulnerability SLAs, and authentication.
  - [privacy.md](privacy.md) — GDPR data subject access requests, encryption, and deletion SLAs.
  - [maintainability.md](maintainability.md) — Test coverage, cyclomatic complexity, and documentation.
  - [observability.md](observability.md) — Golden signals, trace sampling, and retention windows.
  - [disaster-recovery.md](disaster-recovery.md) — Mathematical RTO and RPO targets.
  - [compliance.md](compliance.md) — Regulatory auditability and certification baselines.
  - [cost.md](cost.md) — FinOps cost per transaction and infrastructure budget caps.
  - [testability.md](testability.md) — Mockability, contract testing, and synthetic load testing.
* **Governance**:
  - [checklist.md](checklist.md) — 20-Point NFR Audit Checklist.
