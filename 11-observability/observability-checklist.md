# Enterprise Observability Architecture Audit Checklist

## 1. Executive Summary
This checklist provides a rigorous, 50-point architectural audit rubric to evaluate the observability posture of any enterprise application, microservice, or platform. It is designed for use during Architecture Review Board (ARB) submissions, Production Readiness Reviews (PRR), and post-incident architectural remediations.

---

## 2. The 50-Point Observability Audit

### Section 1: Instrumentation & OpenTelemetry Standards (Points 1–10)
- [ ] **01.** Application uses vendor-neutral OpenTelemetry API/SDK rather than proprietary vendor SDKs.
- [ ] **02.** Distributed context propagation (W3C TraceContext) is implemented on all ingress and egress calls.
- [ ] **03.** Context headers (`traceparent`, `tracestate`) are propagated across asynchronous message brokers (Kafka headers).
- [ ] **04.** Cross-thread context propagation is explicitly handled in asynchronous thread pools / executors.
- [ ] **05.** Standardized OpenTelemetry resource attributes (`service.name`, `service.version`, `deployment.environment`) are attached to all telemetry.
- [ ] **06.** Semantic conventions (OTel v1.26+) are strictly followed for HTTP, database, and messaging spans.
- [ ] **07.** Span creation is restricted to meaningful architectural boundaries; internal utility loops are not traced.
- [ ] **08.** Telemetry exporters use the standard OTLP protocol over gRPC with compression enabled.
- [ ] **09.** Application telemetry buffers are strictly bounded; memory limits prevent telemetry from causing OOM crashes.
- [ ] **10.** Unhealthy telemetry collector endpoints trigger graceful drop policies rather than blocking application threads.

### Section 2: Metrics & Cardinality Governance (Points 11–20)
- [ ] **11.** RED metrics (Rate, Errors, Duration) are emitted for all user-facing endpoints.
- [ ] **12.** USE metrics (Utilization, Saturation, Errors) are collected for all underlying infrastructure and pools.
- [ ] **13.** Latency is tracked via Histograms with exponential or custom buckets tailored to user SLO thresholds.
- [ ] **14.** Averages are banned from latency evaluation; 50th, 90th, 99th, and 99.9th percentiles are utilized.
- [ ] **15.** High-cardinality values (User IDs, Order IDs, UUIDs, email addresses) are strictly excluded from metric labels.
- [ ] **16.** Dynamic REST URL paths (e.g., `/api/v1/users/18294`) are normalized to parameterized templates (`/api/v1/users/{id}`).
- [ ] **17.** Business telemetry (e.g., orders placed, dollars processed) is emitted alongside technical health metrics.
- [ ] **18.** Metric naming follows standard naming conventions (`namespace_subsystem_name_unit`).
- [ ] **19.** Prometheus Exemplars are enabled, linking latency distribution buckets directly to active trace IDs.
- [ ] **20.** Total active metric series per service instance is bounded and monitored ($< 5,000$ series).

### Section 3: Structured Logging & Privacy (Points 21–30)
- [ ] **21.** All application logs are emitted in structured JSON format to `stdout`/`stderr`.
- [ ] **22.** `trace_id` and `span_id` are automatically injected into every log message via MDC/Context correlation.
- [ ] **23.** Standardized log levels (TRACE, DEBUG, INFO, WARN, ERROR, FATAL) are applied consistently.
- [ ] **24.** Production logging level is set to INFO or WARN by default; dynamic runtime level switching is enabled.
- [ ] **25.** PII, passwords, credit card numbers (PAN), and bearer tokens are automatically masked or redacted at source.
- [ ] **26.** Raw request and response bodies containing unvetted customer payloads are excluded from production logs.
- [ ] **27.** Uncaught exceptions emit full stack traces alongside structured contextual error codes.
- [ ] **28.** Log routing pipelines enforce tiered storage policies (Hot NVMe -> Warm SSD -> Cold S3/Blob -> Glacier).
- [ ] **29.** Audit logs recording security/compliance operations are isolated from high-volume operational logs.
- [ ] **30.** Logging pipelines implement backpressure and rate-limiting to prevent disk saturation during error storms.

### Section 4: Distributed Tracing & Sampling (Points 31–38)
- [ ] **31.** End-to-end trace journeys visualize the complete path from edge API gateway to database and worker queue.
- [ ] **32.** Asynchronous workflows utilize Span Links to connect decoupled producer and consumer trace segments.
- [ ] **33.** Downstream third-party external API calls are wrapped in explicit client spans with timeouts recorded.
- [ ] **34.** Intelligent Tail Sampling is deployed at the collector gateway tier (retaining 100% errors, 1-5% nominal).
- [ ] **35.** Database query spans record sanitized SQL templates; literal values and parameters are scrubbed.
- [ ] **36.** Span attributes contain rich diagnostic context (`http.status_code`, `net.peer.name`, `rpc.method`).
- [ ] **37.** Trace retention is optimized (7 days full resolution, 30 days aggregated trends) to control storage costs.
- [ ] **38.** Trace-based testing is incorporated into CI/CD pipelines to assert dependency bounds and contract rules.

### Section 5: Alerting & SRE Control Plane (Points 39–45)
- [ ] **39.** Core alerts are derived from Service Level Objectives (SLOs) and Error Budget consumption rates.
- [ ] **40.** Multi-window multi-burn-rate alerting algorithms are implemented to eliminate false positives and alert fatigue.
- [ ] **41.** Static CPU/Memory threshold alerts are demoted to non-paging warnings unless directly threatening an SLO.
- [ ] **42.** Every paging alert (SEV-1/2) is mapped to an explicit operational runbook with step-by-step triage actions.
- [ ] **43.** Alert deduplication and dependency silencing prevent cascading alert storms during upstream network cuts.
- [ ] **44.** Paging alerts route directly to the on-call engineer via dynamic team schedule integrations (PagerDuty/Opsgenie).
- [ ] **45.** Flapping alerts are automatically suppressed; alert hysteresis prevents high-frequency state oscillations.

### Section 6: Dashboards, Culture & Verification (Points 46–50)
- [ ] **46.** Hierarchical dashboard layouts exist: Executive Overview -> Service RED -> Infrastructure USE.
- [ ] **47.** Dashboards display SLO compliance targets and remaining error budget meters prominently.
- [ ] **48.** Deployment markers and configuration changes are overlaid automatically on time-series telemetry graphs.
- [ ] **49.** Chaos engineering exercises (GameDays) regularly inject faults to verify that alerts fire as engineered.
- [ ] **50.** All production outages conclude with a blameless post-mortem report and verifiable corrective actions (CAPA).
