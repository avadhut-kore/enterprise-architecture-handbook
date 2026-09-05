# ADR-0044: Standardization on AWS as Primary Enterprise Cloud Provider

## Metadata
```yaml
id: ADR-0044
title: Standardization on AWS as Primary Enterprise Cloud Provider
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
The enterprise required establishing a primary hyper-scale cloud provider to consolidate fragmented infrastructure, achieve volume discounting, and focus engineering training.

---

## 2. Decision
We standardize on Amazon Web Services (AWS) as the primary cloud provider for 80% of enterprise workloads, while permitting specialized Azure integration for Microsoft/Entra ID and Google BigQuery for analytics.

---

## 3. Positive Consequences
- Eliminates fractured engineering competencies.
- Unlocks Tier-3 enterprise discounting commitments.
- Deepest ecosystem of managed PaaS and serverless primitives.

---

## 4. Negative Consequences & Trade-offs
- Creates commercial dependency on Amazon Web Services.
- Requires disciplined application layering to prevent accidental SDK coupling.

---

## 5. Alternatives Considered & Rejected
- **Multi-Cloud Split (50/50 AWS and Azure)**: Rejected due to doubling compliance costs and extreme operational complexity.
- **Pure On-Premises Expansion**: Rejected due to high CapEx and slow hardware lead times.
