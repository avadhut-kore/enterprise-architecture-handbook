# Interview Mistakes & Architectural Anti-Patterns

> A catalog of the 20 most frequent fatal errors, red flags, and cognitive traps that derail candidates in senior system design and architecture interviews.

---

## 1. Top 20 Architectural Red Flags

```
 1. Technology-First Thinking (Picking tools before understanding requirements)
 2. Buzzword Architecture (Sprinkling Kafka, K8s, and GraphQL without justification)
 3. Microservices by Default (Premature decomposition on day 1)
 4. Kafka Everywhere (Using a heavy distributed streaming log for simple task queues)
 5. NoSQL by Default (Abandoning ACID transactions without scale justification)
 6. The "Magic Cloud" Trap (Assuming cloud services never experience failure or latency)
 7. Ignoring Non-Functional Requirements (No latency, availability, or consistency targets)
 8. Zero Estimation / False Precision (No capacity numbers or calculating to 6 decimal places)
 9. Designing for Day 1000 on Day 1 (Massive overengineering before reaching PMF)
10. Underengineering (Proposing a single MySQL instance for 500,000 writes/sec)
11. Ignoring Data Models & Schemas (Drawing boxes with zero attention to entity attributes)
12. Forgetting Security & Trust Boundaries (No auth, unencrypted data, no rate limiting)
13. Ignoring Failure Modes & Resiliency (Assuming networks are reliable and databases never crash)
14. Neglecting Observability (No distributed tracing, alerting, or health metrics)
15. Oblivious to Cost & Unit Economics (Deploying hundreds of idle clusters with zero budget awareness)
16. Monologuing & Lack of Collaboration (Talking for 15 minutes straight without checking in)
17. Dogmatic / Defensive Attitude (Refusing to acknowledge trade-offs when challenged)
18. Bluffing / Fabricating Knowledge (Pretending to understand unfamiliar tools or protocols)
19. Neglecting Organizational Impact (Ignoring Conway's Law and team cognitive load)
20. Inability to Evolve (Panicking or erasing the whiteboard when requirements change)
```

---

## 2. Deep Dive Analysis: The Fatal Five

### 1. Technology-First Thinking
* **What candidates do**: The moment the prompt is uttered (*"Design a ridesharing system"*), the candidate says: *"Okay, we will use Go, Kafka, Cassandra, Redis, and deploy on EKS."*
* **Why it hurts**: It reveals that the candidate treats architecture as a shopping list rather than a structured decision process based on constraints.
* **What the interviewer sees**: A junior developer who memorized YouTube architecture videos.
* **The fix**: Always start with business context, core functional scope, and NFR targets before selecting any technology.

### 2. Microservices by Default
* **What candidates do**: Immediately draw 12 microservices (User Service, Auth Service, Notification Service, Search Service, Recommendation Service, Cart Service) for an MVP.
* **Why it hurts**: Distributed systems introduce network latency, partial failures, distributed transactions, eventual consistency challenges, and operational overhead.
* **What the interviewer sees**: An engineer who does not respect the operational and cognitive cost of distributed complexity.
* **The fix**: Start with a clean **Modular Monolith** or a small number of core coarse-grained domain services. Explain: *"To keep operational complexity low for the initial phase, we will start with two core services, maintaining strict bounded context boundaries so we can extract them into independent microservices as team topologies expand."*

### 3. Kafka Everywhere (When a Simple Queue Suffices)
* **What candidates do**: Use Apache Kafka for simple point-to-point worker task execution (e.g., sending an email or generating a PDF).
* **Why it hurts**: Kafka requires cluster management (ZooKeeper/KRaft), partition sizing, consumer group offset tracking, and does not have native individual message ack/nack or dead-letter queue routing without extra machinery.
* **What the interviewer sees**: Lack of depth regarding the difference between a **Distributed Append-Only Log (Kafka)** and a **Message Broker / Task Queue (RabbitMQ / SQS)**.
* **The fix**: Use SQS or RabbitMQ when message processing is independent and workers need simple competing-consumer acknowledgments. Reserve Kafka when you require event replay, strict partitioned ordering, and multiple independent subscriber consumer groups.

### 4. Ignoring Data Models & Keys
* **What candidates do**: Draw an arrow to a box labeled "Database" and never discuss table structures, primary keys, or partition keys.
* **Why it hurts**: In distributed systems, performance is dictated by access patterns and partition key distribution. If you pick the wrong partition key in Cassandra or DynamoDB, you create catastrophic hot partitions.
* **The fix**: Explicitly define the primary entities, their attributes, and their partition/clustering keys:
  ```text
  Table: rides
  Partition Key: driver_id (UUID)
  Clustering Key: timestamp (DESC)
  Attributes: rider_id, pickup_lat, pickup_lng, status, fare
  ```

### 5. Blindness to Total Cost of Ownership (TCO)
* **What candidates do**: Architect a multi-region active-active deployment with replicated distributed caches across three continents for a non-critical internal tool.
* **Why it hurts**: Cloud cross-region network egress, active-active data synchronization, and redundant compute cost tens of thousands of dollars per month.
* **What the interviewer sees**: An engineer who lacks commercial acumen and fiduciary responsibility.
* **The fix**: Calculate rough monthly run rates and explicitly justify cost against business criticality.

---

## 3. Quick Checklist: "Am I Making an Interview Mistake Right Now?"

* [ ] Did I clarify scope before drawing boxes?
* [ ] Did I calculate rough scale numbers?
* [ ] Are my arrows labeled with protocols and data formats?
* [ ] Did I explain **why** I chose this datastore over alternatives?
* [ ] Did I explain what happens when the primary database or downstream API fails?
* [ ] Did I check in with the interviewer in the last 4 minutes?

---

## 4. Cross-References

* **Universal Approach**: [`architect-interview-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architect-interview-framework.md)
* **Whiteboard Execution**: [`system-design-framework.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/system-design-framework.md)
* **Communication Playbook**: [`architecture-communication.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-communication.md)
* **Scoring Rubric**: [`interview-scoring-rubric.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/interview-scoring-rubric.md)
