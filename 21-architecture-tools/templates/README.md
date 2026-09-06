# Architecture Document & Runbook Templates

## 1. Overview
The `templates/` directory provides standardized, production-tested templates for architecture reviews, security threat models, and operational runbooks.

---

## 2. Template Catalog & Ownership Mapping

| Template | File | Purpose | Canonical Parent Link |
|---|---|---|---|
| **STRIDE Threat Model** | [`threat-model-stride-template.md`](threat-model-stride-template.md) | Structured DFD trust boundary & STRIDE threat mitigation matrix | [10-security/](../../10-security/) |
| **Disaster Recovery Runbook** | [`disaster-recovery-runbook-template.md`](disaster-recovery-runbook-template.md) | Step-by-step operational failover, database promotion, and failback guide | [02-system-design/disaster-recovery/](../../02-system-design/disaster-recovery/README.md) |
| **Architecture Decision Record** | [`../generators/adr_generator.py`](../generators/README.md) | Automated CLI generator for standardized ADRs | [16-architecture-deliverables/ADR-TEMPLATE.md](../../16-architecture-deliverables/ADR-TEMPLATE.md) |
| **Non-Functional Requirements** | [`../generators/nfr_matrix_generator.py`](../generators/README.md) | Automated CLI generator for measurable NFR matrices | [16-architecture-deliverables/SYSTEM-DESIGN-TEMPLATE.md](../../16-architecture-deliverables/SYSTEM-DESIGN-TEMPLATE.md) |

---

## 3. Related Modules
* [16-architecture-deliverables/](../../16-architecture-deliverables/) — Canonical enterprise templates: HLD, LLD, SAD, and Risk Registers.
* [21-architecture-tools/generators/](../generators/README.md) — CLI generators for automated scaffolding.
