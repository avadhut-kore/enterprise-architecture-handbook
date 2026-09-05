# Enterprise Metrics Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 common enterprise anti-patterns in metric design, alerting, and operational interpretation, detailing why they happen, their architectural blast radius, and the corrected pattern.

---

## 2. The 12 Metric Anti-Patterns

### 1. The High-Cardinality User ID Bomb
* **Problem**: Adding dynamic identifiers (`user_id`, `email`, `order_id`, `session_token`) as metric labels.
* **Why It Happens**: Developers attempt to use metrics as a search engine for customer-specific debugging.
* **Impact**: Millions of active time series explode time-series DB memory; crashes collectors and results in massive vendor overage fees.
* **Remediation**: Remove user IDs from metrics immediately. High-cardinality values belong in **distributed traces** and **structured logs**.

### 2. The Averaging Averages Fallacy
* **Problem**: Computing the arithmetic mean of average latencies across pods: $\text{avg}(\text{avg\_latency})$.
* **Why It Happens**: Teams misunderstand basic statistics; math appears simple.
* **Impact**: Obscures catastrophic outages. A pod handling 10,000 requests with 10ms latency combined with a dying pod handling 1 request with 60,000ms latency produces a completely misleading average.
* **Remediation**: Use **Histograms** with `histogram_quantile(0.99, ...)` to evaluate true percentile distributions.

### 3. Metric Name Dimension Embedding
* **Problem**: Creating separate metric names for each status or method: `api_get_success_count`, `api_post_fail_count`.
* **Why It Happens**: Legacy monitoring habits from systems without multidimensional labels (e.g., Graphite, StatsD).
* **Impact**: Impossibility of writing generalized PromQL queries or building reusable dashboard templates.
* **Remediation**: Consolidate into a single metric with dimensions: `api_requests_total{method="GET", status="success"}`.

### 4. Logging Everything as a Custom Metric
* **Problem**: Registering a custom metric for every internal if/else branch or utility function in domain code.
* **Why It Happens**: "More data is always better" mentality.
* **Impact**: 80% of emitted metrics are never queried by any dashboard or alert, consuming network bandwidth and scraping compute.
* **Remediation**: Adhere strictly to the RED method. Only instrument architectural boundaries and key business milestones.

### 5. Applying `rate()` to Gauges
* **Problem**: Writing PromQL queries like `rate(node_memory_MemAvailable_bytes[5m])`.
* **Why It Happens**: Misunderstanding counter reset logic vs fluctuating values.
* **Impact**: Bizarre, nonsensical negative or spike values during nominal operations.
* **Remediation**: Use `deriv()` for instantaneous rate-of-change on gauges, or `avg_over_time()` for moving averages.

### 6. Unsynchronized Scrape Intervals (The Nyquist Violation)
* **Problem**: Evaluating rates over a time window shorter than $2\times$ the scrape interval (e.g., `rate(m[30s])` with a 30s scrape interval).
* **Why It Happens**: Responders want "instant" graphs.
* **Impact**: PromQL queries return empty results or jagged, broken lines whenever a single scrape is slightly delayed.
* **Remediation**: The time window must always be at least **$4\times$ the scrape interval** (e.g., `rate(m[2m])` for a 30s scrape interval).

### 7. Paging on Raw Resource Utilization Alone
* **Problem**: Paging an on-call engineer whenever CPU or Memory exceeds 80%.
* **Why It Happens**: "Common sense" infrastructure monitoring heritage.
* **Impact**: Chronic alert fatigue. Systems often operate safely at 85% CPU under nominal batch workloads.
* **Remediation**: Page on **SLO error budget burn** (user symptoms). Demote CPU thresholds to non-paging warnings.

### 8. Percentage Storage of Ratios
* **Problem**: Emitting metrics as percentages ($0.0 - 100.0$) rather than unit intervals ($0.0 - 1.0$).
* **Why It Happens**: Human intuition prefers 99.5% over 0.995.
* **Impact**: Inconsistent mathematical operations across teams; breaking dashboard formatting plugins.
* **Remediation**: Store all ratios between $0.0$ and $1.0$. Let visualization tools (Grafana) format values as percentages.

### 9. Non-Resetting In-Memory Counters
* **Problem**: Custom application code manually resets an internal counter to zero every 60 seconds.
* **Why It Happens**: Misunderstanding that Prometheus handles reset detection automatically.
* **Impact**: `rate()` calculations break completely because Prometheus assumes a reset indicates a process crash.
* **Remediation**: Let counters increment continuously for the lifetime of the process. Never manually zero a counter.

### 10. Missing Units in Metric Names
* **Problem**: Metric named `request_duration` or `cache_size` without unit suffix.
* **Why It Happens**: Lazy naming conventions.
* **Impact**: Responders waste time during outages guessing whether duration is in milliseconds, microseconds, or seconds.
* **Remediation**: Mandatory unit suffixes: `request_duration_seconds`, `cache_size_bytes`.

### 11. Over-Filtering Metric Labels in Dashboards
* **Problem**: Hardcoding static pod names or container IDs in dashboard queries: `{pod="checkout-7fb9-xx"}`.
* **Why It Happens**: Copy-pasting ad-hoc queries during an incident into persistent dashboards.
* **Impact**: Dashboards break immediately upon the next Kubernetes deployment or autoscaling event.
* **Remediation**: Always aggregate over `service` and `namespace` dimensions using template variables.

### 12. Monolithic Scraping Architecture
* **Problem**: A single centralized Prometheus server attempting to scrape 50,000 pods across 5 global regions.
* **Why It Happens**: Delaying regional telemetry architecture investments.
* **Impact**: Massive cross-region network egress bills; scraping timeouts during network blips; single point of failure.
* **Remediation**: Deploy regional Prometheus/OTel Collector instances with federated remote write to a central tier.
