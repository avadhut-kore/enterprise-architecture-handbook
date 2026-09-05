# ADR-0001: Modular Monolith vs Microservices for Core Platform

---
**Metadata**:
* **ADR ID**: ADR-0001
* **Title**: Architectural Decomposition — Modular Monolith for Core Platform MVP
* **Status**: Accepted
* **Date**: 2026-01-10
* **Decision Owners**: Chief Architect, VP of Engineering
* **Decision Reviewers**: Domain Tech Leads, Platform Team
* **Related Requirements**: REQ-CORE-001, NFR-TIME-001
---

## 1. Context & Problem Statement
The company is developing a new enterprise SaaS platform. The engineering organization currently consists of 14 developers across 2 feature teams. We must decide between launching as a distributed microservices architecture or as a well-bounded modular monolith.

## 2. Options Considered

### Option 1: Distributed Microservices Architecture
* Separate services for Auth, Catalog, Billing, Notifications, and Accounts.
* **Pros**: Independent team deployment cadences, polyglot runtime options.
* **Cons**: Massive operational tax (distributed tracing, eventual consistency, network latency, Kubernetes management) on a small 14-person team. High risk of premature domain boundary errors.

### Option 2: Enforced Modular Monolith
* Single deployable artifact structured into strictly isolated internal modules (Hexagonal / Clean Architecture) with strict compiler-enforced boundary rules (ArchUnit / Go packages).
* **Pros**: Zero network hop latency for intra-system calls, atomic database transactions across aggregates during rapid discovery, unified CI/CD pipeline, minimal infrastructure overhead.
* **Cons**: Single deployment artifact; risk of teams leaking internal abstractions if boundaries are not strictly policed.

## 3. Decision & Rationale
**Chosen Option**: Option 2 (Enforced Modular Monolith).

At the current organizational scale (14 engineers), the operational tax of microservices will severely degrade velocity. We will build an enforced Modular Monolith with zero cross-module database foreign keys and strict asynchronous domain event boundaries. This guarantees that individual modules can be extracted into standalone microservices in the future with minimal refactoring.

## 4. Consequences & Trade-offs
* **Accepted Trade-off**: All teams deploy through a single coordinated CI/CD pipeline.
* **Guardrail**: ArchUnit automated architectural unit tests will fail the build if Module A directly imports internal classes of Module B instead of its public API interface.
