# Production Readiness Review (PRR) Mastery

No service should be deployed to enterprise production without completing a rigorous Production Readiness Review (PRR).

## 1. The PRR Checklist Dimensions

### A. Observability & Telemetry
- [ ] Structured JSON logging with correlation/trace IDs propagated across all HTTP/gRPC headers.
- [ ] Prometheus metrics exposed for golden signals: Latency, Traffic, Errors, Saturation (USE/RED).
- [ ] Pre-configured Grafana dashboard displaying p50, p95, and p99 latencies.
- [ ] PagerDuty alerts configured with actionable runbooks linked directly in the alert payload.

### B. Resilience & Degradation
- [ ] Client timeouts configured on all downstream HTTP/database calls (Max timeout <= 1000ms).
- [ ] Exponential backoff with jitter enabled on all retries.
- [ ] Circuit breaker implemented for non-critical dependencies with automated fallback state.
- [ ] Health checks (`/health/live` and `/health/ready`) decoupled from downstream dependencies.

### C. Capacity & Scaling
- [ ] Load testing executed to 2x expected peak traffic in staging environment.
- [ ] Horizontal Pod Autoscaler (HPA) configured with scale-up and scale-down stabilization windows.
- [ ] Database connection pooling configured with strict upper limits.

### D. Security & Compliance
- [ ] Vulnerability scanning passed with 0 Critical and 0 High CVEs in dependencies and base container images.
- [ ] Secrets retrieved from HashiCorp Vault / AWS Secrets Manager; zero hardcoded credentials.
- [ ] Network policies restrict ingress/egress to explicitly whitelisted services.

## Related Modules
- [Observability Architecture](../../11-observability/README.md)
- [Security Architecture](../../10-security/README.md)
