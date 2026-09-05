# Scalability & Elasticity Forensic Case Studies

## 1. Domain Overview & Architectural Scope
Scalability is the property of an architecture to handle increased workload gracefully by adding physical or virtual resources. When scalability breaks down at enterprise scale, it rarely fails uniformly. Instead, failures emerge from non-linear boundary constraints: single partition keys absorbing 99% of traffic in distributed NoSQL tables, noisy neighbors consuming shared IOPS in multi-tenant clusters, asymmetric autoscaling where stateless frontend pods crush unscaled relational databases, cascading Kafka consumer group rebalances that halt real-time event pipelines, and cross-continent active-active split-brain write divergences.

This category presents deep forensic analyses of scalability breakdowns, evaluating why scaling one layer often exacerbates systemic collapse elsewhere.

---

## 2. Case Study Portfolio Index

| Case Study ID | Title | Primary Scalability Issue | Systemic Consequence |
| :--- | :--- | :--- | :--- |
| **[`cs-scale-01`](cs-scale-01-flash-sale-hot-partition-lockup.md)** | **DynamoDB Hot-Partition Throttling in Sneaker Drop** | Single SKU partition key absorbing 50,000 writes/sec | 85% of checkout requests throttled (`ProvisionedThroughputExceededException`) |
| **[`cs-scale-02`](cs-scale-02-multi-tenant-noisy-neighbor-starvation.md)** | **B2B SaaS Multi-Tenant Noisy Neighbor Collapse** | Large enterprise tenant running unindexed batch query | Shared PostgreSQL IOPS exhausted; 4,200 small tenants locked out of CRM |
| **[`cs-scale-03`](cs-scale-03-asymmetric-kubernetes-autoscaling-crash.md)** | **Asymmetric Kubernetes Frontend Autoscaling Crash** | Frontend pods scaled 10x while backend DB remained static | 1,200 Pods overwhelmed database connection limits, knocking entire site offline |
| **[`cs-scale-04`](cs-scale-04-kafka-rebalance-storm-consumer-halt.md)** | **500-Partition Kafka Consumer Rebalance Storm** | Long message processing times exceeding `max.poll.interval.ms` | Cascading rebalance loops completely halting ad impression pipeline for 7 hours |
| **[`cs-scale-05`](cs-scale-05-websocket-epoll-fd-exhaustion.md)** | **1M WebSocket Epoll File Descriptor Exhaustion** | Linux OS file descriptor limits and TCP buffer allocations | Real-time collaborative whiteboard server OOM and connection dropping |
| **[`cs-scale-06`](cs-scale-06-global-active-active-split-brain.md)** | **Global Multi-Region Active-Active Split-Brain** | Concurrent writes to same entity across US and EU regions | Irreconcilable ride-sharing driver state; $3.4M in double-booked rides |
