# Commitment Discounts: Savings Plans, Reserved Instances & Spot

## Executive Summary

Enterprises should never pay On-Demand rates for predictable baseline infrastructure. Combining financial discount instruments reduces compute spend by up to 70%.

---

## 1. Compute Purchasing Portfolio Strategy

```mermaid
graph TD
    Workload[Total Enterprise Compute Capacity]
    Workload --> Baseline[1. 100% Predictable 24/7 Baseline: 3-Year Compute Savings Plans - 66% Discount]
    Workload --> Variable[2. Predictable Daytime Surge: 1-Year Savings Plans - 40% Discount]
    Workload --> FaultTol[3. Stateless Batch & CI/CD: Spot Fleets / Preemptible - 70-90% Discount]
    Workload --> TrueSpike[4. Unpredictable Spikes: On-Demand Compute - Zero Commitment]
```

---

## 2. Savings Plans vs Reserved Instances (RIs)
- **Legacy Reserved Instances**: Bound to specific instance types and regions (`m5.large` in `us-east-1`). If the enterprise modernizes to Graviton (`m7g`), the RI is orphaned.
- **Compute Savings Plans**: Commit to an hourly dollar spend ($/hour) across 1 or 3 years. Automatically applies across any instance family, any region, Fargate serverless containers, and Lambda, providing maximum architectural agility.
