# Alerting Rules and Runbooks for Integration SRE

## 1. Alerting Philosophy: Alert on Symptoms, Not Causes
Do not wake up on-call engineers because "CPU is 85%". Alert when user-facing SLAs or business transactions are failing:
- **P1 (Critical - Page Immediately)**: Error rate $> 2\%$ for 5 minutes, Core Banking API down, Consumer lag growing $> 100,000$ messages.
- **P2 (Major - Notify within 30 min)**: DLQ depth $> 50$, Circuit breaker open for $> 5$ minutes, Partner webhook latency $> 3000	ext{ms}$.
- **P3 (Minor - Ticket for Next Business Day)**: High storage utilization on staging broker, non-critical telemetry stream delayed.

## 2. Production Prometheus Alert Rules
```yaml
groups:
- name: integration-alerts
  rules:
  - alert: CoreBankingIntegrationDown
    expr: sum(rate(http_requests_total{service="core-banking-bridge", status=~"5.."}[5m])) / sum(rate(http_requests_total{service="core-banking-bridge"}[5m])) > 0.05
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: "Core banking integration error rate exceeded 5%"
      runbook_url: "https://wiki.enterprise.internal/runbooks/core-banking-bridge-outage"

  - alert: KafkaConsumerGroupLagSpike
    expr: kafka_consumergroup_lag{consumergroup="payment-clearing"} > 50000
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Payment clearing consumer lag exceeded 50,000 records"
      runbook_url: "https://wiki.enterprise.internal/runbooks/kafka-clearing-lag"
```
