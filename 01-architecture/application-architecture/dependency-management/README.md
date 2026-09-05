# Application Dependency Management

Managing dependencies is the central challenge of software architecture. In large-scale enterprise systems, unconstrained dependencies lead to tight coupling, circular references, fragile builds, and high risk during library upgrades.

This section establishes formal rules for dependency direction, inversion, boundary enforcement, and third-party risk mitigation.

---

## Knowledge Catalog

| Document | Focus Area | Core Principle |
| :--- | :--- | :--- |
| [Dependency Direction](dependency-direction.md) | Flow of Control vs Dependencies | Dependencies must point inward toward business logic |
| [Dependency Inversion](dependency-inversion.md) | DIP & Polymorphic Interfaces | High-level modules must not depend on low-level modules |
| [Dependency Rules](dependency-rules.md) | Clean Architecture Invariants | Inner circles know nothing about outer circles |
| [Dependency Graph](dependency-graph.md) | Directed Acyclic Graphs (DAG) | Managing complexity via acyclic module topologies |
| [Circular Dependencies](circular-dependencies.md) | Deadlocks & Initialization Traps| Detection, elimination, and mediator refactoring |
| [Architectural Boundaries](architectural-boundaries.md) | Layer Isolation | Enforcing strict firewalls between sub-systems |
| [Module Boundaries](module-boundaries.md) | Component Encapsulation | Exporting public contracts while concealing internals |
| [Package Boundaries](package-boundaries.md) | Code Packaging Strategy | Co-locating related types and limiting access modifiers |
| [Interface Boundaries](interface-boundaries.md) | Interface Segregation | Narrow, client-specific interfaces (ISP) |
| [External Dependencies](external-dependencies.md) | Cloud & Vendor Isolation | Wrapping external SDKs behind domain adapters |
| [Third-Party Dependencies](third-party-dependencies.md) | Open Source Library Selection | Vetting dependencies for license, health & security |
| [Dependency Risk](dependency-risk.md) | Supply Chain Threats | Mitigating abandonware, malicious packages & churn |
| [Dependency Upgrades](dependency-upgrades.md) | Lifecycle Management | Automated Dependabot/Renovate cadences & semantic versions|
| [Dependency Vulnerabilities](dependency-vulnerabilities.md) | CVE Scanning & Remediation | Software Bill of Materials (SBOM) and container scanners|
