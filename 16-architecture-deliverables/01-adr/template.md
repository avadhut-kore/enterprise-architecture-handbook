# ADR-[NUMBER]: [SHORT TITLE OF ARCHITECTURAL DECISION]

---
**Metadata**:
* **ADR ID**: ADR-[NUMBER] (e.g., ADR-0042)
* **Title**: [Concise, active-voice title, e.g., Adoption of Apache Kafka for Event Ingestion]
* **Status**: Proposed | Accepted | Rejected | Superseded | Deprecated
* **Date**: YYYY-MM-DD
* **Decision Owners**: [Lead Architect Name, Tech Lead Name]
* **Decision Reviewers**: [Security Architect, Data Architect, ARB Representative]
* **Related Requirements**: [REQ-001, NFR-004]
* **Related ADRs**: [Supersedes ADR-0012, Relates to ADR-0038]
* **Review Date**: YYYY-MM-DD (Scheduled re-evaluation date)
---

## 1. Context & Problem Statement
Describe the architectural context, business environment, and technical challenge requiring a decision.
* What business problem or technical bottleneck are we solving?
* Under what operational conditions does this problem manifest?

## 2. Business Drivers
* [Driver 1: e.g., Time-to-market for partner onboarding]
* [Driver 2: e.g., Regulatory compliance requiring 7-year auditability]

## 3. Technical Drivers
* [Driver 1: e.g., Throughput scaling from 2,000 to 25,000 events/sec]
* [Driver 2: e.g., Strict zero data loss guarantees with p99 latency < 50ms]

## 4. Constraints & Assumptions
### Constraints
* [Constraint 1: Must run on existing Kubernetes platform]
* [Constraint 2: Team must support 24/7 operations with existing staff]

### Assumptions
* [Assumption 1: Network bandwidth between availability zones is $\ge$ 10 Gbps]
* [Assumption 2: Downstream consumers support idempotent message handling]

## 5. Options Considered

### Option 1: [Option Name, e.g., Apache Kafka]
* **Overview**: [Brief description of approach]
* **Pros**:
  - High sustained throughput and partition horizontal scalability.
  - Replayable persistent event log for event sourcing and audit.
* **Cons**:
  - Operational overhead of ZooKeeper / KRaft quorum management.
  - Steeper learning curve for engineering teams.

### Option 2: [Option Name, e.g., RabbitMQ]
* **Overview**: [Brief description of approach]
* **Pros**:
  - Flexible routing keys and lightweight broker model.
  - Lower operational complexity and broad client support.
* **Cons**:
  - Throughput degradation under massive queue backlogs.
  - Does not support arbitrary historical event replay.

### Option 3: [Option Name, e.g., Managed Cloud Pub/Sub]
* **Overview**: [Brief description of approach]
* **Pros**:
  - Zero server management and automated serverless scaling.
* **Cons**:
  - Cloud vendor lock-in; higher operational costs at sustained scale.

## 6. Decision & Decision Rationale
**Chosen Option**: [Specify the selected option, e.g., Option 1: Apache Kafka]

### Rationale
Explain why this option was chosen over the others. Connect the decision directly to the business and technical drivers. Detail the exact trade-offs accepted.

## 7. Consequences & Trade-offs
### Positive Consequences
* [e.g., Decoupled microservice producers from unpredictable consumer processing speeds.]
* [e.g., Guaranteed end-to-end replayability for disaster recovery and schema migrations.]

### Negative Consequences & Accepted Technical Debt
* [e.g., Requires dedicated platform engineering investment to manage cluster health.]
* [e.g., Increases local development environment complexity (requires Docker Compose cluster).]

## 8. Security & Compliance Implications
* How is data encrypted in transit and at rest?
* How are client authentication (mTLS / SASL SCRAM) and authorization (ACLs) enforced?
* Does this decision affect PII or regulatory scope (e.g., PCI-DSS, GDPR)?

## 9. Operational & Observability Implications
* What metrics (e.g., consumer lag, partition balance) will be monitored?
* What are the disaster recovery, backup, and failover characteristics?
* What runbooks must be authored prior to production deployment?

## 10. Financial & Cost Implications
* Estimated monthly compute, storage, and networking costs: [$X / month]
* Licensing or managed service subscription liabilities: [$Y / year]

## 11. Migration & Evolution Implications
* What is the rollout strategy (e.g., dual-writing, canary rollout)?
* What is the fallback/rollback plan if performance targets are missed?

## 12. Alternatives Rejected
* **Rejected Alternative 1**: [Reason for rejection]
* **Rejected Alternative 2**: [Reason for rejection]

## 13. Related Artifacts & Links
* Architectural Diagrams: [[17-diagrams/integration/](../../17-diagrams/integration/README.md)]
* High-Level Design: [[03-hld/template.md](../03-hld/template.md)]
* System Requirements: [[14-requirements/requirements-template.md](../14-requirements/requirements-template.md)]
