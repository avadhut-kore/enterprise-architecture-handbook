# Observability & Reliability: E-Commerce Platform

## 1. Business & Technical Metrics
- **Checkout Conversion Rate**: Monitored in 1-minute sliding windows; an alert trips if conversion drops by $> 15\%$ compared to the baseline hour.
- **Cart-to-Order Abandonment Rate**: Real-time tracking of funnel drop-offs.
- **Payment Gateway P99 Latency**: Monitored per payment provider.

## 2. Site Reliability Engineering (SRE) & Chaos Resilience
- **Multi-Window Multi-Burn-Rate Alerting**: Fast burn (14.4x rate over 1 hour) for immediate paging; slow burn (3x rate over 6 hours) for ticket creation.
- **Graceful Degradation**: Shed non-essential background workloads during peak traffic spikes while keeping revenue-critical paths responsive.
- **Automated Disaster Recovery (DR)**: Periodic automated failover drills verifying RPO and RTO compliance.
