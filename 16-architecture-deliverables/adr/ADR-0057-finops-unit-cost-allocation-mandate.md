# ADR-0057: Mandatory FinOps Tagging and Unit Economics Cost Allocation

## Metadata
```yaml
id: ADR-0057
title: Mandatory FinOps Tagging and Unit Economics Cost Allocation
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Rapid cloud adoption resulted in millions of dollars in unallocated cloud spend with zero visibility into which product lines were driving costs.

---

## 2. Decision
We institute mandatory resource tagging (CostCenter, Owner, Environment) enforced via Service Control Policies and establish FinOps unit economic reporting (Cost per Transaction).

---

## 3. Positive Consequences
- 100% of cloud invoices are allocated directly to business unit P&Ls.
- Real-time cost anomaly detection alerts SREs to runaway spend within hours.
- Connects infrastructure investment directly to gross margin calculations.

---

## 4. Negative Consequences & Trade-offs
- Resources lacking mandatory tags fail to deploy in CI/CD.
- Requires ongoing cross-functional FinOps reviews with finance leadership.

---

## 5. Alternatives Considered & Rejected
- **Unallocated IT Overhead Model**: Rejected due to tragedy-of-the-commons resource waste.
