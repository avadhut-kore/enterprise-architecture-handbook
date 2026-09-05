# ADR-0054: Standardization on Terraform / OpenTofu for 100% Declarative IaC

## Metadata
```yaml
id: ADR-0054
title: Standardization on Terraform / OpenTofu for 100% Declarative IaC
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Manual cloud console configuration ('ClickOps') caused unrecoverable configuration drift, production outages, and irreproducible environments.

---

## 2. Decision
We mandate that 100% of enterprise cloud infrastructure must be defined declaratively in version-controlled Terraform / OpenTofu repositories and applied exclusively via CI/CD pipelines.

---

## 3. Positive Consequences
- Complete reproducibility of environments for disaster recovery.
- Infrastructure changes undergo automated security scanning and peer review.
- State locking prevents conflicting concurrent modifications.

---

## 4. Negative Consequences & Trade-offs
- Engineers must learn HCL syntax and manage state file backends.
- Slower for initial ad-hoc experimentation in non-prod.

---

## 5. Alternatives Considered & Rejected
- **Manual Console Provisioning**: Strictly prohibited.
- **Imperative Scripts (Bash / AWS CLI)**: Rejected due to lack of idempotency and state tracking.
