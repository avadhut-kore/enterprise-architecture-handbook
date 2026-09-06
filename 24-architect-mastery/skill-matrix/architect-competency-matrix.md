# Architect Competency Matrix: 16 Core Competencies Across 6 Tiers

> **"Architectural competency is not a measure of how many technologies you have memorized. It is a measure of systems thinking, trade-off rigor, operational foresight, and organizational influence."**

---

## 1. The 6-Level Capability Maturity Scale (L0 – L5)

| Level | Designation | Operational Definition & Behavioral Anchor |
| :---: | :--- | :--- |
| **L0** | **Awareness** | Knows the terminology, basic definitions, and high-level concepts. Can follow architectural discussions but cannot design or implement independently. |
| **L1** | **Practitioner** | Can implement features and components following established architectural patterns, templates, and senior guidance. |
| **L2** | **Independent** | Autonomously designs and delivers production-grade services, schemas, and components; anticipates common failure modes and writes unit/integration tests. |
| **L3** | **Advanced** | Architects complex multi-service applications; evaluates competing patterns; writes formal ADRs and NFR matrices; mentors other engineers. |
| **L4** | **Architect** | Designs cross-system platforms and solutions; defines enterprise standards and reference blueprints; defends architectures before the ARB; models 3-year TCO. |
| **L5** | **Strategic / Enterprise** | Shapes multi-year corporate technology direction, M&A due diligence, and capital allocation; simplifies enterprise complexity; advises C-Suite and Board. |

---

## 2. Master Competency Matrix (Role by Competency Expected Level)

| Competency Dimension | Senior Engineer | Lead Engineer | Solution Architect | Technical Architect | Enterprise Architect | Principal Architect |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| [**1. Technical Depth & Runtimes**](../competency-model/technical-depth.md) | **L3** | **L3** | **L3** | **L4** | **L2** | **L4** |
| [**2. System Design & Scalability**](../competency-model/system-design.md) | **L2** | **L3** | **L4** | **L4** | **L3** | **L5** |
| [**3. Software Architecture (DDD/Clean)**](../competency-model/software-architecture.md)| **L3** | **L4** | **L4** | **L4** | **L3** | **L4** |
| [**4. Distributed Systems & Consistency**](../competency-model/distributed-systems.md)| **L2** | **L3** | **L4** | **L4** | **L2** | **L5** |
| [**5. Cloud & Infrastructure**](../competency-model/cloud-architecture.md) | **L2** | **L3** | **L4** | **L4** | **L3** | **L4** |
| [**6. Data Architecture & Lakehouses**](../competency-model/data-architecture.md) | **L2** | **L3** | **L4** | **L4** | **L3** | **L4** |
| [**7. Integration & Messaging**](../competency-model/integration-architecture.md) | **L2** | **L3** | **L4** | **L4** | **L4** | **L4** |
| [**8. Security & Zero Trust**](../competency-model/security-architecture.md) | **L2** | **L3** | **L4** | **L4** | **L3** | **L4** |
| [**9. Observability & SRE**](../competency-model/observability-and-sre.md) | **L3** | **L3** | **L3** | **L4** | **L2** | **L4** |
| [**10. DevOps & Platform Engineering**](../competency-model/devops-and-platform-engineering.md) | **L2** | **L3** | **L3** | **L5** | **L2** | **L4** |
| [**11. AI & GenAI Systems**](../competency-model/ai-architecture.md) | **L1** | **L2** | **L3** | **L3** | **L3** | **L4** |
| [**12. Business Acumen & Unit Economics**](../competency-model/business-acumen.md)| **L1** | **L2** | **L4** | **L3** | **L5** | **L5** |
| [**13. Leadership & Influence**](../competency-model/leadership.md) | **L2** | **L3** | **L4** | **L4** | **L4** | **L5** |
| [**14. Executive Communication**](../competency-model/communication.md) | **L1** | **L2** | **L4** | **L3** | **L5** | **L5** |
| [**15. Architecture Governance & ARB**](../competency-model/governance.md) | **L1** | **L2** | **L4** | **L4** | **L5** | **L5** |
| [**16. Strategic Thinking & Evolution**](../competency-model/strategic-thinking.md) | **L1** | **L2** | **L3** | **L4** | **L5** | **L5** |

---

## 3. Deep Behavioral Anchors Across the 16 Competencies

### 1. Technical Depth & Runtime Internals
* **L0**: Understands what a compiler, interpreter, and garbage collector are.
* **L1**: Writes functional code in a primary language (.NET, Java, Python, TypeScript) avoiding syntax errors.
* **L2**: Understands memory allocation, heap vs stack, garbage collection pressure, and thread contention.
* **L3**: Profiles CPU/memory hotspots, tunes connection pools, optimizes SQL execution plans, and analyzes thread dumps.
* **L4**: Compares runtime internals across polyglot ecosystems; designs low-latency zero-copy memory architectures; evaluates JIT vs AOT compilation trade-offs.
* **L5**: Evaluates kernel bypass networking (e.g., DPDK, io_uring), custom hardware acceleration, and next-generation instruction sets.

### 2. System Design & Scalability
* **L0**: Recognizes the difference between vertical scaling (bigger server) and horizontal scaling (more servers).
* **L1**: Deploys multi-instance web servers behind a basic load balancer.
* **L2**: Identifies stateful vs stateless components; designs sticky sessions vs shared cache sessions.
* **L3**: Decomposes systems into microservices or modular monoliths; designs sharding, partitioning, and read-replicas.
* **L4**: Designs multi-region active-active topologies; architects global CDN edge caching and rate-limiting fabrics; formulates formal NFR matrices ([NFR Generator](../../21-architecture-tools/generators/nfr_matrix_generator.py)).
* **L5**: Designs planetary-scale architectures handling millions of QPS; formulates multi-cloud disaster recovery architectures with automated cross-region failover.

### 3. Software Architecture & Modularity
* **L0**: Understands basic object-oriented or functional programming concepts.
* **L1**: Applies standard design patterns (Factory, Singleton, Strategy) within a single codebase.
* **L2**: Applies SOLID principles and Clean Architecture / Hexagonal (Ports & Adapters) boundaries to prevent coupling.
* **L3**: Applies Domain-Driven Design (DDD) strategic modeling: bounded contexts, ubiquitous language, and domain events.
* **L4**: Establishes corporate-wide modularity frameworks, micro-frontend module federation, and decoupled core platform services.
* **L5**: Defines corporate software development tenets and architectural paradigms that outlast individual frameworks and technology generations.

### 4. Distributed Systems & Consistency
* **L0**: Can define the acronym CAP (Consistency, Availability, Partition Tolerance).
* **L1**: Distinguishes synchronous API calls from asynchronous background tasks.
* **L2**: Understands eventual consistency, race conditions, and distributed locks (Redis Redlock, ZooKeeper).
* **L3**: Applies PACELC trade-offs; designs distributed Sagas with compensating transactions; implements idempotent receivers and transactional outboxes.
* **L4**: Analyzes consensus protocols (Raft, Paxos); navigates split-brain resolution, clock drift, and vector clocks; architects multi-leader replication topologies.
* **L5**: Authors foundational distributed system topologies or evaluates breakthrough consensus mechanisms for mission-critical core banking and ledger platforms.

### 5. Cloud & Infrastructure Architecture
* **L0**: Knows the major public cloud providers (AWS, Azure, GCP) and basic virtual machine hosting.
* **L1**: Launches cloud resources manually or via simple Infrastructure as Code (Terraform) scripts.
* **L2**: Designs production VPC topologies, subnets, security groups, auto-scaling groups, and managed databases.
* **L3**: Architects multi-account cloud landing zones, transit gateways, direct connects, and container orchestration clusters (EKS/AKS).
* **L4**: Designs hybrid-cloud and multi-cloud architectures; implements FinOps unit cost modeling ([FinOps](../../08-cloud/cloud-cost-optimization/README.md)); optimizes reserved instances and savings plans.
* **L5**: Formulates enterprise cloud strategy ($100M+ portfolio), cloud repatriation trade-offs, and sovereign cloud compliance.

### 6. Data Architecture & Persistence
* **L0**: Distinguishes relational SQL databases from NoSQL key-value stores.
* **L1**: Writes standard CRUD queries and basic relational database tables.
* **L2**: Designs normalized schemas, composite indexes, foreign keys, and handles connection pool exhaustion.
* **L3**: Selects polyglot persistence (Relational, Document, Columnar, Time-Series, Graph); designs CQRS read models and cache-aside layers.
* **L4**: Architects enterprise Lakehouses (Apache Iceberg, Delta Lake), CDC data pipelines (Debezium), and hybrid search engines (Lucene + HNSW Vector).
* **L5**: Defines corporate Data Mesh strategy, global data governance frameworks, master data management (MDM), and data sovereignty compliance.

### 7. Integration & Messaging Architecture
* **L0**: Understands REST APIs and JSON payload formatting.
* **L1**: Integrates client applications with external REST APIs using API keys or basic auth.
* **L2**: Designs RESTful APIs following OpenAPI specifications; handles HTTP status codes, pagination, and rate limits.
* **L3**: Implements asynchronous event streams (Kafka, RabbitMQ); handles partition keys, consumer lag, poison pills, and dead-letter queues.
* **L4**: Architects enterprise API-led connectivity (System, Process, Experience APIs); designs enterprise iPaaS, SAP ERP, and CRM event integration backbones.
* **L5**: Defines global integration standards, enterprise service bus phase-out roadmaps, and event-driven architecture governance across hundreds of systems.

### 8. Security Architecture & Zero Trust
* **L0**: Aware of passwords, encryption, and basic user authentication.
* **L1**: Implements password hashing (bcrypt/argon2) and protects against basic OWASP Top 10 vulnerabilities (SQLi, XSS).
* **L2**: Implements OAuth2/OIDC token validation, JWT claims verification, and role-based access control (RBAC).
* **L3**: Performs STRIDE threat modeling ([STRIDE Template](../../21-architecture-tools/templates/threat-model-stride-template.md)); implements secrets management (HashiCorp Vault) and encryption-in-transit (mTLS).
* **L4**: Architects Zero Trust enterprise perimeters, service mesh mTLS policies, hardware security modules (HSM/KMS), and KeyStore/Secure Enclave mobile security.
* **L5**: Advises the CISO and Board on corporate cyber-resilience, nation-state threat models, and global regulatory cryptographic compliance (FIPS 140-3).

### 9. Observability & SRE
* **L0**: Understands application console logs.
* **L1**: Adds log statements to code and views logs in a centralized aggregator (ELK, CloudWatch).
* **L2**: Implements structured JSON logging, health check endpoints (`/healthz`, `/ready`), and basic alert rules.
* **L3**: Instruments distributed tracing using OpenTelemetry; defines Service Level Objectives (SLOs) and error budget burn-rate alerts.
* **L4**: Architects unified telemetry platforms (Logs, Metrics, Traces, Profiling); designs automated canary deployment gates and chaos engineering drills.
* **L5**: Transforms corporate culture to blameless operational learning; links technical telemetry directly to business KPIs (e.g., revenue impact per 100ms latency increase).

### 10. DevOps & Platform Engineering
* **L0**: Understands Git commit, push, and pull requests.
* **L1**: Configures basic CI pipelines (GitHub Actions, GitLab CI) running linter and unit tests.
* **L2**: Writes Dockerfiles, Helm charts, and multi-stage container builds; implements automated deployment pipelines.
* **L3**: Architects GitOps deployment fabrics (ArgoCD/Flux), progressive rollouts (canary/blue-green), and automated rollback triggers.
* **L4**: Designs Internal Developer Platforms (IDPs); implements self-service "Golden Paths" that reduce developer cognitive load; enforces automated architectural linters ([Doc Linter](../../21-architecture-tools/linters/doc_linter.py)).
* **L5**: Redesigns the corporate software delivery lifecycle (SDLC) across thousands of engineers to optimize DORA metrics (Deployment Frequency, Lead Time, MTTR, Change Failure Rate).

### 11. AI & GenAI Systems Architecture
* **L0**: Aware of ChatGPT, machine learning, and basic artificial intelligence concepts.
* **L1**: Integrates commercial LLM APIs (OpenAI, Anthropic) into applications via basic REST prompts.
* **L2**: Implements Retrieval-Augmented Generation (RAG) using chunking, embeddings, and vector similarity search.
* **L3**: Architects hybrid search (BM25 + Dense Vector), prompt evaluation harnesses, guardrails against prompt injection, and semantic caching.
* **L4**: Architects production high-throughput LLM serving infrastructure (vLLM, TensorRT-LLM, Triton) with continuous batching and PagedAttention ([12-ai](../../12-ai/model-serving/README.md)).
* **L5**: Defines corporate Enterprise AI Strategy: proprietary foundational model governance, data IP protection, sovereign AI hosting, and autonomous multi-agent orchestration.

### 12. Business Acumen & Unit Economics
* **L0**: Understands that software exists to support business operations.
* **L1**: Understands the user persona and primary business purpose of assigned features.
* **L2**: Understands team budget constraints and prioritizes sprint items that unblock user adoption.
* **L3**: Calculates cost-per-user, cost-per-transaction, and cloud hosting margins; models ROI for proposed technical refactoring.
* **L4**: Conducts rigorous Build vs Buy vs Partner analyses; models 3-year Total Cost of Ownership (TCO) including licensing, labor, and depreciation.
* **L5**: Translates enterprise balance sheets and corporate strategy into technology capital investments; evaluates M&A technical synergies and portfolio enterprise value.

### 13. Leadership & Influence Without Authority
* **L0**: Works cooperatively within a team.
* **L1**: Participates actively in team discussions and assists junior team members.
* **L2**: Mentors junior engineers; leads code reviews that elevate engineering standards.
* **L3**: Leads technical planning across a multidisciplinary team; drives healthy consensus and resolves technical disputes decisively.
* **L4**: Guides and mentors Solution Architects; aligns competing engineering squads toward shared platform standards without managerial authority.
* **L5**: Shapes corporate engineering culture; inspires confidence across executive leadership; cultivates an environment of intellectual humility and psychological safety.

### 14. Executive & Technical Communication
* **L0**: Can explain code logic to immediate peers.
* **L1**: Writes clear pull request descriptions and bug reports.
* **L2**: Authors concise 2–4 page technical design memos (LLD); presents demos to product stakeholders.
* **L3**: Authors unambiguous HLDs and ADRs; presents architecture proposals to the ARB; facilitates technical workshops.
* **L4**: Authors the 1-page Executive Memo; translates complex technical risk into financial and business impact for Directors and VPs.
* **L5**: Briefs the CEO, CFO, and Board of Directors on high-stakes technological investments; represents the corporation at global industry keynotes and standards bodies.

### 15. Architecture Governance & ARB
* **L0**: Aware that company coding standards exist.
* **L1**: Adheres to team linting, formatting, and security policies.
* **L2**: Participates in team design reviews and enforces code review standards.
* **L3**: Submits complete architecture packages to the ARB; addresses review conditions and remediates technical debt.
* **L4**: Presides over Architecture Review Boards; designs lightweight, risk-weighted governance gates; curates the corporate Technology Radar.
* **L5**: Establishes enterprise architecture governance policies that balance regulatory compliance against product velocity, eliminating bureaucratic friction.

### 16. Strategic Thinking & Technology Evolution
* **L0**: Focuses on immediate task execution.
* **L1**: Thinks ahead to the current sprint and upcoming milestone.
* **L2**: Considers the 6-month maintainability of services and anticipates version deprecations.
* **L3**: Designs evolutionary architectures with explicit transition states and modular boundaries that facilitate future replacement.
* **L4**: Maps multi-year technology roadmaps; plans the systematic retirement of legacy systems via the Strangler Fig pattern ([15-modernization](../../15-modernization/README.md)).
* **L5**: Formulates 5–10 year technology horizon strategies; spots disruptive paradigm shifts early; makes bold strategic technical bets that secure corporate survival.
