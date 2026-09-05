# Integration Metrics: RED and Golden Signals

## 1. The Four Golden Signals for Integration Pipelines
1. **Latency**: Time taken to service requests (measured in p50, p95, p99, p99.9). High tail latency indicates downstream queuing.
2. **Traffic**: Demand placed on the integration platform (HTTP requests/sec, Kafka messages/sec).
3. **Errors**: Rate of failed requests (HTTP 5xx, failed consumer offsets, schema rejections).
4. **Saturation**: How full the service is (thread pool utilization, Kafka consumer lag, DB connection pool depth).

## 2. Key Prometheus Metric Definitions
```promql
# 1. API Integration Error Rate (RED Method)
sum(rate(http_requests_total{status=~"5.."}[5m])) 
/ 
sum(rate(http_requests_total[5m])) * 100

# 2. Kafka Consumer Lag per Consumer Group
sum by (consumergroup, topic) (kafka_consumergroup_lag)

# 3. 99th Percentile Integration Latency
histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))
```

## 3. SLA and SLO Metric Tracking
Every critical enterprise integration must define an explicit Service Level Objective (SLO):
- *Example*: 99.9% of payment authorizations must complete in $< 800	ext{ms}$ over a rolling 30-day window.
