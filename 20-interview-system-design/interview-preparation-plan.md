# Architect Interview Preparation Plan & Decision Journal

> A structured curriculum roadmap (4, 8, and 12 weeks), self-assessment skill matrix, and continuous learning interview decision journal.

---

## 1. Structured Preparation Tracks

```
        4-Week Fast Track                8-Week Comprehensive Track             12-Week Mastery Track
  (Senior SDE / Fast Refresher)         (Staff / Solution Architect)        (Principal / Enterprise Architect)
┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐
│ W1: Frameworks & Estimation  │     │ W1-2: Foundations & Scale    │     │ W1-3: Distributed Core & NFRs│
│ W2: Core System Design Cases │     │ W3-4: Storage & Trade-Offs   │     │ W4-6: Enterprise Architecture│
│ W3: Trade-Offs & Reliability │     │ W5-6: Resilience & Security  │     │ W7-9: Leadership & Incidents │
│ W4: Mock Interviews & Polish │     │ W7-8: Leadership & Cases     │     │ W10-12: Mocks, TCO & Strategy│
└──────────────────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘
```

### The 8-Week Standard Curriculum (Staff / Solution Architect)
* **Week 1: Methodology & Estimation**
  * Master the **A-D-A-P-T** framework ([`architect-interview-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architect-interview-framework.md)).
  * Practice back-of-the-envelope calculations daily ([`estimation/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/README.md)).
* **Week 2: High-Throughput & Stateless Systems**
  * Study URL Shortener, Notification Engine, and Distributed Rate Limiters.
  * Deep dive into caching strategies, CDN offload, and API Gateways.
* **Week 3: Stateful & Distributed Storage**
  * Relational vs NoSQL vs NewSQL trade-offs ([`tradeoffs/data.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/data.md)).
  * Partitioning, consistent hashing, replication, and CAP/PACELC consistency models.
* **Week 4: Messaging & Event-Driven Architectures**
  * Message queues (RabbitMQ/SQS) vs. distributed logs (Kafka).
  * Saga patterns (Orchestration vs Choreography), Outbox pattern, and idempotency.
* **Week 5: Enterprise Depth, Security & Observability**
  * Zero Trust architecture, OAuth2/OIDC, mTLS, encryption at rest/in transit.
  * Distributed tracing (OpenTelemetry), RED metrics, and SLO error budgets.
* **Week 6: Reliability, Resilience & Disaster Recovery**
  * Circuit breakers, bulkheads, exponential backoff, rate limiting, and failover.
  * Multi-AZ and multi-region active-active architectures ([`tradeoffs/cloud.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/cloud.md)).
* **Week 7: Leadership, Governance & Incidents**
  * Technical disagreement, stakeholder alignment, and Conway's Law ([`leadership/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/README.md)).
  * Production outage simulations and RCA ([`scenario-based/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/scenario-based/README.md)).
* **Week 8: Timed Mock Interviews & Polish**
  * Conduct four 45-minute timed mock interviews using [`architecture-interviews/mock-interviews.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/mock-interviews.md).
  * Review common mistakes ([`interview-mistakes.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/interview-mistakes.md)).

---

## 2. Personal Architect Skill Self-Assessment Matrix

Rate your mastery from **1 (Novice)** to **5 (Master / Principal Level)** across all eighteen core domains:

| Architecture Domain | Self-Rating (1–5) | Primary Knowledge Gap | Target Handbook Module |
| :--- | :---: | :--- | :--- |
| **System Design Foundations** | ` ` | | [`02-system-design/`](file:///d:/company/products/enterprise-architecture-handbook/02-system-design/) |
| **Distributed Data & Storage** | ` ` | | [`06-data/`](file:///d:/company/products/enterprise-architecture-handbook/06-data/) |
| **Integration & Messaging** | ` ` | | [`07-integration/`](file:///d:/company/products/enterprise-architecture-handbook/07-integration/) |
| **Cloud-Native Infrastructure** | ` ` | | [`08-cloud/`](file:///d:/company/products/enterprise-architecture-handbook/08-cloud/) |
| **DevOps & Platform Engineering** | ` ` | | [`09-devops/`](file:///d:/company/products/enterprise-architecture-handbook/09-devops/) |
| **Zero Trust & Security** | ` ` | | [`10-security/`](file:///d:/company/products/enterprise-architecture-handbook/10-security/) |
| **Observability & SRE** | ` ` | | [`11-observability/`](file:///d:/company/products/enterprise-architecture-handbook/11-observability/) |
| **AI / GenAI Architecture** | ` ` | | [`12-ai/`](file:///d:/company/products/enterprise-architecture-handbook/12-ai/) |
| **Architecture Patterns** | ` ` | | [`13-architecture-patterns/`](file:///d:/company/products/enterprise-architecture-handbook/13-architecture-patterns/) |
| **Enterprise Integration** | ` ` | | [`14-enterprise-integration/`](file:///d:/company/products/enterprise-architecture-handbook/14-enterprise-integration/) |
| **Legacy Modernization** | ` ` | | [`15-modernization/`](file:///d:/company/products/enterprise-architecture-handbook/15-modernization/) |
| **Architecture Deliverables** | ` ` | | [`16-architecture-deliverables/`](file:///d:/company/products/enterprise-architecture-handbook/16-architecture-deliverables/) |
| **Enterprise Architecture (EA)**| ` ` | | [`23-enterprise-architecture/`](file:///d:/company/products/enterprise-architecture-handbook/23-enterprise-architecture/) |
| **Technical Leadership** | ` ` | | [`20-interview-system-design/leadership/`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/leadership/) |
| **Trade-Off Reasoning** | ` ` | | [`20-interview-system-design/tradeoffs/`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/) |
| **Capacity Estimation** | ` ` | | [`20-interview-system-design/estimation/`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/) |
| **Incident Response** | ` ` | | [`20-interview-system-design/scenario-based/`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/scenario-based/) |
| **Architect Mastery** | ` ` | | [`24-architect-mastery/`](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/) |

---

## 3. The Interview Decision Journal Template

After every practice session or live interview, record your retrospection in this standardized journal format:

```markdown
### Interview Decision Journal Entry

* **Date**: YYYY-MM-DD
* **Target Role / Company**: (e.g., Principal Architect @ Global Cloud Provider)
* **Interview Prompt**: (e.g., "Design a globally distributed payment ledger with zero double-charging")

#### 1. Initial Assumptions & Clarifications Made
* Clarified 99.999% consistency requirement on balance queries.
* Scoped out international FX currency conversion for the first 30 minutes.

#### 2. Architecture Chosen
* C4 Container: API Gateway -> Payment Ingestion Service -> Distributed Kafka Topic -> Double-Entry Ledger Worker -> Multi-AZ PostgreSQL with distributed Raft consensus (CockroachDB).

#### 3. Key Trade-Offs Defended
* Defended Raft-based NewSQL over Cassandra to guarantee strict ACID transactions and avoid eventual consistency anomalies in customer balances.

#### 4. What Went Well
* Handled the back-of-the-envelope storage and IOPS calculation smoothly.
* Immediately introduced the Idempotency-Key pattern with Redis atomic locks to prevent double-charging.

#### 5. What Stumbled / Blind Spots
* Failed to consider network partition split-brain behavior across cross-continental links.
* Forgot to explicitly mention database replication lag monitoring until the interviewer probed.

#### 6. Action Items & Knowledge Gaps
* Read [`tradeoffs/cloud.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/cloud.md) on active-active replication conflict resolution.
* Practice 5 minutes of whiteboard pacing with a timer.
```

---

## 4. Cross-References

* **Scoring Rubric**: [`interview-scoring-rubric.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/interview-scoring-rubric.md)
* **Pacing Guide**: [`system-design-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/system-design-framework.md)
* **Mock Interviews**: [`architecture-interviews/mock-interviews.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/mock-interviews.md)
