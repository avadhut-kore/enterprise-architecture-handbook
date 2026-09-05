# Enterprise Observability Checklists & Operational Audits

## Executive Summary

Observability is not a passive installation; it is an active operational discipline. Systems drift, microservices proliferate, new developers introduce un-vetted labels, and production alerts decay into meaningless noise without systematic governance.

This directory provides **12 specialized, production-grade audit checklists** designed for Architecture Review Boards (ARB), Site Reliability Engineers (SRE), Platform Teams, and Engineering Squads to verify telemetry readiness, compliance, cost efficiency, and incident resilience.

---

## Checklists Directory Index

| Checklist | Target Audience | Primary Focus |
| :--- | :--- | :--- |
| **[`01-observability-readiness.md`](01-observability-readiness.md)** | Tech Leads / Squads | Production Readiness Review (PRR) gate before deploying any new service. |
| **[`02-alerting-quality.md`](02-alerting-quality.md)** | SRE Leads / Incident Mgrs | Auditing alerting hygiene, eliminating fatigue, and validating burn-rate math. |
| **[`03-dashboard-usability.md`](03-dashboard-usability.md)** | UI/UX / Platform Leads | Cognitive ergonomics, visual hierarchy, and 5-second incident comprehension. |
| **[`04-distributed-tracing-audit.md`](04-distributed-tracing-audit.md)** | Distributed Systems Eng | Context propagation continuity, span semantic conventions, and tail sampling. |
| **[`05-logging-maturity.md`](05-logging-maturity.md)** | App Leads / SecOps | Structured JSON, schema conformity, level discipline, and sensitive data masking. |
| **[`06-metric-cardinality-audit.md`](06-metric-cardinality-audit.md)** | Platform Eng / SRE | Identifying runaway time series, label entropy, and Prometheus crash prevention. |
| **[`07-slo-implementation.md`](07-slo-implementation.md)** | Product Managers / SRE | User journey identification, SLI formulation, and error budget governance. |
| **[`08-incident-response-readiness.md`](08-incident-response-readiness.md)** | Incident Commanders / On-Call | Runbook coverage, diagnostic tool access, paging escalation, and blameless post-mortems. |
| **[`09-finops-telemetry-cost.md`](09-finops-telemetry-cost.md)** | FinOps / Engineering Directors | Telemetry ROI, tiered storage policies, downsampling, and license optimizations. |
| **[`10-security-compliance-telemetry.md`](10-security-compliance-telemetry.md)** | CISO / Privacy Officers | Zero PII/PAN/PHI, mTLS transport encryption, RBAC, and immutable audit trails. |
| **[`11-chaos-game-day-observability.md`](11-chaos-game-day-observability.md)** | Chaos Eng / Resiliency Leads | Validating telemetry fidelity, alert firing, and runbooks under active failure injection. |
| **[`12-ai-llm-observability.md`](12-ai-llm-observability.md)** | AI/ML Engineers / GenAI Leads | LLMOps telemetry readiness, token cost attribution, vector drift, and prompt injection defense. |
