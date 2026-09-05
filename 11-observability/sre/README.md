# Site Reliability Engineering (SRE) Architecture (`sre/`)

## Executive Summary

Site Reliability Engineering applies software engineering principles to operations problems. This directory defines the architectural foundation of SRE: Error Budgets, SLA/SLO/SLI mathematical models, and toil reduction.

---

## Key Guides in this Directory

| Guide | Scope | Core Metric |
| :--- | :--- | :--- |
| [`sre-foundations-and-philosophy.md`](sre-foundations-and-philosophy.md) | SRE Tenets | Toil budget, 50% rule, blameless culture, shared ownership |
| [`sla-slo-sli-architecture.md`](sla-slo-sli-architecture.md) | Quantitative Sizing | SLA vs SLO vs SLI definitions, mathematical formulas |
| [`error-budget-policies-and-burn-rates.md`](error-budget-policies-and-burn-rates.md) | Alerting Engineering | Multi-window multi-burn-rate alerting without alert fatigue |
| [`toil-reduction-and-automation.md`](toil-reduction-and-automation.md) | Toil Elimination | Identifying, measuring, and eliminating operational toil |
