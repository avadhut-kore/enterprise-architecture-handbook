# Master Knowledge Index

Welcome to the comprehensive master index of the **Enterprise Architecture Handbook**. This document indexes every domain, subdirectory, template, tool, and checklist across the repository.

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

* [`00-foundations/architecture-principles/`](00-foundations/architecture-principles/) — Foundational axioms of software architecture.
* [`00-foundations/engineering-principles/`](00-foundations/engineering-principles/) — SOLID, DRY, KISS, YAGNI, Boy Scout Rule, modularity.
* [`00-foundations/distributed-systems/`](00-foundations/distributed-systems/) — CAP, PACELC, consensus (Raft, Paxos), vector clocks, Fallacies of Distributed Computing.
* [`00-foundations/networking/`](00-foundations/networking/) — OSI model, TCP/IP, UDP, QUIC, HTTP/2, HTTP/3, TLS handshake, DNS, BGP.
* [`00-foundations/operating-systems/`](00-foundations/operating-systems/) — Process vs. Thread, concurrency models, virtual memory, page faults, Linux kernel I/O (epoll, io_uring).
* [`00-foundations/databases/`](00-foundations/databases/) — ACID, BASE, storage engines (B-Tree, LSM-Tree), WAL, indexing internals, transaction isolation levels.
* [`00-foundations/security/`](00-foundations/security/) — Cryptographic primitives, symmetric/asymmetric encryption, hashing, digital signatures, PKI.
* [`00-foundations/cloud-fundamentals/`](00-foundations/cloud-fundamentals/) — Shared responsibility model, hypervisors, virtualization, regions, availability zones, edge compute.

---

## 01. Architecture
*Disciplines of enterprise, solution, application, and infrastructure architecture.*

* [`01-architecture/architecture-styles/`](01-architecture/architecture-styles/) — Monolith, SOA, Microservices, Event-Driven, Space-Based, Layered.
* [`01-architecture/architecture-patterns/`](01-architecture/architecture-patterns/) — Structural, behavioral, and architectural patterns catalog.
* [`01-architecture/enterprise-architecture/`](01-architecture/enterprise-architecture/) — TOGAF, Zachman, business capability mapping, IT landscape planning.
* [`01-architecture/solution-architecture/`](01-architecture/solution-architecture/) — Solution scoping, requirement decomposition, stakeholder alignment.
* [`01-architecture/application-architecture/`](01-architecture/application-architecture/) — Layering, domain modeling, clean code, modular architecture.
* [`01-architecture/integration-architecture/`](01-architecture/integration-architecture/) — Enterprise integration patterns (EIP), middleware, mediation vs. choreography.
* [`01-architecture/data-architecture/`](01-architecture/data-architecture/) — Conceptual, logical, physical data models, data topology, data fabric.
* [`01-architecture/security-architecture/`](01-architecture/security-architecture/) — Defense-in-depth, perimeter vs. identity-based security boundaries.
* [`01-architecture/cloud-architecture/`](01-architecture/cloud-architecture/) — Well-Architected frameworks, multi-region active-active patterns.
* [`01-architecture/ai-architecture/`](01-architecture/ai-architecture/) — AI system topologies, ML engineering pipelines, inference systems.
* [`01-architecture/architecture-governance/`](01-architecture/architecture-governance/) — Architecture Review Boards (ARB), tech debt tracking, compliance gates.

---

## 02. System Design
*High-scale systems engineering, NFR specification, and fault resilience.*

* [`02-system-design/methodology/`](02-system-design/methodology/) — Step-by-step framework for tackling end-to-end system design.
* [`02-system-design/functional-requirements/`](02-system-design/functional-requirements/) — Translating business capabilities into crisp functional boundaries.
* [`02-system-design/non-functional-requirements/`](02-system-design/non-functional-requirements/) — The "-ilities" matrix: Latency, throughput, scalability, availability.
* [`02-system-design/scalability/`](02-system-design/scalability/) — Horizontal vs. vertical, sharding, partitioning, read/write segregation.
* [`02-system-design/availability/`](02-system-design/availability/) — 99.9% to 99.999% calculations, MTBF, MTTR, redundancy models.
* [`02-system-design/reliability/`](02-system-design/reliability/) — Resiliency, fault tolerance, graceful degradation, circuit breakers.
* [`02-system-design/consistency/`](02-system-design/consistency/) — Strong, eventual, causal, read-after-write, session consistency.
* [`02-system-design/performance/`](02-system-design/performance/) — Latency budgets, p95/p99 optimization, caching tiers, compute profiling.
* [`02-system-design/fault-tolerance/`](02-system-design/fault-tolerance/) — Bulkheads, rate limiters, retries with exponential backoff and jitter.
* [`02-system-design/disaster-recovery/`](02-system-design/disaster-recovery/) — RPO, RTO, multi-region strategies (Active-Passive, Active-Active, Pilot Light).
* [`02-system-design/capacity-planning/`](02-system-design/capacity-planning/) — Bandwidth, storage, memory, and IOPS estimations from first principles.

---

## 03. Backend
*Enterprise runtime environments, language ecosystems, and server-side patterns.*

* [`03-backend/dotnet/`](03-backend/dotnet/) — Modern .NET (C#), ASP.NET Core, Kestrel, Entity Framework Core, memory management.
* [`03-backend/java/`](03-backend/java/) — Modern Java, JVM tuning, Spring Boot, Quarkus, virtual threads (Project Loom).
* [`03-backend/python/`](03-backend/python/) — FastAPI, asynchronous I/O (asyncio), Celery, gunicorn/uvicorn concurrency.
* [`03-backend/nodejs/`](03-backend/nodejs/) — Node.js event loop, libuv, NestJS, streams, clustering, TypeScript backend.
* [`03-backend/common-patterns/`](03-backend/common-patterns/) — Repository, Unit of Work, Specification, CQRS, Outbox pattern.

---

## 04. Frontend
*Modern web application architecture, front-end state, and user experience engineering.*

* [`04-frontend/react/`](04-frontend/react/) — React 18+, Server Components (RSC), Next.js, concurrent rendering.
* [`04-frontend/angular/`](04-frontend/angular/) — Enterprise Angular, Signals, RxJS, standalone components, NgRx.
* [`04-frontend/javascript/`](04-frontend/javascript/) — Modern ESNext features, V8 engine internals, memory leaks.
* [`04-frontend/typescript/`](04-frontend/typescript/) — Advanced type systems, generics, compile-time safety.
* [`04-frontend/frontend-architecture/`](04-frontend/frontend-architecture/) — State management architectures, modular client architecture.
* [`04-frontend/micro-frontends/`](04-frontend/micro-frontends/) — Module Federation, iframe isolation, single-spa, runtime composition.
* [`04-frontend/web-performance/`](04-frontend/web-performance/) — Core Web Vitals (LCP, INP, CLS), bundle optimization, code-splitting.
* [`04-frontend/accessibility/`](04-frontend/accessibility/) — WCAG 2.1 AA/AAA compliance, ARIA attributes, keyboard navigation.
* [`04-frontend/design-systems/`](04-frontend/design-systems/) — Design tokens, component libraries, theme management, Storybook.

---

## 05. Mobile
*Cross-platform and native mobile architectures, device constraints, and offline sync.*

* [`05-mobile/react-native/`](05-mobile/react-native/) — New Architecture (Fabric, TurboModules, Hermes), state, performance.
* [`05-mobile/native/`](05-mobile/native/) — iOS (Swift/SwiftUI) and Android (Kotlin/Jetpack Compose) considerations.
* [`05-mobile/mobile-architecture/`](05-mobile/mobile-architecture/) — MVVM, MVI, Clean Architecture on mobile devices.
* [`05-mobile/offline-first/`](05-mobile/offline-first/) — Local persistence (SQLite, WatermelonDB), conflict resolution, sync protocols.
* [`05-mobile/push-notifications/`](05-mobile/push-notifications/) — APNs, FCM, reliable delivery, payload management.
* [`05-mobile/mobile-security/`](05-mobile/mobile-security/) — Certificate pinning, biometric authentication, secure storage (Keyring/Keystore).

---

## 06. Data
*Polyglot persistence, analytical pipelines, storage engines, and data governance.*

* [`06-data/sql/`](06-data/sql/) — PostgreSQL, MySQL, distributed SQL (CockroachDB, YugabyteDB), indexing, query planning.
* [`06-data/nosql/`](06-data/nosql/) — Document (MongoDB), Key-Value (Redis, DynamoDB), Columnar (Cassandra, ScyllaDB).
* [`06-data/caching/`](06-data/caching/) — Cache strategies (Write-Through, Write-Behind, Cache-Aside), cache stampede, invalidation.
* [`06-data/data-lakes/`](06-data/data-lakes/) — S3/ADLS storage, Iceberg, Delta Lake, Parquet file formats.
* [`06-data/data-warehouses/`](06-data/data-warehouses/) — Snowflake, BigQuery, Redshift, dimensional modeling, OLAP cubes.
* [`06-data/streaming/`](06-data/streaming/) — Apache Flink, Spark Streaming, windowing, exactly-once processing semantics.
* [`06-data/search/`](06-data/search/) — Elasticsearch, OpenSearch, inverted index, vector search indexing.
* [`06-data/data-modeling/`](06-data/data-modeling/) — Entity-Relationship, Normalized vs. Denormalized, Data Vault 2.0.
* [`06-data/data-governance/`](06-data/data-governance/) — Data catalogs, lineage, GDPR/CCPA compliance, data quality frameworks.

---

## 07. Integration
*Synchronous and asynchronous enterprise communication fabrics.*

* [`07-integration/rest/`](07-integration/rest/) — OpenAPI specs, Richardson Maturity Model, semantic versioning, hypermedia.
* [`07-integration/graphql/`](07-integration/graphql/) — Schemas, N+1 problem, DataLoader, Apollo Federation, subscriptions.
* [`07-integration/grpc/`](07-integration/grpc/) — Protocol Buffers, HTTP/2 multiplexing, bi-directional streaming, performance.
* [`07-integration/messaging/`](07-integration/messaging/) — Message brokers, publish/subscribe, point-to-point, dead letter queues (DLQ).
* [`07-integration/kafka/`](07-integration/kafka/) — Partitions, consumer groups, log compaction, Kafka Streams, Schema Registry.
* [`07-integration/rabbitmq/`](07-integration/rabbitmq/) — Exchanges (Direct, Topic, Fanout, Headers), ACK/NACK semantics.
* [`07-integration/enterprise-integration/`](07-integration/enterprise-integration/) — Message routers, splitters, aggregators, canonical data models.
* [`07-integration/api-gateway/`](07-integration/api-gateway/) — Kong, Envoy, AWS API Gateway, Azure APIM, rate limiting, token validation.
* [`07-integration/webhooks/`](07-integration/webhooks/) — Reliable egress, HMAC signature verification, retry policies.

---

## 08. Cloud
*Multi-cloud infrastructure, cloud-native design, and FinOps practices.*

* [`08-cloud/aws/`](08-cloud/aws/) — AWS Well-Architected Framework, VPC topology, IAM policies, core service patterns.
* [`08-cloud/azure/`](08-cloud/azure/) — Azure Enterprise Landing Zones, Management Groups, Private Endpoints.
* [`08-cloud/gcp/`](08-cloud/gcp/) — Google Cloud Resource Hierarchy, Shared VPCs, BigQuery architecture.
* [`08-cloud/multi-cloud/`](08-cloud/multi-cloud/) — Workload portability reality, abstraction traps, egress cost mitigation.
* [`08-cloud/hybrid-cloud/`](08-cloud/hybrid-cloud/) — DirectConnect / ExpressRoute, VPN tunnels, on-prem to cloud networking.
* [`08-cloud/cloud-native/`](08-cloud/cloud-native/) — 12-Factor apps, containerized workloads, serverless compute, micro-VMs.
* [`08-cloud/cloud-cost-optimization/`](08-cloud/cloud-cost-optimization/) — FinOps principles, rightsizing, reservations/savings plans, spot instances.

---

## 09. DevOps & Platform Engineering
*Continuous delivery, infrastructure automation, container orchestration.*

* [`09-devops/git/`](09-devops/git/) — Git branching models (Trunk-Based vs. GitFlow), monorepo vs. polyrepo.
* [`09-devops/github/`](09-devops/github/) — GitHub Actions, reusable workflows, environments, branch protections.
* [`09-devops/gitlab/`](09-devops/gitlab/) — GitLab CI pipelines, runner management, Auto DevOps.
* [`09-devops/ci-cd/`](09-devops/ci-cd/) — Canary deployments, Blue/Green, Rolling updates, ArgoCD GitOps.
* [`09-devops/docker/`](09-devops/docker/) — Multi-stage builds, distroless images, container security scanning.
* [`09-devops/kubernetes/`](09-devops/kubernetes/) — Control plane, pods, services, ingress, HPA, CNI, CSI, service meshes.
* [`09-devops/terraform/`](09-devops/terraform/) — State management, modules, drift detection, provider architectures.
* [`09-devops/ansible/`](09-devops/ansible/) — Configuration management, idempotent playbooks, inventory management.
* [`09-devops/helm/`](09-devops/helm/) — Kubernetes packaging, chart versioning, umbrella charts.
* [`09-devops/platform-engineering/`](09-devops/platform-engineering/) — Internal Developer Platforms (IDP), Backstage, developer golden paths.

---

## 10. Security
*Enterprise cybersecurity, Zero Trust models, identity management, and threat modeling.*

* [`10-security/application-security/`](10-security/application-security/) — OWASP Top 10, input sanitization, CSRF, XSS, SSRF defenses.
* [`10-security/api-security/`](10-security/api-security/) — OWASP API Security Top 10, rate limiting, payload validation, mTLS.
* [`10-security/identity/`](10-security/identity/) — Enterprise Identity Governance, Active Directory, Okta, Ping Identity.
* [`10-security/oauth2/`](10-security/oauth2/) — Grant types (Authorization Code + PKCE, Client Credentials), token lifecycles.
* [`10-security/oidc/`](10-security/oidc/) — ID tokens, user info endpoints, claims mapping.
* [`10-security/jwt/`](10-security/jwt/) — Header, Payload, Signature, JWKS validation, revocation strategies.
* [`10-security/zero-trust/`](10-security/zero-trust/) — "Never trust, always verify", micro-segmentation, continuous posture assessment.
* [`10-security/secrets-management/`](10-security/secrets-management/) — HashiCorp Vault, AWS Secrets Manager, dynamic secret rotation.
* [`10-security/encryption/`](10-security/encryption/) — Data-at-rest (AES-256), Data-in-transit (TLS 1.3), envelope encryption.
* [`10-security/threat-modeling/`](10-security/threat-modeling/) — STRIDE methodology, attack trees, mitigation matrices.
* [`10-security/secure-development/`](10-security/secure-development/) — SAST, DAST, SCA, dependency vulnerability remediation.

---

## 11. Observability
*Telemetry platforms, OpenTelemetry, site reliability engineering, and incident triage.*

* [`11-observability/logging/`](11-observability/logging/) — Structured JSON logging, log correlation, ELK/OpenSearch, Loki.
* [`11-observability/metrics/`](11-observability/metrics/) — Prometheus metrics (Counter, Gauge, Histogram, Summary), Grafana dashboards.
* [`11-observability/tracing/`](11-observability/tracing/) — Distributed trace context propagation (W3C), Jaeger, Tempo.
* [`11-observability/opentelemetry/`](11-observability/opentelemetry/) — OTel Collector, auto vs. manual instrumentation, OTLP protocol.
* [`11-observability/alerting/`](11-observability/alerting/) — SLI/SLO burn rate alerting, alert fatigue mitigation, PagerDuty integration.
* [`11-observability/monitoring/`](11-observability/monitoring/) — Blackbox vs. whitebox monitoring, synthetic testing, health endpoints.
* [`11-observability/incident-management/`](11-observability/incident-management/) — Incident severity definitions (SEV1-4), post-mortem root cause analysis (RCA).

---

## 12. AI / GenAI Systems
*Enterprise LLM integration, retrieval augmented generation, and agentic workflows.*

* [`12-ai/ai-architecture/`](12-ai/ai-architecture/) — High-level AI system topology, LLM orchestration layers.
* [`12-ai/llm/`](12-ai/llm/) — Foundation models, context window management, prompting architectures, temperature/top_p.
* [`12-ai/rag/`](12-ai/rag/) — Retrieval-Augmented Generation, chunking, embedding models, re-ranking.
* [`12-ai/agents/`](12-ai/agents/) — Autonomous multi-agent architectures, tool calling, memory management, planning loops.
* [`12-ai/vector-databases/`](12-ai/vector-databases/) — Pinecone, Qdrant, Milvus, pgvector, HNSW vs. IVF indexing.
* [`12-ai/model-serving/`](12-ai/model-serving/) — vLLM, Triton, Ollama, batching, GPU utilization, quantized inference.
* [`12-ai/ai-security/`](12-ai/ai-security/) — Prompt injection defense, data leakage prevention, toxic output filtering.
* [`12-ai/ai-evaluation/`](12-ai/ai-evaluation/) — RAG triad (Faithfulness, Answer Relevance, Context Precision), LLM-as-a-judge.
* [`12-ai/enterprise-ai/`](12-ai/enterprise-ai/) — Enterprise data residency, private model fine-tuning, audit logging.

---

## 13. Architecture Patterns
*Detailed breakdown of modern system architecture patterns.*

* [`13-architecture-patterns/microservices/`](13-architecture-patterns/microservices/) — Service decomposition, bounded contexts, independent deployability.
* [`13-architecture-patterns/modular-monolith/`](13-architecture-patterns/modular-monolith/) — In-process boundary enforcement, domain isolation, migration paths.
* [`13-architecture-patterns/event-driven/`](13-architecture-patterns/event-driven/) — Event notifications, event-carried state transfer, pub/sub.
* [`13-architecture-patterns/cqrs/`](13-architecture-patterns/cqrs/) — Command Query Responsibility Segregation, read-model projection.
* [`13-architecture-patterns/event-sourcing/`](13-architecture-patterns/event-sourcing/) — Immutable event append logs, state rehydration, snapshotting.
* [`13-architecture-patterns/saga/`](13-architecture-patterns/saga/) — Distributed transactions: Choreographed vs. Orchestrated sagas, compensating actions.
* [`13-architecture-patterns/strangler-fig/`](13-architecture-patterns/strangler-fig/) — Incremental legacy replacement, routing interceptors.
* [`13-architecture-patterns/hexagonal/`](13-architecture-patterns/hexagonal/) — Ports and Adapters, decoupling core business logic from outer infrastructure.
* [`13-architecture-patterns/clean-architecture/`](13-architecture-patterns/clean-architecture/) — Concentric dependency rule, entities, use cases, interface adapters.
* [`13-architecture-patterns/domain-driven-design/`](13-architecture-patterns/domain-driven-design/) — Strategic & tactical DDD: Ubiquitous Language, Aggregates, Entities, Value Objects.
* [`13-architecture-patterns/serverless/`](13-architecture-patterns/serverless/) — Event-driven compute, cold starts, ephemeral compute limits.

---

## 14. Enterprise Integration
*Core industry-specific integration domains.*

* [`14-enterprise-integration/erp/`](14-enterprise-integration/erp/) — SAP, Oracle ERP Cloud integration, inventory sync, master data.
* [`14-enterprise-integration/crm/`](14-enterprise-integration/crm/) — Salesforce, Microsoft Dynamics integration, lead/contact syncing.
* [`14-enterprise-integration/payments/`](14-enterprise-integration/payments/) — Payment gateways (Stripe, Adyen), settlement pipelines, 3DS authentication.
* [`14-enterprise-integration/banking/`](14-enterprise-integration/banking/) — Core banking ledgers, ISO 20022 messaging, SWIFT networks.
* [`14-enterprise-integration/insurance/`](14-enterprise-integration/insurance/) — Policy management systems, claims processing engines, underwriting workflows.
* [`14-enterprise-integration/healthcare/`](14-enterprise-integration/healthcare/) — HL7, FHIR, EHR integrations, HIPAA compliance.
* [`14-enterprise-integration/ecommerce/`](14-enterprise-integration/ecommerce/) — Cart, checkout, pricing engines, catalog syndication.
* [`14-enterprise-integration/logistics/`](14-enterprise-integration/logistics/) — Order management, warehouse management systems (WMS), track & trace.
* [`14-enterprise-integration/enterprise-systems/`](14-enterprise-integration/enterprise-systems/) — Service bus, message brokers, enterprise file transfers (MFT).

---

## 15. Modernization
*Strategies for decomposing legacy debt and cloud migrations.*

* [`15-modernization/legacy-modernization/`](15-modernization/legacy-modernization/) — Legacy codebase assessment, technical debt cataloging, ROI evaluation.
* [`15-modernization/monolith-to-microservices/`](15-modernization/monolith-to-microservices/) — Step-by-step extraction blueprints, boundary identification.
* [`15-modernization/on-prem-to-cloud/`](15-modernization/on-prem-to-cloud/) — The 7 Rs of migration (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate).
* [`15-modernization/database-modernization/`](15-modernization/database-modernization/) — Monolithic database decomposition, change data capture (CDC) sync, cutover.
* [`15-modernization/java-modernization/`](15-modernization/java-modernization/) — Java 8 to 21+ upgrade paths, framework modernization (Struts/EJB to Spring Boot).
* [`15-modernization/dotnet-modernization/`](15-modernization/dotnet-modernization/) — .NET Framework 4.x to .NET Core / .NET 8+ migration strategies.
* [`15-modernization/application-migration/`](15-modernization/application-migration/) — Dual-run testing, canary cutovers, automated rollback mechanisms.
* [`15-modernization/modernization-strategies/`](15-modernization/modernization-strategies/) — Risk matrices, business case formulation, migration wave planning.

---

## 16. Architecture Deliverables & Reusable Templates
*Ready-to-use professional markdown templates for solution design.*

* [`16-architecture-deliverables/ADR-TEMPLATE.md`](16-architecture-deliverables/ADR-TEMPLATE.md) — Architecture Decision Record.
* [`16-architecture-deliverables/SOLUTION-ARCHITECTURE-TEMPLATE.md`](16-architecture-deliverables/SOLUTION-ARCHITECTURE-TEMPLATE.md) — Comprehensive Solution Architecture Document (SAD).
* [`16-architecture-deliverables/HLD-TEMPLATE.md`](16-architecture-deliverables/HLD-TEMPLATE.md) — High-Level Design document.
* [`16-architecture-deliverables/LLD-TEMPLATE.md`](16-architecture-deliverables/LLD-TEMPLATE.md) — Low-Level Design document.
* [`16-architecture-deliverables/API-DESIGN-TEMPLATE.md`](16-architecture-deliverables/API-DESIGN-TEMPLATE.md) — Enterprise API specification.
* [`16-architecture-deliverables/DATA-DESIGN-TEMPLATE.md`](16-architecture-deliverables/DATA-DESIGN-TEMPLATE.md) — Data schema, topology, and persistence design.
* [`16-architecture-deliverables/SECURITY-DESIGN-TEMPLATE.md`](16-architecture-deliverables/SECURITY-DESIGN-TEMPLATE.md) — Security & threat modeling blueprint.
* [`16-architecture-deliverables/DEPLOYMENT-DESIGN-TEMPLATE.md`](16-architecture-deliverables/DEPLOYMENT-DESIGN-TEMPLATE.md) — Infrastructure deployment & topology blueprint.
* [`16-architecture-deliverables/INTEGRATION-DESIGN-TEMPLATE.md`](16-architecture-deliverables/INTEGRATION-DESIGN-TEMPLATE.md) — Point-to-point & event integration contract.
* [`16-architecture-deliverables/ARCHITECTURE-REVIEW-TEMPLATE.md`](16-architecture-deliverables/ARCHITECTURE-REVIEW-TEMPLATE.md) — Architecture Review Board (ARB) submission.
* [`16-architecture-deliverables/RISK-REGISTER-TEMPLATE.md`](16-architecture-deliverables/RISK-REGISTER-TEMPLATE.md) — Enterprise technical risk register.
* [`16-architecture-deliverables/REFERENCE-ARCHITECTURE-TEMPLATE.md`](16-architecture-deliverables/REFERENCE-ARCHITECTURE-TEMPLATE.md) — Industry reference architecture template.
* [`16-architecture-deliverables/CASE-STUDY-TEMPLATE.md`](16-architecture-deliverables/CASE-STUDY-TEMPLATE.md) — Post-mortem and transformation case study.
* [`16-architecture-deliverables/SYSTEM-DESIGN-TEMPLATE.md`](16-architecture-deliverables/SYSTEM-DESIGN-TEMPLATE.md) — System design blueprint for enterprise systems and interviews.

---

## 17. Architecture Diagrams & C4 Model
*Visual architecture documentation standards and visual templates.*

* [`17-diagrams/c4/`](17-diagrams/c4/) — C4 Model definitions: Context, Container, Component, and Code.
* [`17-diagrams/context/`](17-diagrams/context/) — System Context diagrams (Level 1).
* [`17-diagrams/container/`](17-diagrams/container/) — Container diagrams (Level 2).
* [`17-diagrams/component/`](17-diagrams/component/) — Component diagrams (Level 3).
* [`17-diagrams/sequence/`](17-diagrams/sequence/) — Sequence diagrams for complex distributed handshakes.
* [`17-diagrams/deployment/`](17-diagrams/deployment/) — Physical & cloud deployment topologies.
* [`17-diagrams/data-flow/`](17-diagrams/data-flow/) — Data flow diagrams (DFD) and pipelines.
* [`17-diagrams/network/`](17-diagrams/network/) — VPC, subnets, DMZ, firewall, and routing topologies.
* [`17-diagrams/security/`](17-diagrams/security/) — Trust boundaries, encryption envelopes, and authentication flows.

---

## 18. Reference Architectures
*End-to-end industry blueprint architectures.*

* [`18-reference-architectures/ecommerce/`](18-reference-architectures/ecommerce/) — Global scale retail e-commerce platform.
* [`18-reference-architectures/fintech/`](18-reference-architectures/fintech/) — High-throughput payments and ledger processing engine.
* [`18-reference-architectures/healthcare/`](18-reference-architectures/healthcare/) — HIPAA-compliant electronic health records & telemetry.
* [`18-reference-architectures/edtech/`](18-reference-architectures/edtech/) — Video streaming, LMS, and collaborative learning engine.
* [`18-reference-architectures/logistics/`](18-reference-architectures/logistics/) — Real-time fleet tracking, geofencing, and supply chain routing.
* [`18-reference-architectures/saas/`](18-reference-architectures/saas/) — Multi-tenant B2B SaaS platform with tenant isolation.
* [`18-reference-architectures/crm/`](18-reference-architectures/crm/) — Distributed customer 360 data and engagement platform.
* [`18-reference-architectures/erp/`](18-reference-architectures/erp/) — Modular enterprise resource planning system.
* [`18-reference-architectures/marketplace/`](18-reference-architectures/marketplace/) — Two-sided marketplace matching engine.
* [`18-reference-architectures/ai-platform/`](18-reference-architectures/ai-platform/) — Enterprise GenAI platform with RAG, governance, and audit trails.

---

## 19. Case Studies & Post-Mortems
*Real-world engineering analyses, scale leaps, and post-mortems.*

* [`19-case-studies/scalability/`](19-case-studies/scalability/) — Scaling systems from 1,000 to 1,000,000 requests per second.
* [`19-case-studies/modernization/`](19-case-studies/modernization/) — Complete core modernization of a 20-year-old mainframe/monolith.
* [`19-case-studies/migration/`](19-case-studies/migration/) — Zero-downtime data center to multi-cloud migration.
* [`19-case-studies/integration/`](19-case-studies/integration/) — Global M&A integration of disparate enterprise technology stacks.
* [`19-case-studies/security/`](19-case-studies/security/) — Post-breach remediation and zero-trust transformation.
* [`19-case-studies/performance/`](19-case-studies/performance/) — Taming tail latency in distributed microservices.
* [`19-case-studies/enterprise/`](19-case-studies/enterprise/) — Global ERP consolidation across 40 countries.

---

## 20. System Design Interview Playbook
*Senior, Staff, Principal, and Architect interview preparation guide.*

* [`20-interview-system-design/system-design/`](20-interview-system-design/system-design/) — System design interview methodology and structured 45-minute pacing.
* [`20-interview-system-design/architecture-interviews/`](20-interview-system-design/architecture-interviews/) — Enterprise & Solution Architect interview rubrics.
* [`20-interview-system-design/scenario-based/`](20-interview-system-design/scenario-based/) — Real-world ambiguous scenarios and structured responses.
* [`20-interview-system-design/tradeoffs/`](20-interview-system-design/tradeoffs/) — Mastering and articulating architectural trade-offs under pressure.
* [`20-interview-system-design/estimation/`](20-interview-system-design/estimation/) — Back-of-the-envelope capacity estimations and formulas.
* [`20-interview-system-design/leadership/`](20-interview-system-design/leadership/) — Technical leadership, stakeholder management, and architectural influence.

---

## 21. Architecture Tools & Checklists
*Production review checklists, sizing tools, and generators.*

### Production Review Checklists
* [`21-architecture-tools/checklists/architecture-review-checklist.md`](21-architecture-tools/checklists/architecture-review-checklist.md) — Comprehensive ARB review scorecard.
* [`21-architecture-tools/checklists/solution-architecture-checklist.md`](21-architecture-tools/checklists/solution-architecture-checklist.md) — Pre-implementation SAD quality gate.
* [`21-architecture-tools/checklists/microservices-checklist.md`](21-architecture-tools/checklists/microservices-checklist.md) — Microservice design and readiness verification.
* [`21-architecture-tools/checklists/api-review-checklist.md`](21-architecture-tools/checklists/api-review-checklist.md) — API contract, security, and versioning standards.
* [`21-architecture-tools/checklists/database-review-checklist.md`](21-architecture-tools/checklists/database-review-checklist.md) — Database schema, indexing, and query hygiene.
* [`21-architecture-tools/checklists/security-review-checklist.md`](21-architecture-tools/checklists/security-review-checklist.md) — Application and infrastructure security assessment.
* [`21-architecture-tools/checklists/cloud-architecture-checklist.md`](21-architecture-tools/checklists/cloud-architecture-checklist.md) — Well-Architected cloud posture review.
* [`21-architecture-tools/checklists/production-readiness-checklist.md`](21-architecture-tools/checklists/production-readiness-checklist.md) — Go-live and production launch verification.
* [`21-architecture-tools/checklists/disaster-recovery-checklist.md`](21-architecture-tools/checklists/disaster-recovery-checklist.md) — DR readiness, failover validation, RPO/RTO testing.
* [`21-architecture-tools/checklists/observability-checklist.md`](21-architecture-tools/checklists/observability-checklist.md) — Metrics, tracing, logging, and alerting coverage.

### Tooling Subdirectories
* [`21-architecture-tools/calculators/`](21-architecture-tools/calculators/) — Capacity and throughput calculators.
* [`21-architecture-tools/templates/`](21-architecture-tools/templates/) — Tool configuration templates.
* [`21-architecture-tools/scripts/`](21-architecture-tools/scripts/) — Architecture validation automation scripts.
* [`21-architecture-tools/linters/`](21-architecture-tools/linters/) — Markdown and architecture spec linters.
* [`21-architecture-tools/generators/`](21-architecture-tools/generators/) — Diagram and scaffolding generators.

---

## 22. Reference
*Authoritative cheatsheets, comparison tables, and technology compendiums.*

* [`22-reference/glossaries/`](22-reference/glossaries/) — Definitions of core architecture terminology.
* [`22-reference/acronyms/`](22-reference/acronyms/) — Enterprise IT and architecture acronym handbook.
* [`22-reference/technology-comparison/`](22-reference/technology-comparison/) — Technology side-by-side matrices (e.g. Kafka vs. RabbitMQ).
* [`22-reference/pattern-comparison/`](22-reference/pattern-comparison/) — Architecture pattern trade-off matrices.
* [`22-reference/protocol-reference/`](22-reference/protocol-reference/) — Network and wire protocol deep dives.
* [`22-reference/cloud-services/`](22-reference/cloud-services/) — AWS vs. Azure vs. GCP service equivalency tables.
* [`22-reference/technology-radar/`](22-reference/technology-radar/) — Radar historical archive and criteria.

---

## 99. Experiments
*Isolated proof-of-concept labs, performance spikes, and architectural validations.*

* [`99-experiments/dotnet/`](99-experiments/dotnet/) — .NET runtime benchmarks and POCs.
* [`99-experiments/java/`](99-experiments/java/) — Java / Virtual thread performance spikes.
* [`99-experiments/python/`](99-experiments/python/) — Async Python and AI pipeline benchmarks.
* [`99-experiments/frontend/`](99-experiments/frontend/) — Frontend rendering and bundle experiments.
* [`99-experiments/cloud/`](99-experiments/cloud/) — Cloud deployment automation spikes.
* [`99-experiments/kubernetes/`](99-experiments/kubernetes/) — Custom controllers and service mesh experiments.
* [`99-experiments/ai/`](99-experiments/ai/) — Local LLM inference, embedding, and agent spikes.
* [`99-experiments/distributed-systems/`](99-experiments/distributed-systems/) — Consensus, partition, and replication tests.
