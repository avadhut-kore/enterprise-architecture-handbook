# Senior Engineer Production Readiness Checklist

> **"Hope is not a production strategy. Production readiness is the disciplined verification that a subsystem can withstand traffic spikes, network drops, database locks, and human operational error."**

---

## 1. Architectural & Schema Integrity
- [ ] **Accepted ADR**: Is there a merged Architecture Decision Record documenting the technical choice, rejected alternatives, and trade-offs?
- [ ] **Backward/Forward Compatibility**: Are API payload schemas (Protobuf/JSON) and database migrations strictly backward compatible?
- [ ] **Zero-Lock DDL**: Do database migrations avoid table-level write locks on high-traffic tables (e.g., using `CONCURRENTLY` in Postgres)?

---

## 2. Telemetry, Observability & SLOs
- [ ] **The Three Pillars Instrumented**:
  - Structured JSON logs contain unified correlation IDs (`trace_id`, `span_id`).
  - Prometheus metrics implement the RED method (Rate, Errors, Duration) with bounded cardinality.
  - OpenTelemetry distributed trace context propagates cleanly over outgoing HTTP/gRPC and Kafka messages.
- [ ] **SLO Dashboard Active**: Is there a live production dashboard tracking customer-facing SLIs against agreed error budgets?
- [ ] **Actionable Alerting**: Do alerts fire *only* on user-facing SLO degradation or rapid error budget burn rates?

---

## 3. Resilience & Fault Tolerance
- [ ] **Bulkheads Configured**: Are outbound HTTP client connection pools and thread pools bounded and isolated per dependency?
- [ ] **Circuit Breakers & Retries**: Do external calls implement circuit breakers and exponential backoff with full jitter?
- [ ] **Graceful Degradation**: Does the service degrade gracefully (returning cached data or friendly warnings) if downstream services fail?

---

## 4. Operational Runbooks & Deployment Safety
- [ ] **Operational Runbook**: Is there a step-by-step markdown runbook in the repository root linked directly from PagerDuty alerts?
- [ ] **Automated Rollback Strategy**: Is the canary deployment configured with automated rollback triggers if 5xx errors exceed 0.5%?
- [ ] **On-Call Handover**: Has the team completed an operational walk-through before the service is placed on primary on-call rotation?
