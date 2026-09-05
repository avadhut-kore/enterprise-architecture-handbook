# Delivery Semantics: At-Least-Once, At-Most-Once, Exactly-Once

## 1. Comparative Analysis

| Semantic | Mechanical Definition | Protocol Mechanics | Enterprise Trade-off |
| :--- | :--- | :--- | :--- |
| **At-Most-Once** | Message delivered 0 or 1 time; loss acceptable | Acknowledge *before* processing | High performance; unacceptable for financial or transactional data |
| **At-Least-Once** | Message delivered 1 or more times; duplicates possible | Acknowledge *after* durable commit | Standard enterprise pattern; mandates downstream idempotency |
| **Exactly-Once** | Message processed effectively 1 time end-to-end | Distributed 2PC / Kafka Transactions | High latency and operational overhead; limited to single broker cluster |

## 2. Why "End-to-End Exactly Once" Across Heterogeneous Systems is Impossible
While Kafka supports transactional producing and consuming *within Kafka itself* (`processing.guarantee=exactly_once_v2`), the moment an event triggers a write to an external database (Oracle, SAP, REST API), dual-write divergence is possible. The only robust solution across disparate enterprise systems is **At-Least-Once delivery coupled with Idempotent Consumer processing**.
