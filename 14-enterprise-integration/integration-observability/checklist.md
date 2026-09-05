# Enterprise Integration Observability Review Checklist

## Logging & Tracing
- [ ] Are all integration logs emitted in structured JSON format according to corporate schema?
- [ ] Are all PII, tokens, and credit card numbers redacted before log serialization?
- [ ] Is W3C Trace Context (`traceparent`) propagated through all HTTP, gRPC, and Kafka hops?
- [ ] Does every cross-system transaction carry a persistent Correlation ID?

## Metrics & Alerting
- [ ] Are RED metrics (Rate, Errors, Duration) collected for every integration endpoint?
- [ ] Is Kafka consumer group lag continuously tracked and alerted on?
- [ ] Are alerting rules tied to business impacts and actionable runbooks?

## Auditing & Governance
- [ ] Are all Dead Letter Queues instrumented with real-time depth alerting?
- [ ] Is end-of-day reconciliation monitored with aging break alerts?
- [ ] Are immutable, tamper-evident audit logs preserved on WORM storage for regulated flows?
