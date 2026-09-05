# Risk Assessment Matrix and Heatmaps

Quantifying architectural risks allows objective prioritization during roadmap planning and ARB deliberations.

## 1. 5x5 Architectural Risk Heatmap

```
Impact 
  5 (Catastrophic) │     [R3]     [R1]     [CRITICAL]
  4 (Major)        │              [R5]     [R2]
  3 (Moderate)     │     [R4]              [R6]
  2 (Minor)        │
  1 (Insignificant)│
                   └──────────────────────────────────►
                     1       2      3       4      5
                                Likelihood
```

- **R1: Monolithic primary database failover failure** (Likelihood: 3, Impact: 5) -> **Severity: 15 (Critical)**
- **R2: Third-party payment gateway outage during peak** (Likelihood: 4, Impact: 4) -> **Severity: 16 (Critical)**
- **R3: Data sovereignty breach in cross-region replication** (Likelihood: 2, Impact: 5) -> **Severity: 10 (High)**
- **R4: Cloud bill auto-scaling spike** (Likelihood: 2, Impact: 3) -> **Severity: 6 (Medium)**

## 2. Risk Mitigation Actions
Every risk scoring >= 12 must have an immediate Architectural Action Item (AAI) assigned to a sprint backlog with an explicit completion deadline.
