# Enterprise Integration Architecture Checklist

This checklist provides a structured 25-point evaluation for enterprise integration topologies, API contracts, and message fabrics.

## 1. Coupling & Architectural Style
- [ ] Are direct point-to-point connections avoided in favor of API gateways or event brokers?
- [ ] Is synchronous call depth minimized (no cascading $A ightarrow B ightarrow C ightarrow D$ chains)?
- [ ] Are long-running or batch operations decoupled using asynchronous publish-subscribe messaging?
- [ ] Is an Event-Carried State Transfer (ECST) pattern considered to prevent query callbacks?

## 2. API Contract & Versioning Governance
- [ ] Are all API contracts explicitly documented using OpenAPI 3.0 or Protobuf specifications?
- [ ] Is backward compatibility enforced (no breaking field deletions without major version deprecation)?
- [ ] Are APIs versioned cleanly via URI path (`/v1/`) or content negotiation headers?
- [ ] Is a Schema Registry used to enforce schema evolution across event topics?

## 3. Resilience, Fault Tolerance & SLAs
- [ ] Are timeouts, retries with exponential backoff, and circuit breakers configured on all remote calls?
- [ ] Are Dead Letter Queues (DLQ) configured for all messaging consumers with alerting?
- [ ] Are rate limits and throttling policies implemented at the API Gateway to prevent service exhaustion?
- [ ] Are mutual TLS (mTLS) certificates enforced for all B2B and internal inter-service integrations?
