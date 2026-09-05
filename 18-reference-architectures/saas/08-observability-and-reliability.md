# Observability & Per-Tenant SLIs: SaaS Platform

## 1. Tenant-Aware Metrics & Golden Signals
- Every Prometheus metric includes `tenant_id` as a label: `http_requests_total{tenant_id="acme", status="200"}`.
- Automated anomaly detection identifies tenants that consume $> 40\%$ of shared database connection pool capacity, triggering automated throttling.

## 2. Site Reliability Engineering (SRE) & Chaos Resilience
- **Multi-Window Multi-Burn-Rate Alerting**: Fast burn (14.4x rate over 1 hour) for immediate paging; slow burn (3x rate over 6 hours) for ticket creation.
- **Graceful Degradation**: Shed non-essential background workloads during peak traffic spikes while keeping revenue-critical paths responsive.
- **Automated Disaster Recovery (DR)**: Periodic automated failover drills verifying RPO and RTO compliance.
