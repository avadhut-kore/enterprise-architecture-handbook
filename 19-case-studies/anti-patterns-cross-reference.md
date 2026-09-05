# Enterprise Anti-Patterns Cross-Reference & Taxonomy

## 1. Architectural Anti-Pattern Catalog

```
                                  [ENTERPRISE ARCHITECTURAL ANTI-PATTERNS]
                                                     │
         ┌───────────────────┬───────────────────────┼───────────────────────┬───────────────────┐
         ▼                   ▼                       ▼                       ▼                   ▼
  [COUPLING TRAPS]    [PERSISTENCE TRAPS]     [RESILIENCY TRAPS]      [BOUNDARY TRAPS]    [GOVERNANCE TRAPS]
   - Distributed       - Dual-Write Pattern    - Retry Storm           - Broken Object     - Second-System
     Monolith          - Hot Partition Lock      Amplification           Authorization       Syndrome
   - Shared Database   - N+1 ORM Explosion     - Stop-The-World GC     - SSRF Cloud        - ARB Waterfall
     Microservices     - Unbounded 2PC / XA    - Connection Pool         Metadata Leak       Paralysis
   - ESB Chokepoint    - Large-Key Monolith      Starvation            - Un-Isolated Blast - Conway's Law
                                               - Cascading Rebalance     Radius              Silos
```

---

## 2. Comprehensive Anti-Pattern Taxonomy & Mapping

### 2.1 Coupling Anti-Patterns
* **The Distributed Monolith (`CS-MOD-01`)**: Decomposing software into dozens of microservices while retaining synchronous HTTP/REST call chains. Cumulative network latency, serialization overhead, and compounded availability drop create an operational nightmare.
  * *Antidote*: Coarse-grained bounded contexts, asynchronous event streaming (Kafka), and compile-time modular monoliths.
* **Shared Database Microservices (`CS-MOD-02`)**: Containerizing compute into separate repositories while pointing all services to the same relational database. Results in circular table deadlocks, schema migration lock-in, and zero domain autonomy.
  * *Antidote*: Strict Database-per-Service pattern with asynchronous domain events.
* **Centralized "Smart-Pipes" ESB Monolith (`CS-INT-05`)**: Funneling all corporate data transformations and orchestrations through a single shared message bus. Creates a giant single point of failure where memory exhaustion in one department's flow takes down the entire corporation.
  * *Antidote*: Dumb pipes (Kafka/RabbitMQ), smart endpoints, and containerized domain integration adapters.

### 2.2 Persistence & Data Integrity Anti-Patterns
* **The Dual-Write Hazard (`CS-INT-01`)**: Committing a transaction to a database and subsequently publishing an event to a message queue in application code. When network packets drop, the system produces irreconcilable ghost state.
  * *Antidote*: Transactional Outbox Pattern with Change Data Capture (Debezium).
* **Hot Partition Contention (`CS-SCALE-01`)**: Concentrating high-frequency writes onto a single domain partition key in distributed NoSQL databases (e.g., DynamoDB, Cassandra). Results in severe throttling despite massive provisioned throughput.
  * *Antidote*: Write-sharding (`Key_Suffix = rand(1, N)`) and in-memory atomic caches.
* **ORM N+1 Query Explosion (`CS-PERF-01`)**: Using ORM eager loading annotations or accessing lazy child relationships inside serialization loops, generating thousands of SQL queries for a single HTTP request.
  * *Antidote*: DTO projection queries with `JOIN FETCH` and automated CI query-budget assertions (QuickPerf).
* **Distributed Two-Phase Commit (2PC) Lockup (`CS-INT-04`)**: Coordinating synchronous XA transactions across heterogeneous relational databases. A single coordinator pause leaves row locks held indefinitely, causing global connection pool exhaustion.
  * *Antidote*: Asynchronous Saga orchestration with compensating transactions.

### 2.3 Resiliency & Scalability Anti-Patterns
* **Unbounded Retry Storm Amplification (`CS-INT-03`)**: Re-attempting failed HTTP calls immediately without exponential backoff or jitter. Amplifies transient downstream blips by 500% to 1000%, triggering partner IP blacklisting or local collapse.
  * *Antidote*: Exponential backoff with full randomized jitter and Circuit Breakers (Resilience4j / Envoy).
* **Asymmetric Autoscaling Crash (`CS-SCALE-03`)**: Horizontally autoscaling stateless frontend pods while downstream stateful databases remain static. Thousands of new pods exhaust database connection limits.
  * *Antidote*: Connection multiplexing proxies (PgBouncer / AWS RDS Proxy) and hard HPA maximum replica ceilings.
* **Cascading Consumer Group Rebalances (`CS-SCALE-04`)**: Executing long-running blocking I/O inside the Kafka `poll()` loop, exceeding `max.poll.interval.ms` and triggering infinite "stop-the-world" partition rebalance storms.
  * *Antidote*: CooperativeStickyAssignor and dedicated worker thread pools isolated from the poll thread.
* **Connection Pool Starvation (`CS-PERF-02`)**: Configuring oversized connection pools with long acquisition timeouts (30s). When queries slow down, all web worker threads block waiting for connections, killing health probes.
  * *Antidote*: Right-sized connection pools, aggressive fast-fail timeouts (1.5s), and dedicated health check ports.

### 2.4 Boundary & Security Anti-Patterns
* **Broken Object-Level Authorization / BOLA (`CS-SEC-01`)**: Verifying that a caller is logged in (Authentication) while failing to verify whether they own the requested database record (Authorization). Exposing sequential integer IDs allows trivial data scraping.
  * *Antidote*: UUIDv4 cryptographic primary keys and Policy-as-Code (Open Policy Agent) authorization.
* **SSRF Cloud Metadata Exfiltration (`CS-SEC-02`)**: Permitting un-sandboxed backend webhooks to make HTTP calls to link-local cloud hypervisor IPs (`169.254.169.254`), exposing temporary IAM credentials.
  * *Antidote*: Mandatory AWS IMDSv2, Calico pod egress network policies, and pod-scoped IAM identities (IRSA).
* **Missing Multi-Tenant Row Filters (`CS-SEC-06`)**: Relying on developers to remember `WHERE tenant_id = :id` in custom SQL queries. A single omitted clause leaks competing tenant data.
  * *Antidote*: Database engine-level Row-Level Security (PostgreSQL RLS).
* **Global Un-Segmented Blast Radius (`CS-CLOUD-02`)**: Pushing configuration, IAM policies, or routing updates globally without cell-based regional boundaries or progressive canary validation.
  * *Antidote*: Cell-Based Architecture, immutable regional control planes, and automated canary rollback gates.

### 2.5 Strategic & Governance Anti-Patterns
* **Second-System Syndrome (`CS-MOD-03`)**: Halting legacy systems to build a grandiose, over-abstracted "clean slate" rewrite. Results in runaway budget overruns, moving target traps, and eventual multi-million-dollar write-offs.
  * *Antidote*: Incremental Strangler Fig evolutionary modernization with 90-day production delivery milestones.
* **Conway's Law Siloed Conway Collisions (`CS-ENT-02`)**: Structuring software architecture around internal corporate org-chart silos rather than end-to-end customer value streams, leading to fragmented APIs and checkout drop-offs.
  * *Antidote*: Team Topologies inverse Conway maneuver: align cross-functional product squads directly with business capabilities.
* **Architecture Review Board Waterfall Paralysis (`CS-ENT-06`)**: Centralizing all architectural decisions in a slow, monthly governance committee. Forces development teams to bypass governance, creating uncontrolled technical debt.
  * *Antidote*: Automated Architectural Fitness Functions (ArchUnit / Packwerk), RFC async review models, and Federated Architecture Guilds.
