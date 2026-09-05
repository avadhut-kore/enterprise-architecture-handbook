# Component Overview Specification

This template defines the internal component structure and interaction matrix for a single microservice or subsystem.

## 1. Component Responsibilities & Boundaries

```text
+-------------------------------------------------------------+
|                     Public API Layer                        |
|   - Request Validation     - Auth & Scope Extraction         |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                    Domain / Business Layer                  |
|   - Aggregate Roots         - Business Rules Engine         |
|   - Domain Events           - State Machine Transitions     |
+-------------------------------------------------------------+
               |                               |
               v                               v
+-----------------------------+ +-----------------------------+
|     Persistence Adapter     | |    Integration Adapter      |
|   - SQL Repositories        | |   - Kafka Outbox Producer   |
|   - Redis Cache Adapter     | |   - gRPC Downstream Client  |
+-----------------------------+ +-----------------------------+
```

## 2. Component Interaction Matrix
| Initiating Component | Target Component | Protocol | Failure Behavior |
|---|---|---|---|
| API Controller | Domain Orchestrator | In-Process Direct Call | Return 400 Bad Request if domain validation fails |
| Domain Orchestrator | Persistence Adapter | SQL / JDBC | Roll back local database transaction |
| Domain Orchestrator | Kafka Outbox | Transactional Outbox Table | Atomic commit with business data; zero dual-write risk |
| Integration Adapter | Payment Gateway | HTTPS REST | 1.5s Timeout; Circuit breaker opens after 5 failures |
