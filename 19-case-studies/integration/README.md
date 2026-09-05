# Enterprise Integration Forensic Case Studies

## 1. Domain Overview & Architectural Scope
Enterprise Integration spans the critical connective tissue between distributed systems: API gateways, message queues, event streaming meshes, ESBs, and multi-system transaction protocols. When integration architectures fail, they exhibit catastrophic non-linear failure modes: dual-write state divergences, unhandled poison-pill consumer deadlocks, self-inflicted retry storms, distributed two-phase commit (2PC) lockouts, and webhook feedback amplification loops.

This category presents rigorous forensic investigations into high-impact integration failures, diagnosing the precise mechanisms of distributed failure and establishing proven patterns for resilient boundary engineering.

---

## 2. Case Study Portfolio Index

| Case Study ID | Title | Primary Architecture Issue | Systemic Consequence |
| :--- | :--- | :--- | :--- |
| **[`cs-int-01`](cs-int-01-dual-write-ghost-payments.md)** | **Dual-Write Ghost Payments** | Non-atomic database write + Kafka publish | $4.2M in duplicate merchant settlements & phantom account debits |
| **[`cs-int-02`](cs-int-02-kafka-poison-pill-consumer-freeze.md)** | **Kafka Poison Pill Consumer Freeze** | Unchecked schema drift in event payload | Total halt of nationwide package tracking for 9 hours |
| **[`cs-int-03`](cs-int-03-unbounded-retry-storm-third-party-api.md)** | **Unbounded Partner API Retry Storm** | Aggressive client retries without jitter or backoff | Complete collapse of global flight booking engine (32,000 QPS storm) |
| **[`cs-int-04`](cs-int-04-distributed-two-phase-commit-deadlock.md)** | **Distributed 2PC Transaction Deadlock** | Synchronous XA transactions across 4 banking databases | Connection pool exhaustion & global payments freeze under load |
| **[`cs-int-05`](cs-int-05-esb-centralized-monolith-chokepoint.md)** | **Centralized ESB Monolith Chokepoint** | All corporate XML transformations funnelled through single ESB | Claims processing backlog exceeding 140,000 requests; CPU starvation |
| **[`cs-int-06`](cs-int-06-webhook-amplification-ddos-loop.md)** | **Webhook Ping-Pong DDoS Feedback Loop** | Mutually subscribing SaaS webhook endpoints | 45 Million synthetic webhook requests crashing customer billing servers |
