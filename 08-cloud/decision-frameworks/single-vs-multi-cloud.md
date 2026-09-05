# Decision Framework: Single-Cloud vs Multi-Cloud

```yaml
status: approved
decision_type: framework
scope: enterprise-cloud-strategy
owners: architecture-review-board
review_cadence: semi-annual
```

## 1. The Multi-Cloud Justification Matrix

| Proposal Scenario | ARB Ruling | Decision Criteria |
| :--- | :--- | :--- |
| **"We want multi-cloud active-active to get 99.999% uptime."** | **REJECTED** | Distributed latency across WAN and split-brain risks reduce actual uptime. |
| **"Regulator mandates verified disaster recovery outside primary provider."**| **APPROVED** | Mandatory for banking operating license (DORA/EBA compliance). |
| **"Use GCP BigQuery for analytics while running core OLTP in AWS."** | **APPROVED** | Asynchronous best-of-breed specialization with measurable 10x ROI. |
| **"Avoid vendor lock-in by writing lowest-common-denominator code."** | **REJECTED** | Massive operational tax and tooling complexity far outweighs theoretical lock-in risk. |
