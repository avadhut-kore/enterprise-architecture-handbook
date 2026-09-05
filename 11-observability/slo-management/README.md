# Enterprise SLO, SLI & Error Budget Architecture

## Executive Summary

Reliability is the most critical feature of any enterprise software system. If a system is offline or unresponsive, all other features are irrelevant. However, demanding **100% reliability is an anti-pattern**: the cost of the final fractional percentage of availability increases exponentially, while producing zero perceptible benefit to end users.

The **Service Level Objective (SLO) and Error Budget Framework** (pioneered by Google SRE) provides a mathematical, objective contract between Product Management and Engineering. It transforms subjective arguments about software release velocity into a data-driven feedback loop.

```mermaid
flowchart LR
    subgraph Data_Layer ["1. Telemetry Measurement"]
        Events["All User Requests"] --> SLI["SLI (Service Level Indicator)\nGood Events / Total Events"]
    end

    subgraph Objective_Layer ["2. Target & Budget Calculation"]
        SLI --> SLO["SLO (Target: e.g. 99.9%)\nRolling 30-Day Window"]
        SLO --> Budget["Error Budget = 100% - SLO\n(e.g., 0.1% = 43.8 mins downtime)"]
    end

    subgraph Governance_Layer ["3. Business & Velocity Governance"]
        Budget -->|Budget Positive (> 20%)| Green["FAST VELOCITY:\nShip features, deploy rapidly, take calculated risks"]
        Budget -->|Budget Near Zero (< 20%)| Orange["CAUTIOUS VELOCITY:\nMandatory canary soaks, freeze risky refactors"]
        Budget -->|Budget Exhausted (0%)| Red["FEATURE FREEZE:\n100% engineering effort diverted to reliability debt"]
    end
```

---

## Directory Index

| Document | Architectural Focus |
| :--- | :--- |
| **[`sli-design.md`](sli-design.md)** | Service Level Indicators: Availability, Latency, Freshness, Correctness, and production PromQL queries. |
| **[`slo-definition.md`](slo-definition.md)** | Defining realistic targets: 99% vs 99.9% vs 99.99%, downtime math, and user happiness thresholds. |
| **[`error-budgets.md`](error-budgets.md)** | Error budget mathematics: Rolling 30-day windows, cumulative exhaustion calculations, and burn rates. |
| **[`error-budget-policy.md`](error-budget-policy.md)** | The formal enterprise contract between Product and SRE: release freezes, exceptions, and escalation ladders. |
| **[`sla-vs-slo.md`](sla-vs-slo.md)** | Legal SLA vs Internal SLO vs Technical SLI: safety buffers, penalty clauses, and measurement differences. |
| **[`anti-patterns.md`](anti-patterns.md)** | 12 Lethal SLO anti-patterns (demanding 100%, vanity SLOs, un-enforced budgets, metric proliferation). |
| **[`checklists/slo-architecture-checklist.md`](checklists/slo-architecture-checklist.md)** | 25-Point practical audit checklist for enterprise SLO governance and SRE organizational readiness. |
