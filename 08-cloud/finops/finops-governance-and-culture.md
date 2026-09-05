# FinOps Governance, KPIs & Anomaly Detection

## Executive Summary

Operationalizing FinOps requires automated cost anomaly detection, strict budget thresholds, and executive scorecards.

---

## 1. Machine-Learning Anomaly Detection

```mermaid
graph LR
    CloudSpend[Daily Cloud Billing Pipeline] --> ML[Cost Anomaly Detection Engine]
    ML --> Baseline{Spend Exceeds 3-Sigma Historical Baseline?}
    Baseline -->|Yes: e.g., DynamoDB API Spikes 500% at 2 AM| Alert[Real-time Slack / PagerDuty Alert to On-Call SRE]
    Baseline -->|No| Store[(Billing Data Warehouse)]
```

---

## 2. Key FinOps KPIs
1. **Unallocated Spend Percentage**: Target $< 5\%$ of total enterprise cloud bill unallocated to cost centers.
2. **Commitment Coverage**: Target $> 75\%$ of steady-state compute covered by Savings Plans or Reserved Instances.
3. **Commitment Utilization**: Target $> 95\%$ utilization of purchased discount commitments.
