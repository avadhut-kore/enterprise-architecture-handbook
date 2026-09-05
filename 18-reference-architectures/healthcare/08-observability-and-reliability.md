# Observability & Clinical Reliability: Healthcare Platform

## 1. SRE Golden Signals for Healthcare
- **HL7 Ingestion Queue Depth**: Alert if queue depth $> 500$ messages or processing delay $> 30\text{ seconds}$.
- **Clinical Chart Fetch Latency**: 99% of chart summaries rendered in $< 200\text{ ms}$.
- **Emergency Code DR RTO**: Disaster recovery RTO $< 15\text{ minutes}$ for life-critical inpatient systems.

## 2. Site Reliability Engineering (SRE) & Chaos Resilience
- **Multi-Window Multi-Burn-Rate Alerting**: Fast burn (14.4x rate over 1 hour) for immediate paging; slow burn (3x rate over 6 hours) for ticket creation.
- **Graceful Degradation**: Shed non-essential background workloads during peak traffic spikes while keeping revenue-critical paths responsive.
- **Automated Disaster Recovery (DR)**: Periodic automated failover drills verifying RPO and RTO compliance.
