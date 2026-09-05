# Enterprise Alerting Architecture & SRE Engineering

## Executive Summary

Alerting is the operational mechanism that summons human beings to intervene when software systems fail. In an enterprise system, poorly designed alerts generate **alert fatigue**—a dangerous psychological condition where engineers become desensitized to pages, resulting in real outages being ignored.

Modern SRE alerting rejects static threshold alerts (e.g., "CPU > 80% for 5 minutes"). Instead, it enforces **Symptom-Driven Multi-Window Multi-Burn-Rate Alerting** based directly on Service Level Objectives (SLOs) and Error Budget consumption rates.

```mermaid
flowchart TD
    subgraph Signal_Evaluation ["1. Telemetry & SLI Evaluation"]
        Telemetry["Continuous SLI Stream\n(Good Events / Total Events)"]
        SLO["SLO Target (e.g., 99.9% Availability)"]
    end

    subgraph Burn_Rate_Engine ["2. Multi-Window Multi-Burn-Rate Engine"]
        BurnCheck{"Burn Rate Calculation\n(How fast is budget dying?)"}
        FastBurn["Fast Burn: 14.4x Rate\n- 2% budget consumed in 1h\n- Long Window: 1h / Short Window: 5m"]
        SlowBurn["Slow Burn: 6.0x Rate\n- 5% budget consumed in 6h\n- Long Window: 6h / Short Window: 30m"]
        TicketBurn["Slow Drift: 1.0x Rate\n- 10% budget consumed in 3d\n- Long Window: 3d / Short Window: 6h"]
    end

    subgraph Action_Routing ["3. Routing & Incident Action"]
        Paging["P1 / P2 Page (24/7 Phone / PagerDuty)\n- Direct to On-Call Engineer\n- Mandatory Runbook Link"]
        Ticketing["P3 / P4 Ticket (Next Business Day Jira)\n- Backlog Remediation"]
    end

    Telemetry --> BurnCheck
    SLO --> BurnCheck
    BurnCheck -->|Critical Emergency| FastBurn
    BurnCheck -->|Major Threat| SlowBurn
    BurnCheck -->|Non-Urgent Trend| TicketBurn

    FastBurn --> Paging
    SlowBurn --> Paging
    TicketBurn --> Ticketing
```

---

## Directory Index

| Document | Architectural Focus |
| :--- | :--- |
| **[`alerting-philosophy.md`](alerting-philosophy.md)** | Core principles: Alert on symptoms not causes; every page actionable; eliminate noise. |
| **[`multi-window-multi-burn-rate.md`](multi-window-multi-burn-rate.md)** | Google SRE alerting algorithm: mathematical formulas, window sizing, and production PromQL rules. |
| **[`error-budget-alerts.md`](error-budget-alerts.md)** | Error budget exhaustion rates: 2% in 1h, 5% in 6h, 10% in 3 days, and governance triggers. |
| **[`alert-severity.md`](alert-severity.md)** | P1/Critical (24/7 Page), P2/Major (Waking Hours Page), P3/Moderate (Ticket), P4/Low (Log/Info). |
| **[`routing-escalation.md`](routing-escalation.md)** | Dynamic routing, PagerDuty/Opsgenie integrations, multi-tiered escalation, and fallback schedules. |
| **[`alert-fatigue.md`](alert-fatigue.md)** | Mitigating fatigue: alert deduplication, dependency tree silencing, flapping detection, and volume budgets. |
| **[`runbook-integration.md`](runbook-integration.md)** | Runbook architecture: linking alerts to deterministic human and automated triage playbooks. |
| **[`anti-patterns.md`](anti-patterns.md)** | 12 Lethal alerting anti-patterns (static CPU alerts, flapping alerts, un-runbooked pages, alert storms). |
| **[`checklists/alerting-architecture-checklist.md`](checklists/alerting-architecture-checklist.md)** | 25-Point practical audit checklist for alerting system design and operational readiness. |
