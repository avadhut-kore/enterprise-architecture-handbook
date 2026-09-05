# Checklist 01: Service Observability Readiness (PRR Gate)

## 1. Overview
This checklist forms the mandatory **Production Readiness Review (PRR)** gate for any microservice or application prior to promoting to production. A service cannot be onboarded to production without a 100% passing score on critical items.

---

## 2. Verification Rubric

| Category | Verification Item | Standard / Expected Artifact | Criticality | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| **Metrics** | Golden Signals Implemented | RED metrics (Rate, Errors, Duration) emitted for all public APIs. | **BLOCKER** | [ ] |
| **Metrics** | Runtime Health Exposed | Language runtime metrics exposed (JVM GC / Go Goroutines / Node EventLoop). | High | [ ] |
| **Metrics** | Zero Unbounded Labels | Metric definitions verified free of `user_id`, `email`, or dynamic UUIDs. | **BLOCKER** | [ ] |
| **Tracing** | Context Propagation | Service extracts incoming W3C `traceparent` and injects into downstream calls. | **BLOCKER** | [ ] |
| **Tracing** | Semantic Attributes | Spans adhere to OpenTelemetry Semantic Conventions (HTTP, DB, RPC). | High | [ ] |
| **Logging** | Structured JSON | Logs emitted in structured JSON conforming to corporate ECS schema. | **BLOCKER** | [ ] |
| **Logging** | Context Injected | Every log line automatically includes `trace_id` and `span_id`. | **BLOCKER** | [ ] |
| **Logging** | Zero Secrets / PII | Log outputs verified clean of passwords, auth headers, and customer PII. | **BLOCKER** | [ ] |
| **Alerting** | Service SLO Defined | At least one Availability SLO and one Latency SLO defined with Product. | **BLOCKER** | [ ] |
| **Alerting** | Multi-Burn Alerts | Multi-window multi-burn rate alerts configured in Alertmanager. | High | [ ] |
| **Alerting** | Actionable Runbook | Every firing alert links directly to a validated operational runbook URL. | **BLOCKER** | [ ] |
| **Dashboard**| Tier-1 Service Dashboard | Golden signals dashboard created using standard corporate Grafana template. | High | [ ] |
| **Health**   | Health Check Endpoints | `/healthz` (liveness) and `/ready` (readiness) implemented cleanly. | **BLOCKER** | [ ] |
