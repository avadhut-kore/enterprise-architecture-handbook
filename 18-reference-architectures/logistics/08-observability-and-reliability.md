# Observability & Fleet SRE: Logistics Platform

## 1. Supply Chain Operational Metrics
- **On-Time In-Full (OTIF)**: Core business SLA measuring percentage of shipments delivered on-time and undamaged (Target: $> 98.5\%$).
- **Geofence Processing Latency**: P99 delay between vehicle entering warehouse boundary and automated status update (Target: $< 3\text{ seconds}$).

## 2. Site Reliability Engineering (SRE) & Chaos Resilience
- **Multi-Window Multi-Burn-Rate Alerting**: Fast burn (14.4x rate over 1 hour) for immediate paging; slow burn (3x rate over 6 hours) for ticket creation.
- **Graceful Degradation**: Shed non-essential background workloads during peak traffic spikes while keeping revenue-critical paths responsive.
- **Automated Disaster Recovery (DR)**: Periodic automated failover drills verifying RPO and RTO compliance.
