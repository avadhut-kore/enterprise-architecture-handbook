# 22 Enterprise Integration Anti-Patterns

Avoid these 22 costly architectural traps when designing enterprise integrations:

1. **Point-to-Point Mesh (Integration Spaghetti)**: Direct connections between systems multiply exponentially, creating an unmaintainable web where changing one system breaks ten others.
2. **The Giant Monolithic ESB**: Concentrating all enterprise business logic, orchestration, and validation inside a heavyweight ESB, recreating a single point of failure and organizational bottleneck.
3. **Universal Canonical Model**: Spending years attempting to standardize every corporate concept into a single enterprise schema before building any working software.
4. **Synchronous Chain of Death**: Microservice A calls B, which calls C, which calls D synchronously over HTTP. If D takes 800ms, A times out; if C restarts, the entire customer flow dies.
5. **Shared Database Integration**: Two autonomous systems reading and writing to the same database tables, creating invisible coupling and preventing schema migrations.
6. **No System of Record (Split-Brain Mutation)**: Allowing Customer records to be mutated independently in CRM, ERP, and Portal without a single authoritative source of truth.
7. **Undocumented API Contracts**: Exposing JSON payloads with no versioned OpenAPI or JSON Schema specification, forcing consumers to guess field types and nullability.
8. **Blind Retries Without Backoff**: Retrying failed HTTP requests immediately in a tight loop, creating a self-inflicted DDoS attack (retry storm) against a struggling downstream server.
9. **Infinite Retries on Poison Pills**: Retrying malformed payloads that will never succeed, permanently blocking a queue partition and starving valid transactions.
10. **Assuming "Exactly-Once" Transport**: Believing network protocols guarantee exactly-once delivery without implementing application-level idempotency keys.
11. **Missing Business Correlation IDs**: Logging generic messages without injecting and propagating W3C `traceparent` and `X-Correlation-ID` across distributed service hops.
12. **The Event Dumping Ground**: Publishing massive, uncurated internal database row dumps into Kafka topics without schema governance or privacy filtering.
13. **Ignoring Automated Reconciliation**: Assuming that message queues never drop records and discovering financial imbalances weeks later during an audit.
14. **Over-Engineering with Distributed Sagas**: Implementing complex 5-step distributed transaction sagas for simple workflows where asynchronous event choreography would suffice.
15. **Treating Legacy as Disposable**: Assuming a 30-year-old core mainframe can be ripped and replaced in 6 months without planning a multi-year Strangler Fig coexistence architecture.
16. **Leaking Sensitive PII Across Boundaries**: Transmitting raw credit card PANs or SSNs across internal messaging topics where unauthorized microservices can ingest them.
17. **Hardcoding Vendor Endpoints**: Embedding vendor-specific URLs, API keys, or proprietary schemas directly into application code rather than abstracting them behind an Anti-Corruption Layer.
18. **Unbounded Webhook Ingestion**: Ingesting third-party webhooks directly into synchronous database writes without queue buffering or HMAC signature verification.
19. **Mixing OLTP and OLAP on the Same Pipeline**: Forcing multi-gigabyte analytical batch files through real-time transactional messaging brokers.
20. **Unchecked Schema Drift**: Modifying producer schemas by renaming or removing fields without automated schema registry backward-compatibility validation.
21. **No Circuit Breaking**: Continuing to pummel an unresponsive downstream integration until all application server worker threads are exhausted.
22. **Documentation-Free Governance Gates**: Imposing bureaucratic architecture review gates that demand massive paperwork without providing copyable templates or automated linting tools.
