# ADR-0051: Standardization on Amazon MSK for Enterprise Event Streaming

## Metadata
```yaml
id: ADR-0051
title: Standardization on Amazon MSK for Enterprise Event Streaming
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Point-to-point synchronous REST calls between microservices caused tight runtime coupling and cascading failure during service degradations.

---

## 2. Decision
We standardize on Amazon Managed Streaming for Apache Kafka (Amazon MSK) as the enterprise asynchronous event backbone, paired with Confluent Schema Registry.

---

## 3. Positive Consequences
- Complete temporal decoupling of producers and consumers.
- High-throughput message persistence and replayability.
- Open-source Kafka API avoids proprietary cloud messaging lock-in.

---

## 4. Negative Consequences & Trade-offs
- Requires event schema governance and complex consumer group lag monitoring.
- Higher baseline infrastructure cost compared to SQS.

---

## 5. Alternatives Considered & Rejected
- **Self-Hosted Kafka on EC2/Kubernetes**: Rejected due to ZooKeeper/KRaft maintenance toil.
- **AWS SQS/SNS Exclusively**: Rejected due to lack of message replayability and partition ordering at hyper-scale.
