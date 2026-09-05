# Metrics Architecture & Design Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads and Architecture Review Boards (ARBs) with an objective verification rubric for designing, naming, and operating enterprise metrics.

---

## 2. The 25-Point Checklist

### Section 1: Metric Types & Mathematical Soundness
- [ ] **01.** Counters are used strictly for monotonically increasing values; raw counter values are never queried directly without `rate()`.
- [ ] **02.** Gauges are used for values that fluctuate naturally (memory, queue depth, active connections).
- [ ] **03.** Histograms are used for all request durations and payload sizes; Summaries are banned from distributed multi-instance services.
- [ ] **04.** Histogram bucket thresholds ($le$) are exponentially distributed and tightly bracket critical SLO targets.
- [ ] **05.** Latency histograms are segmented by status code class (`status=~"2.."`) to prevent fast errors from skewing P99 latencies.
- [ ] **06.** Moving averages on gauges use `avg_over_time()`; `rate()` is never applied to a gauge.
- [ ] **07.** Rate evaluation windows are sized to at least $4\times$ the scrape interval (e.g., `rate(m[2m])` for 30s scrapes).
- [ ] **08.** Prometheus Exemplars are enabled, linking latency distribution buckets directly to active trace IDs.

### Section 2: Methodologies & Business Telemetry
- [ ] **09.** The RED method (Rate, Errors, Duration) is fully implemented for every user-facing API and service.
- [ ] **10.** The USE method (Utilization, Saturation, Errors) is implemented for all compute, memory, disk, and network resources.
- [ ] **11.** Google's Four Golden Signals (Latency, Traffic, Errors, Saturation) are visible on tier-1 service dashboards.
- [ ] **12.** Key business throughput metrics (orders placed, payments authorized) are emitted alongside technical telemetry.
- [ ] **13.** Business metrics are utilized in CI/CD automated canary analysis to detect silent functional failures.

### Section 3: Cardinality & Governance
- [ ] **14.** Metric labels are strictly bounded enums; dynamic identifiers (`user_id`, `order_id`, `uuid`) are prohibited.
- [ ] **15.** Dynamic URL paths are normalized to parameterized templates (`/users/{id}`) before metric emission.
- [ ] **16.** Total active time series per service instance is bounded and monitored ($< 5,000$ series).
- [ ] **17.** OpenTelemetry Collector transform/filter processors are configured to drop accidental high-cardinality labels.

### Section 4: Naming Standards & Aggregation
- [ ] **18.** Metric names follow the canonical formula: `namespace_subsystem_name_unit`.
- [ ] **19.** Standard SI base units are enforced: seconds for duration (`_seconds`), bytes for storage (`_bytes`).
- [ ] **20.** Counters are suffixed with `_total` (e.g., `http_requests_total`).
- [ ] **21.** Ratios are suffixed with `_ratio` and bounded between $0.0$ and $1.0$ (never percentages).
- [ ] **22.** Standard resource attributes (`service.name`, `deployment.environment`) are attached via the OTel SDK.
- [ ] **23.** Expensive dashboard queries are pre-computed using Prometheus Recording Rules.
- [ ] **24.** Metrics older than 30 days are downsampled to 1-hour resolution to control storage costs.
- [ ] **25.** Automated alert thresholds are based on SLO error budget burn rates rather than static resource thresholds.
