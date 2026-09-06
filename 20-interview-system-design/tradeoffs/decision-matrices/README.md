# Architecture Decision Matrices: Consolidated Whiteboard Defense Sheets

> Ultra-dense, quick-reference comparison tables designed for rapid recall and instant whiteboard defense in high-stakes architecture interviews.

---

## 1. Storage Paradigm Quick-Matrix

| Store Type | Primary Candidate | Query Latency | Write Scale | Consistency | When NOT to Use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Relational (RDBMS)** | PostgreSQL | Low ($2–10\text{ms}$) | Medium (~10k RPS) | Strong ACID | Unstructured schemas; massive write throughput ($> 50\text{k RPS}$) |
| **Distributed NewSQL** | Google Spanner / Cockroach | Med ($15–50\text{ms}$) | High (linear) | Strong Distributed | Budget-constrained projects; single-region simple apps |
| **Key-Value** | Redis / DynamoDB | Ultra-Low ($< 1–3\text{ms}$) | Highest | Configurable | Complex multi-table JOINs; ad-hoc reporting |
| **Document** | MongoDB / DocumentDB | Low ($3–10\text{ms}$) | High | Scoped to doc | Strict cross-entity relational constraints |
| **Wide-Column** | Cassandra / ScyllaDB | Lowest Write ($< 2\text{ms}$) | Ultra-High | Eventual | Systems requiring frequent ad-hoc secondary queries |
| **Search Index** | OpenSearch / Elasticsearch | Low ($10–50\text{ms}$) | Medium | Near Real-Time | Primary source of truth for transactional state |
| **Vector DB** | Qdrant / Pinecone / Milvus | Med ($15–75\text{ms}$) | Medium | Eventual | Traditional scalar relational queries |

---

## 2. Communication & Integration Quick-Matrix

| Protocol / Pattern | Transport | Payload | Coupling | Delivery Guarantee | Best Suited For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REST (HTTP/1.1 or 2)** | TCP / TLS | JSON / Text | Synchronous | At-least-once (client retries) | Public APIs, partner integrations |
| **gRPC** | HTTP/2 | Protobuf (Binary) | Synchronous | At-least-once | High-throughput internal microservice RPCs |
| **GraphQL** | HTTP/POST | JSON | Synchronous | At-least-once | Frontends with heterogeneous data needs (BFF) |
| **Task Queue (SQS/RabbitMQ)**| TCP / AMQP | Any / JSON | Asynchronous | At-least-once / Competing | Discrete worker task execution (emails, PDF rendering) |
| **Event Stream (Kafka)** | TCP | Avro / Protobuf | Asynchronous | At-least-once / Partition Ordered| Event sourcing, streaming analytics, CDC pipelines |
| **WebSockets** | TCP Persistent | Text / Binary | Bidirectional | Connection-bound | Real-time chat, live location streaming, gaming |

---

## 3. Compute & Hosting Quick-Matrix

| Runtime | Cold Start | Operational Burden | Statefulness | Cost Efficiency at Scale |
| :--- | :--- | :--- | :--- | :--- |
| **Bare Metal / VMs (EC2)** | Minutes | Medium to High | Stateful | High (if fully utilized via reserved instances) |
| **Containers (ECS / Fargate)**| Seconds ($15–30\text{s}$) | Low | Stateless | Balanced |
| **Kubernetes (EKS / GKE)** | Seconds ($5–15\text{s}$) | **Very High** | Polyglot (Stateful + Stateless) | **Highest** (bin-packing across massive fleets) |
| **Serverless (AWS Lambda)** | Milliseconds ($50–500\text{ms}$) | **Lowest** | Stateless Ephemeral | Expensive for continuous high sustained throughput |

---

## 4. Multi-Region Disaster Recovery Quick-Matrix

| Architecture Strategy | RTO (Recovery Time) | RPO (Data Loss) | Cost Multiplier | Operational Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Multi-AZ Single Region** | $< 1\text{ minute}$ | **0 (Zero)** | $1.5\times$ | Low |
| **Pilot Light (Warm Standby)** | $10\text{ to }30\text{ minutes}$ | Minutes ($< 5\text{ min}$) | $1.8\times$ | Medium |
| **Active-Passive (Hot Standby)**| $1\text{ to }5\text{ minutes}$ | Seconds ($< 15\text{ sec}$) | $2.2\times$ | High |
| **Active-Active (Global Mesh)** | **$\approx 0\text{ seconds}$** | Zero / Conflict dependent | **$3.5\times$ to $5\times$** | **Very High** |

---

## 5. Cross-References

* **Detailed Architectural Trade-Offs**: [`architecture.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/architecture.md)
* **Data Storage Trade-Offs**: [`data.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/data.md)
* **Reliability & Circuit Breakers**: [`reliability.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/reliability.md)
