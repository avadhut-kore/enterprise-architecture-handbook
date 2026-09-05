# Production Readiness Review (PRR) Checklist

The final operational quality gate executed before any service or platform is approved for production traffic cutover.

---

## 1. Capacity & Performance Verification
* [ ] **Peak Load Testing**: Has the system sustained 2x the anticipated peak traffic load for at least 4 hours with stable memory, CPU, and p99 latency?
* [ ] **Stress & Breakpoint Testing**: Has the system been driven to saturation to determine the exact failure point and verify graceful degradation?
* [ ] **End-to-End Latency Budget**: Does the p95 and p99 response time meet the contractual SLA under full synthetic load?
* [ ] **Connection Pool Limits**: Are database and HTTP client connection pools sized with headroom under max concurrent load?

---

## 2. Resiliency & Chaos Validation
* [ ] **Downstream Outage Simulation**: Has every downstream dependency (payment gateway, search cluster, email provider) been cut off to confirm graceful degradation?
* [ ] **Worker Pod Crash Testing**: Were Kubernetes pods randomly terminated during high load to verify zero-downtime recovery?
* [ ] **Circuit Breaker Tripping**: Did circuit breakers open cleanly when mock dependencies failed, preventing connection pool starvation?

---

## 3. Observability & Alerting Readiness
* [ ] **Dashboards Created**: Are operational dashboards (RED metrics, CPU/memory, database connection pool, queue lag) accessible to the on-call team?
* [ ] **SLO Alert Rules Deployed**: Are multi-window multi-burn-rate alerts configured in Prometheus / Datadog?
* [ ] **PagerDuty Escalation Configured**: Is the on-call schedule configured with a primary, secondary, and escalation manager?
* [ ] **Synthetic Probes Active**: Are synthetic health probes continuously executing key customer journeys from external regions?

---

## 4. Security & Compliance Go-Live Gates
* [ ] **SAST / DAST Vulnerabilities Resolved**: Zero `Critical` or `High` vulnerabilities remaining in application code or container images.
* [ ] **Penetration Test Sign-off**: Has the third-party or internal InfoSec penetration test been completed with all blocking findings remediated?
* [ ] **Secrets Rotated**: Have all temporary staging secrets and developer credentials been rotated before production initialization?
* [ ] **Audit Logs Streaming**: Are compliance audit events actively streaming to the immutable SIEM log store?

---

## 5. Operational Documentation & Runbooks
* [ ] **Standard Operating Procedures (SOP)**: Are runbooks documented for common failure modes (database failover, cache flushing, queue draining)?
* [ ] **Rollback Runbook**: Is there a step-by-step procedure to roll back a deployment within 10 minutes?
* [ ] **Incident Communication Plan**: Are stakeholder communication templates and incident channel configurations pre-drafted?
* [ ] **Architecture Sign-off**: Has the Solution Architect and SRE Lead signed off on production release authorization?
