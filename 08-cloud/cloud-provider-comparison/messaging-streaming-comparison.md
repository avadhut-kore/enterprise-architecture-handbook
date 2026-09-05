# Messaging & Event Streaming Comparison: AWS vs Azure vs GCP

## Executive Summary

Decoupled event architectures rely on message queues for point-to-point asynchronous buffering and event streaming backbones for high-throughput event sourcing.

---

## 1. Enterprise Messaging Services

| Feature | AWS (SQS + SNS) | Azure (Service Bus) | GCP (Cloud Pub/Sub) |
| :--- | :--- | :--- | :--- |
| **Primary Architecture** | SQS (Pull Queue) + SNS (Push Topic Fanout) | Service Bus (Queues & Topics Unified) | Pub/Sub (Global Anycast Topics & Subscriptions) |
| **FIFO Ordering** | Strict FIFO options on SQS & SNS | Strict FIFO via **Message Sessions** | Strict FIFO via **Ordering Keys** |
| **Message Deduplication** | 5-minute sliding window via hash | Native duplicate detection window (up to 7 days) | At-least-once delivery; deduplication in app |
| **Max Message Size** | 256 KB (Up to 2 GB via S3 Extended Client) | Up to 100 MB (Large Message Support) | 10 MB |

---

## 2. High-Throughput Event Streaming

| Architectural Dimension | Amazon MSK (Kafka) | Azure Event Hubs | Google Cloud Pub/Sub |
| :--- | :--- | :--- | :--- |
| **Native Protocol** | Standard Apache Kafka Wire Protocol | AMQP 1.0 + Apache Kafka Wire Protocol | gRPC / REST |
| **Partition Management** | Manual partition sizing per Kafka topic | Fixed partition count set at creation | **Fully automated; zero partition management** |
| **Serverless Ingestion** | Available (MSK Serverless) | Native serverless ingestion model | **100% Serverless global streaming** |
| **Long-Term Offloading** | Requires custom S3 Sink Connectors | **Event Hubs Capture** (Automated Blob/ADLS dump)| **Direct BigQuery / GCS Subscriptions** |
