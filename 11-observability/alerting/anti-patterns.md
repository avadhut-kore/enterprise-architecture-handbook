# Enterprise Alerting Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 widespread enterprise alerting anti-patterns, explaining why they occur, their impact on engineering organizations, and concrete architectural remediations.

---

## 2. The 12 Alerting Anti-Patterns

### 1. The 3:00 AM Static CPU Alert
* **Problem**: Paging an on-call engineer at night because a batch worker pod reached 85% CPU.
* **Why It Happens**: Legacy infrastructure monitoring mindset.
* **Impact**: Destroys on-call morale; engineers wake up, see batch job running normally, and mute PagerDuty.
* **Remediation**: Never page on raw CPU utilization alone. Page on **SLO error budget burn** or **queue processing lag**.

### 2. Paging Without a Runbook URL
* **Problem**: Alert notification states: `Alert: CheckoutServiceErrorSpike` with no description, links, or instructions.
* **Why It Happens**: Developer configured alert hastily in Grafana UI.
* **Impact**: Responders waste 20 minutes trying to remember how to debug the service; high MTTR.
* **Remediation**: Mandatory CI/CD linter rule: fail alert configuration PRs if `runbook_url` is missing or returns a 404.

### 3. The Unowned Alert (#alerts Slack Dumpster)
* **Problem**: Routing all alerts from 50 microservices into a single public Slack channel.
* **Why It Happens**: Teams avoid assigning formal on-call rotations.
* **Impact**: The channel accumulates 5,000 unread messages per day; everyone mutes the channel; outages go unnoticed.
* **Remediation**: Route alerts strictly to the owning squad's dedicated on-call schedule via PagerDuty/Opsgenie.

### 4. Alert Flapping Storms
* **Problem**: An alert fires, resolves, fires, and resolves 40 times in one hour.
* **Why It Happens**: Metric oscillates tightly around a static boundary with no `for` duration or hysteresis.
* **Impact**: Responders receive dozens of SMS messages; pager becomes unusable.
* **Remediation**: Enforce `for: 5m` and asymmetrical fire/resolve thresholds.

### 5. Paging on Client Errors (HTTP 4xx)
* **Problem**: Alerting and paging when HTTP 401 Unauthorized or HTTP 404 Not Found spikes.
* **Why It Happens**: Grouping all non-200 responses together: `status != 200`.
* **Impact**: A script kiddie running a vulnerability scanner against your website triggers 10,000 404s, waking up your lead architect at 2:00 AM.
* **Remediation**: Restrict paging alerts strictly to server errors (HTTP 5xx, gRPC error status). Track 4xx on security dashboards.

### 6. Alert Amnesia (Ignoring Acknowledged Outages)
* **Problem**: Setting `repeat_interval: 5m` so that even after an engineer acknowledges an alert and begins fixing it, PagerDuty continues calling their phone every 5 minutes.
* **Why It Happens**: Misunderstanding AlertManager repeat intervals.
* **Impact**: Severely distracts responders while executing delicate database failover commands.
* **Remediation**: Set `repeat_interval: 4h` once an alert is acknowledged.

### 7. The Cascading Dependency Avalanche
* **Problem**: Downstream payment gateway outage causes 25 upstream microservices to fire individual pages.
* **Why It Happens**: Missing AlertManager inhibition rules.
* **Impact**: On-call engineers across 8 different squads are paged simultaneously for the exact same root cause.
* **Remediation**: Configure AlertManager inhibition rules to mute downstream symptoms when the root cause alert fires.

### 8. Paging on Single-Instance Failures in Resilient Clusters
* **Problem**: Paging an engineer because 1 of 50 stateless Kubernetes pods crashed and restarted in 2 seconds.
* **Why It Happens**: Monitoring container restarts instead of service availability.
* **Impact**: Needless interruption for a self-healing event handled by Kubernetes.
* **Remediation**: Alert only if pod restart crash-looping exceeds threshold and impacts overall service capacity.

### 9. Lack of Testing for Alert Rules (The Silent Alert Failure)
* **Problem**: A PromQL query in an alert has a syntax error or references an obsolete metric name.
* **Why It Happens**: Alerts are never tested in staging.
* **Impact**: An outage occurs, but the alert never fires because the query silently evaluates to empty!
* **Remediation**: Write automated unit tests for Prometheus rules using `promtool test rules`.

### 10. The Boy Who Cried Wolf Alert
* **Problem**: An alert has been firing continuously in production for 6 months, and everyone ignores it ("Oh, that's just the staging sync bug, ignore it").
* **Why It Happens**: Inadequate technical debt prioritization.
* **Impact**: Engineers develop a subconscious culture that alert triggers are optional.
* **Remediation**: **Delete or fix it today**. If an alert can be safely ignored for 6 months, it is not an alert.

### 11. Over-Sensitive Single-Window Alerts
* **Problem**: Evaluating error rates over a single 5-minute window with a low threshold.
* **Why It Happens**: Attempting to minimize Mean Time to Detect (MTTD).
* **Impact**: Nominal network blips trigger false pages constantly.
* **Remediation**: Deploy **Multi-Window Multi-Burn-Rate alerting** requiring both long and short windows to confirm the failure.

### 12. Paging Product Managers and Executives
* **Problem**: PagerDuty routing configured to call the VP of Engineering or Product Manager for technical alerts.
* **Why It Happens**: Misunderstanding operational escalation vs executive communication.
* **Impact**: Non-technical leaders panic; disrupt technical triage on the audio bridge.
* **Remediation**: Page technical responders only. Use automated StatusPage updates and Slack summaries for executive leadership.
