# Role Readiness Gate: Solution Architect (SA)

> **"Readiness for Solution Architect is proven by end-to-end business problem decomposition, rigorous NFR engineering, defensible trade-off justification (ADRs), and successful defense at the Architecture Review Board."**

---

## 1. Readiness Threshold Matrix

| Pillar | Required Standard | Verification Method |
| :--- | :--- | :--- |
| **1. Knowledge** | Level 4 (Architect) in System Design, Data, Integration, and Security; Level 3 in Business Acumen. | Review against [Competency Matrix](../skill-matrix/architect-competency-matrix.md). |
| **2. Experience** | Designed and delivered an end-to-end multi-system solution spanning 3+ distinct platforms; successfully passed formal ARB review. | ARB meeting records and production release metrics. |
| **3. Decisions** | Authored 5+ peer-reviewed ADRs; modeled 3-year Total Cost of Ownership (TCO) comparing 3 distinct options. | Inspect Git ADR directory and FinOps projections. |
| **4. Evidence** | 1 approved Solution Architecture Document (SAD); 1 complete NFR Matrix; 1 STRIDE Threat Model; 1 Disaster Recovery Runbook. | Complete architecture deliverables package in Git. |

---

## 2. Core Readiness Checklist

### Business Problem Framing & NFR Engineering
- [ ] Interrogates business stakeholders to uncover core drivers, success metrics, and constraints before proposing architecture.
- [ ] Generates measurable engineering budgets using `python 21-architecture-tools/generators/nfr_matrix_generator.py` (p99 latency, throughput, RPO/RTO).
- [ ] Evaluates Total Cost of Ownership (TCO) across compute, storage, data egress, and third-party SaaS licenses.

### End-to-End Solution Architecture & Governance
- [ ] Authors comprehensive SADs covering Context, Container, Integration, Security, and Data topologies ([SAD Template](../../16-architecture-deliverables/SOLUTION-ARCHITECTURE-TEMPLATE.md)).
- [ ] Produces formal STRIDE Threat Models identifying trust boundaries, encryption policies, and IAM scopes ([Threat Model Template](../../21-architecture-tools/templates/threat-model-stride-template.md)).
- [ ] Defends complex solutions before the Architecture Review Board (ARB) with poise, data, and explicit trade-offs.

### Cross-Disciplinary Harmonization
- [ ] Harmonizes conflicting requirements across Security, Operations, Product, and Finance.
- [ ] Formulates viable migration strategies (e.g., Strangler Fig, Dual Run) for transitioning from legacy systems.
- [ ] Provides clear architectural guidance (Paved Roads) enabling delivery squads to execute autonomously.

---

## 3. Mandatory Evidence Portfolio Items
1. **Solution Architecture Document (SAD)**: Complete, production-vetted solution package ([Template](../../16-architecture-deliverables/SOLUTION-ARCHITECTURE-TEMPLATE.md)).
2. **Formal NFR Matrix**: Measurable SLAs, SLOs, and capacity projections ([NFR Matrix Guide](../../16-architecture-deliverables/15-nfr/README.md)).
3. **5+ Documented ADRs**: Rigorous decision records using `python 21-architecture-tools/generators/adr_generator.py`.
4. **STRIDE Threat Model**: Security and compliance blueprint ([Threat Model Template](../../21-architecture-tools/templates/threat-model-stride-template.md)).
5. **Disaster Recovery Plan**: Validated RPO/RTO failover runbook ([DR Template](../../21-architecture-tools/templates/disaster-recovery-runbook-template.md)).

---

## 4. Remediation Plan if Not Ready
* **If lacking business/financial modeling**: Shadow an Enterprise Architect on a capital allocation business case; model the 3-year TCO of an existing cloud workload.
* **If lacking ARB experience**: Submit an architectural spike or RFC to the ARB; practice defending design trade-offs in a mock review panel.
