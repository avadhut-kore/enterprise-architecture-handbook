# 20. Architect Interview & System Design Playbook

> A production-grade preparation and reference system for Principal Engineers, Solution Architects, Technical Architects, and Enterprise Architects.

---

## 1. Mission & Philosophy

This playbook is designed to transform interview preparation from **rote memorization** to **repeatable architectural judgment under ambiguity**. 

Senior architecture interviews do not evaluate whether you can recite the features of Kafka or Redis. They evaluate how you navigate incomplete requirements, reason through competing trade-offs, identify insidious failure modes, model total cost of ownership, and communicate technical decisions to both engineering squads and C-suite executives.

```
Ambiguous Problem
       ↓
Clarifying Questions
       ↓
Business Understanding
       ↓
Functional Requirements & Scope Boundary
       ↓
Non-Functional Requirements (NFRs) & SLOs
       ↓
Scale & Resource Estimation
       ↓
High-Level Architecture (C4 Model)
       ↓
Data Architecture & Storage Strategy
       ↓
Critical Request & Event Flows
       ↓
Failure Modes, Resilience & Graceful Degradation
       ↓
Security & Trust Boundaries
       ↓
Observability & Operability
       ↓
Cost Modeling & Unit Economics
       ↓
Trade-Off Defense & Multi-Year Evolution
```

---

## 2. Senior Architect vs. Junior System Design Mindset

| Dimension | Junior / Mid-Level System Design | Senior / Principal / Enterprise Architect |
| :--- | :--- | :--- |
| **Primary Question** | *"What technologies would you use?"* | *"Why this architecture over alternatives, and under what constraints does it break?"* |
| **Scope Boundary** | Implements the prompt as stated. | Clarifies business objectives, uncovers hidden constraints, and defines what is explicitly out of scope. |
| **Technology Choice** | Tech-first (e.g., *"We'll use Kafka, Cassandra, and Kubernetes"*). | Constraint-driven (evaluates operational complexity, team skill, consistency needs, and TCO). |
| **Failure Analysis** | Mentions replication or basic retries. | Models cascading failures, thundering herds, split-brain, poison pills, and defines RTO/RPO recovery plans. |
| **Economics** | Rarely mentions cost. | Calculates infrastructure, networking, egress, licensing, and operational headcount economics. |
| **Organizational Impact** | Ignores team structure. | Considers Conway's Law, Team Topologies, developer cognitive load, and organizational governance. |
| **Communication** | Monologues technical jargon. | Collaborative dialogue, drives whiteboard clarity, actively checks in with the interviewer. |

---

## 3. Directory Structure & Navigation

The playbook is organized across five core practice dimensions supported by root architectural frameworks:

```
20-interview-system-design/
├── README.md                            # Directory index, philosophy, and study tracks
├── architect-interview-framework.md     # The canonical A-D-A-P-T interview methodology
├── system-design-framework.md          # 45–60 min time allocation and diagramming standards
├── architecture-answer-framework.md    # Reusable 22-step answer sequencing
├── interview-question-framework.md     # Interviewer psychology and probe questions
├── requirements-discovery.md           # Business, functional, and scope boundary discovery
├── nfr-discovery.md                    # Latency, throughput, availability, consistency discovery
├── architecture-communication.md       # Whiteboard execution, "When Stuck", and "I Don't Know"
├── interview-mistakes.md               # Catalog of 20 architectural red flags & anti-patterns
├── interview-scoring-rubric.md         # 12-dimension evaluation rubric (1 to 5 scale)
├── interview-preparation-plan.md       # 4/8/12-week study plan, journal, and skill matrix
│
├── architecture-interviews/            # Comprehensive end-to-end interview problems
│   ├── README.md                       # Catalog & difficulty levels
│   ├── progressive-levels.md           # Level 1 (Senior) to Level 5 (Principal/Enterprise)
│   ├── mock-interviews.md              # Full scripted mock interviews with hidden constraints
│   ├── url-shortener.md                # High-throughput distributed URL service
│   ├── notification-platform.md        # Multi-channel, priority-queued global notification engine
│   ├── distributed-chat.md             # Real-time WebSocket, ephemeral & persistent messaging
│   ├── payment-platform.md             # Idempotent, distributed ledger, PCI-DSS compliant engine
│   ├── ecommerce-platform.md           # Flash-sale inventory, checkout saga, CQRS catalog
│   ├── enterprise-api-platform.md      # API Gateway, rate limiting, OAuth2/mTLS, developer portal
│   ├── multi-region-active-active.md   # Global active-active, latency-routed data sync
│   ├── enterprise-ai-assistant.md      # Enterprise RAG, vector database, LLM security guardrails
│   └── legacy-modernization.md         # Strangler fig, CDC event-driven mainframe offload
│
├── estimation/                         # Back-of-the-envelope estimation & financial modeling
│   ├── README.md                       # Principles, powers of 2/10, latency cheatsheet
│   ├── traffic.md                      # RPS, DAU/MAU, peak factors, concurrent connections
│   ├── storage.md                      # Payload calculation, replication, index overhead, retention
│   ├── bandwidth.md                    # Ingress/egress, wire protocols (JSON vs Protobuf), CDN
│   ├── compute.md                      # CPU/RAM sizing, thread pools, async I/O worker density
│   ├── database.md                     # IOPS, working set, connection pools, sharding sizing
│   ├── capacity.md                     # Complete holistic capacity model synthesis
│   ├── cost.md                         # Infrastructure, networking, licensing, TCO economics
│   └── exercises/                      # 8 end-to-end capacity and cost exercises
│
├── leadership/                         # Technical leadership & stakeholder dynamics
│   ├── README.md                       # Architecture leadership competencies
│   ├── stakeholder-management.md       # Product vs Platform, Security vs Velocity, Cost vs SLA
│   ├── technical-leadership.md         # Architecture principles, standards, and mentorship
│   ├── influencing-without-authority.md # Consensus building, RFC/ADR processes, executive narratives
│   ├── architecture-governance.md      # Architecture Review Boards (ARB) & fitness functions
│   ├── team-topology.md                # Conway's Law, stream-aligned & platform team dynamics
│   ├── conflict-management.md          # Resolving engineering deadlocks & technological disputes
│   └── scenarios/                      # Realistic leadership interview behavioral challenges
│
├── scenario-based/                     # Architecture judgment simulator & incident response
│   ├── README.md                       # 10-step emergency response framework
│   ├── production.md                   # Cascading outages, connection exhaustion, poison pills
│   ├── architecture.md                 # Unraveling microservice spaghettis & distributed saga deadlocks
│   ├── modernization.md                # Dual-write drift, CDC lag, and strangler migration failures
│   ├── organizational.md               # Post-M&A platform consolidation & governance gridlocks
│   ├── incident-response.md            # Incident command, post-mortems, architectural remediation
│   └── exercises/                      # 10 hands-on crisis simulation exercises
│
└── tradeoffs/                          # Conditional decision matrices & technology trade-offs
    ├── README.md                       # The philosophy of trade-off reasoning
    ├── architecture.md                 # Monolith vs Microservices vs Serverless vs Event-Driven
    ├── data.md                         # SQL vs NoSQL vs NewSQL, Strong vs Eventual Consistency
    ├── integration.md                  # REST vs gRPC vs GraphQL, Queues vs Event Streams
    ├── infrastructure.md               # VMs vs Containers vs Kubernetes vs Managed Serverless
    ├── cloud.md                        # Single vs Multi-Region, Active-Active vs Active-Passive
    ├── performance.md                  # Caching strategies vs Database indexing & read replicas
    ├── reliability.md                  # Synchronous vs Async replication, Circuit breakers, Idempotency
    ├── security.md                     # Zero Trust vs Perimeter, Token vs Session, mTLS
    ├── ai.md                           # Hosted SaaS LLM vs Self-Hosted Open Weights, RAG vs Fine-Tuning
    └── decision-matrices/              # Consolidated quick-reference comparison tables
```

---

## 4. Progressive Difficulty Taxonomy

```
Level 1: Senior Software Engineer (Focus: Components, APIs, Database Schemas, Basic Scale)
   ↓
Level 2: Staff Engineer / Tech Lead (Focus: Non-functional depth, Resiliency, Async decoupling)
   ↓
Level 3: Solution Architect (Focus: End-to-end integration, Enterprise constraints, Operations, TCO)
   ↓
Level 4: Technical Architect / Domain Architect (Focus: Distributed trade-offs, Platform scaling, Cross-team alignment)
   ↓
Level 5: Principal Engineer / Enterprise Architect (Focus: Portfolio governance, Strategy, Conway's Law, Multi-year evolution)
```

For detailed expectations at each tier, see [`architecture-interviews/progressive-levels.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/progressive-levels.md).

---

## 5. Cross-Repository Architectural Integration

This playbook serves as the **evaluation and practice layer** across the entire Handbook. Refer to specialized modules for deep technical implementations:

* **Foundations & Methodologies**: [`01-architecture/`](file:///d:/company/products/enterprise-architecture-handbook/01-architecture/), [`02-system-design/`](file:///d:/company/products/enterprise-architecture-handbook/02-system-design/)
* **Tier Implementations**: [`03-backend/`](file:///d:/company/products/enterprise-architecture-handbook/03-backend/), [`04-frontend/`](file:///d:/company/products/enterprise-architecture-handbook/04-frontend/), [`05-mobile/`](file:///d:/company/products/enterprise-architecture-handbook/05-mobile/)
* **Data & Streaming**: [`06-data/`](file:///d:/company/products/enterprise-architecture-handbook/06-data/), [`07-integration/`](file:///d:/company/products/enterprise-architecture-handbook/07-integration/)
* **Cloud & Infrastructure**: [`08-cloud/`](file:///d:/company/products/enterprise-architecture-handbook/08-cloud/), [`09-devops/`](file:///d:/company/products/enterprise-architecture-handbook/09-devops/)
* **Security & Reliability**: [`10-security/`](file:///d:/company/products/enterprise-architecture-handbook/10-security/), [`11-observability/`](file:///d:/company/products/enterprise-architecture-handbook/11-observability/)
* **Emerging Tech & Enterprise Systems**: [`12-ai/`](file:///d:/company/products/enterprise-architecture-handbook/12-ai/), [`14-enterprise-integration/`](file:///d:/company/products/enterprise-architecture-handbook/14-enterprise-integration/), [`15-modernization/`](file:///d:/company/products/enterprise-architecture-handbook/15-modernization/)
* **Enterprise Strategy & Mastery**: [`23-enterprise-architecture/`](file:///d:/company/products/enterprise-architecture-handbook/23-enterprise-architecture/), [`24-architect-mastery/`](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/)
