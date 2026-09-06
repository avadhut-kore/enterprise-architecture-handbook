# Competency Deep Dive: System Design & Scalability

> **"System design is the art of assembling modular components into high-scale, resilient architectures that satisfy non-functional requirements under severe production constraints."**

---

## 1. Definition & Core Essence

**System Design** is the holistic discipline of architecting end-to-end distributed software systems. It encompasses:
* Horizontal vs vertical scalability models (Stateless service tier, database read-replicas, partitioning).
* High availability engineering (Multi-AZ, Multi-Region Active-Passive vs Active-Active, quorum models).
* Non-Functional Requirements (NFR) elicitation (Availability %, p99 latency budgets, throughput QPS, RTO/RPO).
* Capacity planning and sizing (Storage growth projections, network bandwidth, IOPS requirements).

---

## 2. Why It Matters for Modern Architects

* **Solution Architects**: Defines whether an application can survive a 10x traffic spike during a holiday flash sale without collapsing or blowing past cloud budgets.
* **Technical Architects**: Establishes global traffic routing standards (Anycast DNS, Cloudflare, Global Accelerator) and standard scaling policies across engineering squads.
* **Enterprise Architects**: Balances business availability expectations against infrastructure costs (e.g., explaining why 99.999% availability costs 10x more than 99.9%).

---

## 3. 5-Tier Behavioral Capability Progression

| Level | Behavioral Capability Anchor |
| :---: | :--- |
| **L1 (Practitioner)** | Deploys standard multi-instance web servers behind an Application Load Balancer (ALB). |
| **L2 (Independent)** | Separates stateful from stateless components; designs session state offloading to Redis; configures basic auto-scaling groups. |
| **L3 (Advanced)** | Designs database read-replicas and connection pooling; architects rate limiting and edge caching; calculates capacity sizing for 3x growth. |
| **L4 (Architect)** | Designs multi-region active-active systems with global traffic routing; formulates formal NFR matrices using `python 21-architecture-tools/generators/nfr_matrix_generator.py`; navigates cross-region replication lag. |
| **L5 (Strategic)** | Architects planetary-scale systems handling millions of QPS; designs multi-cloud disaster recovery architectures with automated failover and zero data loss. |

---

## 4. Practical Experiences & Apprenticeship Exercises

1. **Calculate System Capacity for 50,000 QPS**: Size the compute, memory, network bandwidth, and database IOPS required to sustain 50,000 requests/sec with a 250ms p99 latency budget.
2. **Design Multi-Region Failover**: Design an active-passive disaster recovery architecture with Route 53 health checks, Aurora Global Database, and automated cross-region DNS failover; test in a game-day drill.
3. **Resolve a Thundering Herd Problem**: Architect a multi-tier caching layer incorporating probabilistic early expiration (XFetch algorithm) to prevent database collapse when a hot cache key expires.

---

## 5. Objective Evidence of Capability (What to Inspect in Git)

- [ ] Complete Solution Architecture Document (SAD) with C4 Context and Container diagrams.
- [ ] Formal Non-Functional Requirements (NFR) Matrix generated using standard repository templates.
- [ ] Documented Disaster Recovery Plan specifying measurable RTO/RPO targets and failover procedures.

---

## 6. Common Cognitive Gaps & Blind Spots

* **Whiteboard Fantasy Scale**: Designing architectures for "Google scale" (millions of QPS) for a system that will handle 50 requests per minute, creating massive operational overhead.
* **Ignoring Network Physics**: Assuming cross-region network latency is negligible, resulting in distributed deadlocks and terrible user latency.
* **Conflating Uptime with Availability**: Claiming 99.99% uptime when upstream third-party dependencies only provide 99.5% SLAs.

---

## 7. Authoritative Repository Links

* System Design Core: [`02-system-design/`](../../02-system-design/README.md)
* High Availability Deep Dive: [`02-system-design/availability/`](../../02-system-design/availability/README.md)
* Disaster Recovery: [`02-system-design/disaster-recovery/`](../../02-system-design/disaster-recovery/README.md)
* Interview System Design: [`20-interview-system-design/`](../../20-interview-system-design/README.md)

---

## 8. Diagnostic Assessment Questions

1. *What is the mathematical difference between 99.9% availability and 99.99% availability in terms of allowable annual downtime, and how does that impact architecture cost?*
2. *How do you handle cross-region write conflicts in an active-active multi-region database topology?*
3. *What mechanisms prevent a cascading outage when a primary downstream database becomes unresponsive?*
