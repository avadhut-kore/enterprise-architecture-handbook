# Checklist 02: Alerting Quality & Hygiene Audit

## 1. Overview
Used quarterly by SRE Leads and Incident Commanders to audit existing alert rules, eradicate alert fatigue, and ensure high operational signal-to-noise ratios.

---

## 2. Verification Rubric

| Audit Dimension | Evaluation Criteria | Remediation If Failed | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **SLO Alignment** | Does the alert represent actual customer pain, or just a component metric? | Convert static CPU/memory alerts into SLO Error Budget burn-rate alerts. | [ ] |
| **Multi-Burn Windows**| Does the alert use dual short/long time windows to eliminate transient spikes? | Re-architect using multi-burn rate PromQL patterns. | [ ] |
| **Actionability** | Can the on-call engineer take an immediate, concrete action upon receiving the page? | If no human action exists, delete the page and convert to a ticket or dashboard. | [ ] |
| **Runbook Link** | Does the alert payload contain a valid, tested runbook URL? | Add mandatory `runbook_url` annotation in Prometheus alerting rule. | [ ] |
| **False-Positive Rate**| Has this alert fired $\ge 3$ times in the last 30 days without an incident created? | Tune threshold, extend window duration, or delete alert. | [ ] |
| **Routing Severity** | Are non-urgent alerts routing to Slack/Jira rather than paging humans at 3:00 AM? | Re-classify severity: Reserve `page` strictly for fast-burning customer outages. | [ ] |
| **Deduplication** | Are upstream gateway failures masking downstream dependency pages? | Configure Alertmanager `inhibit_rules` to suppress cascading child alerts. | [ ] |
