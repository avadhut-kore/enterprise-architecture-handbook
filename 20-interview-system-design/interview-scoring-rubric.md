# The Architect Interview Scoring Rubric

> A calibrated, 12-dimension evaluation framework used by hiring committees at FAANG, Tier-1 tech firms, and global enterprise platforms to assess Senior, Staff, Principal, and Enterprise Architects.

---

## 1. Overview of the 12-Dimension Evaluation Model

Candidates are scored on a scale from **1 (Weak)** to **5 (Distinguished / Executive-Level)** across twelve comprehensive architectural dimensions:

```mermaid
radar
    title Candidate Architectural Competency Profile
    "1. Requirements & Scope" : 4
    "2. NFRs & SLOs" : 5
    "3. Scale Estimation" : 4
    "4. Structural Architecture" : 5
    "5. Data & Schemas" : 4
    "6. Resilience & DR" : 5
    "7. Security & Privacy" : 4
    "8. Observability" : 4
    "9. Trade-Off Reasoning" : 5
    "10. Economics & Cost" : 4
    "11. Communication & Presence" : 5
    "12. Evolution & Strategy" : 4
```

---

## 2. Detailed 12-Dimension Scoring Matrix

| Dimension | 1 — Weak (No Hire) | 3 — Solid (Senior SDE / Tech Lead) | 5 — Distinguished (Principal / Chief Architect) |
| :--- | :--- | :--- | :--- |
| **1. Requirements & Scope** | Jumps straight to coding/drawing; ignores business context; accepts prompt without question. | Asks standard clarifying questions; identifies functional requirements; defines basic scope. | Uncovers hidden constraints; ties design to core business metrics; defines clear out-of-scope boundaries. |
| **2. NFRs & SLOs** | Uses vague buzzwords ("fast, reliable"); no numerical latency or availability targets. | Quantifies p95/p99 latency, 99.9% availability, and identifies CAP consistency model. | Defines error budgets, percentile distributions (p99.9), RTO/RPO metrics, and data sovereignty compliance. |
| **3. Scale Estimation** | Omits calculations or produces wild mathematical errors; exhibits false precision. | Accurately calculates RPS, storage per year, and network bandwidth using round numbers. | Back-of-the-envelope calculations translate directly into cluster sizing, memory footprints, and IOPS requirements. |
| **4. Architecture & Topology** | Chaotic box-and-arrow diagrams; monolithic thinking or uncontrolled microservice sprawl. | Clear C4 Container diagram; separates presentation, business logic, storage, and asynchronous queues. | Modular, decoupled domain boundaries; cell-based or event mesh patterns; accounts for team cognitive load. |
| **5. Data & Storage** | Vague "Database" box; picks SQL/NoSQL without justification; ignores keys and schemas. | Defines primary schema entities; specifies partition keys; contrasts relational vs document stores. | Polyglot persistence strategy; deep indexing and query access patterns; handles partition skew and sharding. |
| **6. Resilience & Reliability** | Assumes networks and nodes never fail; no retries, circuit breakers, or redundancy. | Includes multi-AZ deployment, read replicas, exponential backoff retries, and dead-letter queues. | Models cascading failure; implements bulkheads and circuit breakers; designs zero-data-loss cross-region DR. |
| **7. Security & Compliance** | Security completely absent or treated as an afterthought; unencrypted transport. | Mentions TLS termination, OAuth2/JWT tokens, and basic role-based access control (RBAC). | Zero Trust architecture; inter-service mTLS; envelope encryption (KMS); threat modeling; GDPR/PCI isolation. |
| **8. Observability & Operability** | No monitoring mentioned; assumes bugs are caught in staging. | Incorporates centralized logging, Prometheus metrics (RED), and basic threshold alerting. | Full OpenTelemetry distributed tracing (W3C trace context); SLO burn-rate alerts; automated canary rollbacks. |
| **9. Trade-Off Reasoning** | Dogmatic ("X is always better than Y"); defensive when challenged by the interviewer. | Explains why technology X was chosen over Y; acknowledges minor trade-offs. | Nuanced, conditional reasoning ("X is superior under constraints A and B, but fails under C"); welcomes probes. |
| **10. Economics & Cost** | Oblivious to cloud costs; deploys excessive idle infrastructure. | Estimates major cost drivers (compute, storage, and cross-region egress bandwidth). | Comprehensive TCO modeling; calculates cost per transaction / active user; optimizes for FinOps unit economics. |
| **11. Communication & Presence** | Monologues endlessly; chaotic whiteboard; combative or unresponsive to feedback. | Structured explanation; clean diagrams; checks in periodically with the interviewer. | Executive presence; driving the whiteboard with clarity; collaborative; guides the interviewer through decisions. |
| **12. Evolution & Strategy** | Designs an inflexible system; panics or erases the board when scale or constraints shift. | Proposes a basic 2-phase roadmap (MVP followed by scaling optimizations). | Articulates multi-year horizons (Strangler Fig, CDC, 10x scale inflection points, organizational Conway's Law). |

---

## 3. Calibrated Leveling Guidelines

* **Level 1 (Senior Software Engineer)**: Scores mostly 3s across Dimensions 1–5, with basic awareness of 6–8. Focus is on reliable component design and working APIs.
* **Level 2 (Lead / Staff Engineer)**: Scores 3s and 4s across Dimensions 1–9. Strong grasp of distributed systems, resilience, and trade-offs.
* **Level 3 (Solution Architect)**: Scores 4s across Dimensions 1–10. Deep client-facing discovery, enterprise integration, security, and operational viability.
* **Level 4 (Technical Architect / Domain Architect)**: Scores 4s and 5s across Dimensions 1–11. Unquestioned distributed systems depth, performance tuning, and technical leadership.
* **Level 5 (Principal Engineer / Enterprise Architect)**: Consistent 4s and 5s across all 12 Dimensions, with distinguished mastery in Dimensions 9, 10, 11, and 12 (Strategy, Economics, Governance, and Evolution).

---

## 4. Cross-References

* **Universal Framework**: [`architect-interview-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architect-interview-framework.md)
* **Interview Anti-Patterns**: [`interview-mistakes.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/interview-mistakes.md)
* **Progressive Difficulty Guide**: [`architecture-interviews/progressive-levels.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/progressive-levels.md)
* **Mock Interviews**: [`architecture-interviews/mock-interviews.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/mock-interviews.md)
