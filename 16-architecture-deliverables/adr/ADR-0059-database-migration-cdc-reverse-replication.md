# ADR-0059: Zero-Downtime Database Migration via CDC and Reverse Replication

## Metadata
```yaml
id: ADR-0059
title: Zero-Downtime Database Migration via CDC and Reverse Replication
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Migrating a 14 TB production database to the cloud carried immense business risk: an extended maintenance window was impossible, and post-cutover bugs could corrupt live transactions.

---

## 2. Decision
We mandate that all large database cloud migrations must utilize log-based Change Data Capture (CDC) replication paired with Reverse Replication back to on-premises during cutover.

---

## 3. Positive Consequences
- Reduces cutover downtime window to sub-5 minutes.
- Reverse replication guarantees a risk-free rollback path with zero data loss if production issues emerge post-cutover.
- Continuous data validation verifies parity prior to cutover.

---

## 4. Negative Consequences & Trade-offs
- Requires managing CDC replication instances and monitoring replication lag.
- Reverse replication must be decommissioned after the 7-day stabilization window.

---

## 5. Alternatives Considered & Rejected
- **Big-Bang Offline Export/Import**: Rejected due to requiring 36 hours of business downtime.
- **Dual-Write from Application Code**: Rejected due to high risk of distributed partial failures and data divergence.
