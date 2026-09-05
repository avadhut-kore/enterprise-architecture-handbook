# Changelog

All notable architectural iterations, structural updates, and additions to the **Enterprise Architecture Handbook** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and adheres to semantic milestone versioning.

---

## [1.5.0] - 2026-09-05 (Phase 6: Cloud & Infrastructure Architecture)

### Added
* **Cloud Principles & Foundations (`08-cloud/`)**:
  * 20 non-negotiable enterprise cloud principles emphasizing static stability, least privilege, and blast radius isolation.
  * Comprehensive foundations: Architectural shifts, service models (IaaS/PaaS/FaaS), shared responsibility, regions/AZs, control plane vs data plane, managed vs self-managed, and failure domains.
* **Cloud Strategy, Hybrid & Multi-Cloud**:
  * Adoption strategy, repatriation economics, exit planning, lock-in governance, and CCOE operating model.
  * Hybrid cloud architecture, DirectConnect/ExpressRoute, identity federation, and hybrid data synchronization.
  * Multi-cloud reality: active-passive DR, Kubernetes portability, cross-cloud networking/DNS, and Multi-Cloud Decision Framework.
* **Provider Deep Dives (AWS, Azure, GCP)**:
  * 53 in-depth provider architectural guides across compute, networking, databases, messaging, and security.
  * Cloud Provider Selection Framework evaluating organizational maturity, licensing, and workload fit.
* **Compute, Containers, Kubernetes & Serverless**:
  * Compute selection framework, virtualization vs bare-metal vs containers vs serverless.
  * Hardened container architectures, OCI runtimes, multi-stage image optimization, and supply-chain security.
  * Production Kubernetes: etcd quorums, Karpenter node autoscaling, Gateway API, GitOps (ArgoCD), and **When NOT to use Kubernetes**.
  * Serverless patterns, Cloud Run / Fargate serverless containers, cold-start mitigation, and event-driven state sagas.
* **Networking, Edge & Storage**:
  * VPC foundations, transit gateways, PrivateLink endpoints, and Zero Trust network segmentation.
  * L4/L7 load balancing, global Anycast routing, connection draining, and TLS termination.
  * Split-horizon DNS, latency/geo routing, and hybrid DNS resolution.
  * Edge CDN architecture, surrogate keys, origin shielding, edge compute, and DDoS mitigation.
  * Block, File, and Object storage internals, lifecycle tiering, and Storage Selection Framework.
* **Security, IaC, Platform Engineering & Governance**:
  * Defense-in-depth, perimeter hardening, agentless CSPM, and microsegmentation.
  * Workload Identity Federation (EKS Pod Identity / Azure Workload Identity) eliminating static credentials.
  * Dynamic secret management and External Secrets Operator (ESO) integration.
  * Enterprise Terraform/OpenTofu structure, remote state locking, and declarative IaC governance.
  * Internal Developer Platforms (Backstage), Golden Paths, and Team Topologies.
  * Multi-account Landing Zones from startup to regulated enterprise scale (AWS Control Tower / Azure ALZ).
* **HA, DR, FinOps, Observability & Deployment**:
  * High availability topologies, multi-AZ quorums, and static stability.
  * Disaster recovery: RTO/RPO engineering, Backup/Restore, Pilot Light, Warm Standby, Active-Active, and automated failover.
  * Capacity planning formulas, peak load forecasting, and headroom sizing.
  * Cloud cost optimization, data egress reduction, Savings Plans, and Spot instance strategies.
  * FinOps operating model, showback/chargeback, and transaction unit cost economics.
  * OpenTelemetry standardization, multi-window SLO burn-rate alerting, and distributed tracing.
  * Cellular architectures, shuffle sharding, circuit breakers, and Chaos Engineering game days.
  * Zero-downtime rolling, blue-green, canary deployments, and expand-contract database schema migrations.
* **Migration, Patterns, Decision Frameworks & Anti-Patterns**:
  * AWS 7Rs, automated discovery, migration factory wave planning, CDC database migration, and cutover/rollback runbooks.
  * 10 Core enterprise cloud patterns and 8 formal decision frameworks.
  * 12 Lethal cloud anti-patterns (Resume-Driven Multi-Cloud, Premature K8s, Egress Blindness, Lift-and-Dump, etc.).
* **Reference Deliverables, Case Studies, ADRs & Tools**:
  * 11 Cloud Reference Architectures (`18-reference-architectures/cloud/`).
  * 18 Enterprise Case Studies (`19-case-studies/cloud/`).
  * 17 Architecture Decision Records (ADR-0044 through ADR-0060 in `16-architecture-deliverables/adr/`).
  * 5 ARB Review Checklists (`21-architecture-tools/checklists/cloud/`).
  * 7 Quantitative Sizing & Cost Calculators (`21-architecture-tools/calculators/`).
  * 10 Multidimensional Technology Trade-off Matrices (`22-reference/technology-comparison/cloud/`).
  * Cloud Architecture Interview & Review Playbook (`21-architecture-tools/architecture-review/`).

---

## [1.0.0] - 2026-09-05 (Phase 1: Repository Foundation)

### Added
* **Repository Architecture & Taxonomy**:
  * Established the complete 23-domain root directory structure (`00-foundations` through `99-experiments`).
  * Created 190+ structured subdirectories covering backend, frontend, mobile, data, integration, cloud, devops, security, observability, AI, and modernization.
  * Added clean directory anchors across all domain folders.
* **Core Governance & Strategic Baselines**:
  * `README.md`: Handbook vision, audience personas, architecture-first philosophy, domain summary, and navigation.
  * `INDEX.md`: Exhaustive master index linking to all domains, subdirectories, templates, checklists, and references.
  * `ARCHITECTURE.md`: Meta-architecture of the knowledge repository, numbering taxonomy, separation of concerns, and content lifecycles.
  * `ARCHITECTURE-PRINCIPLES.md`: The 15 non-negotiable architectural principles for modern enterprise software systems.
  * `ARCHITECTURE-WORKFLOW.md`: 20-step end-to-end architecture lifecycle workflow from business problem discovery to Day-2 continuous evolution.
  * `DECISION-MAKING-FRAMEWORK.md`: 15-dimension architectural trade-off evaluation rubric, weighted decision matrix, and sensitivity analysis.
  * `DOCUMENTATION-STANDARD.md`: Universal 19-point documentation schema, 9 mandatory engineering inquiries, and Markdown/Mermaid rules.
  * `TECHNOLOGY-RADAR.md`: Enterprise radar model with Adopt, Trial, Assess, and Hold rings across 4 major engineering quadrants.
  * `ROADMAP.md`: 10-Phase strategic roadmap spanning from repository foundation to architectural mastery.
  * `CONTRIBUTING.md`: Authoring standards, naming conventions, directory routing, diagram rules, and ADR guidelines.
* **Enterprise Architecture Deliverables Templates (`16-architecture-deliverables/`)**:
  * `ADR-TEMPLATE.md`: Architecture Decision Record template with status, context, options, consequences, and compliance gates.
  * `SOLUTION-ARCHITECTURE-TEMPLATE.md`: End-to-end Solution Architecture Document (SAD) for enterprise platforms.
  * `HLD-TEMPLATE.md`: High-Level Design specification template with C4 diagrams and integration topologies.
  * `LLD-TEMPLATE.md`: Low-Level Design template for component internals, sequence flows, data models, and error handling.
  * `API-DESIGN-TEMPLATE.md`: Enterprise API design specification for REST, GraphQL, and gRPC contracts.
  * `DATA-DESIGN-TEMPLATE.md`: Data persistence architecture template for polyglot storage, schemas, sharding, and retention.
  * `SECURITY-DESIGN-TEMPLATE.md`: Security architecture and STRIDE threat modeling blueprint.
  * `DEPLOYMENT-DESIGN-TEMPLATE.md`: Infrastructure topology, VPC networking, container sizing, and CI/CD deployment template.
  * `INTEGRATION-DESIGN-TEMPLATE.md`: Enterprise integration contract for synchronous and asynchronous messaging patterns.
  * `ARCHITECTURE-REVIEW-TEMPLATE.md`: Architecture Review Board (ARB) submission and governance scorecard.
  * `RISK-REGISTER-TEMPLATE.md`: Enterprise technical risk register with probability, impact, mitigation, and contingency plans.
  * `REFERENCE-ARCHITECTURE-TEMPLATE.md`: Industry-standard blueprint reference architecture template.
  * `CASE-STUDY-TEMPLATE.md`: Retrospective case study and architectural post-mortem template.
  * `SYSTEM-DESIGN-TEMPLATE.md`: High-scale distributed system design template for enterprise systems and interview preparation.
* **Architecture Review Checklists (`21-architecture-tools/checklists/`)**:
  * `architecture-review-checklist.md`: Comprehensive ARB governance quality gate.
  * `solution-architecture-checklist.md`: Pre-implementation solution architecture verification.
  * `microservices-checklist.md`: Microservices boundary, decoupling, and distributed resilience review.
  * `api-review-checklist.md`: API design, REST maturity, versioning, and contract verification.
  * `database-review-checklist.md`: Database schema, indexing, connection pooling, and replication hygiene.
  * `security-review-checklist.md`: Zero Trust, OWASP, identity, and cryptographic assessment.
  * `cloud-architecture-checklist.md`: Cloud-native resilience, multi-AZ, and FinOps cost optimization review.
  * `production-readiness-checklist.md`: Go-live verification, load testing, chaos testing, and operational runbooks.
  * `disaster-recovery-checklist.md`: RPO/RTO validation, backup verification, and multi-region failover testing.
  * `observability-checklist.md`: Telemetry coverage across logs, metrics, distributed traces, and SLO alerting.

---

## Next Milestones
* [Phase 2: Architecture Fundamentals](ROADMAP.md#phase-2-architecture-fundamentals) — Deep dives into distributed systems theory, OS internals, networking, and foundational architectural styles.
