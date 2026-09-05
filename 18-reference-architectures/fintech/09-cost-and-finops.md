# Cost Estimation & FinOps Model: Fintech Platform

## 1. Monthly TCO Across Scale Tiers

| Cost Category | 1M Accounts / 250 TPS | 25M Accounts / 5,000 TPS |
| :--- | :--- | :--- |
| **Distributed SQL (Spanner/CockroachDB)**| $8,500 / month | $48,000 / month |
| **CloudHSM Clusters (Redundant Pairs)** | $3,600 / month | $10,800 / month |
| **Compute (EKS Container Fleet)** | $4,500 / month | $26,000 / month |
| **Fraud Scoring & Kafka Event Mesh** | $3,200 / month | $18,500 / month |
| **Total Monthly TCO** | **$19,800 / month** | **$103,300 / month** |
