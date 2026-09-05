# Architecture Retrospectives and Decision Reviews

Architectural Decision Records (ADRs) must not be write-only artifacts. High-performing architecture teams conduct recurring decision reviews to assess whether choices delivered their intended outcomes.

## 1. The 6-Month ADR Audit Ritual

Every 6 months post-implementation, the architecture guild reviews approved ADRs:
1. **Did the projected benefits materialize?** (e.g., Did moving to GraphQL actually decrease mobile latency?)
2. **Did unexpected costs or complexities emerge?** (e.g., Did GraphQL query complexity introduce N+1 database bottlenecks?)
3. **Has external technology moved?** (e.g., Has an AWS managed service rendered our bespoke custom broker obsolete?)

## 2. ADR Lifecycle Transitions
- `PROPOSED` -> `ACCEPTED` -> `DEPRECATED` -> `SUPERSEDED`
- When a decision is reversed or replaced, the original ADR is never deleted or edited; it is marked `SUPERSEDED by ADR-042` with an explanation of what changed in the operating environment.

## Related Modules
- [Pragmatic Governance](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/governance/pragmatic-architecture-governance.md)
- [Architecture Deliverables](../../16-architecture-deliverables/README.md)
