# The "Refactor" Strategy: Code-Level Modernization

## 1. Architectural Definition
**Refactor** modifies the internal structure, code quality, and non-functional characteristics of an application while strictly preserving its external observable behavior and public API contracts.

---

## 2. Primary Refactoring Patterns
- **Monolith to Modular Monolith**: Breaking tight spaghetti coupling inside a single codebase by establishing strict package-private boundaries, eliminating circular dependencies, and enforcing bounded contexts.
- **Runtime & Framework Upgrades**: Upgrading legacy .NET Framework 4.6 to modern .NET 8, or Java 8 with Spring 4 to Java 21 with Spring Boot 3.
- **Blocking I/O to Asynchronous**: Replacing thread-per-request blocking calls with non-blocking async/await or Java 21 Virtual Threads.
- **Extract Domain Layer**: Separating tangled database access code (SQL queries inside UI controllers) into clean Domain, Application, and Infrastructure layers (Hexagonal Architecture).
