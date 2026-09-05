# Changelog

## [2.0.0] - 2026-09-05

### Added - Phase 10: Architect Mastery (Landmark Release & Capstone OS)
* **Architect Mindset & Judgment (`24-architect-mastery/mindset/`, `architecture-judgment/`)**:
  * Foundational definition: *"An architect is paid for judgment, not diagrams."*
  * Developer-to-Enterprise Architect evolutionary journey and mental model shifts.
  * Architecture under extreme ambiguity, real-options thinking, and cost of delay.
  * Known vs Unknown Unknowns classification and decision velocity heuristics.
* **Discovery, Question Frameworks & Requirements (`question-frameworks/`, `discovery/`, `requirements/`)**:
  * Multi-dimensional question frameworks for business, data, scale, and operational discovery.
  * Non-Functional Requirements (NFR) engineering and quantifiable SLO/SLI modeling.
* **Master Trade-offs Library (`trade-offs/`)**:
  * Comprehensive deep-dive analysis of all 20 fundamental architectural trade-offs: Consistency vs Availability, Latency vs Durability, Throughput vs Cost, Simplicity vs Flexibility, Build vs Buy vs Partner, Centralized vs Decentralized, Sync vs Async, Schema-on-Read vs Schema-on-Write, Real-Time vs Batch, Monolith vs Microservices, General-Purpose vs Purpose-Built, In-Memory vs Externalized State, Tight vs Loose Coupling, Normalization vs Denormalization, Push vs Pull, Single-Region vs Multi-Region, Best-of-Breed vs Single-Vendor, Fast Delivery vs High Reliability, Deep Security vs Velocity, Standardization vs Innovation.
* **Constraints, Evolutionary Architecture & Strategy (`constraints/`, `evolution/`, `strategy/`)**:
  * Theory of constraints, physical/legal boundaries, and navigating hard vs soft constraints.
  * Evolutionary architecture, architectural seams, and automated fitness functions in CI/CD.
  * Strategy formulation (Rumelt's Kernel: Diagnosis, Guiding Policy, Coherent Actions) and Wardley Mapping.
  * Technology radar lifecycle governance and Internal Developer Platform (IDP) architecture.
* **Organizational Design & Leadership (`organizational-design/`, `leadership/`)**:
  * Conway's Law, Team Topologies (Stream-aligned, Platform, Enabling, Complicated-subsystem), and the Reverse Conway Maneuver.
  * Architectural leadership without authority, managing technical conflict, and multiplying engineers.
* **Executive Communication & Storytelling (`executive-communication/`, `architecture-storytelling/`)**:
  * C-suite translation dictionary, Minto Pyramid Principle, 1-page architecture briefs, and business case templates.
  * Narrative architecture framing: The Hero's Journey of technical transformation.
* **Pragmatic Governance & Review (`governance/`, `architecture-review/`)**:
  * Guardrails over gates, DORA metrics, coupling indices, and FinOps unit economics.
  * Architecture Review Board (ARB) charter, operating model, and asynchronous RFC workflows.
* **Risk, Enterprise Failure Modes & War Stories (`risk/`, `failure-analysis/`, `war-stories/`)**:
  * 5x5 architectural risk matrix, blast radius containment, and cell-based bulkheading.
  * 20 Enterprise Failure Mode Post-Mortems (cascading failures, split-brain, 2PC deadlocks, cache stampedes, retry storms, Kafka rebalance storms, K8s OOM cascades, connection exhaustion, etc.).
  * 15 Architectural War Stories from the trenches analyzing multi-million dollar recoveries and lessons learned.
  * Incident-driven architecture feedback loops and Production Readiness Reviews (PRR).
* **Specialized Architecture Disciplines**:
  * Enterprise AI systems, legacy modernization (7Rs, Strangler Fig, CDC), M&A due diligence, global multi-region compliance, regulated enterprise architecture, application portfolio management (TIME model), architectural optionality, radical simplification, and system sunsetting.
* **Capstone Reference Architectures (REF-101 to REF-120)**:
  * 20 Planetary-scale reference blueprints covering payment engines, national identity, fraud meshes, e-commerce, healthcare AI, connected vehicles, telco 5G, trading exchanges, GenAI lakehouses, smart cities, and decentralized identity in strict 26-section format.
* **Capstone Case Studies (CS-101 to CS-120)**:
  * 20 In-depth crisis turnaround and large-scale transformation case studies in strict 19-section format.
* **System Design Interview Masterclass & 50 Scenario Library**:
  * 18-Step live system design interview framework (`20-interview-system-design/architect-mastery/`).
  * 50 Comprehensive architectural scenarios across 12 enterprise verticals with complete technical specifications (`24-architect-mastery/scenario-library/`).
* **Capstone Artifacts**:
  * Anti-Patterns Master Index, Decision Journal Template, Learning Loop, and 100-Point Master Checklist.
  * The Personal Architect Operating System (`personal-operating-system.md`) and Master Enterprise Architecture Model (`master-architecture-model.md`).

## [1.8.0] - 2026-09-05

### Added - Phase 9: Enterprise Architecture Operating System
* **Foundations, Roles & Leadership (`23-enterprise-architecture/`)**:
  * Established the Core Enterprise Architecture Mental Model (Strategy -> Outcomes -> Value Streams -> Capabilities -> Applications/Data/Tech -> Transformation -> Governance).
  * Role profiles and RACI matrices for Enterprise, Solution, Technical, Business, and Chief Architects.
  * Executive communication playbooks: Minto Pyramid storytelling, C-suite briefing decks, influence without authority, and trade-off negotiations.
  * Git-based living architecture repository and catalog schema standards.
* **Business Architecture & Capability Modeling**:
  * Distinct definitions and boundary rules for Process vs Capability vs Value Stream vs Function vs Org.
  * Industry business architecture models across 8 major verticals (Banking, Insurance, Healthcare, Retail, Manufacturing, Logistics, SaaS, Government).
  * 3-tier capability decomposition (MECE), capability ownership, 5-stage maturity scoring, and investment heatmaps.
  * End-to-end capability mapping templates connecting Capability -> Process -> Application -> Data -> Infrastructure.
* **Enterprise Portfolio & Modernization Management**:
  * Gartner TIME model (Tolerate, Invest, Migrate, Eliminate) and 7R rationalization playbook.
  * Multi-criteria application scorecard and quantitative modernization prioritization calculator.
  * Technology lifecycle governance (Strategic, Standard, Tolerated, Restricted, Retire) and Technology Radar alignment.
* **Enterprise Governance, Strategy & Debt**:
  * Master Catalog of 20 Enterprise Architecture Principles in strict 7-part format.
  * Architecture Review Board (ARB) charter, meeting agendas, and compliance review templates.
  * Architecture exception lifecycle, risk acceptance formulas, and compensating control architectures.
  * Financial architecture: 5-year TCO formula, unit economics, FinOps showback/chargeback.
  * Enterprise debt taxonomy (Technical vs Architectural vs Organizational debt) and the 20% engineering capacity rule.
* **Global Architecture, M&A & Regulated Industries**:
  * Global Core / Regional Edge platform architecture and data sovereignty models (GDPR, China PIPL).
  * M&A technical due diligence checklist, application overlap rationalization, and two-tier integration.
  * Divestiture technical carve-out architecture and Transitional Service Agreements (TSAs).
  * Comprehensive regulatory playbooks across 12 global industries.
* **Reference Blueprints, Case Studies, Decisions & Anti-Patterns**:
  * 20 Enterprise Reference Architectures (`ref-081` to `ref-100`) using strict 26-section format.
  * 20 Enterprise Case Studies (`cs-081` to `cs-100`) using strict 19-section format.
  * 24 Lethal Enterprise Architecture Anti-Patterns with concrete symptoms, root causes, and remedies.
  * 20 Formal Decision Framework scorecards evaluating high-stakes enterprise trade-offs.
  * 8 Reusable Enterprise Reference Models and 10 Automated Architectural Fitness Functions.
* **Architecture Deliverables & Interview System Design**:
  * 20 new Architecture Decision Records (ADR-0096 to ADR-0115) cataloged in Master ADR registry.
  * 13 Enterprise Architecture scenario-based interview playbooks with strict 14-section format (`20-interview-system-design/enterprise-architecture/`).
  * Master Enterprise Architecture Checklist spanning 9 domains and quantitative sizing tools.

## [1.7.0] - 2026-09-05
### Added - Phase 8: AI & Modern Architecture
- **AI Systems & Platform Architecture (`12-ai/ai-systems-architecture/`)**: 24 comprehensive specifications covering AI system design, gateways, model routing, serving, inference, workflows, agent platforms, evaluation, observability, security, governance, and cost management.
- **AI Foundations, Fundamentals & ML Architecture (`12-ai/`)**: System boundaries, workload taxonomy, mathematical foundations, feature stores, model registries, and data/concept drift monitoring.
- **Generative AI, LLMs & Prompt Engineering (`12-ai/`)**: Foundation models, multimodal synthesis, constrained structured outputs, transformer mechanics, attention scaling (GQA, FlashAttention), reasoning models, prompts-as-code, and context compression.
- **RAG & Knowledge Architecture (`12-ai/`)**: Hybrid search, vector databases, ANN algorithms (HNSW vs IVF-PQ), GraphRAG, Agentic RAG, Parent-Child chunking, RAG Triad evaluation, and CDC freshness pipelines.
- **Agents, Workflows & Tool Calling (`12-ai/`)**: ReAct agent loops, cognitive planning, durable execution (Temporal), human-in-the-loop gates, Model Context Protocol (MCP), sandboxed microVMs, multi-agent topologies, and persistent memory.
- **Security, Governance & Observability (`12-ai/`)**: OWASP Top 10 for LLMs, prompt injection defense, guardrails, PII redaction, Zero Data Retention, EU AI Act compliance, OTel GenAI semantic conventions, and token FinOps.
- **Modern Architecture Patterns (`13-architecture-patterns/`)**: Composable PBCs, headless API-first systems, edge computing with WebAssembly (Wasm), event-driven CDC modernization, serverless AI, and architectural fitness functions.
- **Patterns, Anti-Patterns & Decision Frameworks**: 15 AI design patterns, 22 lethal AI anti-patterns, and 18 formal decision scorecards.
- **Reference Architectures & Case Studies**: 20 AI reference blueprints (`18-reference-architectures/ai-modern/`) and 20 enterprise case studies (`19-case-studies/ai-modern/`).
- **Architecture Decision Records**: 20 new ADRs (ADR-0076 through ADR-0095) in `16-architecture-deliverables/adr/`.
- **Tools & References**: AI Architecture Review Checklist, AI Production Readiness Checklist, AI Cost Calculator, and Interview Playbook.

All notable architectural iterations, structural updates, and additions to the **Enterprise Architecture Handbook** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and adheres to semantic milestone versioning.

---

## [1.6.0] - 2026-09-05 (Phase 7: Security & Operations Architecture)

### Added
* **Security Principles, Foundations & Governance (`10-security/`)**:
  * 15 Non-negotiable enterprise security architecture principles (`security-principles.md`).
  * 5-Level Security Maturity Model (`security-maturity-model.md`).
  * Core architecture guides: Defense in depth, least privilege, secure by design/default, fail secure, assume breach, blast radius, separation of duties, and quantitative risk economics (SLE/ALE).
  * Enterprise governance: Three Lines of Defense, Federated Security Champions, ARB security review gates, and 90-day exception lifecycles.
* **Threat Modeling & Identity Architecture**:
  * STRIDE, PASTA, Attack Trees, 7-step repeatable threat modeling workflow, and reusable specification template.
  * Universal identity architecture (Human, Machine, Workload, Service Principal), SCIM 2.0 lifecycle, Workload Identity Federation, and Just-in-Time (JIT) privileged access.
  * Phishing-resistant authentication (FIDO2/WebAuthn Passkeys), adaptive risk scoring, session lifecycles, and credential rotation.
  * Authorization paradigms: RBAC vs ABAC vs ReBAC vs PBAC, Policy as Code (OPA/Rego), and BOLA mitigation.
* **OAuth 2.0, OpenID Connect (OIDC), JWT & Zero Trust**:
  * OAuth 2.0 Authorization Code with PKCE (RFC 7636), client credentials, refresh token family rotation, and scope namespacing.
  * OIDC architecture, ID token vs Access token semantics, standard claims, UserInfo, dynamic JWKS discovery, and nonce replay defense.
  * JSON Web Tokens (JWT) format, signing algorithms (RS256, ES256, EdDSA), deterministic 8-step validation algorithm, and client storage.
  * Enterprise Single Sign-On (SSO), SP-Initiated vs IdP-Initiated, SAML vs OIDC, and multi-tenant SaaS federation.
  * Zero Trust Architecture (NIST SP 800-207), identity-as-perimeter, device posture checks, and eBPF microsegmentation.
* **Application, API, Web & Mobile Security**:
  * Multi-tier API security architecture, OWASP API Top 10 mitigations, distributed sliding-window rate limiting, and HMAC-SHA256 request signing.
  * AppSec architecture principles, OWASP Top 10 prevention, SSRF defense proxies, parameterized SQL, and finite state machines.
  * Frontend browser security: Strict CSP nonces, SameSite cookies, CORS governance, and Subresource Integrity (SRI).
  * Mobile security: Hardware enclaves (iOS Keychain / Android KeyStore), public key certificate pinning, and SQLCipher.
* **Platform, Cryptography & DevSecOps**:
  * Cloud shared responsibility, agentless CSPM with event-driven auto-remediation, and network subnet tiering.
  * Container hardening: Distroless images, non-root execution, vulnerability scanning (Trivy), and Sigstore Cosign image signing.
  * Kubernetes security: Pod Security Standards (`restricted`), eBPF NetworkPolicies, Kyverno admission controllers, and External Secrets Operator.
  * Infrastructure security: CIS benchmarks, immutable golden images (Packer), IaC scanning (Checkov), and SSM Session Manager.
  * Cryptographic architecture: AES-256-GCM envelope encryption, Cloud KMS vs Cloud HSM, TLS 1.3 forward secrecy, and HashiCorp Vault dynamic secrets.
  * DevSecOps pipelines: Pre-commit secret scanning (Gitleaks), SAST (Semgrep), SCA (Snyk), and non-bypassable PR gates.
  * Software supply chain security: CycloneDX SBOMs, Dependency-Track, and SLSA Level 3 build provenance.
  * Risk-based vulnerability management (CVSS vs EPSS), remediation SLAs (Critical: 7 days), and WAF virtual patching.
  * Security monitoring: SIEM integration (Microsoft Sentinel/Splunk), UEBA anomaly detection, and tamper-proof WORM audit logging.
  * Incident response runbooks: Credential compromise, enterprise ransomware containment, and data breach forensics.
  * Compliance & privacy: PCI-DSS 4.0 tokenization, GDPR data residency, Privacy by Design, and cryptographic shredding.
* **Operational Architecture & SRE (`11-observability/`)**:
  * 15 Non-negotiable operational principles and 5-Level Operational Maturity Model.
  * SRE foundations, toil reduction (50% rule), and SLA vs SLO vs SLI mathematical downtime formulas.
  * Multi-window multi-burn-rate alerting paging on Error Budget depletion.
  * Reliability engineering: Graceful degradation, Resilience4j circuit breakers, thread bulkheads, load shedding, and chaos game days.
  * Production Readiness Review (PRR) framework and 6-dimension evaluation checklist.
  * Operational readiness: Service ownership, on-call models, and dependency mapping.
  * Incident management: SEV-1 to SEV-4 severity classification, Incident Commander system, and blameless post-mortems (PIR).
  * Problem management: 5 Whys, Ishikawa Fishbone diagrams, and Known Error Database (KEDB).
  * Change & release management: Standard vs Normal vs Emergency changes, GitOps with ArgoCD, progressive canaries, and Expand-Contract database migrations.
  * Backup & BCP operations: 3-2-1-1-0 backup rule, immutable WORM backups, automated monthly restore testing, and Business Impact Analysis (BIA).
  * 8 Production operational runbooks with standard 12-section specs.
* **Patterns, Anti-Patterns, Decision Frameworks & Reference Deliverables**:
  * 17 Production Security Architecture Patterns (`10-security/security-patterns/`).
  * 20 Lethal Security Anti-Patterns (`10-security/security-anti-patterns/`).
  * 16 Formal Security Decision Frameworks (`10-security/decision-frameworks/`).
  * 6 Operational Architecture Patterns (`11-observability/operational-patterns/`).
  * 12 Operational Anti-Patterns (`11-observability/operational-anti-patterns/`).
  * 8 SRE Decision Frameworks (`11-observability/decision-frameworks/`).
  * 6 End-to-End Reference Architectures (`18-reference-architectures/security-operations/`).
  * 20 Comprehensive Enterprise Case Studies (`19-case-studies/security-operations/`).
  * 15 Architecture Decision Records (ADR-0061 through ADR-0075 in `16-architecture-deliverables/adr/`).
  * 16 Security and Operational Review Checklists (`21-architecture-tools/checklists/`).
  * Production Readiness Scorecard (0 to 5 rating scale).
  * Security & Operations Architecture Interview Playbook (14 high-stakes scenarios).

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
