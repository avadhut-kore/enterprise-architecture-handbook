# Application Architecture Review Checklist

This checklist provides a structured 25-point evaluation for application software structure, domain boundaries, and code organization.

## 1. Domain Modeling & Encapsulation
- [ ] Are business domain entities decoupled from database schema annotations and external framework classes?
- [ ] Are aggregate roots responsible for enforcing all internal business invariants before saving?
- [ ] Are Value Objects immutable and compared by structural equality rather than identity?
- [ ] Are domain events published only after transactions successfully commit?

## 2. Layering & Dependency Management
- [ ] Does the codebase enforce the Dependency Inversion Principle (dependencies point toward business logic)?
- [ ] Are architectural boundary violations detected and blocked automatically via automated unit tests (ArchUnit)?
- [ ] Are circular dependencies between modules or packages completely eliminated?

## 3. Microservices vs Modular Monolith
- [ ] If using microservices, is decentralized data ownership strictly preserved (no shared databases)?
- [ ] If using a modular monolith, are cross-module calls restricted to public interface contracts?
- [ ] Are inter-service communications authenticated via mTLS and bounded with circuit breakers?

## 4. Concurrency & Data Integrity
- [ ] Are concurrency conflicts handled gracefully using optimistic locking (`@Version`) or distributed locks?
- [ ] Are asynchronous message consumers strictly idempotent?
- [ ] Is transactional outbox implemented to avoid dual-write inconsistencies?
