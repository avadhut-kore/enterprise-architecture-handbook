# Microservices Architecture Readiness Checklist

Verify that proposed or existing microservices architectures avoid common distributed traps, tight coupling, and operational bloat.

---

## 1. Domain Decomposition & Service Boundaries
* [ ] **Bounded Context Alignment**: Does the microservice align with a single business capability / bounded context?
* [ ] **Database per Service**: Does each microservice own its private database schema? Are direct cross-service database queries strictly forbidden?
* [ ] **Independent Deployability**: Can this service be deployed, tested, scaled, and rolled back independently without coordinating releases with other services?
* [ ] **Team Ownership**: Is there a single, clearly identifiable engineering squad responsible for the service throughout its lifecycle?

---

## 2. Distributed Communication & Decoupling
* [ ] **Avoid Deep Synchronous Chaining**: Are deep synchronous HTTP call chains (`A -> B -> C -> D`) avoided to prevent latency amplification and brittle dependencies?
* [ ] **Event-Driven Choreography / Orchestration**: Are cross-domain workflows coordinated via Kafka/RabbitMQ events or dedicated Saga orchestrators?
* [ ] **Contract Testing**: Are Pact or OpenAPI contract tests automated in the CI pipeline to prevent breaking downstream consumers?
* [ ] **Circuit Breakers & Timeouts**: Does every external outbound network call use an explicit circuit breaker and bounded connection/read timeouts?

---

## 3. Data Consistency & Transactions
* [ ] **Saga Pattern Implemented**: Are multi-service business transactions managed via Sagas with defined compensating transactions for failure scenarios?
* [ ] **Transactional Outbox Pattern**: Are domain events published reliably using an Outbox table or CDC (Debezium) rather than dual writes?
* [ ] **Idempotent Message Processing**: Can consumers safely process duplicate messages without corrupting business state?
* [ ] **Eventual Consistency Accepted**: Have product stakeholders formally agreed to eventual consistency latency windows?

---

## 4. Observability & SRE in Distributed Systems
* [ ] **Distributed Trace Propagation**: Is W3C `traceparent` passed across all HTTP headers, gRPC metadata, and Kafka record headers?
* [ ] **Unified Log Aggregation**: Do logs include `trace_id`, `span_id`, `service_name`, and `environment`?
* [ ] **Service Mesh / Ingress Metrics**: Are service-level RED metrics (Rate, Error, Duration) automatically scraped and displayed on Grafana dashboards?
* [ ] **Synthetic Probing**: Are synthetic user journeys periodically probing cross-service critical paths?

---

## 5. Security & Infrastructure
* [ ] **Mutual TLS (mTLS)**: Is all inter-service (east-west) traffic encrypted and authenticated via mTLS?
* [ ] **Service Identity (SPIFFE)**: Are service identities cryptographically verifiable with short-lived x509 certificates?
* [ ] **Container Hardening**: Are containers running as non-root on minimal or distroless base images?
* [ ] **Horizontal Pod Autoscaling (HPA)**: Are HPA rules defined based on custom business metrics or CPU/Memory thresholds?
