# Application Architecture Styles & Patterns

Application architecture styles govern how classes, modules, packages, and layers are organized to manage dependencies, isolate business rules, and ensure long-term maintainability.

---

## Architectural Styles Catalog

| Style | Central Philosophy | Primary Dependency Rule |
| :--- | :--- | :--- |
| [Layered Architecture](layered-architecture.md) | Traditional horizontal segregation | Inward/downward toward database |
| [N-Tier Architecture](n-tier-architecture.md) | Physically separated process tiers | Client -> Web -> App -> DB network tiers |
| [Clean Architecture](clean-architecture.md) | Concentric circles around pure domain | All dependencies point strictly inward |
| [Hexagonal Architecture](hexagonal-architecture.md) | Ports and Adapters | Core isolated via driver/driven ports |
| [Onion Architecture](onion-architecture.md) | Inverted domain core with layers | Infrastructure depends on Domain Core |
| [Vertical Slice Architecture](vertical-slice-architecture.md) | Feature slicing over technical layers | Each request is a self-contained vertical slice |
| [Feature-Based Architecture](feature-based-architecture.md) | Screaming business modularity | Organized by domain capability |
| [Modular Monolith](modular-monolith.md) | Monolithic deployment with strict modules | Modules coordinate via contracts/events |
| [Plugin Architecture](plugin-architecture.md) | Extensibility via dynamic plugins | Core system unaware of custom extensions |
| [Microkernel Architecture](microkernel-architecture.md) | Minimal core with pluggable engines | Core runtime orchestrates add-on modules |
| [Domain-Centric Architecture](domain-centric-architecture.md) | Domain Model as the central gravity | Models domain richness over technical plumbing |

---

## Architecture Style Comparisons

| Comparison | Core Trade-Off Evaluated |
| :--- | :--- |
| [Layered vs Clean](comparisons/layered-vs-clean.md) | Database-centric vs Domain-centric dependency flow |
| [Clean vs Hexagonal](comparisons/clean-vs-hexagonal.md) | Concentric use-case circles vs Ports & Adapters ports |
| [Clean vs Onion](comparisons/clean-vs-onion.md) | Use-case orchestration vs Layered concentric interfaces |
| [Layered vs Vertical Slice](comparisons/layered-vs-vertical-slice.md) | Horizontal technical coupling vs Autonomous feature slices |
| [Feature-Based vs Layer-Based](comparisons/feature-based-vs-layer-based.md) | High cohesion by business feature vs Technical categorization |
| [Modular Monolith vs Microservices](comparisons/modular-monolith-vs-microservices.md) | In-process boundary safety vs Distributed operational complexity |
