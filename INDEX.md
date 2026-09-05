# Master Knowledge Index

Welcome to the comprehensive master index of the **Enterprise Architecture Handbook**. This document indexes every domain, subdirectory, template, tool, checklist, and architectural document across the repository.

---

## Quick Navigation

* [00. Foundations](#00-foundations)
* [01. Architecture Disciplines](#01-architecture)
* [02. System Design & NFRs](#02-system-design)
* [03. Backend Platforms](#03-backend)
* [04. Frontend Architecture](#04-frontend)
* [05. Mobile Architecture](#05-mobile)
* [06. Data Engineering & Persistence](#06-data)
* [07. Integration & Messaging](#07-integration)
* [08. Cloud Computing & FinOps](#08-cloud)
* [09. DevOps & Platform Engineering](#09-devops)
* [10. Security & Zero Trust](#10-security)
* [11. Observability & SRE](#11-observability)
* [12. AI, LLM & GenAI Systems](#12-ai)
* [13. Architecture Patterns](#13-architecture-patterns)
* [14. Enterprise Integration Domains](#14-enterprise-integration)
* [15. Modernization & Migration](#15-modernization)
* [16. Architecture Deliverables & Templates](#16-architecture-deliverables)
* [17. Architecture Diagrams & C4 Model](#17-diagrams)
* [18. Reference Architectures](#18-reference-architectures)
* [19. Case Studies & Post-Mortems](#19-case-studies)
* [20. System Design Interview Playbook](#20-interview-system-design)
* [21. Architecture Tools & Checklists](#21-architecture-tools)
* [22. Reference & Standards](#22-reference)
* [99. Experimental Labs](#99-experiments)

---

## Core Governance & Framework Documents

* [README.md](README.md) — Executive Overview, Vision, Target Audience, and Operational Model.
* [ARCHITECTURE.md](ARCHITECTURE.md) — Meta-architecture of the handbook, taxonomy, lifecycle, and cross-linking rules.
* [ARCHITECTURE-PRINCIPLES.md](ARCHITECTURE-PRINCIPLES.md) — 15 Core architectural principles for enterprise systems.
* [ARCHITECTURE-WORKFLOW.md](ARCHITECTURE-WORKFLOW.md) — End-to-end delivery lifecycle from business requirements to Day-2 operations.
* [DECISION-MAKING-FRAMEWORK.md](DECISION-MAKING-FRAMEWORK.md) — 15-Dimension trade-off scorecard and evaluation rubric.
* [DOCUMENTATION-STANDARD.md](DOCUMENTATION-STANDARD.md) — Universal standard format for technical documentation.
* [TECHNOLOGY-RADAR.md](TECHNOLOGY-RADAR.md) — Portfolio radar: Adopt, Trial, Assess, Hold.
* [ROADMAP.md](ROADMAP.md) — 10-Phase progression roadmap for this handbook.
* [CONTRIBUTING.md](CONTRIBUTING.md) — Quality guidelines, naming rules, and pull request criteria.
* [CHANGELOG.md](CHANGELOG.md) — Version history and iteration records.

---

## 00. Foundations
*Theoretical baselines, compute models, and core engineering fundamentals.*

### Architecture Principles (`00-foundations/architecture-principles/`)
* [`what-is-software-architecture.md`](00-foundations/architecture-principles/what-is-software-architecture.md) — Definitions, scopes, boundaries, and architectural responsibilities.
* [`architecture-vs-design.md`](00-foundations/architecture-principles/architecture-vs-design.md) — The boundary between strategic architecture and tactical design.
* [`architecture-characteristics.md`](00-foundations/architecture-principles/architecture-characteristics.md) — System "-ilities" and operational characteristics.
* [`architecture-principles.md`](00-foundations/architecture-principles/architecture-principles.md) — Core axioms guiding enterprise system design.
* [`architecture-tradeoffs.md`](00-foundations/architecture-principles/architecture-tradeoffs.md) — Managing conflicting architectural forces.
* [`complexity-management.md`](00-foundations/architecture-principles/complexity-management.md) — Essential vs. accidental complexity.
* [`coupling-and-cohesion.md`](00-foundations/architecture-principles/coupling-and-cohesion.md) — Connascence, afferent/efferent coupling metrics.
* [`architecture-evolution.md`](00-foundations/architecture-principles/architecture-evolution.md) — Evolutionary architecture and continuous fitness functions.

### Distributed Systems (`00-foundations/distributed-systems/`)
* [`introduction.md`](00-foundations/distributed-systems/introduction.md) — Distributed systems foundations and the 8 fallacies.
* [`distributed-system-characteristics.md`](00-foundations/distributed-systems/distributed-system-characteristics.md) — Core distributed characteristics and network primitives.
* [`latency.md`](00-foundations/distributed-systems/latency.md) — Latency distribution, numbers every engineer should know, tail latency.
* [`throughput.md`](00-foundations/distributed-systems/throughput.md) — Measuring and optimizing throughput across distributed nodes.
* [`concurrency.md`](00-foundations/distributed-systems/concurrency.md) — Concurrency models, race conditions, memory barriers, locks.
* [`replication.md`](00-foundations/distributed-systems/replication.md) — Primary-replica, multi-master, quorum-based replication models.
* [`partitioning.md`](00-foundations/distributed-systems/partitioning.md) — Horizontal partitioning, range vs. hash partitioning.
* [`sharding.md`](00-foundations/distributed-systems/sharding.md) — Database sharding, shard keys, re-sharding strategies.
* [`consistency.md`](00-foundations/distributed-systems/consistency.md) — Consistency continuum from strict linearizability to eventual.
* [`eventual-consistency.md`](00-foundations/distributed-systems/eventual-consistency.md) — BASE semantics, CRDTs, read-your-writes guarantees.
* [`strong-consistency.md`](00-foundations/distributed-systems/strong-consistency.md) — Linearizable consistency, two-phase locking, consensus protocols.
* [`distributed-transactions.md`](00-foundations/distributed-systems/distributed-transactions.md) — Two-Phase Commit (2PC) vs. Sagas.
* [`consensus.md`](00-foundations/distributed-systems/consensus.md) — Distributed consensus algorithms: Paxos and Raft.
* [`cap-theorem.md`](00-foundations/distributed-systems/cap-theorem.md) — Consistency, Availability, Partition Tolerance trade-offs.
* [`pacelc.md`](00-foundations/distributed-systems/pacelc.md) — PACELC theorem and normal-state latency trade-offs.
* [`idempotency.md`](00-foundations/distributed-systems/idempotency.md) — Designing idempotent mutation APIs and message handlers.
* [`retries.md`](00-foundations/distributed-systems/retries.md) — Retry policies, exponential backoff, and full jitter.
* [`timeouts.md`](00-foundations/distributed-systems/timeouts.md) — Fail-fast timeouts and dead-socket prevention.
* [`circuit-breaker.md`](00-foundations/distributed-systems/circuit-breaker.md) — Circuit Breaker pattern states and sliding window trip metrics.
* [`backpressure.md`](00-foundations/distributed-systems/backpressure.md) — Flow control, reactive streams, buffer drop policies.
* [`load-balancing.md`](00-foundations/distributed-systems/load-balancing.md) — L4 vs. L7 load balancing, health checks, algorithms.
* [`failure-models.md`](00-foundations/distributed-systems/failure-models.md) — Crash-stop, crash-recovery, network partitions, Byzantine faults.

### Networking (`00-foundations/networking/`)
* [`osi-model.md`](00-foundations/networking/osi-model.md) — 7-Layer OSI model mapped to modern protocols.
* [`tcp-ip.md`](00-foundations/networking/tcp-ip.md) — Three-way handshake, congestion control, TIME_WAIT states.
* [`dns.md`](00-foundations/networking/dns.md) — Hierarchical DNS resolution, records, TTL, Anycast.
* [`http.md`](00-foundations/networking/http.md) — HTTP/1.1 semantics, keep-alive, headers, status codes.
* [`http2.md`](00-foundations/networking/http2.md) — Multiplexing, binary framing, HPACK, stream priorities.
* [`http3.md`](00-foundations/networking/http3.md) — QUIC over UDP, 0-RTT handshakes, connection migration.
* [`tls.md`](00-foundations/networking/tls.md) — TLS 1.3 cryptographic handshake, cipher suites, mTLS.
* [`reverse-proxy.md`](00-foundations/networking/reverse-proxy.md) — Reverse proxy architectures, TLS offloading, NGINX/Envoy.
* [`load-balancer.md`](00-foundations/networking/load-balancer.md) — Consistent hashing, least connections, sticky sessions.
* [`cdn.md`](00-foundations/networking/cdn.md) — Edge caching, origin shielding, cache invalidation strategies.
* [`firewall.md`](00-foundations/networking/firewall.md) — Stateful packet inspection, WAF, security groups.
* [`vpn.md`](00-foundations/networking/vpn.md) — IPsec, WireGuard, Site-to-Site and Client-to-Site VPNs.
* [`ingress-egress.md`](00-foundations/networking/ingress-egress.md) — Kubernetes Ingress controllers, API gateways, NAT gateways.
* [`service-discovery.md`](00-foundations/networking/service-discovery.md) — Client-side vs. server-side discovery, Consul, CoreDNS.
* [`network-segmentation.md`](00-foundations/networking/network-segmentation.md) — VPCs, subnets, DMZ, zero-trust micro-segmentation.

### Databases (`00-foundations/databases/`)
* [`relational-databases.md`](00-foundations/databases/relational-databases.md) — Relational algebra, storage structures, buffer pools.
* [`nosql-databases.md`](00-foundations/databases/nosql-databases.md) — Document, key-value, wide-column, and graph architectures.
* [`sql-vs-nosql.md`](00-foundations/databases/sql-vs-nosql.md) — Systematic trade-off matrix: schema vs. flexibility.
* [`normalization.md`](00-foundations/databases/normalization.md) — 1NF through BCNF normalization and pragmatic denormalization.
* [`indexing.md`](00-foundations/databases/indexing.md) — B-Trees, LSM-Trees, Hash indexes, GIN/GiST, covering indexes.
* [`transactions.md`](00-foundations/databases/transactions.md) — Transaction lifecycles, WAL, write amplification.
* [`isolation-levels.md`](00-foundations/databases/isolation-levels.md) — Read Uncommitted to Serializable; dirty reads, phantom reads.
* [`replication.md`](00-foundations/databases/replication.md) — Synchronous vs. asynchronous replication, failover lag.
* [`partitioning.md`](00-foundations/databases/partitioning.md) — Horizontal table partitioning by range, list, and hash.
* [`sharding.md`](00-foundations/databases/sharding.md) — Application-level sharding, cross-shard joins, distributed routing.
* [`database-scaling.md`](00-foundations/databases/database-scaling.md) — Read replicas, connection pooling, write scaling strategies.
* [`polyglot-persistence.md`](00-foundations/databases/polyglot-persistence.md) — Designing heterogeneous data architectures.
* [`database-selection.md`](00-foundations/databases/database-selection.md) — Comprehensive decision tree for database selection.

### Cloud Fundamentals (`00-foundations/cloud-fundamentals/`)
* [`cloud-computing.md`](00-foundations/cloud-fundamentals/cloud-computing.md) — Cloud computing definitions, multi-tenancy, economies of scale.
* [`iaas-paas-saas.md`](00-foundations/cloud-fundamentals/iaas-paas-saas.md) — Service models comparison and responsibility boundaries.
* [`cloud-native.md`](00-foundations/cloud-fundamentals/cloud-native.md) — Cloud-native architecture principles (CNCF definition).
* [`twelve-factor-app.md`](00-foundations/cloud-fundamentals/twelve-factor-app.md) — The Twelve-Factor App methodology for cloud applications.
* [`containers.md`](00-foundations/cloud-fundamentals/containers.md) — Linux namespaces, cgroups, OCI images, Docker runtimes.
* [`serverless.md`](00-foundations/cloud-fundamentals/serverless.md) — Function-as-a-Service, event sources, cold start mitigation.
* [`managed-services.md`](00-foundations/cloud-fundamentals/managed-services.md) — Evaluating managed cloud services vs. self-hosted OSS.
* [`cloud-networking.md`](00-foundations/cloud-fundamentals/cloud-networking.md) — VPCs, Peering, Transit Gateways, PrivateLink.
* [`cloud-security.md`](00-foundations/cloud-fundamentals/cloud-security.md) — Cloud IAM, KMS, shared responsibility model.
* [`cloud-resilience.md`](00-foundations/cloud-fundamentals/cloud-resilience.md) — Multi-AZ, Multi-Region, Chaos engineering in the cloud.
* [`cloud-cost-model.md`](00-foundations/cloud-fundamentals/cloud-cost-model.md) — Cloud pricing mechanics, egress fees, FinOps foundations.

---

## 01. Architecture
*Disciplines of enterprise, solution, application, and infrastructure architecture.*

### Architecture Styles (`01-architecture/architecture-styles/`)
* [`layered-architecture.md`](01-architecture/architecture-styles/layered-architecture.md) — Classical N-Tier / Layered pattern.
* [`client-server.md`](01-architecture/architecture-styles/client-server.md) — Client-Server architecture topologies.
* [`monolithic.md`](01-architecture/architecture-styles/monolithic.md) — Monolithic application architecture.
* [`modular-monolith.md`](01-architecture/architecture-styles/modular-monolith.md) — In-process modular monolith pattern.
* [`microservices.md`](01-architecture/architecture-styles/microservices.md) — Distributed microservices architecture.
* [`service-oriented-architecture.md`](01-architecture/architecture-styles/service-oriented-architecture.md) — Enterprise Service-Oriented Architecture (SOA) & ESB.
* [`event-driven-architecture.md`](01-architecture/architecture-styles/event-driven-architecture.md) — Event-Driven Architecture (EDA).
* [`serverless.md`](01-architecture/architecture-styles/serverless.md) — Serverless / FaaS architecture.
* [`space-based-architecture.md`](01-architecture/architecture-styles/space-based-architecture.md) — Space-Based / In-memory data grid architecture.
* [`pipe-and-filter.md`](01-architecture/architecture-styles/pipe-and-filter.md) — Pipe-and-Filter streaming processing pattern.
* [`microkernel.md`](01-architecture/architecture-styles/microkernel.md) — Microkernel / Plugin-based architecture.
* [`hexagonal.md`](01-architecture/architecture-styles/hexagonal.md) — Hexagonal Architecture / Ports and Adapters.
* [`clean-architecture.md`](01-architecture/architecture-styles/clean-architecture.md) — Robert C. Martin's Clean Architecture.

#### Architecture Style Comparisons (`01-architecture/architecture-styles/comparisons/`)
* [`monolith-vs-modular-monolith.md`](01-architecture/architecture-styles/comparisons/monolith-vs-modular-monolith.md)
* [`modular-monolith-vs-microservices.md`](01-architecture/architecture-styles/comparisons/modular-monolith-vs-microservices.md)
* [`monolith-vs-microservices.md`](01-architecture/architecture-styles/comparisons/monolith-vs-microservices.md)
* [`soa-vs-microservices.md`](01-architecture/architecture-styles/comparisons/soa-vs-microservices.md)
* [`microservices-vs-serverless.md`](01-architecture/architecture-styles/comparisons/microservices-vs-serverless.md)
* [`synchronous-vs-asynchronous.md`](01-architecture/architecture-styles/comparisons/synchronous-vs-asynchronous.md)
* [`centralized-vs-decentralized.md`](01-architecture/architecture-styles/comparisons/centralized-vs-decentralized.md)

### Enterprise Architecture (`01-architecture/enterprise-architecture/`)
* [`enterprise-architecture-overview.md`](01-architecture/enterprise-architecture/enterprise-architecture-overview.md) — Frameworks, TOGAF 10, Zachman, BIZBOK.
* [`business-architecture.md`](01-architecture/enterprise-architecture/business-architecture.md) — Business capabilities, value streams, operating models.
* [`application-architecture.md`](01-architecture/enterprise-architecture/application-architecture.md) — Application landscape planning, component boundaries.
* [`data-architecture.md`](01-architecture/enterprise-architecture/data-architecture.md) — Enterprise data governance, DAMA-DMBOK, Master Data (MDM).
* [`technology-architecture.md`](01-architecture/enterprise-architecture/technology-architecture.md) — Infrastructure platforms, hybrid cloud, technology lifecycles.
* [`security-architecture.md`](01-architecture/enterprise-architecture/security-architecture.md) — Enterprise security frameworks, SABSA, zero-trust controls.
* [`integration-architecture.md`](01-architecture/enterprise-architecture/integration-architecture.md) — Enterprise Integration Patterns (EIP), ESB vs. Mesh.
* [`enterprise-architecture-governance.md`](01-architecture/enterprise-architecture/enterprise-architecture-governance.md) — EAB, ARB, compliance gates, waiver lifecycles.
* [`architecture-principles.md`](01-architecture/enterprise-architecture/architecture-principles.md) — Enterprise architectural axioms and rationale.
* [`technology-standards.md`](01-architecture/enterprise-architecture/technology-standards.md) — Technology radar, golden paths, permitted stacks.
* [`architecture-roadmaps.md`](01-architecture/enterprise-architecture/architecture-roadmaps.md) — Transition architectures, multi-year horizon roadmaps.
* [`application-portfolio.md`](01-architecture/enterprise-architecture/application-portfolio.md) — Application Portfolio Management (APM) & Gartner TIME model.
* [`technology-portfolio.md`](01-architecture/enterprise-architecture/technology-portfolio.md) — Technology Portfolio Management (TPM), OSS governance, vendor lock-in.
* [`technical-debt.md`](01-architecture/enterprise-architecture/technical-debt.md) — Technical debt quantification (TDR), debt registers, remediation waves.
* [`architecture-risk.md`](01-architecture/enterprise-architecture/architecture-risk.md) — Enterprise architecture risk management, 5x5 scoring matrix.

### Solution Architecture (`01-architecture/solution-architecture/`)
* [`solution-architecture-overview.md`](01-architecture/solution-architecture/solution-architecture-overview.md) — Scope, role, EA vs. SA vs. TA comparison.
* [`solution-architecture-process.md`](01-architecture/solution-architecture/solution-architecture-process.md) — End-to-end SA delivery lifecycle.
* [`requirements-to-architecture.md`](01-architecture/solution-architecture/requirements-to-architecture.md) — Translating business stories into architectural drivers.
* [`architecture-context.md`](01-architecture/solution-architecture/architecture-context.md) — System boundaries, external dependencies, C4 context modeling.
* [`architecture-options.md`](01-architecture/solution-architecture/architecture-options.md) — Divergent-convergent option analysis and spikes.
* [`architecture-evaluation.md`](01-architecture/solution-architecture/architecture-evaluation.md) — ATAM methodology, utility trees, automated fitness tests.
* [`architecture-decisions.md`](01-architecture/solution-architecture/architecture-decisions.md) — Architecture Decision Records (ADRs) and decision thresholds.
* [`architecture-tradeoffs.md`](01-architecture/solution-architecture/architecture-tradeoffs.md) — Managing architectural tensions in solution design.
* [`architecture-estimation.md`](01-architecture/solution-architecture/architecture-estimation.md) — Back-of-the-envelope scale sizing, FinOps, PERT estimation.
* [`architecture-risk-management.md`](01-architecture/solution-architecture/architecture-risk-management.md) — STRIDE threat modeling, cascading failure mitigation.
* [`architecture-communication.md`](01-architecture/solution-architecture/architecture-communication.md) — Stakeholder management, 4+1 View Model, elevator pitches.
* [`architecture-review.md`](01-architecture/solution-architecture/architecture-review.md) — ARB review hearings, determinations, and PRR gates.

### Master Architecture Trade-Offs Framework
* [`architecture-tradeoffs.md`](01-architecture/architecture-patterns/architecture-tradeoffs.md) — Comprehensive cross-pattern trade-off evaluation matrix.

---

## 02. System Design & NFRs
*High-scale systems engineering, NFR specification, and fault resilience.*

### Non-Functional Requirements (`02-system-design/non-functional-requirements/`)
* [`availability.md`](02-system-design/non-functional-requirements/availability.md) — The nines table, MTBF/MTTR formulas, high-availability topologies.
* [`reliability.md`](02-system-design/non-functional-requirements/reliability.md) — Availability vs. Reliability, SRE error budgets, transactional outbox.
* [`scalability.md`](02-system-design/non-functional-requirements/scalability.md) — Universal Scalability Law (USL), vertical vs. horizontal scale.
* [`performance.md`](02-system-design/non-functional-requirements/performance.md) — Latency percentiles (p50, p99), tail-at-scale effects, non-blocking I/O.
* [`security.md`](02-system-design/non-functional-requirements/security.md) — CIA triad, Zero Trust, envelope encryption, CVSS metrics.
* [`maintainability.md`](02-system-design/non-functional-requirements/maintainability.md) — Maintainability Index, Cyclomatic Complexity, Clean Architecture.
* [`testability.md`](02-system-design/non-functional-requirements/testability.md) — Test Pyramid, mutation testing, Testcontainers, Pact contract tests.
* [`observability.md`](02-system-design/non-functional-requirements/observability.md) — 4 Pillars, OpenTelemetry, RED/USE methods, tail sampling.
* [`resilience.md`](02-system-design/non-functional-requirements/resilience.md) — Circuit breakers, full jitter backoff, bulkheads, load shedding.
* [`recoverability.md`](02-system-design/non-functional-requirements/recoverability.md) — RPO and RTO, disaster recovery tiers (Pilot Light to Active-Active).
* [`portability.md`](02-system-design/non-functional-requirements/portability.md) — Vendor lock-in mitigation, Twelve-Factor App, container standards.
* [`interoperability.md`](02-system-design/non-functional-requirements/interoperability.md) — Postel's Law, Anti-Corruption Layer, Canonical Data Model, CloudEvents.
* [`accessibility.md`](02-system-design/non-functional-requirements/accessibility.md) — WCAG 2.2 AA/AAA, legal compliance, design systems, ARIA.
* [`cost-efficiency.md`](02-system-design/non-functional-requirements/cost-efficiency.md) — FinOps, unit economics, cloud waste reduction, spot instances.

### System Design Methodology (`02-system-design/methodology/`)
* [`system-design-process.md`](02-system-design/methodology/system-design-process.md) — The 8-step end-to-end system design lifecycle.
* [`requirements-analysis.md`](02-system-design/methodology/requirements-analysis.md) — 4-Quadrant clarification framework, uncovering hidden constraints.
* [`nfr-analysis.md`](02-system-design/methodology/nfr-analysis.md) — SLI/SLO/SLA hierarchy, NFR conflict matrix, Top-3 rule.
* [`scale-estimation.md`](02-system-design/methodology/scale-estimation.md) — Step-by-step QPS, 5-year storage, network bandwidth, and 80/20 cache sizing.
* [`capacity-planning.md`](02-system-design/methodology/capacity-planning.md) — Little's Law, database connection pool sizing, IOPS provisioning.
* [`architecture-selection.md`](02-system-design/methodology/architecture-selection.md) — Architecture style decision tree, Conway's Law, monolith-first.
* [`api-design.md`](02-system-design/methodology/api-design.md) — REST vs. gRPC vs. GraphQL, cursor pagination, idempotency keys, RFC 7807.
* [`data-design.md`](02-system-design/methodology/data-design.md) — Polyglot persistence matrix, relational vs. NoSQL, shard key selection.
* [`failure-analysis.md`](02-system-design/methodology/failure-analysis.md) — Single Point of Failure (SPOF) audit, FMEA matrix, split-brain, quorum.
* [`security-analysis.md`](02-system-design/methodology/security-analysis.md) — STRIDE threat modeling on architecture diagrams, envelope encryption.
* [`cost-analysis.md`](02-system-design/methodology/cost-analysis.md) — FinOps cloud cost modeling, hidden cost traps, worked 3-year TCO.
* [`tradeoff-analysis.md`](02-system-design/methodology/tradeoff-analysis.md) — PACELC theorem, push vs. pull fanout, 4-sentence trade-off defense.

---

## 13. Architecture Patterns
*Detailed breakdown of modern system architecture patterns.*

* [`13-architecture-patterns/microservices/README.md`](13-architecture-patterns/microservices/README.md) — Microservices architecture pattern.
* [`13-architecture-patterns/modular-monolith/README.md`](13-architecture-patterns/modular-monolith/README.md) — Modular monolith architecture pattern.
* [`13-architecture-patterns/event-driven/README.md`](13-architecture-patterns/event-driven/README.md) — Event-driven architecture (EDA) pattern.
* [`13-architecture-patterns/cqrs/README.md`](13-architecture-patterns/cqrs/README.md) — Command Query Responsibility Segregation (CQRS) pattern.
* [`13-architecture-patterns/event-sourcing/README.md`](13-architecture-patterns/event-sourcing/README.md) — Event sourcing pattern.
* [`13-architecture-patterns/saga/README.md`](13-architecture-patterns/saga/README.md) — Saga pattern for distributed transactions.
* [`13-architecture-patterns/strangler-fig/README.md`](13-architecture-patterns/strangler-fig/README.md) — Strangler Fig legacy modernization pattern.
* [`13-architecture-patterns/hexagonal/README.md`](13-architecture-patterns/hexagonal/README.md) — Hexagonal architecture (Ports and Adapters) pattern.
* [`13-architecture-patterns/clean-architecture/README.md`](13-architecture-patterns/clean-architecture/README.md) — Clean architecture pattern.
* [`13-architecture-patterns/domain-driven-design/README.md`](13-architecture-patterns/domain-driven-design/README.md) — Domain-Driven Design (DDD) strategic and tactical patterns.
* [`13-architecture-patterns/serverless/README.md`](13-architecture-patterns/serverless/README.md) — Serverless architecture pattern.

---

## 16. Architecture Deliverables & Reusable Templates
*Ready-to-use professional markdown templates and governance deliverables.*

### Architecture Decision Records (`16-architecture-deliverables/adr/`)
* [`README.md`](16-architecture-deliverables/adr/README.md) — ADR repository index, lifecycle states, and governance.
* [`ADR-0001-template.md`](16-architecture-deliverables/adr/ADR-0001-template.md) — Standard enterprise ADR template.
* [`ADR-0002-example-modular-monolith-vs-microservices.md`](16-architecture-deliverables/adr/ADR-0002-example-modular-monolith-vs-microservices.md) — Production ADR example: Modular Monolith vs. Microservices.
* [`ADR-0003-example-rest-vs-grpc.md`](16-architecture-deliverables/adr/ADR-0003-example-rest-vs-grpc.md) — Production ADR example: REST vs. gRPC for inter-service RPC.
* [`ADR-0004-example-sql-vs-nosql.md`](16-architecture-deliverables/adr/ADR-0004-example-sql-vs-nosql.md) — Production ADR example: Relational PostgreSQL vs. NoSQL DynamoDB.
* [`ADR-0005-example-sync-vs-async.md`](16-architecture-deliverables/adr/ADR-0005-example-sync-vs-async.md) — Production ADR example: Sync REST vs. Asynchronous Kafka event processing.

### Architecture Review Framework (`16-architecture-deliverables/architecture-review/`)
* [`README.md`](16-architecture-deliverables/architecture-review/README.md) — Architecture Review framework overview and lifecycle gates.
* [`architecture-review-process.md`](16-architecture-deliverables/architecture-review/architecture-review-process.md) — Operational review workflow, intake, hearings, and escalations.
* [`architecture-review-checklist.md`](16-architecture-deliverables/architecture-review/architecture-review-checklist.md) — Universal 8-domain architectural evaluation checklist.
* [`design-review.md`](16-architecture-deliverables/architecture-review/design-review.md) — Inception-stage design review guide and probing questions.
* [`security-review.md`](16-architecture-deliverables/architecture-review/security-review.md) — Security review guide: threat modeling, IAM, encryption controls.
* [`scalability-review.md`](16-architecture-deliverables/architecture-review/scalability-review.md) — Scalability review guide: capacity checks, database queries, load testing gates.
* [`production-readiness-review.md`](16-architecture-deliverables/architecture-review/production-readiness-review.md) — Pre-launch PRR guide: zero-downtime canary, runbooks, chaos drills.
* [`architecture-sign-off.md`](16-architecture-deliverables/architecture-review/architecture-sign-off.md) — Formal ARB sign-off certificate and 12-month exception waiver template.

### Reusable Architecture Templates
* [`ADR-TEMPLATE.md`](16-architecture-deliverables/ADR-TEMPLATE.md) — Architecture Decision Record.
* [`SOLUTION-ARCHITECTURE-TEMPLATE.md`](16-architecture-deliverables/SOLUTION-ARCHITECTURE-TEMPLATE.md) — Comprehensive Solution Architecture Document (SAD).
* [`HLD-TEMPLATE.md`](16-architecture-deliverables/HLD-TEMPLATE.md) — High-Level Design document.
* [`LLD-TEMPLATE.md`](16-architecture-deliverables/LLD-TEMPLATE.md) — Low-Level Design document.
* [`API-DESIGN-TEMPLATE.md`](16-architecture-deliverables/API-DESIGN-TEMPLATE.md) — Enterprise API specification.
* [`DATA-DESIGN-TEMPLATE.md`](16-architecture-deliverables/DATA-DESIGN-TEMPLATE.md) — Data schema, topology, and persistence design.
* [`SECURITY-DESIGN-TEMPLATE.md`](16-architecture-deliverables/SECURITY-DESIGN-TEMPLATE.md) — Security & threat modeling blueprint.
* [`DEPLOYMENT-DESIGN-TEMPLATE.md`](16-architecture-deliverables/DEPLOYMENT-DESIGN-TEMPLATE.md) — Infrastructure deployment & topology blueprint.
* [`INTEGRATION-DESIGN-TEMPLATE.md`](16-architecture-deliverables/INTEGRATION-DESIGN-TEMPLATE.md) — Point-to-point & event integration contract.
* [`ARCHITECTURE-REVIEW-TEMPLATE.md`](16-architecture-deliverables/ARCHITECTURE-REVIEW-TEMPLATE.md) — Architecture Review Board (ARB) submission.
* [`RISK-REGISTER-TEMPLATE.md`](16-architecture-deliverables/RISK-REGISTER-TEMPLATE.md) — Enterprise technical risk register.
* [`REFERENCE-ARCHITECTURE-TEMPLATE.md`](16-architecture-deliverables/REFERENCE-ARCHITECTURE-TEMPLATE.md) — Industry reference architecture template.
* [`CASE-STUDY-TEMPLATE.md`](16-architecture-deliverables/CASE-STUDY-TEMPLATE.md) — Post-mortem and transformation case study.
* [`SYSTEM-DESIGN-TEMPLATE.md`](16-architecture-deliverables/SYSTEM-DESIGN-TEMPLATE.md) — System design blueprint.

---

## 17. Architecture Diagrams & C4 Model
*Visual architecture documentation standards and visual templates.*

### The C4 Model (`17-diagrams/c4/`)
* [`c4-overview.md`](17-diagrams/c4/c4-overview.md) — Four levels of zoom, map analogies, core diagramming rules.
* [`context-diagram.md`](17-diagrams/c4/context-diagram.md) — Level 1: System Context diagram guide and enterprise banking example.
* [`container-diagram.md`](17-diagrams/c4/container-diagram.md) — Level 2: Container diagram guide, deployable units, technologies, and protocols.
* [`component-diagram.md`](17-diagrams/c4/component-diagram.md) — Level 3: Component diagram guide, internal modularity, and Spring Boot API example.
* [`code-diagram.md`](17-diagrams/c4/code-diagram.md) — Level 4: Code/Class diagram guide, when to use vs. avoid, UML modeling.
* [`c4-model-guidelines.md`](17-diagrams/c4/c4-model-guidelines.md) — 10 Commandments of C4 diagramming, visual conventions, Mermaid vs. Structurizr.

---

## 21. Architecture Tools & Checklists
*Production review checklists, sizing tools, and generators.*

### Production Review Checklists (`21-architecture-tools/checklists/`)
* [`architecture-review-checklist.md`](21-architecture-tools/checklists/architecture-review-checklist.md) — Comprehensive ARB review scorecard.
* [`solution-architecture-checklist.md`](21-architecture-tools/checklists/solution-architecture-checklist.md) — Pre-implementation SAD quality gate.
* [`microservices-checklist.md`](21-architecture-tools/checklists/microservices-checklist.md) — Microservice design and readiness verification.
* [`api-review-checklist.md`](21-architecture-tools/checklists/api-review-checklist.md) — API contract, security, and versioning standards.
* [`database-review-checklist.md`](21-architecture-tools/checklists/database-review-checklist.md) — Database schema, indexing, and query hygiene.
* [`security-review-checklist.md`](21-architecture-tools/checklists/security-review-checklist.md) — Application and infrastructure security assessment.
* [`cloud-architecture-checklist.md`](21-architecture-tools/checklists/cloud-architecture-checklist.md) — Well-Architected cloud posture review.
* [`production-readiness-checklist.md`](21-architecture-tools/checklists/production-readiness-checklist.md) — Go-live and production launch verification.
* [`disaster-recovery-checklist.md`](21-architecture-tools/checklists/disaster-recovery-checklist.md) — DR readiness, failover validation, RPO/RTO testing.
* [`observability-checklist.md`](21-architecture-tools/checklists/observability-checklist.md) — Metrics, tracing, logging, and alerting coverage.

---

## 22. Reference
*Authoritative cheatsheets, comparison tables, and technology compendiums.*

### Pattern Comparisons (`22-reference/pattern-comparison/`)
* [`monolith-vs-microservices.md`](22-reference/pattern-comparison/monolith-vs-microservices.md) — Monolith vs. Microservices deep comparison.
* [`modular-monolith-vs-microservices.md`](22-reference/pattern-comparison/modular-monolith-vs-microservices.md) — Modular Monolith vs. Microservices comparison.

### Technology Comparisons (`22-reference/technology-comparison/`)
* [`rest-vs-grpc.md`](22-reference/technology-comparison/rest-vs-grpc.md) — REST vs. gRPC comparative analysis.
* [`sql-vs-nosql.md`](22-reference/technology-comparison/sql-vs-nosql.md) — Relational SQL vs. NoSQL database comparison.
* [`sync-vs-async.md`](22-reference/technology-comparison/sync-vs-async.md) — Synchronous vs. Asynchronous communication comparison.
* [`queue-vs-stream.md`](22-reference/technology-comparison/queue-vs-stream.md) — Message Queues vs. Event Streams comparison.
* [`centralized-vs-distributed.md`](22-reference/technology-comparison/centralized-vs-distributed.md) — Centralized vs. Distributed architecture comparison.

### Glossaries & Acronyms
* [`architecture-glossary.md`](22-reference/glossaries/architecture-glossary.md) — Authoritative enterprise architecture terminology definitions.
* [`architecture-acronyms.md`](22-reference/acronyms/architecture-acronyms.md) — Master enterprise architecture acronym dictionary.

---

## Additional Domains (Scheduled for Phases 3–10)
* [`03-backend/`](03-backend/) — Enterprise runtime platforms (.NET, Java, Python, Go, Node.js).
* [`04-frontend/`](04-frontend/) — Frontend architectures (React, Angular, Micro-frontends).
* [`05-mobile/`](05-mobile/) — Mobile architecture (iOS, Android, Flutter, React Native).
* [`06-data/`](06-data/) — Data pipelines, Warehousing, Lakes, Meshes, and Analytics.
* [`07-integration/`](07-integration/) — Messaging, Event streaming, API Gateways, Service Meshes.
* [`08-cloud/`](08-cloud/) — AWS, Azure, GCP well-architected blueprints, FinOps.
* [`09-devops/`](09-devops/) — Platform engineering, GitOps, CI/CD, Kubernetes.
* [`10-security/`](10-security/) — Zero trust, IAM, DevSecOps, AppSec.
* [`11-observability/`](11-observability/) — Telemetry, Prometheus, Grafana, OpenTelemetry, SRE.
* [`12-ai/`](12-ai/) — GenAI, LLM architectures, RAG systems, Model serving.
* [`14-enterprise-integration/`](14-enterprise-integration/) — ERP, CRM, Core Banking, Healthcare.
* [`15-modernization/`](15-modernization/) — Legacy decommissioning, cloud migration frameworks.
* [`18-reference-architectures/`](18-reference-architectures/) — Full industry blueprints.
* [`19-case-studies/`](19-case-studies/) — Real-world production case studies.
* [`20-interview-system-design/`](20-interview-system-design/) — Architect interview guide.
* [`99-experiments/`](99-experiments/) — POC sandbox.
