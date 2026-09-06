# Competency Deep Dive: Software Architecture & Modularity

> **"Software architecture is about the boundaries you draw and the dependencies you restrict. Good boundaries allow systems to evolve gracefully; bad boundaries turn systems into unmaintainable distributed balls of mud."**

---

## 1. Definition & Core Essence

**Software Architecture** is the structural organization of software components, their interfaces, and the fundamental constraints governing their relationships. It encompasses:
* Domain-Driven Design (DDD): Strategic modeling (Bounded Contexts, Ubiquitous Language, Context Maps) and tactical modeling (Entities, Value Objects, Aggregates, Domain Events).
* Decoupling paradigms: Clean Architecture, Hexagonal Architecture (Ports & Adapters), and Onion Architecture.
* Modularization strategies: Monolith vs Modular Monolith vs Microservices vs Micro-Frontends.
* Dependency management: Inversion of Control (IoC), stable abstractions principle, and preventing cyclic dependencies.

---

## 2. Why It Matters for Modern Architects

* **Solution Architects**: Ensures business logic remains independent of transient UI frameworks, database drivers, and cloud vendor SDKs.
* **Technical Architects**: Prevents organizational friction; aligns service boundaries with team boundaries according to Conway's Law and Team Topologies.
* **Enterprise Architects**: Establishes reusable domain capability boundaries across multiple business divisions, preventing duplicate application development.

---

## 3. 5-Tier Behavioral Capability Progression

| Level | Behavioral Capability Anchor |
| :--- | :--- |
| **L1 (Practitioner)** | Applies basic design patterns (Factory, Strategy, Repository) within a single codebase. |
| **L2 (Independent)** | Applies SOLID principles and Ports & Adapters to isolate core domain logic from infrastructure frameworks. |
| **L3 (Advanced)** | Conducts Event Storming workshops; identifies DDD Bounded Contexts and defines Context Maps (Shared Kernel, Customer/Supplier, Anti-Corruption Layer). |
| **L4 (Architect)** | Defines enterprise modular monolith and microservice decomposition standards; implements automated architectural fitness functions (ArchUnit); designs Micro-Frontend Module Federation. |
| **L5 (Strategic)** | Establishes corporate-wide software design philosophies and domain boundaries that remain stable across multiple technology generations and business pivots. |

---

## 4. Practical Experiences & Apprenticeship Exercises

1. **Conduct an Event Storming Workshop**: Facilitate an Event Storming session with domain experts and developers to map a complex domain (e.g., Order-to-Cash or Claims Processing) into explicit Bounded Contexts.
2. **Refactor a Ball of Mud into a Modular Monolith**: Enforce compile-time or package-level boundary rules (e.g., using Java modules or .NET project references) in an entangled monolith to prevent cross-domain database queries.
3. **Design an Anti-Corruption Layer (ACL)**: Design an ACL translating legacy mainframe COBOL data structures into clean DDD domain entities in a modern cloud service.

---

## 5. Objective Evidence of Capability (What to Inspect in Git)

- [ ] Strategic Domain Context Map documenting Bounded Context relationships and translation layers.
- [ ] Codebase applying Clean / Hexagonal Architecture with 100% framework-independent domain models.
- [ ] Automated CI architectural boundary rules (e.g., ArchUnit tests failing on invalid layer dependencies).

---

## 6. Common Cognitive Gaps & Blind Spots

* **Microservices as Code Organization**: Splitting a codebase into 30 microservices to enforce modularity instead of using packages/modules, inheriting distributed network latency and failure modes.
* **Anemic Domain Models**: Treating entities as dumb data bags with getters/setters while scattering business logic across hundreds of procedural service classes.
* **Entity Leaks across Contexts**: Exposing internal database entities directly across API boundaries instead of explicit, versioned Data Transfer Objects (DTOs).

---

## 7. Authoritative Repository Links

* Architecture Patterns: [`13-architecture-patterns/`](../../13-architecture-patterns/README.md)
* Domain-Driven Design: [`13-architecture-patterns/domain-driven-design/`](../../13-architecture-patterns/README.md)
* Modernization & Decomposition: [`15-modernization/`](../../15-modernization/README.md)
* Frontend Modularity: [`04-frontend/micro-frontends/`](../../04-frontend/micro-frontends/README.md)

---

## 8. Diagnostic Assessment Questions

1. *How do you identify the boundary of an Aggregate Root in Domain-Driven Design to guarantee transactional consistency?*
2. *Under what conditions should two services share a database schema, and when is that a fatal architectural flaw?*
3. *How does an Anti-Corruption Layer (ACL) protect a modern cloud architecture during a multi-year migration from a legacy ERP?*
