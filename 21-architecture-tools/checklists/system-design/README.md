# System Design Engineering Checklists

Production systems fail not because engineers lack knowledge, but because complex edge cases, failure domains, security controls, and operational guardrails are overlooked during design reviews.

These comprehensive, production-grade checklists ensure architectural rigor at every stage of the system design lifecycle—from requirements gathering to production launch.

---

## Catalog of System Design Checklists

| Checklist | Lifecycle Stage | Core Objective |
| :--- | :--- | :--- |
| [Requirements Checklist](requirements-checklist.md) | Inception | Functional scope, NFR quantification & boundaries |
| [Scale Estimation Checklist](scale-estimation-checklist.md) | Sizing | QPS, storage, bandwidth & working set math |
| [API Design Checklist](api-design-checklist.md) | Interface Definition | Contracts, idempotency, versioning & pagination |
| [Data Model Checklist](data-model-checklist.md) | Persistence Design | Schemas, indexing, sharding keys & consistency |
| [High-Level Design Checklist](high-level-design-checklist.md) | Topology & Blueprint | C4 containers, data flow & separation of concerns |
| [Detailed Design Checklist](detailed-design-checklist.md) | Component Internals | Concurrency, caching, state machines & algorithms |
| [Scalability Checklist](scalability-checklist.md) | Growth Planning | Stateless elasticity, DB read/write scaling & limits |
| [Reliability Checklist](reliability-checklist.md) | Fault Tolerance | Single points of failure, redundancy & replication |
| [Performance Checklist](performance-checklist.md) | Latency & Throughput | P99 budgets, connection pools & thread models |
| [Security Checklist](security-checklist.md) | Threat Modeling | Zero Trust, mTLS, encryption & least privilege |
| [Observability Checklist](observability-checklist.md) | Telemetry | Traces, metrics, structured logs & alerting rules |
| [Resilience Checklist](resilience-checklist.md) | Failure Engineering | Circuit breakers, timeouts, retries & bulkheads |
| [Production Readiness Checklist](production-readiness-checklist.md) | Launch Gate | Runbooks, disaster recovery, load tests & rollback |
