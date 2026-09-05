# Architecture Decision Record (ADR) Ledger Index

This index tracks all Architecture Decision Records across the system lifecycle.

## Status Legend
* **PROPOSED**: Under active review by architects and engineering teams.
* **ACCEPTED**: Formally approved blueprint; authorized for production implementation.
* **REJECTED**: Evaluated and discarded; documented to avoid repeated discussions.
* **SUPERSEDED**: Formerly accepted, now replaced by a newer ADR.
* **DEPRECATED**: Technology marked for phase-out and decommission.

---

| ADR ID | Date | Title | Status | Decision Owner | Supersedes / Superseded By | Tags |
|---|---|---|---|---|---|---|
| [ADR-0001](examples/monolith-vs-microservices.md) | 2026-01-10 | Modular Monolith vs Microservices for Initial MVP | ACCEPTED | Tech Lead | — | `architecture`, `decomposition` |
| [ADR-0002](examples/database-selection.md) | 2026-01-20 | Distributed SQL (CockroachDB) for Multi-Region Ledger | ACCEPTED | Data Architect | — | `database`, `distributed-sql` |
| [ADR-0003](examples/messaging-selection.md) | 2026-02-05 | Kafka for High-Throughput Event Streaming | ACCEPTED | Solution Architect | — | `messaging`, `event-driven` |
| [ADR-0004](examples/synchronous-vs-asynchronous.md) | 2026-02-18 | Asynchronous Event Choreography for Order Lifecycle | ACCEPTED | Principal Architect | — | `integration`, `async` |
| [ADR-0005](examples/sql-vs-nosql.md) | 2026-03-02 | PostgreSQL vs MongoDB for Customer Profile Service | ACCEPTED | Lead Developer | — | `storage`, `nosql` |
| [ADR-0006](examples/cloud-selection.md) | 2026-03-15 | Cloud-Native Managed Services vs Portability | ACCEPTED | Cloud Architect | — | `cloud`, `infrastructure` |
| [ADR-0007](examples/ai-vs-non-ai.md) | 2026-04-01 | Rule Engine vs LLM for Automated Fraud Scoring | ACCEPTED | AI Architect | — | `ai`, `compliance` |
