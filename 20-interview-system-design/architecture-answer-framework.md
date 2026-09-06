# The Architecture Answer Framework: 22-Step Reusable Blueprint

> The master sequence for articulating an end-to-end architecture answer in senior and executive-level system design interviews.

---

## 1. The 22-Step Architecture Sequence

Senior candidates often suffer from either **under-communicating** (jumping immediately into code/databases) or **rambling** without a clear structure. This 22-step sequence ensures every dimension—from business context to multi-year evolution—is logically presented.

> [!NOTE]
> Not every 45-minute interview requires equal depth across all 22 steps. Treat this as an **indexed menu** of architectural competencies: execute steps 1–12 by default, and expand steps 13–22 based on the interviewer's priorities and domain requirements.

```
PHASE I: CONTEXT & SCOPE (Steps 1–6)
  1. Restate the problem & business intent
  2. Clarify assumptions & constraints
  3. Define explicit scope boundaries (In vs Out)
  4. Functional requirements (Top 3–4 User Journeys)
  5. Non-functional requirements (Latency, Availability, Consistency)
  6. Back-of-the-envelope scale estimation

PHASE II: STRUCTURAL DESIGN (Steps 7–13)
  7. High-level architecture (C4 Container Diagram)
  8. Core request & event flows
  9. Core data models & schema strategy
  10. API contracts & event payloads
  11. Storage strategy (SQL vs NoSQL vs NewSQL vs Object Store)
  12. Caching architecture & invalidation policies
  13. Messaging, asynchronous decoupling & streaming

PHASE III: ENTERPRISE DEPTH & RESILIENCE (Steps 14–18)
  14. Security architecture & trust boundaries
  15. Observability, metrics, logs, traces & SLOs
  16. Reliability, redundancy & disaster recovery (RTO/RPO)
  17. Scaling strategy (Horizontal, Sharding, Read Replicas)
  18. Failure handling, graceful degradation & circuit breakers

PHASE IV: REALITY & EVOLUTION (Steps 19–22)
  19. Deployment, infrastructure & CI/CD topology
  20. Cost modeling & unit economics
  21. Architectural trade-offs & rejected alternatives
  22. Multi-year evolution & 10x scale roadmap
```

---

## 2. Detailed Execution of Each Step

### Phase I: Context & Scope

#### 1. Restate the Problem
* *What to say*: Summarize the prompt in your own words, highlighting the core business value.
* *Example*: *"We need to design a high-throughput, low-latency URL shortening platform similar to TinyURL or Bitly that enables users to generate short aliases, redirect at scale, and gather basic click analytics."*

#### 2. Clarify Assumptions
* *What to say*: Surface hidden constraints regarding tenancy, user geography, or hardware limitations.
* *Example*: *"I assume global read traffic is geographically distributed, write traffic is lower volume, and 99.9% of requests will be redirects rather than new link creations."*

#### 3. Define Scope Boundaries (In vs. Out)
* *What to say*: Define what will be delivered today versus what is deferred to keep the design focused.
* *Example*: *"In scope: URL generation, redirect resolution, analytics event capture, and high availability. Out of scope: custom vanity domains, multi-tenant billing, and deep fraud/spam detection algorithms."*

#### 4. Functional Requirements
* *What to say*: List the 3 or 4 fundamental user actions.
* *Example*:
  1. User submits a long URL and receives a unique 7-character short URL.
  2. User accesses a short URL and is redirected via HTTP 302/301 to the original URL.
  3. User can view basic click analytics (total clicks, referrer country).

#### 5. Non-Functional Requirements (NFRs)
* *What to say*: Quantify operational targets.
* *Example*:
  * **Availability**: 99.99% for redirection (Tier-1 path).
  * **Latency**: p95 redirect latency < 30ms; p99 < 80ms.
  * **Consistency**: Eventual consistency is acceptable for analytics; read-after-write consistency for link creation.
  * **Durability**: 100% link durability over a 5-year retention period.

#### 6. Back-of-the-Envelope Scale Estimation
* *What to say*: Calculate daily volume, average/peak RPS, storage growth, and bandwidth.
* *Example*: 100M new URLs/month $\rightarrow \approx 40$ writes/sec. 100:1 read-to-write ratio $\rightarrow 4,000$ redirects/sec (Peak: 10,000 RPS). 5-year storage: $\approx 3 \text{ TB}$ (manageable on modern storage engines).

---

### Phase II: Structural Design

#### 7. High-Level Architecture
* *What to say*: Present the core containers: CDN $\rightarrow$ API Gateway $\rightarrow$ Stateless Link Services $\rightarrow$ Cache $\rightarrow$ Persistent Store.

#### 8. Core Request & Event Flows
* *What to say*: Trace the write path (create URL) and read path (redirect) step by step, identifying where latency is shaved off.

#### 9. Core Data Models
* *What to say*: Define entity keys, foreign keys, partition keys, and serialization types.
* *Example*: `urls (short_hash [PK], long_url, user_id, created_at, expires_at)`.

#### 10. API Contracts & Event Payloads
* *What to say*: Specify endpoint signatures, HTTP status codes, headers (e.g., `Idempotency-Key`), and event schemas.
* *Example*: `POST /v1/urls` $\rightarrow$ `201 Created { short_url, expires_at }`. `GET /{short_hash}` $\rightarrow$ `302 Found (Location: {long_url})`.

#### 11. Storage Strategy
* *What to say*: Justify the database paradigm. Relational (PostgreSQL) with connection pooling vs. Distributed NoSQL (Cassandra / DynamoDB) with partition keys based on `short_hash`.

#### 12. Caching Architecture
* *What to say*: Detail caching layer (Redis Cluster / Memcached), caching pattern (Cache-Aside), eviction policy (LRU / LFU), TTLs, and cache warmup.

#### 13. Messaging & Async Decoupling
* *What to say*: Decouple non-critical paths (e.g., sending click events to analytics via Apache Kafka / AWS Kinesis) so user-facing redirects are never blocked by analytics sinks.

---

### Phase III: Enterprise Depth & Resilience

#### 14. Security Architecture
* *What to say*: API Gateway rate-limiting (Token Bucket) per IP/API-Key, WAF to block DDoS/SQLi, OAuth2 / JWT authentication, TLS termination at the edge, and least-privilege IAM service roles.

#### 15. Observability & Telemetry
* *What to say*: Distributed tracing using OpenTelemetry (trace ID propagation), RED metrics (Rate, Errors, Duration) for service health, SLO burn-rate alerts, and structured audit logs.

#### 16. Reliability & Disaster Recovery
* *What to say*: Multi-AZ redundancy, read replicas with automatic failover, database backup schedules, and clear RTO (< 15 min) and RPO (< 1 min) definitions.

#### 17. Scaling Strategy
* *What to say*: Horizontal auto-scaling of stateless pods (Kubernetes HPA based on CPU/RPS), database read replicas for read offloading, and hash-range sharding for storage expansion.

#### 18. Failure Handling & Degradation
* *What to say*: Circuit breakers (Resilience4j / Envoy) on downstream calls, fallback to in-memory local caches if distributed cache fails, and graceful degradation for secondary features.

---

### Phase IV: Reality & Evolution

#### 19. Deployment & Infrastructure
* *What to say*: Multi-stage CI/CD pipelines, blue-green or canary deployments, Kubernetes cluster topology, and automated rollback upon elevated error rates.

#### 20. Cost Modeling & Unit Economics
* *What to say*: Calculate cost per million requests. Highlight that CDN caching reduces database IOPS costs by 80%, keeping total monthly infrastructure expenses under target envelopes.

#### 21. Trade-Offs & Rejected Alternatives
* *What to say*: Clearly state what was rejected and why:
  * *"I evaluated a Big-Bang SQL cluster with read replicas vs. DynamoDB. I chose DynamoDB for zero-maintenance auto-partitioning at predictable sub-10ms latency, accepting the trade-off of weaker ad-hoc query capabilities."*

#### 22. Multi-Year Evolution & 10x Scale Roadmap
* *What to say*: Detail how this architecture changes if traffic increases by 10x or 100x (e.g., moving from single-region to multi-region active-active with GeoDNS routing and DynamoDB Global Tables).

---

## 3. Cross-References

* **Universal Framework**: [`architect-interview-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architect-interview-framework.md)
* **Pacing & Timing**: [`system-design-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/system-design-framework.md)
* **Discovery Questions**: [`requirements-discovery.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/requirements-discovery.md)
* **Decision Matrices**: [`tradeoffs/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/README.md)
