# Architectural Risk Management

Risk is the probability of an adverse event multiplied by its potential blast radius. Managing risk is the core duty of the software architect.

## 1. Architectural Risk Taxonomy

```
┌─────────────────────────────────────────────────────────────┐
│ 1. STRUCTURAL RISKS                                         │
│ Single points of failure (SPOF), shared monolithic databases│
│ cyclic dependencies, non-isolated blast radiuses.           │
├─────────────────────────────────────────────────────────────┤
│ 2. OPERATIONAL & CAPACITY RISKS                             │
│ Unbounded queues, memory leaks, runaway auto-scaling costs, │
│ hard connection limits, lack of circuit breaking.           │
├─────────────────────────────────────────────────────────────┤
│ 3. COMPLIANCE & LEGAL RISKS                                 │
│ Unencrypted PII, lack of auditability, GDPR right-to-forget │
│ violations, multi-tenant cross-tenant leakage.              │
├─────────────────────────────────────────────────────────────┤
│ 4. THIRD-PARTY & VENDOR RISKS                               │
│ SaaS API rate limits, provider outages, deprecation cycles, │
│ proprietary lock-in with steep pricing renegotiations.      │
└─────────────────────────────────────────────────────────────┘
```

## 2. Blast Radius Containment Strategies

- **Bulkheading**: Isolate thread pools, connection pools, and compute clusters so failure in one tenant or domain cannot saturate shared capacity.
- **Cell-Based Architecture**: Shard the entire infrastructure into fully autonomous, self-contained "cells" (e.g., cell = 10,000 customers). A failure in Cell 4 affects only Cell 4.
- **Fail-Open vs Fail-Closed**: Decide consciously whether safety or availability dominates during subsystem failure (e.g., authorization checks must fail-closed; recommendation widgets must fail-open).

## Related Modules
- [Risk Assessment Matrix and Heatmaps](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/risk/risk-assessment-matrix-and-heatmaps.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
