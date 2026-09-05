# ADR-0003: Adopting Multi-Window Multi-Burn-Rate Alerting over Static Thresholds

* **Status**: Accepted
* **Date**: 2026-04-05
* **Deciders**: SRE Practice Lead, Director of Operations, Incident Commander Lead
* **Technical Story**: [ARCH-OBS-003] Modernize Alerting Strategy

---

## Context and Problem Statement
Engineering teams suffer from severe on-call alert fatigue, receiving over 1,400 PagerDuty notifications per week. Over 80% of alerts are false alarms caused by static thresholds (e.g., `CPU > 80%` or `Error Rate > 1% for 5 minutes`). Crucially, these alerts do not correlate with user-impacting outages.

## Decision Drivers
* Drastic reduction of false positive alerts.
* Strict correlation between pages and customer-perceived SLO degradation.
* Clear operational urgency: fast burns page immediately; slow burns notify during business hours.

## Considered Options
1. **Option 1**: Retain static single-window threshold alerts (Status Quo).
2. **Option 2**: Standardize on **Google SRE Multi-Window Multi-Burn-Rate Alerting** in Prometheus.
3. **Option 3**: Anomaly detection / ML-based alerting.

## Decision Outcome
**Chosen Option**: **Option 2: Multi-Window Multi-Burn-Rate Alerting**.

### Positive Consequences
* **92% Reduction in Alert Fatigue**: Pagers fire only when an outage threatens to consume significant portions of the 30-day error budget.
* **Dual-Window Confirmation**: Short window detects immediate spikes; long window confirms sustained burning, eliminating transient reset flashes.
* **Actionable Urgency**: Critical pages reserved for $14.4\times$ burn rates (2% budget consumed in 1 hour).

### Negative Consequences
* Requires educating all engineering squads on Error Budget mathematics and PromQL multi-burn rate syntax.

---

## Links
* Google SRE Book - Alerting on SLOs: https://sre.google/workbook/alerting-on-slos/
* Implementation Spec: [`../alerting/multi-window-multi-burn-rate.md`](../alerting/multi-window-multi-burn-rate.md)
