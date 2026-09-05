# Solution Architecture Quality Checklist

Use this checklist during the design phase of a Solution Architecture Document (SAD) to ensure all dimensions of the solution are rigorously addressed.

---

## 1. Solution Completeness & Scope
* [ ] **Business Problem Addressed**: Does the SAD explicitly solve the primary business need without unnecessary scope creep?
* [ ] **C4 Visuals Provided**: Are Level 1 (System Context) and Level 2 (Container Topology) diagrams complete, unambiguous, and compliant with C4 standards?
* [ ] **Interface Contracts Defined**: Are all ingress and egress APIs defined using OpenAPI 3.1, Protobuf, or GraphQL schemas?
* [ ] **Data Flow Sequences**: Are critical transactional workflows documented with sequence diagrams detailing happy paths and failure branches?

---

## 2. Distributed Systems & Integration
* [ ] **Idempotency Guarantees**: Do all mutating operations support idempotency keys to handle client-side retries safely?
* [ ] **Asynchronous Decoupling**: Are non-critical operations (email alerts, analytical updates, third-party sync) offloaded to asynchronous message queues?
* [ ] **Poison Message Handling**: Are Dead Letter Queues (DLQs) configured with automated alerts and reprocessing mechanisms?
* [ ] **Contract Versioning**: Does the API design enforce backward compatibility and explicit semantic versioning policies?

---

## 3. Data Integrity & Persistence
* [ ] **Storage Engine Justification**: Is the choice between Relational, Document, Key-Value, or Distributed SQL explicitly justified based on query patterns?
* [ ] **Indexing Hygiene**: Are all high-cardinality filters and join columns indexed? Are unused indexes purged?
* [ ] **Consistency Model Stated**: Is the consistency model (Strict Serializable vs. Eventual Consistency) documented and acceptable to product stakeholders?
* [ ] **Lifecycle & Archival**: Are data retention, purge, and cold-storage archival policies defined to control long-term database bloat?

---

## 4. Security & Privacy
* [ ] **Least Privilege Access**: Are database users, cloud IAM roles, and service accounts scoped strictly to the minimum required permissions?
* [ ] **Data Encryption**: Is data encrypted at rest (AES-256) and in transit (TLS 1.3)?
* [ ] **PII Protection**: Is sensitive PII protected via application-level envelope encryption or cryptographic erasure tokens?
* [ ] **Input Sanitization**: Is every inbound payload validated against a strict schema to prevent injection attacks (SQLi, XSS, SSRF)?

---

## 5. Operability & Disaster Recovery
* [ ] **RPO & RTO Adherence**: Does the data replication and backup architecture comfortably meet the target Recovery Point and Recovery Time objectives?
* [ ] **Health Probes**: Are distinct liveness (`/livez`) and readiness (`/readyz`) probes implemented correctly?
* [ ] **Zero-Downtime Deployment**: Can the solution be deployed via Canary or Blue/Green rollouts without dropping active customer connections?
* [ ] **SRE Runbook Created**: Has an initial troubleshooting guide been drafted for on-call engineers?
