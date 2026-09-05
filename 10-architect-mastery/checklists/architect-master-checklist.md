# Architect Master Checklist: The 100-Point Review

Use this checklist during architecture design phases, ARB reviews, and pre-production gates.

### 1. Requirements & Discovery
- [ ] 1. Are business capabilities clearly identified?
- [ ] 2. Are measurable SLOs defined (p95, p99 latency, availability)?
- [ ] 3. Are scale projections calculated (QPS, storage over 3 years)?
- [ ] 4. Are hard vs soft constraints explicitly documented?

### 2. Data & Storage
- [ ] 5. Is there a single, clear source of truth for each entity?
- [ ] 6. Are database connection pool limits strictly configured?
- [ ] 7. Are queries verified with EXPLAIN plans to avoid table scans?
- [ ] 8. Is data retention and purging policy defined?
- [ ] 9. Are backups automated and restoration verified in staging?

### 3. Distributed Communication & APIs
- [ ] 10. Are all inter-service client timeouts set <= 1000ms?
- [ ] 11. Are exponential backoff and randomized jitter implemented?
- [ ] 12. Are circuit breakers configured for external dependencies?
- [ ] 13. Are API contracts versioned and backwards-compatible?
- [ ] 14. Are idempotency keys required on all non-idempotent write APIs?

### 4. Security & Compliance
- [ ] 15. Is mTLS or zero-trust identity enforced between services?
- [ ] 16. Are secrets injected dynamically from Vault/Secrets Manager?
- [ ] 17. Is data encrypted at rest and in transit (AES-256 / TLS 1.3)?
- [ ] 18. Are PII attributes isolated and tagged for GDPR compliance?

### 5. Observability & SRE
- [ ] 19. Are OpenTelemetry trace IDs propagated in headers?
- [ ] 20. Are Prometheus metrics exposed for golden signals (RED/USE)?
- [ ] 21. Are PagerDuty alerts configured with direct runbook links?
- [ ] 22. Are health checks decoupled from downstream dependencies?

### 6. Resilience & Disaster Recovery
- [ ] 23. Is RPO and RTO defined and tested?
- [ ] 24. Does the system survive single-AZ outage automatically?
- [ ] 25. Is cell-based architecture or bulkheading in place?
- [ ] 26. Has an architectural pre-mortem been conducted?

## Related Modules
- [Production Readiness Review](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/operations/production-readiness-review-mastery.md)
- [Enterprise Failure Modes](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/failure-analysis/enterprise-failure-modes-post-mortems.md)
