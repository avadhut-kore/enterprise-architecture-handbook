# Checklist 05: Logging Maturity & Schema Adherence Audit

## 1. Overview
Evaluates application logging practices for machine-readability, standardized schemas, level discipline, and compliance data sanitization.

---

## 2. Verification Rubric

| Audit Check | Requirement | Pass/Fail |
| :--- | :--- | :--- |
| **Structured Output** | 100% of logs emitted as single-line structured JSON (no raw stdout multiline text). | [ ] |
| **Schema Conformity** | Core keys conform to ECS (`@timestamp`, `log.level`, `service.name`, `message`). | [ ] |
| **Trace Correlation** | Logs contain active `trace_id` and `span_id` fields whenever executed within a trace context. | [ ] |
| **Level Discipline** | Default production level set to `INFO`; `DEBUG`/`TRACE` strictly prohibited in steady state. | [ ] |
| **Exception Formats** | Stack traces serialized into structured `error.stack_trace` string blocks rather than split lines. | [ ] |
| **PII / Secret Masking**| Credit cards, passwords, authorization tokens, and national IDs automatically redacted. | [ ] |
| **Health Probe Silence**| `/healthz` and `/ready` probes filtered out from production access logs. | [ ] |
| **Rate Limiting** | Error logger employs token-bucket rate limiting to prevent disk exhaustion during loops. | [ ] |
