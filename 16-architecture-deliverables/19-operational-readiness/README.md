# 19-OPERATIONAL-READINESS: Operational Readiness Review (ORR) Framework

## 1. Overview & Purpose
The **Operational Readiness Review (ORR)** answers the decisive SRE question:

> **"Can the operations and SRE organization safely run, monitor, support, and troubleshoot this system in production?"**

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Operational Readiness Review packet.
* **Operational Disciplines**:
  - [monitoring.md](monitoring.md) — Prometheus metrics, node exporters, and RED/USE methods.
  - [alerting.md](alerting.md) — Alert thresholds, routing, and alert fatigue reduction.
  - [logging.md](logging.md) — Centralized JSON structured logging and PII masking.
  - [tracing.md](tracing.md) — OpenTelemetry distributed tracing and span context propagation.
  - [dashboards.md](dashboards.md) — Grafana executive and service-level dashboards.
  - [runbooks.md](runbooks.md) — Standard operating procedures and emergency runbooks.
  - [on-call.md](on-call.md) — PagerDuty rotation schedules and escalation policies.
  - [incident-management.md](incident-management.md) — P1/P2 severity definitions and post-mortem guidelines.
  - [capacity.md](capacity.md) — Headroom monitoring and seasonal capacity planning.
  - [backup.md](backup.md) — Operational backup verification and restore tests.
  - [recovery.md](recovery.md) — Self-healing liveness probes and restart policies.
  - [support-model.md](support-model.md) — Tier 1 / Tier 2 / Tier 3 support boundaries.
  - [checklist.md](checklist.md) — 20-Point Operational Readiness Review Checklist.
