# Tenant Monitoring & Observability

## 1. High-Cardinality Tenant Telemetry
* **Tagging Strategy**: Tag every metric, log, and distributed trace with `tenant_id`.
* **Cardinality Protection**: To avoid Prometheus TSDB crashes, aggregate tenant metrics into percentiles or tier-based summaries at the edge collector.
