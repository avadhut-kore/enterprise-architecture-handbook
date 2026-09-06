# Architecture Interview Problems & Playbooks

> Production-grade, end-to-end system design and enterprise architecture interview cases structured around the 20-part senior decision framework.

---

## 1. The Standard 20-Part Problem Format

Every interview case in this module is executed using a rigorous, senior architectural structure designed to demonstrate technical depth, commercial judgment, and operational reality:

```
 1. Business Context & Problem Statement
 2. Candidate Prompt & Executive Premise
 3. Clarifying Questions to Ask the Interviewer
 4. Expected Functional Scope & Boundaries (In vs. Out)
 5. Non-Functional Requirements (NFRs) & Concrete Targets
 6. Back-of-the-Envelope Scale & Capacity Estimation
 7. High-Level Architecture (C4 Container Diagram)
 8. Key Architectural Components
 9. Core Data Models & Schema Design
10. APIs & Event Contracts
11. Critical Request & Data Flows (Sequence)
12. Security Architecture & Trust Boundaries
13. Observability, Metrics & Telemetry (SLOs)
14. Failure Modes & Graceful Degradation Strategies
15. Horizontal & Vertical Scaling Strategy
16. Trade-Off Analysis & Rejected Alternatives
17. Cost Modeling & Unit Economics
18. Multi-Year Evolution & 10x Scale Roadmap
19. Interviewer Follow-Up Probes & Curveballs
20. Interviewer Evaluation Rubric: Weak vs. Strong Answers
```

---

## 2. The Playbook Catalog

### Core System Design & Distributed Systems
* **[`url-shortener.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/url-shortener.md)**: High-throughput URL shortening service (Base62 tokenization, distributed KGS, cache invalidation, and click analytics).
* **[`notification-platform.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/notification-platform.md)**: Multi-channel global notification engine (Email, SMS, Push, token-bucket rate limiting, priority queues, and provider failover).
* **[`distributed-chat.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/distributed-chat.md)**: Real-time messaging platform (10M concurrent WebSockets, ephemeral presence, Cassandra message persistence, and group fanout).
* **[`payment-platform.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/payment-platform.md)**: Mission-critical payment gateway (Double-entry ledger, idempotency keys, PCI-DSS vault isolation, and 2-phase saga commit).
* **[`ecommerce-platform.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/ecommerce-platform.md)**: High-scale e-commerce & flash-sale architecture (Atomic inventory reservation, CQRS catalog, and saga checkout).

### Enterprise & Platform Architecture
* **[`enterprise-api-platform.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/enterprise-api-platform.md)**: Enterprise API Gateway (OAuth2 token translation, Envoy service mesh, rate limiting, and developer portal).
* **[`legacy-modernization.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/legacy-modernization.md)**: Mainframe legacy offload (Strangler Fig, Change Data Capture via Debezium, and cloud-native read mesh).

### Cloud & AI Architecture
* **[`multi-region-active-active.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/multi-region-active-active.md)**: Globally distributed active-active architecture (GeoDNS routing, CRDT / NewSQL replication, and split-brain resilience).
* **[`enterprise-ai-assistant.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/enterprise-ai-assistant.md)**: Enterprise GenAI & RAG platform (Vector databases, hybrid search, document chunking pipelines, and LLM security guardrails).

### Frameworks & Preparation Guides
* **[`progressive-levels.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/progressive-levels.md)**: Architectural expectations broken down across Level 1 (Senior Engineer) through Level 5 (Principal / Enterprise Architect).
* **[`mock-interviews.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/mock-interviews.md)**: Scripted 45-minute mock interview transcripts with hidden constraints and scoring rubrics.

---

## 3. Cross-References

* **Universal Approach**: [`../architect-interview-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architect-interview-framework.md)
* **Pacing Guide**: [`../system-design-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/system-design-framework.md)
* **Capacity Sizing**: [`../estimation/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/README.md)
* **Trade-Off Matrices**: [`../tradeoffs/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/README.md)
