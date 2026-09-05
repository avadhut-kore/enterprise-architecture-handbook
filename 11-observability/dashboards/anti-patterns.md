# Enterprise Dashboard Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 widespread enterprise dashboard anti-patterns, explaining why they occur, their impact on incident resolution times, and concrete architectural remediations.

---

## 2. The 12 Dashboard Anti-Patterns

### 1. The Wall of Dashboards (Information Paralysis)
* **Problem**: A single dashboard containing 60+ individual graphs, gauges, and tables.
* **Why It Happens**: Developers add a new panel for every incident or bug they investigate, never pruning old panels.
* **Impact**: During an outage, responders spend 15 minutes scrolling up and down trying to find relevant graphs; dashboard takes 30 seconds to load.
* **Remediation**: Limit tier-1 dashboards to **$< 12$ panels**. Use dashboard links to route responders to tier-2 drill-down boards.

### 2. The Non-Templated Hardcoded Query
* **Problem**: Hardcoding static environment or pod names into PromQL queries: `http_requests_total{pod="checkout-7fb9-xx"}`.
* **Why It Happens**: Copying ad-hoc queries from local exploratory sessions directly into dashboard panels.
* **Impact**: Panel breaks as soon as the Kubernetes deployment rotates pods; zero reusability across staging and production.
* **Remediation**: Use Grafana template variables (`$environment`, `$cluster`, `$namespace`, `$service`).

### 3. The Un-Anchored Y-Axis (Misleading Scaling)
* **Problem**: Bar or area charts configured with dynamic Y-axis baselines (e.g., scaling from 98.5% to 99.5%).
* **Why It Happens**: Trying to make minor fluctuations visible.
* **Impact**: A nominal 0.1% jitter looks like a catastrophic cliff drop, causing unnecessary panic.
* **Remediation**: Always anchor percentage and count axes at **zero** ($0.0$).

### 4. Running Heavy Real-Time Quantiles on Dashboards
* **Problem**: 10 dashboard panels running raw `histogram_quantile(0.99, ...)` over 30-day ranges with 10-second refresh.
* **Why It Happens**: Responders wanting instant high-resolution percentile graphs.
* **Impact**: Freezes the Prometheus server; exhausts memory; causes dashboard query timeouts for all users.
* **Remediation**: Pre-compute expensive quantiles using **Prometheus Recording Rules**.

### 5. Color Inconsistency (The Rainbow Dashboard)
* **Problem**: Using 10 random bright colors for arbitrary lines; using Red for a nominal cache metric.
* **Why It Happens**: Relying on default palette rotation.
* **Impact**: Responders mistake healthy spikes for severe errors; high cognitive strain.
* **Remediation**: Reserve Red strictly for errors and SLO breaches. Use neutral blues, greys, and greens for nominal metrics.

### 6. Missing Units and Labels
* **Problem**: A graph showing values from 0 to 1,000 with no Y-axis label or unit (Is it milliseconds? Seconds? Bytes? Dollars?).
* **Why It Happens**: Rushing dashboard creation.
* **Impact**: Responders waste precious minutes during SEV-1 calls arguing over whether latency is 200ms or 200 seconds.
* **Remediation**: Enforce mandatory unit definitions in Grafana panel settings (`seconds (s)`, `bytes (B)`).

### 7. The Un-Maintained Ghost Dashboard
* **Problem**: 500 deprecated, abandoned dashboards created by former employees cluttering Grafana search.
* **Why It Happens**: Lack of dashboard lifecycle management.
* **Impact**: Responders open an obsolete dashboard during an outage that displays flatlined metrics from an old architecture.
* **Remediation**: Enforce Dashboard-as-Code in Git; delete orphan dashboards automatically if unviewed for 90 days.

### 8. The Missing Runbook Link
* **Problem**: A dashboard indicates that the database connection pool is 100% saturated, but contains no guidance on what to do next.
* **Why It Happens**: Dashboards viewed strictly as monitoring tools rather than operational triage consoles.
* **Impact**: Responders stall while searching confluence for remediation commands.
* **Remediation**: Add a prominent markdown panel or header link pointing directly to the service's triage runbook.

### 9. Lack of Log and Trace Integration
* **Problem**: Dashboards showing metric spikes in isolation with no way to navigate to corresponding logs or traces.
* **Why It Happens**: Siloed monitoring tools.
* **Impact**: Responders must manually copy timestamps, open a separate logging tab, and search for errors manually.
* **Remediation**: Enable Grafana Data Links and Exemplars, allowing engineers to click a latency spike and jump directly to the offending trace in Tempo/Jaeger.

### 10. Auto-Refresh Overload
* **Problem**: Setting high-frequency auto-refresh (e.g., 5 seconds) on 50 dashboards displayed on unattended TV monitors across the office.
* **Why It Happens**: "Mission control" aesthetic.
* **Impact**: Generates millions of wasted queries against monitoring backends, degrading query performance for real incident responders.
* **Remediation**: Restrict unattended TV dashboards to 60-second refresh; use query caching.

### 11. Clashing Timezone Displays
* **Problem**: Dashboard panels displaying times in the engineer's local browser timezone (PST), while logs and servers run in UTC.
* **Why It Happens**: Leaving Grafana timezone setting at "Default / Browser".
* **Impact**: Responders correlate a 14:00 error on the dashboard with 06:00 in server logs, wasting 20 minutes before noticing the offset.
* **Remediation**: **Enforce UTC across all enterprise operational dashboards**.

### 12. Un-Alerted Dashboards (Dashboard-Watching Operations)
* **Problem**: Expecting engineers to sit and watch dashboards all day to catch incidents.
* **Why It Happens**: Incomplete alerting architecture.
* **Impact**: Humans cannot stare at screens for hours without missing anomalies; outages go unnoticed for hours.
* **Remediation**: Dashboards are for **triage after an alert fires**. If an anomaly requires action, create an automated alerting rule.
