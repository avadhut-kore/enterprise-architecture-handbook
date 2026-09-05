# Modular Monolith Architecture

A **Modular Monolith** is an architectural pattern where a single physical deployable unit (one container, one process) is engineered with strictly bounded, loosely coupled, and encapsulated logical domain modules.

> [!TIP]
> **Why Modular Monolith is Often a Better Starting Point than Microservices**:
> Microservices introduce massive distributed systems overhead on Day 1: network latency, partial failures, distributed transactions (Sagas), complex CI/CD pipelines, container orchestration (Kubernetes), distributed tracing, and high cloud hosting costs.
> A Modular Monolith provides **the same clean domain boundaries, independent module testability, and team autonomy**, but executes inside a single memory space with zero network latency and local ACID transactions.

---

## Modular Monolith Curriculum

| Document | Focus | Key Concept |
| :--- | :--- | :--- |
| [Modular Monolith Overview](modular-monolith-overview.md) | Architectural Blueprint | Why modular monolith beats premature microservices |
| [Module Boundaries](module-boundaries.md) | Encapsulation Rules | Public contract assemblies vs internal private packages |
| [Module Communication](module-communication.md) | Synchronous & Async Calls | In-process facades vs in-memory mediator events |
| [Module Dependencies](module-dependencies.md) | Directed Dependency Graph | Preventing cyclic references across domain modules |
| [Internal Events](internal-events.md) | Decoupled Choreography | In-memory pub/sub using MediatR / Spring ApplicationEvent |
| [Shared Kernel](shared-kernel.md) | Controlled Sharing | Guidelines for shared primitives without coupling |
| [Database Boundaries](database-boundaries.md) | Schema Isolation | Separate schemas or table prefixes per module |
| [Transaction Boundaries](transaction-boundaries.md) | ACID vs Sagas | Single DB transaction vs outbox events across modules |
| [Testing Modules](testing-modules.md) | Isolated Module Tests | Fast in-memory integration testing without mocks |
| [Deployment Model](deployment-model.md) | Operational Simplicity | Single Docker container / unified release pipeline |
| [Scaling Model](scaling-model.md) | Horizontal Scaling | Replicating the entire modular container behind an L7 LB |
| [Migration to Microservices](migration-to-microservices.md) | Extraction Blueprint | Carving a module out into an independent microservice |
| [Modular Monolith Governance](modular-monolith-governance.md) | Automated Enforcement | Enforcing module boundaries via NetArchTest and ArchUnit |
