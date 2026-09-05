# Cost Estimation & FinOps Model: SaaS Platform

## 1. Cost-per-Tenant Attribution
```
Total Cost per Tenant = 
    Shared Pooled Compute / Active Tenant Count
  + Dedicated Silo Infrastructure (if Enterprise)
  + Storage Consumption ($0.023/GB)
  + Third-Party Auth & Metering API Fees
```
- Tracking cost-per-tenant enables accurate SaaS gross margin calculations across pricing tiers (Target: $\ge 80\%$ gross margin).

## 2. FinOps Optimization Levers & Governance
- **Autoscaling & Rightsizing**: Karpenter / KEDA dynamic provisioning eliminating idle instance waste.
- **Commitment Discounts**: 1-year and 3-year Compute Savings Plans covering predictable baseline capacity.
- **Storage Lifecycle Tiering**: Transition unaccessed data and logs to cold/archive storage tiers after 30 days.
