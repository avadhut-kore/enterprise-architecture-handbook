# Enterprise Integration Operational Dashboards

## 1. Dashboard Taxonomy
1. **Tier 1: Global Platform Health (NOC / Executive)**:
   - Total transactional throughput (TPS).
   - Platform-wide error rate (% 5xx).
   - Overall p99 latency gauge.
   - Active critical incident counter.
2. **Tier 2: System-Specific Ingress & Integration (SRE)**:
   - Kafka consumer group lag by topic.
   - API Gateway rate limit rejections (HTTP 429).
   - Circuit breaker states (Open / Half-Open / Closed).
   - Thread pool and database connection saturation.
3. **Tier 3: Partner & Vendor Health (Operations)**:
   - Third-party SaaS availability (Salesforce, SAP, SWIFT).
   - Outbound webhook delivery success rate.
   - DLQ queue depths and pending reconciliation breaks.
