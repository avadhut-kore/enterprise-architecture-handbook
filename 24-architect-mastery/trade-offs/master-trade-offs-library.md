# Master Trade-Offs Library: 20 Architectural Decisions Analyzed

This reference documents the 20 fundamental trade-offs encountered by enterprise and solution architects, providing analysis, failure modes, and concrete decision heuristics.

---

### 1. Consistency vs Availability (CAP / PACELC)
- **Trade-off**: Strong linearizable consistency ensures all reads receive the latest write, but partitions cause system failure. High availability ensures writes/reads always succeed, at the cost of stale reads and conflict resolution.
- **When to choose Consistency**: Financial ledger entries, inventory reservations, authorization permissions.
- **When to choose Availability**: Social feeds, analytics ingestion, product reviews, catalog browsing.
- **Key Failure Mode**: Attempting distributed 2PC across WAN links, resulting in cascading lock contention and total downtime.

---

### 2. Latency vs Durability
- **Trade-off**: Synchronous disk fsync and quorum writes ensure data survive crash loops, but dramatically increase request latency. Asynchronous write-behind caching achieves sub-millisecond latency with small data-loss windows.
- **When to choose Durability**: High-value transactions, audit logs, ledger events.
- **When to choose Latency**: High-frequency telemetry, gaming state, UI session caching.
- **Key Failure Mode**: Assuming Redis async persistence (`bgsave`) guarantees zero data loss during power failure.

---

### 3. Throughput vs Cost
- **Trade-off**: Over-provisioning compute, memory, and database IOPS achieves massive throughput at immense capital cost. Batching and queue buffering maximize resource utilization at the cost of processing delays.
- **Heuristic**: Size for peak + 30% headroom only when backed by auto-scaling and spot/preemptible instances.

---

### 4. Simplicity vs Flexibility
- **Trade-off**: Simple, bespoke code is easy to read, debug, and ship. Highly configurable, plugin-driven, abstraction-heavy systems support unpredictable future requirements at the expense of cognitive overload.
- **Golden Rule**: "Rule of Three" — Never abstract until you have three distinct, working implementations.

---

### 5. Build vs Buy vs Partner
- **Trade-off**: Building grants complete IP control and custom fit, but burdens the enterprise with lifetime maintenance. Buying provides instant time-to-market and vendor innovation, but risks vendor lock-in and high licensing costs.
- **Heuristic**: Build core differentiators that generate competitive advantage; buy commodity capabilities (CRM, Auth, Payment Gateways, ERP).

---

### 6. Centralized vs Decentralized
- **Trade-off**: Centralization (enterprise data lake, centralized API gateway) provides strict governance and unified compliance, but becomes an organizational bottleneck. Decentralization (Data Mesh, federated gateways) fosters team velocity at the risk of fragmentation.

---

### 7. Synchronous vs Asynchronous
- **Trade-off**: Synchronous REST/gRPC offers simple mental models and immediate feedback, but introduces temporal coupling and cascading failures. Asynchronous messaging decouples systems in time and space, but requires complex out-of-order handling, saga orchestrations, and eventual consistency.

---

### 8. Schema-on-Read vs Schema-on-Write
- **Trade-off**: Schema-on-Write (RDBMS, Protobuf) validates contracts upfront, preventing dirty data from entering storage. Schema-on-Read (JSON document stores, data lakes) allows instant schema evolution, but transfers validation burden to every reader.

---

### 9. Real-Time vs Batch
- **Trade-off**: Real-time streaming (Kafka, Flink) enables sub-second reaction to business events, with high infrastructure complexity and cost. Batch processing (Spark, SQL ELT) maximizes compute efficiency and cost, but incurs business data latency.

---

### 10. Monolith vs Microservices
- **Trade-off**: A modular monolith offers zero network latency between components, single transactional boundaries, and simple deployment. Microservices allow independent scaling, decoupled deployment cycles, and autonomous team ownership at the cost of distributed systems operational overhead.

---

### 11. General-Purpose vs Purpose-Built
- **Trade-off**: Postgres handles relational, JSON, vectors, and full-text search reasonably well. Purpose-built engines (Elasticsearch, Pinecone, Neo4j) provide 10x performance for specialized access patterns, but multiply operational burden.

---

### 12. State In-Memory vs State Externalized
- **Trade-off**: In-memory state delivers microsecond response times, but complicates failover and horizontal autoscaling. Externalizing state to Redis/DB enables stateless, cattle-like compute instances, but incurs network round-trip overhead.

---

### 13. Tight Coupling vs Loose Coupling
- **Trade-off**: Tight coupling allows maximum compile-time type safety, shared memory efficiency, and rapid unified changes across a single codebase. Loose coupling isolates failures and teams, but introduces API contract management and distributed debugging complexity.

---

### 14. Normalization vs Denormalization
- **Trade-off**: Normalization guarantees write integrity and eliminates data redundancy. Denormalization optimizes read throughput by eliminating expensive joins, at the expense of complex write synchronization and data duplication.

---

### 15. Push vs Pull
- **Trade-off**: Push (WebSockets, SSE, Webhooks) delivers instant event delivery, but risks overwhelming downstream receivers. Pull (polling, consumer-driven queue consumption) enables receivers to control backpressure, at the cost of polling latency and unnecessary load.

---

### 16. Single Region vs Multi-Region
- **Trade-off**: Single region with multi-AZ gives low latency, zero cross-region data replication cost, and simple transactional semantics. Multi-region delivers disaster survival and global low latency, with exponential cost and split-brain risk.

---

### 17. Best-of-Breed vs Single-Vendor
- **Trade-off**: Best-of-breed selects the absolute best tool for each domain (Datadog, Snowflake, Auth0, AWS), resulting in high integration friction. Single-vendor (all-AWS or all-Azure) simplifies contracting, IAM, and networking, but compromises on individual component quality.

---

### 18. Fast Delivery vs High Reliability
- **Trade-off**: Fast delivery ships code directly with minimal verification stages, maximizing market agility. High reliability imposes rigorous staging, canary verification, chaos testing, and architectural gating, slowing velocity.

---

### 19. Deep Security vs Developer Velocity
- **Trade-off**: Strict zero-trust, ephemeral secrets, air-gapped networks, and rigorous code reviews protect enterprise assets, but can slow developer onboarding and feedback loops.

---

### 20. Standardization vs Innovation
- **Trade-off**: Rigid technology standard catalogs ensure organizational mobility, predictable hiring, and volume discount licensing. Unconstrained technical freedom allows teams to leverage cutting-edge tooling, but risks an unmaintainable zoo of orphaned tech stacks.

## Related Resources
- [Trade-Off Analysis Template](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/trade-offs/trade-off-analysis-template.md)
- [Architecture Judgment](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/architecture-judgment/README.md)
