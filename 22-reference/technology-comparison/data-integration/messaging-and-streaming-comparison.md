# Technology Comparison: Messaging & Streaming Brokers Comparison

## 1. Architectural Evaluation Context
Apache Kafka vs RabbitMQ vs Apache Pulsar vs AWS SQS/SNS: delivery guarantees, routing flexibility, ordered replay, and operational overhead.

---

## 2. Enterprise Decision Matrix

| Evaluation Dimension | Option A | Option B | Option C | Option D |
|---|---|---|---|---|
| **Primary Architectural Fit** | Core Transactional OLTP | High-Scale Distributed | Analytical Aggregation | Real-Time Reactive |
| **Consistency Model** | Strict ACID (Immediate) | Tunable / Eventual (BASE) | Snapshot Isolation | Eventual Consistency |
| **Throughput Ceiling** | Moderate - High | Very High (Linear Scale) | High Batch Throughput | High Stream Throughput |
| **Operational Complexity** | Low - Moderate | Moderate - High | Moderate | High |
| **Total Cost of Ownership** | Predictable / Low | Moderate | Variable Cloud Compute | Moderate - High |

---

## 3. Architecture Selection Guidelines
- Select based on workload characteristics (read/write ratio, latency SLAs, consistency needs).
- Avoid adopting complex distributed architectures when simpler proven solutions satisfy the requirements.
