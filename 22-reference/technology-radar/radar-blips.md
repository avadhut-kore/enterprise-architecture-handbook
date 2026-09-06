# Technology Radar Blip Registry & Architectural Evaluations

> **Evaluation Cadence**: Quarterly Review  
> **Status**: Active Production Standard  
> **Governing Body**: Enterprise Architecture Review Board (ARB)  

---

## Quadrant I: Languages & Runtimes

| Technology | Ring | Architectural Rationale & Evaluation | Migration / Roadmap Notes |
|---|---|---|---|
| **TypeScript 5.x** | **ADOPT** | Universal standard for frontend and Node.js backend. Enforces compile-time contracts, refactoring safety, and shared schemas with backend. | Default standard for all web, mobile, and BFF services. |
| **Java 21+** | **ADOPT** | Enterprise backend standard. Virtual Threads (Project Loom) drastically reduce memory footprint and context switching for I/O workloads. | Mandate LTS versions (Java 21+); deprecate Java 8/11. |
| **Go 1.22+** | **ADOPT** | Preferred for high-throughput networking proxies, Kubernetes operators, and CPU-efficient microservices. | Standard for infrastructure tooling and edge services. |
| **Python 3.11+** | **ADOPT** | Universal standard for AI/ML pipelines, data science, and scripting automation. | Mandate strict static typing with `mypy` or `pyright`. |
| **Rust** | **TRIAL** | High-performance, memory-safe systems programming. Evaluated for core cryptographic engines and low-latency proxies. | Permitted for specialized high-throughput components with ARB sign-off. |
| **Kotlin Multiplatform (KMP)**| **TRIAL** | Sharing business logic across iOS and Android while retaining native UI rendering. | Evaluated for mobile squad cross-platform pilot projects. |
| **PHP / Ruby on Rails** | **HOLD** | Declining enterprise footprint, lack of strong typing contracts, high memory overhead at scale. | No new projects. Existing apps scheduled for strangler fig migration. |

---

## Quadrant II: Platforms, Cloud & Compute

| Technology | Ring | Architectural Rationale & Evaluation | Migration / Roadmap Notes |
|---|---|---|---|
| **AWS EKS / Azure AKS** | **ADOPT** | Enterprise container orchestration standard. Broad ecosystem, GitOps integration, and mature service meshes. | Default for complex distributed microservice workloads. |
| **AWS Lambda / Cloud Run** | **ADOPT** | Event-driven serverless compute. Zero idle cost, rapid auto-scaling for spiky workloads. | Default for webhooks, cron jobs, and low-traffic APIs. |
| **PostgreSQL 16+ / Aurora** | **ADOPT** | Primary enterprise relational database. Exceptional ACID reliability, JSONB flexibility, and extensions. | Default database choice for new transactional microservices. |
| **Redis Cluster 7+** | **ADOPT** | In-memory distributed caching, session storage, and rate limiting. | Enforce TTL jitter and mutex locking to prevent cache stampedes. |
| **Apache Iceberg** | **ADOPT** | Open table format for modern data lakehouses. ACID guarantees and hidden partitioning on cloud object storage. | Standard format for analytical data lakes. |
| **Google Cloud Spanner** | **TRIAL** | Globally distributed SQL database with external consistency (TrueTime). | Cleared for global multi-region active-active architectures. |
| **Oracle Database 11g/12c**| **HOLD** | Prohibitive core-based licensing costs, high operational toil, vendor lock-in. | Active migration to PostgreSQL / Aurora via AWS DMS. |

---

## Quadrant III: Integration & Infrastructure

| Technology | Ring | Architectural Rationale & Evaluation | Migration / Roadmap Notes |
|---|---|---|---|
| **Apache Kafka** | **ADOPT** | Distributed event streaming backbone. High throughput, ordered partitions, long retention. | Default for asynchronous cross-domain event choreography. |
| **RabbitMQ (Quorum Queues)**| **ADOPT** | Smart-broker queuing with AMQP 0-9-1. Complex routing, dead-letter exchanges, and worker pools. | Default for point-to-point task queues and AMQP workflows. |
| **OpenTelemetry (OTel)** | **ADOPT** | Vendor-neutral distributed tracing, metrics, and log collection standard. | Mandatory instrumentation in all service Docker base images. |
| **ArgoCD** | **ADOPT** | GitOps declarative continuous delivery for Kubernetes clusters. | Default deployment automation tool for production infrastructure. |
| **Envoy Proxy / Istio** | **ADOPT** | Service mesh for automated mutual TLS (mTLS), traffic routing, and observability. | Standard for internal microservice-to-service communication. |
| **vLLM Inference Engine** | **TRIAL** | High-throughput LLM model serving with PagedAttention and continuous batching. | Preferred inference runtime for self-hosted AI workloads. |
| **Monolithic ESBs (Mule 3/TIBCO)**| **HOLD** | Centralized integration bottleneck, expensive licensing, and single point of failure. | Decompose into lightweight microservice APIs and Kafka event mesh. |

---

## Quadrant IV: Architecture Techniques & Patterns

| Technique | Ring | Architectural Rationale & Evaluation | Migration / Roadmap Notes |
|---|---|---|---|
| **Zero Trust Architecture** | **ADOPT** | Continuous authentication, per-request authorization, and micro-segmentation (NIST 800-207). | Mandatory security standard across all cloud VPCs. |
| **Domain-Driven Design (DDD)**| **ADOPT** | Bounded Contexts, Ubiquitous Language, and aggregate root boundaries. | Standard methodology for microservice decomposition. |
| **Transactional Outbox Pattern**| **ADOPT** | Eliminates the distributed dual-write problem between databases and Kafka via CDC. | Mandatory pattern for services publishing domain events. |
| **Architecture Fitness Functions**| **ADOPT** | Automated CI/CD assertions validating architectural boundaries and dependencies. | Enforce via ArchUnit (Java) and Spectral (OpenAPI). |
| **Micro-Frontends** | **TRIAL** | Independent deployment for large engineering teams ($> 50$ engineers) via Module Federation. | Prohibited for small teams; permitted only with explicit ARB waiver. |
| **Shared Database Integration**| **HOLD** | Multiple microservices reading/writing to the same shared database schema. | Strictly prohibited anti-pattern. Enforce private databases per service. |
| **Two-Phase Commit (2PC)** | **HOLD** | Blocking distributed transactions across WAN/cloud boundaries. | Replace with asynchronous Saga choreography. |
