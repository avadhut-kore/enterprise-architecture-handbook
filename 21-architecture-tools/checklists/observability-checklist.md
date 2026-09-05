# Observability & Site Reliability Engineering (SRE) Checklist

Verify that distributed services possess comprehensive telemetry coverage across logs, metrics, distributed traces, and intelligent alerting.

---

## 1. Structured Logging Standards
* [ ] **Structured JSON Format**: Are all application logs serialized as machine-parseable JSON lines? Plaintext log formats prohibited.
* [ ] **Standard Correlation Headers**: Does every log record include `trace_id`, `span_id`, `service_name`, `version`, `environment`, and `tenant_id`?
* [ ] **Appropriate Log Levels**: Are log levels configured correctly (`ERROR` actionable failures, `WARN` unexpected state, `INFO` lifecycle milestones, `DEBUG` development only)?
* [ ] **PII & Credential Masking**: Are passwords, credit card numbers, authorization headers, and sensitive PII scrubbed before emitting logs?
* [ ] **Log Retention & Sampling**: Are high-volume debug logs sampled and auto-purged after 14 days to prevent storage cost explosion?

---

## 2. Metrics & The Golden Signals
* [ ] **RED Method Implemented**:
  * **Rate**: Request rate (RPS) tracked per endpoint and status code.
  * **Errors**: Error count and percentage of 4xx/5xx responses.
  * **Duration**: Latency distributions exposed as histograms (p50, p90, p95, p99).
* [ ] **USE Method for Infrastructure**: Are Utilization, Saturation, and Errors tracked for CPU, RAM, Disk I/O, and Network interfaces?
* [ ] **Custom Business Metrics**: Are domain KPIs exposed (e.g., `orders_placed_total`, `payment_failures_total`, `active_websocket_connections`)?
* [ ] **Prometheus Scraping Standards**: Do applications expose a standard `/metrics` endpoint protected from public internet exposure?

---

## 3. Distributed Tracing (OpenTelemetry)
* [ ] **W3C Trace Context**: Is `traceparent` context propagated across all HTTP, gRPC, and Kafka boundaries?
* [ ] **Database & Cache Spans**: Are SQL queries and Redis commands instrumented with sanitized query statements and execution latencies?
* [ ] **Downstream Client Spans**: Are calls to third-party APIs tracked with individual spans capturing HTTP status and network latency?
* [ ] **Trace Sampling Strategy**: Is tail-based or probabilistic head-based sampling configured (e.g., sample 100% of errors and 5% of successful requests) to control data volume?

---

## 4. Alerting & SLO Governance
* [ ] **Multi-Window Multi-Burn-Rate Alerts**: Are alerts based on SLO error budget burn rates rather than brittle static threshold spikes?
* [ ] **Actionable Alert Descriptions**: Does every alert include a direct link to the corresponding SRE triage runbook and Grafana dashboard?
* [ ] **No Alert Fatigue**: Are non-actionable warnings categorized as informational tickets rather than paging on-call engineers at night?
* [ ] **Silent Failure Detection**: Are synthetic health probes continuously validating that transactions are actually completing end-to-end?

---

## 5. Dashboards & Incident Triage
* [ ] **Standard Service Dashboard**: Does every service have a standard Grafana / Datadog dashboard displaying RED metrics, error rates, and pod resource saturation?
* [ ] **Dependency Topology View**: Is a live service dependency map generated automatically from distributed traces?
* [ ] **Pre-Configured Rollback Triggers**: Are automated alerts linked to deployment tools (ArgoCD / Spinnaker) to trigger automatic rollbacks when canary metrics breach thresholds?
