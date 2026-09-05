# Application Architecture

Application architecture defines the internal structural patterns, module boundaries, layering, state management, dependency direction, and execution lifecycles within software systems.

While Enterprise Architecture plans portfolios and Solution Architecture designs cross-cutting systems, **Application Architecture dictates how code is engineered** to fulfill non-functional requirements (NFRs) such as maintainability, testability, security, and performance.

---

## Knowledge Index

| Document | Core Subject | Primary Architectural Focus |
| :--- | :--- | :--- |
| [Application Architecture Overview](application-architecture-overview.md) | Structural Blueprint | The role of application architecture in enterprise delivery |
| [Application Boundaries](application-boundaries.md) | Domain & Boundary Sizing | Deciding component perimeters, facades, and blast radiuses |
| [Application Responsibilities](application-responsibilities.md) | Layer Duties | Assigning responsibilities across Presentation, Domain & Infra |
| [Application Layering](application-layering.md) | Logical Segmentation | Strict vs relaxed layering and bypass antipatterns |
| [Application Modularity](application-modularity.md) | Encapsulation | Public API facades vs internal implementation details |
| [Application Dependency Management](application-dependency-management.md) | Inversion & Direction | Protecting domain cores from infrastructural churn |
| [Application Coupling](application-coupling.md) | Connascence & Metrics | Afferent/efferent coupling, instability, and abstractness |
| [Application Cohesion](application-cohesion.md) | Semantic Grouping | Functional, sequential, and communicational cohesion |
| [Application Composition](application-composition.md) | Structural Assembly | Composition over inheritance, decorators, and pipelines |
| [Application Configuration](application-configuration.md) | Dynamic Settings | Environment externalization, 12-Factor app, and overrides |
| [Application Secrets](application-secrets.md) | Secret Lifecycles | Vault integration, in-memory protection, and rotation |
| [Application State](application-state.md) | State Management | Stateless compute vs stateful domain entities and caches |
| [Application Lifecycle](application-lifecycle.md) | Boot & Shutdown | Pre-flight validation, graceful draining, and health gates |
| [Application Extensibility](application-extensibility.md) | Open/Closed Principle | Plugins, strategy patterns, hooks, and middleware |
| [Application Testability](application-testability.md) | Test Architecture | Designing seams, test doubles, and deterministic harnesses |
| [Application Observability](application-observability.md) | In-App Telemetry | Context propagation, span creation, and metric counters |
| [Application Performance](application-performance.md) | Low-Latency Code | Memory allocations, GC pressure, async I/O, and pooling |
| [Application Resilience](application-resilience.md) | In-Process Faults | Bulkheads, circuit breakers, timeouts, and fallbacks |
