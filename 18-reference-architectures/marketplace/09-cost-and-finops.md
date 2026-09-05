# Cost Estimation & FinOps Model: Marketplace Platform

## 1. Monthly TCO Across Scale Tiers

| Cost Dimension | 50k Sellers / $300M GMV | 1.2M Sellers / $10B GMV |
| :--- | :--- | :--- |
| **Payment Payout API Fees** | $12,000 / month | $180,000 / month |
| **Catalog OpenSearch Cluster**| $3,500 / month | $24,000 / month |
| **Relational Aurora Database**| $2,800 / month | $18,500 / month |
| **EKS Container Fleet** | $2,200 / month | $15,000 / month |
| **Total Monthly TCO** | **$20,500 / month** | **$237,500 / month** |

## 2. FinOps Optimization Levers & Governance
- **Autoscaling & Rightsizing**: Karpenter / KEDA dynamic provisioning eliminating idle instance waste.
- **Commitment Discounts**: 1-year and 3-year Compute Savings Plans covering predictable baseline capacity.
- **Storage Lifecycle Tiering**: Transition unaccessed data and logs to cold/archive storage tiers after 30 days.
