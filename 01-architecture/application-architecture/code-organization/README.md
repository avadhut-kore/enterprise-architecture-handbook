# Code Organization & Structural Architecture

The way code is organized in repositories, directories, packages, and assemblies directly impacts architectural integrity. Bad organization obscures domain boundaries, encourages improper coupling, and slows developer onboarding.

This directory establishes standards for organizing enterprise codebases across monoliths, modular systems, and microservices.

---

## Catalog of Organization Guides

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [Project Structure](project-structure.md) | High-Level Directory Layout | Standard enterprise repository topology |
| [Feature-Based Organization](feature-based-organization.md) | Screaming Architecture | Grouping code by business capability |
| [Layer-Based Organization](layer-based-organization.md) | Technical Grouping | When technical layering is acceptable |
| [Domain-Based Organization](domain-based-organization.md) | Domain-Driven Design | Aligning folders with Bounded Contexts |
| [Module-Based Organization](module-based-organization.md) | Modular Monoliths | Self-contained independent modules |
| [Shared Code](shared-code.md) | Common Logic Governance | Rules for sharing code across services |
| [Common Libraries](common-libraries.md) | Internal Frameworks | Building vs avoiding enterprise shared SDKs |
| [Utility Libraries](utility-libraries.md) | Helper Classes | Preventing "Utils" junk drawers |
| [Dependency Boundaries](dependency-boundaries.md) | Physical Isolation | Enforcing boundaries via projects and packages |
| [Naming Conventions](naming-conventions.md) | Ubiquitous Vocabulary | Naming classes, packages, DTOs & interfaces |
| [Package Structure](package-structure.md) | Java/Go/Python Packaging | Internal vs public namespace strategies |
| [Repository Structure](repository-structure.md) | Mono-repo vs Multi-repo | Architectural trade-offs of repo strategies |
