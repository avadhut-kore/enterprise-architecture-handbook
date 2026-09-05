# Testing Observability Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 widespread enterprise anti-patterns in chaos engineering, GameDays, synthetic monitoring, and pre-production telemetry verification.

---

## 2. The 12 Testing Observability Anti-Patterns

### 1. The Untested Alerting Rule
* **Problem**: Writing complex PromQL alert expressions that are never tested against synthetic failure data.
* **Why It Happens**: Assuming query syntax is correct without verification.
* **Impact**: During a real catastrophic outage, the alert fails to fire due to a typo or label mismatch; responders are never paged.
* **Remediation**: Mandate `promtool test rules` in continuous integration.

### 2. Unannounced Chaos Engineering (Surprise Chaos)
* **Problem**: A chaos engineer kills production database nodes without informing on-call squads or having rollbacks ready.
* **Why It Happens**: Misguided belief that chaos tests must be "surprise attacks" to be realistic.
* **Impact**: Causes panic; triggers real business customer outages; erodes organizational trust in SRE practices.
* **Remediation**: Chaos experiments must be **pre-announced, blast-radius bounded, and equipped with automated abort triggers**.

### 3. Ignoring Synthetic Failures (Synthetic Alert Fatigue)
* **Problem**: Synthetic Playwright tests fail 10 times a day due to flaky UI selectors, leading engineers to mute synthetic alerts.
* **Why It Happens**: Poorly maintained test scripts that break on trivial frontend CSS changes.
* **Impact**: When the checkout backend genuinely fails, no one notices because synthetic tests were silenced.
* **Remediation**: Use resilient test selectors (`data-testid`); treat synthetic test maintenance with Tier-1 production priority.

### 4. GameDays Without Clear Hypotheses
* **Problem**: Running a 4-hour GameDay with vague objectives: "Let's break some things and see what happens."
* **Why It Happens**: Lack of structured planning.
* **Impact**: Wasted engineering hours; no actionable post-mortem improvements.
* **Remediation**: Every GameDay scenario must have a written hypothesis: *"Injecting 200ms latency on Service X will trigger Alert Y within 180 seconds."*

### 5. Testing Observability Only in Production
* **Problem**: Relying entirely on production outages to discover whether alerts and dashboards work.
* **Why It Happens**: Staging environments lack realistic traffic and configuration parity.
* **Impact**: Customers suffer through extended outages caused by un-tested operational runbooks.
* **Remediation**: Maintain production-parity staging environments with automated synthetic load generators.

### 6. Synthetic Probes That Skirt Authentication
* **Problem**: Synthetic health checks hitting an unauthenticated `/health` endpoint that returns `200 OK` even when the database is offline.
* **Why It Happens**: Avoiding the complexity of managing synthetic service accounts and credentials.
* **Impact**: Monitoring reports 100% availability while real authenticated users are 100% blocked from logging in.
* **Remediation**: Synthetics must execute full, authenticated end-to-end user journeys.

### 7. Missing Automated Abort Conditions (Runaway Chaos)
* **Problem**: A chaos experiment begins degrading production, but has no automated circuit breaker to abort the test.
* **Why It Happens**: Relying on manual human cancellation.
* **Impact**: The chaos tool consumes the squad's entire monthly error budget in 15 minutes before someone finds the "Stop" button.
* **Remediation**: Configure automated abort triggers: if production error rate spikes $> 1\%$, Chaos Mesh terminates instantly.

### 8. Single-Region Synthetic Probing
* **Problem**: Running synthetic probes exclusively from a single cloud region (e.g., AWS US-East-1).
* **Why It Happens**: Minimizing synthetic infrastructure costs.
* **Impact**: Fails to detect regional DNS outages, CDN edge routing failures, or trans-oceanic fiber cuts affecting European or Asian users.
* **Remediation**: Probe from at least 3 geographically diverse global regions.

### 9. Blind Trust in Synthetic Test Data (Excluding Real Traffic)
* **Problem**: Declaring an application healthy based purely on green synthetic checks while ignoring real user complaints.
* **Why It Happens**: Management trusting synthetic availability over real-user monitoring.
* **Impact**: Synthetic scripts may test a path that 5% of users use, missing bugs on paths that 95% of users use.
* **Remediation**: Pair synthetics (active probing) with real-user telemetry (passive telemetry).

### 10. Neglecting Runbook Verification During GameDays
* **Problem**: Senior engineers during GameDays bypass runbooks and fix issues using undocumented terminal commands.
* **Why It Happens**: Experienced engineers wanting to win the exercise quickly.
* **Impact**: Runbooks remain outdated, leaving junior engineers stranded during real nighttime outages.
* **Remediation**: Mandate that responders **must strictly follow published runbooks**; any missing step is logged as a defect.

### 11. Testing Without Telemetry Baselines
* **Problem**: Injecting chaos before establishing steady-state telemetry baselines.
* **Why It Happens**: Rushing experiment execution.
* **Impact**: Impossible to determine whether an observed metric shift was caused by the chaos test or unrelated background activity.
* **Remediation**: Establish 15 minutes of steady-state telemetry verification prior to every injection.

### 12. Stale Test Credentials Locking Synthetic Canaries
* **Problem**: Synthetic test account password expires every 90 days, causing synthetic monitors to flood PagerDuty with false P1 alerts.
* **Why It Happens**: Missing credential lifecycle automation.
* **Impact**: Spurious nighttime pages; on-call frustration.
* **Remediation**: Automate synthetic credential rotation or exempt synthetic test service principals from interactive password expiry.
