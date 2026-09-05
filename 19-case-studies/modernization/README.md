# Legacy Modernization Forensic Case Studies

## 1. Domain Overview & Architectural Scope
Legacy modernization is frequently romanticized as an unalloyed good: decomposing monolithic codebases into microservices, replacing mainframes with event streams, or rewriting legacy code from scratch. In enterprise reality, modernization initiatives often make systems significantly worse: replacing an in-memory method call with 45 synchronous network hops, creating distributed deadlocks across shared legacy databases, falling victim to multi-year Second-System Syndrome write-offs, or mismanaging Strangler Fig facade routing.

This category presents rigorous forensic investigations into high-stakes modernization projects, dissecting both catastrophic modernization failures and an exemplary modular monolith refactoring success.

---

## 2. Case Study Portfolio Index

| Case Study ID | Title | Primary Architecture Issue | Systemic Consequence |
| :--- | :--- | :--- | :--- |
| **[`cs-mod-01`](cs-mod-01-distributed-monolith-latency-collapse.md)** | **Distributed Monolith Latency Collapse** | 45 Synchronous microservice network hops | P99 latency degraded from 180ms to 8.5 seconds; 65% customer checkout drop |
| **[`cs-mod-02`](cs-mod-02-shared-database-microservices-deadlock.md)** | **Shared Database Microservices Deadlock** | 22 Independent microservices querying single legacy Oracle DB | Cross-service foreign key table locks paralyzing hospital patient admissions |
| **[`cs-mod-03`](cs-mod-03-second-system-syndrome-rewrite-abandonment.md)** | **Second-System Syndrome Rewrite Write-Off** | 3-Year $60M complete ground-up rewrite attempt | Project cancelled and written off; scope creep and moving business target |
| **[`cs-mod-04`](cs-mod-04-strangler-fig-facade-timeout-cascade.md)** | **Strangler Fig Facade Timeout Cascade** | Monolithic reverse proxy memory leak & unbuffered routing | Retail portal blackout on Cyber Monday; facade single point of failure |
| **[`cs-mod-05`](cs-mod-05-mainframe-ebcdic-copybook-drift-crisis.md)** | **Mainframe Offload EBCDIC Copybook Drift** | CDC offload with undocumented COBOL REDEFINES clauses | $14M ledger reconciliation break; corrupted interest calculations |
| **[`cs-mod-06`](cs-mod-06-successful-modular-monolith-refactoring.md)** | **Modular Monolith Refactoring (Success)** | Refactoring chaotic monolith into compile-time bounded contexts | Engineering deployment velocity surged 400% without distributed overhead |
