# Alerting Architecture & Operational Readiness Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads and Architecture Review Boards (ARBs) with an objective verification rubric for designing, tuning, and operating enterprise alerting systems.

---

## 2. The 25-Point Checklist

### Section 1: Alerting Philosophy & Severity Tiers
- [ ] **01.** Paging alerts (P1/P2) are derived from Service Level Objectives (SLOs) and Error Budget burn rates.
- [ ] **02.** Static threshold alerts on raw CPU and memory are strictly demoted to non-paging status.
- [ ] **03.** Every P1 alert represents an active catastrophe requiring immediate human intervention within 5 minutes.
- [ ] **04.** P3 and P4 alerts route to Jira backlogs or Slack digests; they never page on-call engineers.
- [ ] **05.** Server-side errors (HTTP 5xx) trigger reliability alerts; client errors (HTTP 4xx) are tracked separately.

### Section 2: Multi-Window Multi-Burn-Rate Implementation
- [ ] **06.** Fast burn rate alerting is configured: $14.4\times$ burn rate over 1-hour (long) and 5-minute (short) windows.
- [ ] **07.** Slow burn rate alerting is configured: $6.0\times$ burn rate over 6-hour (long) and 30-minute (short) windows.
- [ ] **08.** Non-urgent burn rate alerting is configured: $1.0\times$ burn rate over 3-day windows triggering tickets.
- [ ] **09.** PromQL alert expressions are pre-computed using Prometheus Recording Rules to minimize evaluation load.
- [ ] **10.** Prometheus alert rules are unit-tested in CI/CD using `promtool test rules`.

### Section 3: Fatigue Elimination & Noise Reduction
- [ ] **11.** AlertManager grouping rules (`group_by`, `group_wait: 30s`) batch related alerts to prevent alert storms.
- [ ] **12.** Inhibition rules are configured: root-cause infrastructure alerts mute downstream application alerts.
- [ ] **13.** Alert flapping protection is implemented using duration hysteresis (`for: 5m`) and asymmetric thresholds.
- [ ] **14.** Acknowledged active alerts are silenced for a minimum of 4 hours (`repeat_interval: 4h`).
- [ ] **15.** Alert volume metrics are tracked: on-call rotations receiving $> 2$ pages per shift trigger operational reviews.

### Section 4: Routing, Escalation & Runbooks
- [ ] **16.** Every alert rule contains a mandatory, verified link to a production runbook (`runbook_url`).
- [ ] **17.** Runbooks contain step-by-step diagnostic commands, safe rollback instructions, and verification checks.
- [ ] **18.** P1 alerts escalate automatically if unacknowledged within 5 minutes by the primary on-call engineer.
- [ ] **19.** Secondary and management fallback schedules are configured in PagerDuty/Opsgenie.
- [ ] **20.** On-call rotations contain at least 6 qualified engineers to prevent burnout.

### Section 5: Verification & Continuous Improvement
- [ ] **21.** Chaos engineering drills (GameDays) regularly inject faults to verify that alerts fire and route correctly.
- [ ] **22.** Stale alerts firing continuously for $> 30$ days are formally triaged, fixed, or deleted.
- [ ] **23.** Error budget exhaustion automatically triggers software release freeze policies.
- [ ] **24.** Post-incident reviews evaluate whether alerts fired on time and whether runbooks were effective.
- [ ] **25.** Automated status page updates keep internal and external stakeholders informed without distracting responders.
