# Architecture Metrics and KPIs

How do you measure the value and health of enterprise software architecture? If you cannot measure it, you cannot improve it.

## 1. Core Architectural Health Metrics

```
┌─────────────────────────────────────────────────────────────┐
│ 1. DELIVERY VELOCITY & AGILITY (DORA METRICS)               │
│ - Deployment Frequency (Per day/week)                       │
│ - Lead Time for Changes (Commit to Production)              │
│ - Change Failure Rate (%)                                   │
│ - Mean Time to Recovery (MTTR)                              │
├─────────────────────────────────────────────────────────────┤
│ 2. STRUCTURAL HEALTH & MODULARITY                           │
│ - Instability (I = Ce / (Ca + Ce))                          │
│ - Abstractness (A = Na / Nc)                                │
│ - Distance from Main Sequence (D = |A + I - 1|)             │
│ - Cyclomatic Complexity and Dependency Inversion violations │
├─────────────────────────────────────────────────────────────┤
│ 3. OPERATIONAL & CLOUD EFFICIENCY (FINOPS)                  │
│ - Unit Economics (Cost per active user / Cost per API call) │
│ - SLO Attainment (% of time within latency/availability SLI)│
│ - Unallocated / Idle Cloud Infrastructure Waste (%)         │
└─────────────────────────────────────────────────────────────┘
```

## Related Modules
- [Pragmatic Architecture Governance](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/governance/pragmatic-architecture-governance.md)
- [Operations & SRE Architecture](../../11-observability/README.md)
