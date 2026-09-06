# Progressive Difficulty Levels: Senior Engineer to Enterprise Architect

> The explicit calibration rubric detailing what interviewers look for, what changes, and what is tested from Level 1 to Level 5.

---

## 1. The 5 Architecture Difficulty Levels

```
Level 1: Senior Software Engineer (Focus: Components, Schemas, APIs & Working Code)
   ↓
Level 2: Staff Engineer / Tech Lead (Focus: Resiliency, Decoupling, Concurrency & Scale)
   ↓
Level 3: Solution Architect (Focus: End-to-End Enterprise Systems, Integrations & TCO)
   ↓
Level 4: Technical Architect / Domain Architect (Focus: Distributed Trade-offs, Core Engines)
   ↓
Level 5: Principal Engineer / Enterprise Architect (Focus: Portfolio Governance, Multi-Year Strategy & Conway's Law)
```

---

## 2. Detailed Leveling Breakdown

### Level 1: Senior Software Engineer (SDE III / Senior Developer)
* **Primary Scope**: A single service or well-defined subsystem.
* **Core Expectations**:
  * Correct API design (HTTP status codes, REST/gRPC conventions).
  * Relational vs. NoSQL schema design (Primary Keys, Foreign Keys, Indexes).
  * Basic caching (Redis/Memcached) and basic scale calculations (RPS, storage).
  * Understands unit tests and continuous integration.
* **What is NOT Expected**: Complex multi-region active-active architectures, enterprise cost modeling, or organizational team restructuring.

### Level 2: Staff Engineer / Technical Lead
* **Primary Scope**: Multiple interacting microservices and asynchronous messaging topologies.
* **Core Expectations**:
  * Advanced non-functional requirements: Tail latency (p99), graceful degradation, and circuit breakers.
  * Asynchronous decoupling: Event streams (Kafka) vs. task queues (SQS), idempotency keys, and outbox patterns.
  * Distributed data challenges: Partition keys, sharding strategies, and eventual consistency handling.
  * Ability to mentor senior engineers and lead technical design reviews (RFCs).

### Level 3: Solution Architect
* **Primary Scope**: End-to-end commercial solutions integrating client requirements, enterprise platforms, and cloud infrastructure.
* **Core Expectations**:
  * Deep requirements discovery: Uncovering business outcomes, commercial constraints, and compliance mandates.
  * Enterprise integration: Legacy ERPs (SAP), CRMs (Salesforce), Identity Providers (Okta/Ping), and API Gateways.
  * Security & Compliance: Zero Trust, OAuth2 token exchange, PCI-DSS, GDPR data sovereignty.
  * Total Cost of Ownership (TCO): Infrastructure sizing, licensing costs, and operational ROI.

### Level 4: Technical Architect / Domain Architect
* **Primary Scope**: Enterprise-wide technical domain (e.g., Core Payments, Global Data Platform, High-Throughput Edge).
* **Core Expectations**:
  * Distributed systems depth: Consensus algorithms (Raft/Paxos), PACELC theorem, CRDTs, and network partition recovery.
  * High-concurrency performance tuning: Kernel TCP parameters, non-blocking I/O worker density, and memory fragmentation.
  * Defining reusable architecture patterns and paved roads across the entire company.
  * Resolving deep technical conflicts and setting enterprise technology standards.

### Level 5: Principal Engineer / Enterprise Architect
* **Primary Scope**: The entire enterprise technology portfolio, multi-year business strategy, and organizational topology.
* **Core Expectations**:
  * Conway's Law & Team Topologies: Structuring stream-aligned and platform teams to match target architectures.
  * Multi-year transformation roadmaps: Strangler fig migrations, M&A technology consolidation, and platform rationalization.
  * Executive communication: Advising the CTO, CEO, and Board of Directors on technical risk and capital investments.
  * Modern architectural governance: Architecture Review Boards, automated fitness functions, and tech debt lifecycle management.

---

## 3. Comparison by Interview Prompt: "Design a Payment System"

| Evaluation Level | Candidate Response Focus |
| :--- | :--- |
| **Level 1 (Senior SDE)** | Focuses on `POST /v1/charge`, writing to a PostgreSQL `charges` table, checking card validity, and calling the Stripe API with a `try/catch` block. |
| **Level 2 (Staff / Lead)** | Introduces the **Idempotency-Key** pattern with Redis atomic locks, creates an asynchronous event queue for receipt generation, and implements circuit breakers for the third-party gateway. |
| **Level 3 (Solution Architect)**| Adds PCI-DSS compliance isolation (tokenized cardholder data environment), handles double-entry bookkeeping ledger models, models transaction fee economics, and designs automated merchant settlement reconciliations. |
| **Level 4 (Technical Architect)**| Focuses on distributed 2-phase sagas with compensating transactions, multi-region active-active ledger replication, clock-skew mitigation, and hardware security module (HSM) key lifecycle. |
| **Level 5 (Principal / Enterprise)**| Analyzes multi-provider banking redundancy (interchange fee optimization), regulatory financial license requirements (PSD2/Open Banking), organizational ownership across Checkout, Fraud, and Treasury squads, and multi-year vendor contract negotiations. |

---

## 4. Cross-References

* **Rubric**: [`../interview-scoring-rubric.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/interview-scoring-rubric.md)
* **Preparation Curriculum**: [`../interview-preparation-plan.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/interview-preparation-plan.md)
* **Mock Interviews**: [`mock-interviews.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/mock-interviews.md)
