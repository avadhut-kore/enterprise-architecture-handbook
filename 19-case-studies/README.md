# 19. Case Studies & Post-Mortems: Master Forensic Catalog

Welcome to the **Master Case Study & Forensic Post-Mortem Catalog** of the Enterprise Architecture Handbook. This domain catalogs real-world system failures, scaling breakdowns, architectural anti-patterns, legacy transformations, and forensic root-cause investigations.

Every flagship case study follows the canonical **19-Section Post-Mortem Standard** to provide senior architects, engineering leaders, and review boards with rigorous, blameless analyses of how complex distributed systems break, how latent vulnerabilities align, and how to engineer resilient architectures.

---

## 1. Forensic Governance, Standards & Post-Mortem Templates

Standardized frameworks, templates, and investigation rubrics for conducting architectural post-mortems and review board submissions:

* **Canonical Standards**:
  * [`post-mortem-template.md`](post-mortem-template.md) — The canonical 19-section post-mortem template.
  * [`forensic-investigation-checklist.md`](forensic-investigation-checklist.md) — 50-Point architectural diagnostic checklist.
* **Governance & Post-Mortem Template Library ([`post-mortem-templates/`](post-mortem-templates/README.md))**:
  * [`blameless-post-mortem-template.md`](post-mortem-templates/blameless-post-mortem-template.md) — Standardized blameless incident post-mortem template.
  * [`five-whys-root-cause-analysis-template.md`](post-mortem-templates/five-whys-root-cause-analysis-template.md) — 5-Whys recursive interrogation framework.
  * [`corrective-preventive-actions-template.md`](post-mortem-templates/corrective-preventive-actions-template.md) — Corrective and Preventive Actions (CAPA) tracking matrix.
  * [`incident-timeline-reconstruction-guide.md`](post-mortem-templates/incident-timeline-reconstruction-guide.md) — Forensic guide for reconciling telemetry and constructing verified timelines.
  * [`architecture-review-board-incident-submission-template.md`](post-mortem-templates/architecture-review-board-incident-submission-template.md) — Formal ARB incident submission template for policy amendments.

---

## 2. Cross-Cutting Forensic Synthesis & Decision Frameworks

* **[`comparative-analysis-matrix.md`](comparative-analysis-matrix.md)** — Comprehensive comparative analysis matrix indexing all 48 core forensic case studies across blast radius, MTTD, MTTR, financial cost, root cause, and architectural remediation patterns.
* **[`anti-patterns-cross-reference.md`](anti-patterns-cross-reference.md)** — Taxonomy of enterprise architectural anti-patterns (Coupling, Persistence, Resiliency, Boundary, Governance traps) cross-referenced to forensic case studies.
* **[`architecture-decision-framework.md`](architecture-decision-framework.md)** — Enterprise Architecture Pre-Mortem Guide: The 5 Inquiries and trade-off decision matrix.

---

## 3. Core Forensic Case Study Collections (48 In-Depth Investigations)

| Category | Directory | Domain Scope & Typical Architectural Failures Analyzed | Case Studies |
| :--- | :--- | :--- | :--- |
| **Cloud Outages & Resilience** | [`cloud/`](cloud/README.md) | Global BGP routing loops, IAM policy blast radius cascades, multi-AZ network stalls, wildcard TLS expirations, active-active DB split-brain, and multi-cloud DNS cascades. | 6 Cases (`CS-CLOUD-01` to `06`) |
| **Enterprise Architecture** | [`enterprise/`](enterprise/README.md) | Core banking ledger sprawl, Conway's Law organizational silos, M&A systems collision, runaway SAP ERP customization, shadow IT data swamps, and ARB waterfall paralysis. | 6 Cases (`CS-ENT-01` to `06`) |
| **Enterprise Integration** | [`integration/`](integration/README.md) | Dual-write ghost payments, Kafka poison pills, unbounded retry storms, distributed 2PC deadlocks, centralized ESB chokepoints, and webhook ping-pong loops. | 6 Cases (`CS-INT-01` to `06`) |
| **Cloud & Data Migration** | [`migration/`](migration/README.md) | Stored procedure migration traps, point-of-no-return cutovers, CDC replication lag drift, cloud lift-and-shift egress shocks, SAN storage starvation, and migration factory success. | 6 Cases (`CS-MIG-01` to `06`) |
| **Legacy Modernization** | [`modernization/`](modernization/README.md) | Distributed monolith latency collapse, shared DB microservice deadlocks, Second-System Syndrome write-offs, Strangler Fig facade memory leaks, EBCDIC copybook drift, and modular monolith refactoring. | 6 Cases (`CS-MOD-01` to `06`) |
| **Performance Engineering** | [`performance/`](performance/README.md) | ORM N+1 query explosions, HikariCP connection pool starvation, 45-second JVM Stop-The-World GC pauses, Redis large-key freezes, reflection JSON CPU sinks, and TLS handshake storms. | 6 Cases (`CS-PERF-01` to `06`) |
| **Scalability & Partitions** | [`scalability/`](scalability/README.md) | DynamoDB hot-partition throttling, B2B SaaS noisy neighbors, asymmetric K8s autoscaling crashes, Kafka rebalance storms, 1M WebSocket epoll exhaustion, and global active-active split-brain. | 6 Cases (`CS-SCALE-01` to `06`) |
| **Security & Zero Trust** | [`security/`](security/README.md) | Broken Object-Level Authorization (BOLA), AWS IMDSv1 SSRF credential exfiltration, CI/CD supply chain poisoning, hardcoded JWT secrets, exposed Kubelet APIs, and cross-tenant data leaks. | 6 Cases (`CS-SEC-01` to `06`) |

---

## 4. Specialized Domain Post-Mortems & Case Studies

* **[`system-design/`](system-design/README.md)** — Planetary-scale retrospectives and architectural breakdowns.
* **[`financial/`](financial/README.md)** — Core banking settlement engines, SWIFT messaging, and financial ledger reconciliation.
* **[`ai-modern/`](ai-modern/README.md)** — Production LLM prompt injection, vector embedding drift, and GPU cluster starvation.
* **[`security-operations/`](security-operations/README.md)** — Enterprise SOC incidents, ransomware resilience, and IAM leakage.
* **[`data-integration/`](data-integration/README.md)** — Enterprise data lakehouse, CDC pipeline, and stream processing post-mortems.
* **[`application-architecture/`](application-architecture/README.md)** — High-volume enterprise web application and API gateway post-mortems.
