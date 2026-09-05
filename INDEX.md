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


### Distributed Systems Design Principles (`00-foundations/distributed-systems/design-principles/`)
* [`README.md`](00-foundations/distributed-systems/design-principles/README.md) — Architectural principles catalog and core philosophy.
* [`stateless-architecture.md`](00-foundations/distributed-systems/design-principles/stateless-architecture.md) — Externalizing state from compute tiers for horizontal elasticity.
* [`share-nothing-architecture.md`](00-foundations/distributed-systems/design-principles/share-nothing-architecture.md) — Linear scaling without cross-node synchronization bottlenecks.
* [`idempotency.md`](00-foundations/distributed-systems/design-principles/idempotency.md) — Repeated operations yielding identical state under retries.
* [`immutability.md`](00-foundations/distributed-systems/design-principles/immutability.md) — Append-only state transitions and zero lock contention.
* [`event-driven-architecture.md`](00-foundations/distributed-systems/design-principles/event-driven-architecture.md) — Asynchronous choreography over RPC orchestration.
* [`loose-coupling.md`](00-foundations/distributed-systems/design-principles/loose-coupling.md) — Spatial, temporal, and platform decoupling.
* [`high-cohesion.md`](00-foundations/distributed-systems/design-principles/high-cohesion.md) — Grouping elements that change together within bounded contexts.
* [`separation-of-concerns.md`](00-foundations/distributed-systems/design-principles/separation-of-concerns.md) — Layered separation from edge to domain logic.
* [`single-responsibility.md`](00-foundations/distributed-systems/design-principles/single-responsibility.md) — Single reason to change at microservice boundaries.
* [`graceful-degradation.md`](00-foundations/distributed-systems/design-principles/graceful-degradation.md) — High availability under partial infrastructure failure.
* [`fail-fast.md`](00-foundations/distributed-systems/design-principles/fail-fast.md) — Surfacing validation errors immediately at boundaries.
* [`defense-in-depth.md`](00-foundations/distributed-systems/design-principles/defense-in-depth.md) — Multi-layered perimeter, transport, and data security.
* [`observability-first.md`](00-foundations/distributed-systems/design-principles/observability-first.md) — Telemetry as a first-class architectural citizen.
* [`evolutionary-architecture.md`](00-foundations/distributed-systems/design-principles/evolutionary-architecture.md) — Designing for incremental, guided change.
* [`simplicity.md`](00-foundations/distributed-systems/design-principles/simplicity.md) — Eliminating accidental complexity via Occam's razor.

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


### Scale Estimation & Sizing (`02-system-design/scale-estimation/`)
* [`README.md`](02-system-design/scale-estimation/README.md) — Scale estimation methodology and back-of-the-envelope formulas.
* Detailed estimation guides: [`traffic-estimation.md`](02-system-design/scale-estimation/traffic-estimation.md), [`storage-estimation.md`](02-system-design/scale-estimation/storage-estimation.md), [`bandwidth-estimation.md`](02-system-design/scale-estimation/bandwidth-estimation.md), [`cache-capacity.md`](02-system-design/scale-estimation/cache-capacity.md), [`database-capacity.md`](02-system-design/scale-estimation/database-capacity.md), [`growth-projection.md`](02-system-design/scale-estimation/growth-projection.md).

### Capacity Planning (`02-system-design/capacity-planning/`)
* [`capacity-planning-overview.md`](02-system-design/capacity-planning/capacity-planning-overview.md) — Production capacity planning frameworks.
* Subsystem sizing: [`compute-capacity.md`](02-system-design/capacity-planning/compute-capacity.md), [`database-capacity.md`](02-system-design/capacity-planning/database-capacity.md), [`cache-capacity.md`](02-system-design/capacity-planning/cache-capacity.md), [`message-queue-capacity.md`](02-system-design/capacity-planning/message-queue-capacity.md), [`capacity-testing.md`](02-system-design/capacity-planning/capacity-testing.md).

### Scalability (`02-system-design/scalability/`)
* [`README.md`](02-system-design/scalability/README.md) — Horizontal scaling patterns, elasticity, and partitioning.
* Scaling blueprints: [`horizontal-scaling.md`](02-system-design/scalability/horizontal-scaling.md), [`stateless-services.md`](02-system-design/scalability/stateless-services.md), [`database-scaling.md`](02-system-design/scalability/database-scaling.md), [`sharding.md`](02-system-design/scalability/sharding.md), [`replication.md`](02-system-design/scalability/replication.md), [`hotspot-management.md`](02-system-design/scalability/hotspot-management.md).

### Performance (`02-system-design/performance/`)
* [`README.md`](02-system-design/performance/README.md) — Latency optimization, tail-latency reduction, and profiling.
* Guides: [`latency.md`](02-system-design/performance/latency.md), [`throughput.md`](02-system-design/performance/throughput.md), [`tail-latency.md`](02-system-design/performance/tail-latency.md), [`connection-pools.md`](02-system-design/performance/connection-pools.md), [`load-testing.md`](02-system-design/performance/load-testing.md).

### Reliability (`02-system-design/reliability/`)
* [`README.md`](02-system-design/reliability/README.md) — Fault tolerance, high availability modeling, and circuit breakers.
* Resilience patterns: [`circuit-breaker.md`](02-system-design/reliability/circuit-breaker.md), [`bulkheads.md`](02-system-design/reliability/bulkheads.md), [`rate-limiting.md`](02-system-design/reliability/rate-limiting.md), [`backpressure.md`](02-system-design/reliability/backpressure.md), [`chaos-engineering.md`](02-system-design/reliability/chaos-engineering.md).

### Distributed Caching (`02-system-design/caching/`)
* [`README.md`](02-system-design/caching/README.md) — Cache-aside, write-through, write-behind, eviction algorithms.
* Caching mechanics: [`cache-aside.md`](02-system-design/caching/cache-aside.md), [`cache-stampede.md`](02-system-design/caching/cache-stampede.md), [`distributed-cache.md`](02-system-design/caching/distributed-cache.md), [`redis-architecture.md`](02-system-design/caching/redis-architecture.md).

### Real-Time Architectures (`02-system-design/real-time/`)
* [`README.md`](02-system-design/real-time/README.md) — WebSockets, SSE, long-polling, presence tracking, and chat architecture.

### Job & Batch Processing (`02-system-design/job-processing/`)
* [`README.md`](02-system-design/job-processing/README.md) — Asynchronous task queues, distributed cron, and worker pools.

### Multi-Tenancy (`02-system-design/multi-tenancy/`)
* [`README.md`](02-system-design/multi-tenancy/README.md) — Tenant isolation models, cell-based architecture, noisy neighbor mitigation.

### Search Architecture (`02-system-design/search/`)
* [`README.md`](02-system-design/search/README.md) — Inverted indexes, BM25 ranking, typeahead, Elasticsearch architecture.

### File & Object Storage (`02-system-design/file-storage/`)
* [`README.md`](02-system-design/file-storage/README.md) — Chunked upload, presigned URLs, S3 architecture, storage tiering.

### Failure Engineering (`02-system-design/failure-engineering/`)
* [`README.md`](02-system-design/failure-engineering/README.md) — Split-brain, thundering herd, cascading collapse, clock drift, gray failures.

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

### Engineering Calculators (`21-architecture-tools/calculators/`)
* [`README.md`](21-architecture-tools/calculators/README.md) — Master catalog of capacity and sizing calculators.
* Models: [`traffic-calculator.md`](21-architecture-tools/calculators/traffic-calculator.md), [`storage-calculator.md`](21-architecture-tools/calculators/storage-calculator.md), [`bandwidth-calculator.md`](21-architecture-tools/calculators/bandwidth-calculator.md), [`cache-calculator.md`](21-architecture-tools/calculators/cache-calculator.md), [`database-sizing-calculator.md`](21-architecture-tools/calculators/database-sizing-calculator.md), [`availability-calculator.md`](21-architecture-tools/calculators/availability-calculator.md), [`latency-budget-calculator.md`](21-architecture-tools/calculators/latency-budget-calculator.md), [`cost-estimator.md`](21-architecture-tools/calculators/cost-estimator.md).

### System Design Checklists (`21-architecture-tools/checklists/system-design/`)
* [`README.md`](21-architecture-tools/checklists/system-design/README.md) — 13-stage lifecycle design checklists.
* Checklists: [`requirements-checklist.md`](21-architecture-tools/checklists/system-design/requirements-checklist.md), [`scale-estimation-checklist.md`](21-architecture-tools/checklists/system-design/scale-estimation-checklist.md), [`api-design-checklist.md`](21-architecture-tools/checklists/system-design/api-design-checklist.md), [`data-model-checklist.md`](21-architecture-tools/checklists/system-design/data-model-checklist.md), [`high-level-design-checklist.md`](21-architecture-tools/checklists/system-design/high-level-design-checklist.md), [`detailed-design-checklist.md`](21-architecture-tools/checklists/system-design/detailed-design-checklist.md), [`scalability-checklist.md`](21-architecture-tools/checklists/system-design/scalability-checklist.md), [`reliability-checklist.md`](21-architecture-tools/checklists/system-design/reliability-checklist.md), [`performance-checklist.md`](21-architecture-tools/checklists/system-design/performance-checklist.md), [`security-checklist.md`](21-architecture-tools/checklists/system-design/security-checklist.md), [`observability-checklist.md`](21-architecture-tools/checklists/system-design/observability-checklist.md), [`resilience-checklist.md`](21-architecture-tools/checklists/system-design/resilience-checklist.md), [`production-readiness-checklist.md`](21-architecture-tools/checklists/system-design/production-readiness-checklist.md).


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


---

## 06. Data Architecture & Persistence
*Distributed data, consistency models, and transaction management.*

### Distributed Data (`06-data/distributed-data/`)
* [`README.md`](06-data/distributed-data/README.md) — Consistency continuum, distributed consensus, and transaction protocols.
* Theorems: [`cap-theorem.md`](06-data/distributed-data/cap-theorem.md), [`pacelc-theorem.md`](06-data/distributed-data/pacelc-theorem.md), [`acid-vs-base.md`](06-data/distributed-data/acid-vs-base.md).
* Consistency models: [`strong-consistency.md`](06-data/distributed-data/strong-consistency.md), [`eventual-consistency.md`](06-data/distributed-data/eventual-consistency.md), [`causal-consistency.md`](06-data/distributed-data/causal-consistency.md).
* Transactions & Consensus: [`distributed-transactions.md`](06-data/distributed-data/distributed-transactions.md), [`two-phase-commit.md`](06-data/distributed-data/two-phase-commit.md), [`saga-pattern.md`](06-data/distributed-data/saga-pattern.md), [`outbox-pattern.md`](06-data/distributed-data/outbox-pattern.md), [`raft.md`](06-data/distributed-data/raft.md), [`paxos.md`](06-data/distributed-data/paxos.md).

---

## 07. Integration Architecture & Messaging
*Enterprise integration, event streaming, REST standards, and API gateways.*

### Messaging & Event Streaming (`07-integration/messaging/`)
* [`README.md`](07-integration/messaging/README.md) — Message brokers, event logs, delivery guarantees, and CDC.
* Broker Architectures: [`kafka-architecture.md`](07-integration/messaging/kafka-architecture.md), [`rabbitmq-architecture.md`](07-integration/messaging/rabbitmq-architecture.md).
* Guarantees & Patterns: [`ordering-guarantees.md`](07-integration/messaging/ordering-guarantees.md), [`exactly-once.md`](07-integration/messaging/exactly-once.md), [`idempotent-consumer.md`](07-integration/messaging/idempotent-consumer.md), [`cdc.md`](07-integration/messaging/cdc.md).

### REST Architecture (`07-integration/rest/`)
* [`README.md`](07-integration/rest/README.md) — REST principles, resource modeling, versioning, pagination, idempotency.

### API Gateway (`07-integration/api-gateway/`)
* [`README.md`](07-integration/api-gateway/README.md) — Edge gateway patterns, reverse proxies, BFF, Envoy vs. Kong.

---

## 15. Modernization & System Evolution
*Deconstructing legacy monoliths and executing zero-downtime transformations.*

### System Evolution (`15-modernization/system-evolution/`)
* [`README.md`](15-modernization/system-evolution/README.md) — Modernization principles and migration playbooks.
* Playbooks: [`monolith-to-microservices.md`](15-modernization/system-evolution/monolith-to-microservices.md), [`database-decomposition.md`](15-modernization/system-evolution/database-decomposition.md), [`event-driven-migration.md`](15-modernization/system-evolution/event-driven-migration.md), [`sync-to-async.md`](15-modernization/system-evolution/sync-to-async.md), [`cache-introduction.md`](15-modernization/system-evolution/cache-introduction.md), [`sharding-migration.md`](15-modernization/system-evolution/sharding-migration.md), [`read-write-splitting.md`](15-modernization/system-evolution/read-write-splitting.md), [`zero-downtime-migration.md`](15-modernization/system-evolution/zero-downtime-migration.md), [`strangler-fig-pattern.md`](15-modernization/system-evolution/strangler-fig-pattern.md), [`anti-corruption-layer.md`](15-modernization/system-evolution/anti-corruption-layer.md).

---

## 18. Reference Architectures
*Production-grade 26-section reference architecture blueprints.*

### System Design Reference Architectures (`18-reference-architectures/system-design/`)
* [`README.md`](18-reference-architectures/system-design/README.md) — Master catalog of 30 system design blueprints.
* Tier 1 Blueprints: [`url-shortener.md`](18-reference-architectures/system-design/url-shortener.md), [`rate-limiter.md`](18-reference-architectures/system-design/rate-limiter.md), [`notification-service.md`](18-reference-architectures/system-design/notification-service.md), [`distributed-cache.md`](18-reference-architectures/system-design/distributed-cache.md), [`key-value-store.md`](18-reference-architectures/system-design/key-value-store.md), [`chat-application.md`](18-reference-architectures/system-design/chat-application.md).
* Streaming & Content: [`video-streaming-platform.md`](18-reference-architectures/system-design/video-streaming-platform.md), [`social-media-feed.md`](18-reference-architectures/system-design/social-media-feed.md), [`content-delivery-network.md`](18-reference-architectures/system-design/content-delivery-network.md).
* Mobility & Commerce: [`ride-sharing-service.md`](18-reference-architectures/system-design/ride-sharing-service.md), [`e-commerce-platform.md`](18-reference-architectures/system-design/e-commerce-platform.md), [`payment-system.md`](18-reference-architectures/system-design/payment-system.md).
* Enterprise & Data: [`search-autocomplete.md`](18-reference-architectures/system-design/search-autocomplete.md), [`ad-click-aggregation.md`](18-reference-architectures/system-design/ad-click-aggregation.md), [`distributed-task-scheduler.md`](18-reference-architectures/system-design/distributed-task-scheduler.md), [`iot-data-platform.md`](18-reference-architectures/system-design/iot-data-platform.md).

---

## 19. Real-World Case Studies
*Deep-dive retrospectives of planetary-scale production systems.*

### System Design Case Studies (`19-case-studies/system-design/`)
* [`README.md`](19-case-studies/system-design/README.md) — Real-world case studies index and analytical schema.
* Deep Dives: [`netflix-video-streaming.md`](19-case-studies/system-design/netflix-video-streaming.md), [`uber-dispatch-system.md`](19-case-studies/system-design/uber-dispatch-system.md), [`twitter-timeline-service.md`](19-case-studies/system-design/twitter-timeline-service.md), [`amazon-shopping-cart.md`](19-case-studies/system-design/amazon-shopping-cart.md), [`stripe-payment-infrastructure.md`](19-case-studies/system-design/stripe-payment-infrastructure.md), [`whatsapp-messaging-architecture.md`](19-case-studies/system-design/whatsapp-messaging-architecture.md), [`airbnb-booking-engine.md`](19-case-studies/system-design/airbnb-booking-engine.md), [`spotify-music-streaming.md`](19-case-studies/system-design/spotify-music-streaming.md), [`youtube-video-pipeline.md`](19-case-studies/system-design/youtube-video-pipeline.md), [`slack-realtime-messaging.md`](19-case-studies/system-design/slack-realtime-messaging.md).

---

## 20. System Design Interview Playbook
*Staff+ and Principal Architect interview preparation and scoring rubrics.*

### System Design Interview Mastery (`20-interview-system-design/system-design/`)
* [`README.md`](20-interview-system-design/system-design/README.md) — Curriculum overview and scoring pillars.
* Core Guides: [`interview-framework.md`](20-interview-system-design/system-design/interview-framework.md), [`time-management.md`](20-interview-system-design/system-design/time-management.md), [`clarifying-questions.md`](20-interview-system-design/system-design/clarifying-questions.md), [`scale-estimation.md`](20-interview-system-design/system-design/scale-estimation.md), [`api-design.md`](20-interview-system-design/system-design/api-design.md), [`data-modeling.md`](20-interview-system-design/system-design/data-modeling.md), [`high-level-design.md`](20-interview-system-design/system-design/high-level-design.md), [`deep-dive.md`](20-interview-system-design/system-design/deep-dive.md), [`trade-off-discussion.md`](20-interview-system-design/system-design/trade-off-discussion.md), [`common-mistakes.md`](20-interview-system-design/system-design/common-mistakes.md), [`evaluation-criteria.md`](20-interview-system-design/system-design/evaluation-criteria.md), [`faang-rubric.md`](20-interview-system-design/system-design/faang-rubric.md), [`mock-interview-guide.md`](20-interview-system-design/system-design/mock-interview-guide.md).

---


---

## 03. Backend Platforms & Runtime Architecture
*Enterprise backend runtimes, internals, data access, concurrency, performance, and security.*

### .NET Enterprise Architecture (`03-backend/dotnet/`)
* [`README.md`](03-backend/dotnet/README.md) — .NET enterprise runtime landscape, CLR internals, and architecture guide.
* Architecture: [`clr-internals.md`](03-backend/dotnet/architecture/clr-internals.md), [`garbage-collection.md`](03-backend/dotnet/architecture/garbage-collection.md), [`memory-management.md`](03-backend/dotnet/architecture/memory-management.md), [`threading-and-concurrency.md`](03-backend/dotnet/architecture/threading-and-concurrency.md), [`async-await.md`](03-backend/dotnet/architecture/async-await.md), [`dependency-injection.md`](03-backend/dotnet/architecture/dependency-injection.md), [`configuration.md`](03-backend/dotnet/architecture/configuration.md), [`middleware-pipeline.md`](03-backend/dotnet/architecture/middleware-pipeline.md), [`options-pattern.md`](03-backend/dotnet/architecture/options-pattern.md), [`hosted-services.md`](03-backend/dotnet/architecture/hosted-services.md), [`clean-architecture.md`](03-backend/dotnet/architecture/clean-architecture.md), [`modular-monolith.md`](03-backend/dotnet/architecture/modular-monolith.md), [`vertical-slices.md`](03-backend/dotnet/architecture/vertical-slices.md), [`cqrs.md`](03-backend/dotnet/architecture/cqrs.md), [`domain-events.md`](03-backend/dotnet/architecture/domain-events.md), [`fitness-functions.md`](03-backend/dotnet/architecture/fitness-functions.md), [`netarchtest.md`](03-backend/dotnet/architecture/netarchtest.md), [`anti-patterns.md`](03-backend/dotnet/architecture/anti-patterns.md).
* Data, APIs, Resilience, Testing, Performance, Security: [`03-backend/dotnet/data/`](03-backend/dotnet/data/), [`03-backend/dotnet/api/`](03-backend/dotnet/api/), [`03-backend/dotnet/resilience/`](03-backend/dotnet/resilience/), [`03-backend/dotnet/testing/`](03-backend/dotnet/testing/), [`03-backend/dotnet/performance/`](03-backend/dotnet/performance/), [`03-backend/dotnet/security/`](03-backend/dotnet/security/).

### Java Enterprise Architecture (`03-backend/java/`)
* [`README.md`](03-backend/java/README.md) — JVM runtime ecosystem, Spring Boot 3, memory hierarchy, and GC tuning.
* Architecture: [`jvm-internals.md`](03-backend/java/architecture/jvm-internals.md), [`garbage-collection.md`](03-backend/java/architecture/garbage-collection.md), [`memory-management.md`](03-backend/java/architecture/memory-management.md), [`threads-and-concurrency.md`](03-backend/java/architecture/threads-and-concurrency.md), [`virtual-threads.md`](03-backend/java/architecture/virtual-threads.md), [`spring-boot-architecture.md`](03-backend/java/architecture/spring-boot-architecture.md), [`spring-framework.md`](03-backend/java/architecture/spring-framework.md), [`dependency-injection.md`](03-backend/java/architecture/dependency-injection.md), [`hexagonal-architecture.md`](03-backend/java/architecture/hexagonal-architecture.md), [`spring-modulith.md`](03-backend/java/architecture/spring-modulith.md), [`archunit.md`](03-backend/java/architecture/archunit.md), [`anti-patterns.md`](03-backend/java/architecture/anti-patterns.md).
* Data, APIs, Resilience, Testing, Performance, Security: [`03-backend/java/data/`](03-backend/java/data/), [`03-backend/java/api/`](03-backend/java/api/), [`03-backend/java/resilience/`](03-backend/java/resilience/), [`03-backend/java/testing/`](03-backend/java/testing/), [`03-backend/java/performance/`](03-backend/java/performance/), [`03-backend/java/security/`](03-backend/java/security/).

### Python Enterprise Architecture (`03-backend/python/`)
* [`README.md`](03-backend/python/README.md) — Python runtime internals, GIL, async concurrency, and enterprise frameworks.
* Architecture: [`cpython-internals.md`](03-backend/python/architecture/cpython-internals.md), [`gil.md`](03-backend/python/architecture/gil.md), [`memory-management.md`](03-backend/python/architecture/memory-management.md), [`asyncio-architecture.md`](03-backend/python/architecture/asyncio-architecture.md), [`multiprocessing-vs-threading.md`](03-backend/python/architecture/multiprocessing-vs-threading.md), [`typing-and-contracts.md`](03-backend/python/architecture/typing-and-contracts.md), [`dependency-injection.md`](03-backend/python/architecture/dependency-injection.md), [`clean-architecture.md`](03-backend/python/architecture/clean-architecture.md), [`fastapi-architecture.md`](03-backend/python/architecture/fastapi-architecture.md), [`django-architecture.md`](03-backend/python/architecture/django-architecture.md), [`anti-patterns.md`](03-backend/python/architecture/anti-patterns.md).
* APIs, Data, Resilience, Testing, Performance, Security: [`03-backend/python/api/`](03-backend/python/api/), [`03-backend/python/data/`](03-backend/python/data/), [`03-backend/python/resilience/`](03-backend/python/resilience/), [`03-backend/python/testing/`](03-backend/python/testing/), [`03-backend/python/performance/`](03-backend/python/performance/), [`03-backend/python/security/`](03-backend/python/security/).

### Node.js Enterprise Architecture (`03-backend/nodejs/`)
* [`README.md`](03-backend/nodejs/README.md) — V8 engine internals, event loop mechanics, libuv, and enterprise TypeScript backends.
* Architecture: [`v8-internals.md`](03-backend/nodejs/architecture/v8-internals.md), [`event-loop.md`](03-backend/nodejs/architecture/event-loop.md), [`libuv-architecture.md`](03-backend/nodejs/architecture/libuv-architecture.md), [`memory-management.md`](03-backend/nodejs/architecture/memory-management.md), [`concurrency-model.md`](03-backend/nodejs/architecture/concurrency-model.md), [`worker-threads.md`](03-backend/nodejs/architecture/worker-threads.md), [`cluster-architecture.md`](03-backend/nodejs/architecture/cluster-architecture.md), [`streams-architecture.md`](03-backend/nodejs/architecture/streams-architecture.md), [`async-hooks.md`](03-backend/nodejs/architecture/async-hooks.md), [`typescript-architecture.md`](03-backend/nodejs/architecture/typescript-architecture.md), [`nestjs-architecture.md`](03-backend/nodejs/architecture/nestjs-architecture.md), [`express-architecture.md`](03-backend/nodejs/architecture/express-architecture.md), [`fastify-architecture.md`](03-backend/nodejs/architecture/fastify-architecture.md), [`clean-architecture.md`](03-backend/nodejs/architecture/clean-architecture.md), [`anti-patterns.md`](03-backend/nodejs/architecture/anti-patterns.md).
* APIs, Data, Testing, Performance, Security: [`03-backend/nodejs/api/`](03-backend/nodejs/api/), [`03-backend/nodejs/data/`](03-backend/nodejs/data/), [`03-backend/nodejs/testing/`](03-backend/nodejs/testing/), [`03-backend/nodejs/performance/`](03-backend/nodejs/performance/), [`03-backend/nodejs/security/`](03-backend/nodejs/security/).

### Common Backend Patterns & Comparisons (`03-backend/common-patterns/`)
* [`README.md`](03-backend/common-patterns/README.md) — 18 Universal cross-language design patterns and runtime trade-offs.
* Technology Comparisons: [`dotnet-vs-java.md`](03-backend/common-patterns/technology-comparison/dotnet-vs-java.md), [`dotnet-vs-python.md`](03-backend/common-patterns/technology-comparison/dotnet-vs-python.md), [`dotnet-vs-nodejs.md`](03-backend/common-patterns/technology-comparison/dotnet-vs-nodejs.md), [`java-vs-python.md`](03-backend/common-patterns/technology-comparison/java-vs-python.md), [`java-vs-nodejs.md`](03-backend/common-patterns/technology-comparison/java-vs-nodejs.md), [`python-vs-nodejs.md`](03-backend/common-patterns/technology-comparison/python-vs-nodejs.md).

---

## 04. Frontend Architecture
*Enterprise single-page apps, SSR, micro-frontends, state management, and web performance.*

### Frontend Architecture Core & API Clients (`04-frontend/frontend-architecture/` & `api-client-architecture/`)
* [`frontend-architecture/README.md`](04-frontend/frontend-architecture/README.md) — Rendering strategies (SPA, SSR, SSG, ISR), micro-frontends, module federation, and design systems.
* [`api-client-architecture/README.md`](04-frontend/api-client-architecture/README.md) — HTTP client architecture, OpenAPI SDK generation, auth tokens, caching, retries, and offline queuing.

### React Enterprise Architecture (`04-frontend/react/`)
* [`README.md`](04-frontend/react/README.md) — Fiber reconciliation, concurrent mode, Server Components (RSC), hooks architecture, scalability, and security.

### Angular Enterprise Architecture (`04-frontend/angular/`)
* [`README.md`](04-frontend/angular/README.md) — Standalone components, Signals, OnPush change detection, dependency injection, Nx monorepos, and enterprise security.

### State Management & Web Performance (`04-frontend/state-management/` & `web-performance/`)
* [`state-management/README.md`](04-frontend/state-management/README.md) — Server state vs client state, Redux Toolkit, Zustand, Signals, optimistic updates.
* [`web-performance/README.md`](04-frontend/web-performance/README.md) — Core Web Vitals (LCP, INP, CLS), bundle optimization, code splitting, lazy loading, and asset caching.

---

## 05. Mobile Architecture
*Enterprise cross-platform mobile architectures, native bridge internals, offline synchronization, and security.*

### Mobile Architecture Core (`05-mobile/mobile-architecture/`)
* [`README.md`](05-mobile/mobile-architecture/README.md) — Native vs Cross-Platform, offline-first synchronization, local SQLite persistence, background tasks, and battery optimization.

### React Native Enterprise Architecture (`05-mobile/react-native/`)
* [`README.md`](05-mobile/react-native/README.md) — New Architecture (Fabric, TurboModules, JSI, Hermes), state management, navigation, testing, and security hardening.

---

## Application Reference Architectures, Case Studies & Deliverables
* **Application References**: [`18-reference-architectures/application/`](18-reference-architectures/application/) — .NET, Java, Python, Node, React, Angular reference blueprints.
* **Full-Stack References**: [`18-reference-architectures/full-stack/`](18-reference-architectures/full-stack/) — End-to-end full-stack architectures.
* **Application Case Studies**: [`19-case-studies/application-architecture/`](19-case-studies/application-architecture/) — 10 Real-world transformation case studies.
* **Application Review Checklists**: [`21-architecture-tools/checklists/application/`](21-architecture-tools/checklists/application/) — 16 Specialized review checklists.
* **Architecture Decision Records**: [`16-architecture-deliverables/adr/`](16-architecture-deliverables/adr/) — ADR-0010 through ADR-0020.
* **Technology Comparisons**: [`22-reference/technology-comparison/application-architecture/`](22-reference/technology-comparison/application-architecture/) — 9 Rigorous comparative matrices.
* **ARB Review Specification**: [`16-architecture-deliverables/architecture-review/application-architecture-review.md`](16-architecture-deliverables/architecture-review/application-architecture-review.md).


---

## 06. Data Architecture & Persistence
*Enterprise data architecture, modeling, mapping, SQL/NoSQL engines, consistency, CDC, streaming, and lakehouses.*

### Data Architecture & Governance (`06-data/data-architecture/`, `governance/`, `lineage/`, `data-quality/`)
* [`data-architecture/README.md`](06-data/data-architecture/README.md) — Enterprise data taxonomy, lifecycle, sensitivity classification, contracts, and data products.
* [`governance/README.md`](06-data/governance/README.md) — Enterprise data governance frameworks, catalogs, and stewardship models.
* [`lineage/README.md`](06-data/lineage/README.md) — Technical, business, and column-level lineage tracking for regulatory auditability and impact analysis.
* [`data-quality/README.md`](06-data/data-quality/README.md) — Six dimensions of data quality, automated assertion tests, and quarantine workflows.

### Data Modeling & Mapping (`06-data/data-modeling/`, `data-mapping/`)
* [`data-modeling/README.md`](06-data/data-modeling/README.md) — Relational, document, key-value, wide-column, graph, time-series, and Data Vault 2.0 modeling.
* [`data-mapping/README.md`](06-data/data-mapping/README.md) — Source-to-target mapping, canonical models, code translation, settlement and reconciliation mappings.
* [Data Mapping Specification Template](16-architecture-deliverables/DATA-MAPPING-TEMPLATE.md) — Reusable enterprise mapping specification deliverable.

### Database Architectures & Selection (`06-data/sql/`, `nosql/`, `database-selection/`, `data-access/`, `database-performance/`)
* [`sql/README.md`](06-data/sql/README.md) — Relational engine internals, ACID, isolation levels, locking, deadlocks, execution plans, connection pools, and PITR.
* [`nosql/README.md`](06-data/nosql/README.md) — Key-value, document, wide-column, graph, time-series, partition keys, and tunable consistency quorums.
* [`database-selection/README.md`](06-data/database-selection/README.md) — Objective multi-dimensional database selection framework and workload profiling.
* [`data-access/README.md`](06-data/data-access/README.md) — Repositories, Unit of Work, ORM vs micro-ORM, pagination, and N+1 query mitigation.
* [`database-performance/README.md`](06-data/database-performance/README.md) — Query execution plan analysis, slow query remediation, lock contention, and cache stampede prevention.

### Consistency, Distributed Transactions & Synchronization (`06-data/consistency/`, `distributed-transactions/`, `cdc/`, `data-synchronization/`)
* [`consistency/README.md`](06-data/consistency/README.md) — The consistency continuum: strong, eventual, causal, read-your-writes, and conflict resolution.
* [`distributed-transactions/README.md`](06-data/distributed-transactions/README.md) — 2PC, Saga orchestration/choreography, transactional outbox/inbox, and workflow engines.
* [`cdc/README.md`](06-data/cdc/README.md) — Log-based Change Data Capture (Debezium), CDC to Kafka/lakehouse, and zero-dual-write synchronization.
* [`data-synchronization/README.md`](06-data/data-synchronization/README.md) — One-way vs two-way sync, event-driven sync, and continuous data drift detection.

### Data Platforms, Streaming & Mesh (`06-data/data-platforms/`, `streaming/`, `etl-elt/`, `data-mesh/`, `mdm/`, `migration/`)
* [`data-platforms/README.md`](06-data/data-platforms/README.md) — Data lakes, warehouses, open lakehouses (Apache Iceberg), and operational data stores (ODS).
* [`streaming/README.md`](06-data/streaming/README.md) — Event streams vs queues, event time watermarks, tumbling/session windows, and stateful Flink processing.
* [`etl-elt/README.md`](06-data/etl-elt/README.md) — Cloud ELT pipelines, orchestration (Airflow/Dagster), dbt transformations, and idempotent backfills.
* [`data-mesh/README.md`](06-data/data-mesh/README.md) — Decentralized domain data products, self-service infrastructure, and federated computational governance.
* [`mdm/README.md`](06-data/mdm/README.md) — Master Data Management: Customer 360, Product Master, matching algorithms, and survivorship rules.
* [`migration/README.md`](06-data/migration/README.md) — Zero-downtime database migration playbook, dual-writing, CDC catch-up, and instant rollback.

---

## 07. Integration Architecture & Financial Systems
*Enterprise APIs, protocols, edge gateways, event-driven architecture, financial transactions, settlement, and reconciliation.*

### API Architecture, Protocols & Edge Governance (`07-integration/api/`, `rest/`, `graphql/`, `grpc/`, `api-gateway/`, `bff/`, `webhooks/`, `api-management/`)
* [`api/README.md`](07-integration/api/README.md) — API-first strategy, API as a product, lifecycle governance, versioning, and OpenAPI specs.
* [`rest/README.md`](07-integration/rest/README.md) — REST principles, resource modeling, status codes, pagination, rate limiting, and Problem Details.
* [`graphql/README.md`](07-integration/graphql/README.md) — Schema design, resolvers, DataLoader batching, query depth limits, and Apollo Federation.
* [`grpc/README.md`](07-integration/grpc/README.md) — Protocol Buffers, unary vs streaming RPC, deadlines, L7 load balancing (Envoy), and error models.
* [`api-gateway/README.md`](07-integration/api-gateway/README.md) — Edge gateway routing, rate limiting, authentication, and perimeter traffic enforcement.
* [`bff/README.md`](07-integration/bff/README.md) — Backend-for-Frontend architectures for web and mobile channels.
* [`webhooks/README.md`](07-integration/webhooks/README.md) — Webhook architecture, HMAC-SHA256 signatures, exponential retries, and consumer idempotency.
* [`api-management/README.md`](07-integration/api-management/README.md) — Developer portals, API subscriptions, consumer quotas, and usage analytics.

### Messaging & Event-Driven Architecture (`07-integration/event-driven/`, `kafka/`, `messaging/`, `patterns/`)
* [`event-driven/README.md`](07-integration/event-driven/README.md) — Events vs commands vs messages, choreography vs orchestration, and schema registry contracts.
* [`kafka/README.md`](07-integration/kafka/README.md) — Apache Kafka broker clustering, partition sizing, idempotency, consumer rebalancing, and KRaft.
* [`messaging/README.md`](07-integration/messaging/README.md) — RabbitMQ exchange topologies, routing, publisher confirms, and dead-letter queue governance.
* [`patterns/README.md`](07-integration/patterns/README.md) — Enterprise Integration Patterns (EIP): Content-Based Router, Splitter, Aggregator, Enricher, Wire Tap.

### System, Legacy & SaaS Integration (`07-integration/legacy/`, `saas/`)
* [`legacy/README.md`](07-integration/legacy/README.md) — Mainframe CICS/IMS integration, COBOL copybooks, flat-file batch interfaces, and Anti-Corruption Layers.
* [`saas/README.md`](07-integration/saas/README.md) — Third-party SaaS integration, OAuth token lifecycle, rate-limit resilience, and vendor outage circuit breaking.

### Financial Transactions, Settlement & Reconciliation (`07-integration/financial/`)
* [`financial/transactions/README.md`](07-integration/financial/transactions/README.md) — Transaction lifecycle, idempotency keys, integer minor unit precision, fees, taxes, and immutable audit ledgers.
* [`financial/settlement/README.md`](07-integration/financial/settlement/README.md) — Gross vs net settlement, T+0/T+1/T+2 cycles, settlement batches, ISO 20022 banking files, and settlement finality.
* [`financial/reconciliation/README.md`](07-integration/financial/reconciliation/README.md) — Automated reconciliation platform, matching engines (exact, rule-based, tolerance), 1:1 vs N:M matching, exception queues, and four-eyes adjustment workflows.

### Cross-Cutting Integration Standards (`07-integration/`)
* [Integration Decision Framework](07-integration/integration-decision-framework.md) — Multi-dimensional decision matrix for APIs, events, streaming, and messaging.
* [Integration Security Architecture](07-integration/integration-security.md) — Zero-trust integration security, mTLS, and webhook signature verification.
* [Integration Observability Architecture](07-integration/integration-observability.md) — W3C distributed tracing, OpenTelemetry, and integration health metrics.
* [Integration Failure Engineering](07-integration/failure-engineering.md) — Circuit breakers, timeouts, exponential backoff with jitter, and bulkhead isolation.

---

## 10. Security & Zero Trust Additions
* [`10-security/data-security/README.md`](10-security/data-security/README.md) — Data classification, envelope encryption at rest, field-level tokenization, dynamic masking, and database RLS.

---

## 14. Enterprise Integration Architecture
* [`14-enterprise-integration/README.md`](14-enterprise-integration/README.md) — Point-to-point vs hub-and-spoke, API-led 3-tier connectivity, and federated integration operating models.

---

## 15. Modernization & System Evolution Additions
* [`15-modernization/data-integration/README.md`](15-modernization/data-integration/README.md) — Point-to-point to API-led, batch to streaming, database decomposition, and financial reconciliation modernization.

---

## Reference Architectures, Case Studies & Governance (Phase 5 Additions)
* **Data Reference Architectures**: [`18-reference-architectures/data/`](18-reference-architectures/data/) — 10 Reference blueprints (Operational DB, Lakehouse, Streaming, CDC, Data Mesh, MDM).
* **Integration Reference Architectures**: [`18-reference-architectures/integration/`](18-reference-architectures/integration/) — 12 Reference blueprints (API-Led, Event Bus, SaaS Integration, Payment Platform, B2B Gateway).
* **Financial Reference Architectures**: [`18-reference-architectures/financial/`](18-reference-architectures/financial/) — 10 Reference blueprints (Payment Processing, Settlement Engine, Reconciliation Hub, Multi-Way Recon).
* **Data & Integration Case Studies**: [`19-case-studies/data-integration/`](19-case-studies/data-integration/) — 10 Production transformation case studies.
* **Financial Case Studies**: [`19-case-studies/financial/`](19-case-studies/financial/) — 15 Real-world settlement and reconciliation incident case studies.
* **Architecture Decision Records**: [`16-architecture-deliverables/adr/`](16-architecture-deliverables/adr/) — ADR-0021 through ADR-0043 (23 Architecture Decision Records).
* **Architecture Review Checklists**: [`21-architecture-tools/checklists/`](21-architecture-tools/checklists/) — 27 Specialized data and integration review checklists.
* **ARB Review Specification**: [`21-architecture-tools/architecture-review/data-and-integration-architecture-review.md`](21-architecture-tools/architecture-review/data-and-integration-architecture-review.md).
* **Quantitative Sizing Calculators**: [`21-architecture-tools/calculators/`](21-architecture-tools/calculators/) — Database storage growth, Kafka partition sizing, queue throughput, API capacity, and financial reconciliation volume calculators.
* **Technology Comparisons**: [`22-reference/technology-comparison/data-integration/`](22-reference/technology-comparison/data-integration/) — 6 Rigorous comparative decision matrices.


---

## 08. Cloud & Infrastructure Architecture {#08-cloud}
*Enterprise cloud strategy, AWS/Azure/GCP deep dives, compute, containers, Kubernetes, serverless, VPC networking, infrastructure security, IaC, high availability, disaster recovery, FinOps, cloud migration, architecture patterns, and decision frameworks.*

### Principles & Foundations (`08-cloud/`, `08-cloud/fundamentals/`)
* [`08-cloud/README.md`](08-cloud/README.md) - Cloud Architecture discipline overview, taxonomy, and navigation.
* [`08-cloud/cloud-principles.md`](08-cloud/cloud-principles.md) - The 20 non-negotiable enterprise cloud architecture principles.
* [`08-cloud/fundamentals/README.md`](08-cloud/fundamentals/README.md) - Cloud fundamentals index.
* [`08-cloud/fundamentals/architectural-shifts.md`](08-cloud/fundamentals/architectural-shifts.md) - Shifts from static infrastructure to dynamic software-defined topologies.
* [`08-cloud/fundamentals/service-models.md`](08-cloud/fundamentals/service-models.md) - IaaS vs CaaS vs PaaS vs FaaS vs SaaS architectural trade-offs.
* [`08-cloud/fundamentals/shared-responsibility-model.md`](08-cloud/fundamentals/shared-responsibility-model.md) - Security, compliance, and operational boundaries.
* [`08-cloud/fundamentals/regions-and-availability-zones.md`](08-cloud/fundamentals/regions-and-availability-zones.md) - Blast radius boundaries, latency characteristics, and failure containment.
* [`08-cloud/fundamentals/control-plane-vs-data-plane.md`](08-cloud/fundamentals/control-plane-vs-data-plane.md) - Static stability and surviving cloud management control plane outages.
* [`08-cloud/fundamentals/managed-vs-self-managed.md`](08-cloud/fundamentals/managed-vs-self-managed.md) - Operational toil vs custom engineering autonomy trade-off rubric.
* [`08-cloud/fundamentals/cloud-operating-model.md`](08-cloud/fundamentals/cloud-operating-model.md) - Team Topologies, self-service platforms, and decentralized delivery.
* [`08-cloud/fundamentals/cloud-failure-domains.md`](08-cloud/fundamentals/cloud-failure-domains.md) - Hardware racks, AZs, regional impairments, and correlated catastrophic failures.
* [`08-cloud/fundamentals/evolution-spectrum.md`](08-cloud/fundamentals/evolution-spectrum.md) - Bare metal to VMs, containers, and serverless abstraction continuum.

### Cloud Strategy, Hybrid & Multi-Cloud (`08-cloud/cloud-strategy/`, `hybrid-cloud/`, `multi-cloud/`)
* [`08-cloud/cloud-strategy/README.md`](08-cloud/cloud-strategy/README.md) - Strategic adoption, exit planning, lock-in governance, and CCOE operating models.
* [`08-cloud/hybrid-cloud/README.md`](08-cloud/hybrid-cloud/README.md) - Datacenter interconnects (DirectConnect/ExpressRoute), identity federation, and hybrid data sync.
* [`08-cloud/multi-cloud/README.md`](08-cloud/multi-cloud/README.md) - The reality of multi-cloud: active-passive DR, Kubernetes portability, and the Multi-Cloud Decision Framework.

### Cloud Provider Architectures & Comparisons (`08-cloud/aws/`, `azure/`, `gcp/`, `cloud-provider-comparison/`)
* [`08-cloud/aws/README.md`](08-cloud/aws/README.md) - Deep AWS enterprise architectures: Nitro EC2, ECS/Fargate, EKS, Aurora, DynamoDB, MSK, Landing Zones.
* [`08-cloud/azure/README.md`](08-cloud/azure/README.md) - Deep Azure enterprise architectures: Entra ID, vWAN, AKS, Cosmos DB, Service Bus, Azure SQL.
* [`08-cloud/gcp/README.md`](08-cloud/gcp/README.md) - Deep Google Cloud architectures: Global VPC, Cloud Run, GKE Autopilot, Spanner, BigQuery, Pub/Sub.
* [`08-cloud/cloud-provider-comparison/README.md`](08-cloud/cloud-provider-comparison/README.md) - Provider comparison index and the Cloud Provider Selection Framework.

### Compute, Containers, Kubernetes & Serverless (`08-cloud/compute/`, `containers/`, `kubernetes/`, `serverless/`)
* [`08-cloud/compute/README.md`](08-cloud/compute/README.md) - Compute runtime paradigms, virtualization internals, and Compute Selection Framework.
* [`08-cloud/containers/README.md`](08-cloud/containers/README.md) - Container architecture, OCI runtimes, cgroups/namespaces, image optimization, and security hardening.
* [`08-cloud/kubernetes/README.md`](08-cloud/kubernetes/README.md) - Production Kubernetes: etcd quorums, Karpenter, Gateway API, GitOps (ArgoCD), and **When NOT to use Kubernetes**.
* [`08-cloud/serverless/README.md`](08-cloud/serverless/README.md) - FaaS, Cloud Run / Fargate serverless containers, cold-start mitigation, and event-driven patterns.

### Networking, Edge & Storage (`08-cloud/networking/`, `load-balancing/`, `dns/`, `cdn-edge/`, `storage/`)
* [`08-cloud/networking/README.md`](08-cloud/networking/README.md) - VPC topologies, transit hubs, PrivateLink endpoints, and Zero Trust network segmentation.
* [`08-cloud/load-balancing/README.md`](08-cloud/load-balancing/README.md) - L4 vs L7 load balancing, global Anycast, health check draining, and TLS termination.
* [`08-cloud/dns/README.md`](08-cloud/dns/README.md) - Split-horizon DNS, latency/geo routing, failover TTL engineering, and hybrid DNS resolution.
* [`08-cloud/cdn-edge/README.md`](08-cloud/cdn-edge/README.md) - Global Edge caching, surrogate keys, origin shielding, edge compute, and DDoS mitigation.
* [`08-cloud/storage/README.md`](08-cloud/storage/README.md) - Block (EBS/Managed Disks), File (EFS/Azure Files), Object (S3/GCS), tiering, WORM retention, and Storage Selection Framework.

### Security, IaC, Platform Engineering & Governance (`08-cloud/infrastructure-security/`, `iam/`, `secrets-management/`, `infrastructure-as-code/`, `terraform/`, `configuration-management/`, `platform-engineering/`, `landing-zones/`, `governance/`)
* [`08-cloud/infrastructure-security/README.md`](08-cloud/infrastructure-security/README.md) - Defense-in-depth, perimeter hardening, agentless CSPM, and microsegmentation.
* [`08-cloud/iam/README.md`](08-cloud/iam/README.md) - Least-privilege IAM, Workload Identity Federation (EKS Pod Identity/Workload Identity), and IAM Decision Framework.
* [`08-cloud/secrets-management/README.md`](08-cloud/secrets-management/README.md) - Dynamic secret generation, automated rotation, and External Secrets Operator (ESO).
* [`08-cloud/infrastructure-as-code/README.md`](08-cloud/infrastructure-as-code/README.md) - Declarative vs imperative IaC, drift detection, and state governance.
* [`08-cloud/terraform/README.md`](08-cloud/terraform/README.md) - Enterprise Terraform/OpenTofu: directory structure, remote state locking, and module design.
* [`08-cloud/configuration-management/README.md`](08-cloud/configuration-management/README.md) - Dynamic configuration, Ansible automation, and runtime feature flagging.
* [`08-cloud/platform-engineering/README.md`](08-cloud/platform-engineering/README.md) - Internal Developer Platforms (Backstage), Golden Paths, and Team Topologies.
* [`08-cloud/landing-zones/README.md`](08-cloud/landing-zones/README.md) - AWS Control Tower and Azure Landing Zones from startup to regulated multi-account scale.
* [`08-cloud/governance/README.md`](08-cloud/governance/README.md) - Enterprise resource tagging, Cloud Governance Framework, and service approval gates.

### HA, DR, FinOps, Observability & Deployment (`08-cloud/high-availability/`, `disaster-recovery/`, `business-continuity/`, `capacity-planning/`, `cloud-cost/`, `finops/`, `observability/`, `reliability/`, `deployment/`)
* [`08-cloud/high-availability/README.md`](08-cloud/high-availability/README.md) - N+1, N+2, and active-active multi-AZ topologies.
* [`08-cloud/disaster-recovery/README.md`](08-cloud/disaster-recovery/README.md) - RTO/RPO engineering: Backup/Restore, Pilot Light, Warm Standby, Active-Active, and DR Decision Matrix.
* [`08-cloud/business-continuity/README.md`](08-cloud/business-continuity/README.md) - Business Impact Analysis (BIA) and tier-based application criticality mapping.
* [`08-cloud/capacity-planning/README.md`](08-cloud/capacity-planning/README.md) - Mathematical sizing formulas, headroom buffers, and autoscaling policies.
* [`08-cloud/cloud-cost/README.md`](08-cloud/cloud-cost/README.md) - Cost drivers, egress optimization, Savings Plans, Spot instance strategies, and estimation formulas.
* [`08-cloud/finops/README.md`](08-cloud/finops/README.md) - Inform-Optimize-Operate phases, showback/chargeback, and unit economics ($/transaction).
* [`08-cloud/observability/README.md`](08-cloud/observability/README.md) - OpenTelemetry standards, multi-window SLO burn-rate alerting, and distributed tracing.
* [`08-cloud/reliability/README.md`](08-cloud/reliability/README.md) - Cellular architectures, shuffle sharding, circuit breakers, and Chaos Engineering game days.
* [`08-cloud/deployment/README.md`](08-cloud/deployment/README.md) - Zero-downtime rolling, blue-green, canary, and expand-contract database schema migrations.

### Migration, Patterns, Decision Frameworks & Anti-Patterns (`08-cloud/migration/`, `architecture-patterns/`, `decision-frameworks/`, `anti-patterns/`)
* [`08-cloud/migration/README.md`](08-cloud/migration/README.md) - AWS 7Rs, automated discovery, migration factory wave planning, CDC database migration, and cutover/rollback runbooks.
* [`08-cloud/architecture-patterns/README.md`](08-cloud/architecture-patterns/README.md) - 10 Core enterprise cloud patterns (Static Stability, Cell-Based, Hub-and-Spoke, Egress Inspection, etc.).
* [`08-cloud/decision-frameworks/README.md`](08-cloud/decision-frameworks/README.md) - 8 Architectural decision frameworks (Cloud vs On-Prem, Single vs Multi-Cloud, Single vs Multi-Region, etc.).
* [`08-cloud/anti-patterns/README.md`](08-cloud/anti-patterns/README.md) - 12 Lethal cloud anti-patterns (Resume-Driven Multi-Cloud, Premature K8s, Egress Blindness, Lift-and-Dump, etc.).

### Reference Deliverables, Case Studies, ADRs & Tools
* **Cloud Reference Architectures**: [`18-reference-architectures/cloud/`](18-reference-architectures/cloud/) - 11 Production blueprints (Enterprise Web, B2B SaaS, E-Commerce, Banking, API Platform, Event-Driven, Multi-Region Active-Active, Hybrid Cloud, Enterprise Kubernetes, Serverless Event Platform, Cloud Landing Zone).
* **Cloud Case Studies**: [`19-case-studies/cloud/`](19-case-studies/cloud/) - 18 Enterprise transformation case studies (Egress Shock, Global Outage Survival, FinOps Turnaround, 14TB Oracle Migration, K8s Rollback, etc.).
* **Architecture Decision Records**: [`16-architecture-deliverables/adr/`](16-architecture-deliverables/adr/) - ADR-0044 through ADR-0060 (17 Cloud & Infrastructure ADRs).
* **Cloud Review Checklists**: [`21-architecture-tools/checklists/cloud/`](21-architecture-tools/checklists/cloud/) - 5 ARB review checklists (Architecture Review, Landing Zone, Migration Readiness, Disaster Recovery, Security Guardrails).
* **Quantitative Calculators**: [`21-architecture-tools/calculators/`](21-architecture-tools/calculators/) - Capacity, Kubernetes node sizing, network egress, storage lifecycle, compound SLA, DR cost, and FinOps unit cost calculators.
* **Technology Trade-Off Matrices**: [`22-reference/technology-comparison/cloud/`](22-reference/technology-comparison/cloud/) - 10 Multidimensional trade-off evaluation matrices.
* **Interview & ARB Playbook**: [`21-architecture-tools/architecture-review/cloud-architecture-interview-playbook.md`](21-architecture-tools/architecture-review/cloud-architecture-interview-playbook.md).

## Additional Domains (Scheduled for Phases 7–10)
* [`09-devops/`](09-devops/) — Platform engineering, GitOps, CI/CD, Kubernetes.
* [`10-security/`](10-security/) — Zero trust, IAM, DevSecOps, AppSec.
* [`11-observability/`](11-observability/) — Telemetry, Prometheus, Grafana, OpenTelemetry, SRE.
* [`12-ai/`](12-ai/) — GenAI, LLM architectures, RAG systems, Model serving.
* [`99-experiments/`](99-experiments/) — POC sandbox.
