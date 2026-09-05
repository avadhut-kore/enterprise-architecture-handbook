# ADR-0003: Selection of Apache Kafka for Event Streaming

---
**Metadata**:
* **ADR ID**: ADR-0003
* **Title**: Event Broker Selection — Apache Kafka vs RabbitMQ
* **Status**: Accepted
* **Date**: 2026-02-05
* **Decision Owners**: Principal Solution Architect, Lead Data Engineer
---

## 1. Context & Problem Statement
Order lifecycle, inventory updates, and fraud evaluation events must be distributed to over 15 internal downstream services. Projected peak throughput is 35,000 events/second with mandatory historical replayability for audit and training downstream machine learning models.

## 2. Options Considered
* **Option 1: Apache Kafka**: Distributed append-only log with partitioned consumers and persistent retention.
* **Option 2: RabbitMQ**: Traditional AMQP message broker with exchange routing and queue acknowledgment.
* **Option 3: AWS SQS/SNS**: Managed pub/sub with high durability.

## 3. Decision & Rationale
**Chosen Option**: Apache Kafka.
Kafka's persistent log architecture allows multiple independent consumer groups to read at their own pace and replay messages up to 30 days historically. RabbitMQ message deletion upon acknowledgment prohibits retroactive analytics and ML backfilling.

## 4. Consequences
* Producers must implement partitioning keys to preserve per-order causality.
* Consumers must be strictly idempotent to safely absorb at-least-once delivery duplicates.
