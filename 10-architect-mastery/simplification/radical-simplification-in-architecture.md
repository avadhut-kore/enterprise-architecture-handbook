# Radical Simplification in Architecture

"Fools ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it." — Alan Perlis

## 1. Accidental vs Essential Complexity

- **Essential Complexity**: Inherent to the business problem (e.g., complex insurance claim rules, international tax tariffs). Cannot be removed, only organized cleanly.
- **Accidental Complexity**: Introduced by our own architectural choices (e.g., microservices where a monolith works, multi-region replication where single-region suffices, distributed caches where local memory works).

## 2. The Architectural Subtraction Heuristic

Before adding a new layer, queue, or service, ask:
1. *What happens if we delete this component entirely?*
2. *Can our existing relational database handle this queue workload via `SKIP LOCKED`?*
3. *Are we building this to solve a real scale problem, or an imaginary future hypothetical?*

Every component in an architecture is a liability that requires monitoring, security patching, upgrades, and on-call paging.

## Related Modules
- [Cognitive Biases](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/decision-making/cognitive-biases-in-architecture.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
