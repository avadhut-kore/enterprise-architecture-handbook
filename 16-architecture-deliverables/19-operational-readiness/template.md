# Operational Readiness Review (ORR): [SYSTEM NAME]

---
**Metadata**:
```yaml
orr_id: "ORR-[PROJECT-ID]"
title: "Operational Readiness Review — [System Name]"
version: "1.0.0"
status: "Draft" # Draft | In Review | Approved | Rejected
sre_lead: "[Lead SRE Name <email>]"
lead_engineer: "[Engineering Lead Name]"
review_date: "YYYY-MM-DD"
```
---

## 1. Telemetry & Monitoring Coverage
* **RED Metrics**: Rate (req/sec), Errors (4xx/5xx count), Duration (latency histograms) configured in Prometheus.
* **Golden Signals Dashboard**: Grafana dashboard URL linked and verified.

## 2. Alerting & On-Call Rotation
* PagerDuty Service: `svc-order-processing-prod`.
* Escalation Policy: Primary On-Call (5 min ack) $ightarrow$ Secondary On-Call (10 min ack) $ightarrow$ Engineering Manager (15 min ack).

## 3. Emergency Runbooks
* [High Error Rate Runbook](runbooks.md#high-error-rate)
* [Database Connection Pool Exhaustion Runbook](runbooks.md#db-exhaustion)
* [Kafka Consumer Lag Spike Runbook](runbooks.md#kafka-lag)

## 4. SRE Sign-Off
* [ ] All telemetry metrics verified active in Staging environment.
* [ ] SRE team successfully completed shadow on-call drill.
* **SRE Lead Sign-Off**: ___________________________ Date: _________
