# Enterprise Architecture Glossary

## Overview

This glossary provides an authoritative, standardized reference of foundational software and enterprise architecture terminology. It establishes a common vocabulary for Solution Architects, Enterprise Architects, Principal Engineers, and engineering leaders across global enterprise environments.

---

## Architectural Terms & Definitions

### A
- **Acid Transactions**: A database transaction model guaranteeing **Atomicity** (all operations succeed or roll back), **Consistency** (database constraints remain valid), **Isolation** (concurrent transactions do not interfere), and **Durability** (committed data survives system crashes).
- **Anti-Corruption Layer (ACL)**: A Domain-Driven Design pattern that translates between two differing domain models or subsystems, shielding a clean domain model from legacy or third-party schema pollution.
- **Application Portfolio Management (APM)**: The enterprise governance practice of cataloging, scoring, and rationalizing an organization's software applications using models like Gartner's TIME (Tolerate, Invest, Migrate, Eliminate).
- **Architecture Decision Record (ADR)**: A structured document capturing an important architectural decision, its context, considered options, trade-offs, and consequences.
- **Architecture Review Board (ARB)**: A cross-functional governance body responsible for reviewing, challenging, and ratifying technical architectures against enterprise standards.
- **Architecturally Significant Requirement (ASR)**: A requirement (functional or non-functional) that exerts profound structural influence on a software system's topology and design.
- **Availability**: The percentage of time a system remains operational and accessible to process requests over a given observation window.

### B
- **Backpressure**: A flow-control mechanism where a downstream consumer signals to an upstream producer to slow down or buffer data generation when overloaded, preventing out-of-memory crashes.
- **BASE Model**: An architectural consistency model used in distributed systems: **Basically Available**, **Soft state**, and **Eventual consistency** (contrasted with ACID).
- **Bounded Context**: A central pattern in Domain-Driven Design defining an explicit linguistic, contextual, and architectural boundary within which a specific domain model applies.
- **Bulkhead Pattern**: A resilience pattern that isolates critical resources (such as thread pools or memory) into separate compartments to prevent a failure in one area from exhausting system-wide resources.

### C
- **C4 Model**: A hierarchical architecture visualization framework created by Simon Brown consisting of four levels of zoom: Context, Containers, Components, and Code.
- **CAP Theorem**: Formulated by Eric Brewer; states that a distributed data store can simultaneously provide at most two out of three guarantees: **Consistency**, **Availability**, and **Partition Tolerance**.
- **Cell-Based Architecture**: An architectural pattern that partitions an entire platform into independent, self-contained units (cells) to isolate failure blast radiuses and enable linear scaling.
- **Circuit Breaker**: A resilience design pattern that detects downstream service failures and temporarily halts outbound network traffic to the failing dependency, failing fast to prevent cascading outages.
- **Command Query Responsibility Segregation (CQRS)**: An architectural pattern that segregates the data models and execution paths used to mutate state (Commands) from those used to read state (Queries).
- **Conway's Law**: The observation by Melvin Conway that organizations design systems that mirror the communication structures of the organization itself.

### D
- **Database-per-Service**: A core microservices pattern where each microservice owns and encapsulates its private data store, forbidding direct external database access.
- **Dead Letter Queue (DLQ)**: A specialized message queue that captures and isolates unprocessable or malformed messages (poison pills) after maximum retry attempts have been exhausted.
- **Domain-Driven Design (DDD)**: An architectural approach pioneered by Eric Evans that centers software design on a rich domain model developed via a Ubiquitous Language shared with business experts.

### E
- **Event-Driven Architecture (EDA)**: A distributed architecture paradigm where components communicate primarily by producing, detecting, and reacting to asynchronous state change events.
- **Event Sourcing**: An architectural pattern where state is not persisted as a mutable record, but as an append-only, immutable sequence of business domain events.
- **Eventual Consistency**: A consistency model where, in the absence of new mutations, all replicas in a distributed system will eventually converge to identical values.

### H
- **Hexagonal Architecture (Ports and Adapters)**: An architectural style formulated by Alistair Cockburn that decouples core business logic from external frameworks, user interfaces, and databases via abstract ports and interchangeable adapters.

### I
- **Idempotency**: The property of an operation wherein executing it multiple times with the exact same inputs produces the identical state outcome as executing it once.

### L
- **Little's Law**: A fundamental queuing theory principle: $L = \lambda W$, stating that the average number of items in a stationary queue ($L$) equals the arrival rate ($\lambda$) multiplied by the average waiting time ($W$).
- **Load Shedding**: An architectural resilience technique where a server under severe CPU or memory saturation intentionally rejects low-priority incoming requests to preserve core functionality.

### M
- **Microservices**: An architectural style that structures an application as a collection of small, autonomous, loosely coupled services organized around business capabilities.
- **Modular Monolith**: An architectural style where a system is deployed as a single runtime artifact, but internally structured into strictly isolated, loosely coupled modules with schema-isolated data.

### O
- **OpenTelemetry (OTel)**: A vendor-neutral, CNCF-standardized observability framework providing APIs, SDKs, and tooling to generate, collect, and export traces, metrics, and logs.

### P
- **PACELC Theorem**: An extension of the CAP theorem stating that if there is a **Partition (P)**, trade off **Availability (A)** or **Consistency (C)**; **Else (E)** under normal health, trade off **Latency (L)** or **Consistency (C)**.
- **Paved Road (Golden Path)**: A curated, pre-approved, and fully supported set of standardized technologies, deployment pipelines, and templates provided by enterprise platform teams.

### S
- **Saga Pattern**: A design pattern for coordinating distributed transactions across multiple microservices via a sequence of local transactions and compensating actions.
- **Strangler Fig Pattern**: An incremental legacy modernization pattern where new features and refactored domains are built alongside a legacy monolith behind an intercepting facade until the legacy system can be retired.

### T
- **TIME Framework**: Gartner's application portfolio rationalization model: **Tolerate** (high value, low tech quality), **Invest** (high value, high tech quality), **Migrate** (low value, high tech quality), **Eliminate** (low value, low tech quality).
- **Transactional Outbox Pattern**: A pattern that guarantees atomic database updates and message broker publication by writing domain events to an outbox table within the same local database transaction.

### Z
- **Zero Trust Architecture**: A security paradigm based on the principle of "never trust, always verify," requiring strict identity verification and cryptographic authorization for every request regardless of network location.
