# System Design Checklist: Telemetry & Monitoring

## 1. The Three Pillars
- [ ] Distributed tracing enabled with W3C `traceparent` context propagation?
- [ ] Golden Signals tracked: Latency, Traffic (QPS), Errors (4xx/5xx), and Saturation?
- [ ] Structured JSON logging implemented with correlated `trace_id` and `user_id`?

## 2. Alerting & Dashboards
- [ ] PagerDuty alerts configured on SLO burn rates rather than noisy raw metrics?
- [ ] High-priority alerts actionable with linked runbooks?
- [ ] Executive latency dashboards (P50, P95, P99) visible on central Grafana?
