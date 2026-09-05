# Irreversible vs Reversible Decisions (Type 1 vs Type 2)

A primary failure mode of software engineering leadership is treating all decisions as if they have equal permanence. Applying Type 1 rigor to Type 2 decisions paralyzes teams, while treating Type 1 decisions casually leads to catastrophic technical debt.

## 1. Type 1 vs Type 2 Taxonomy

```
                   Decision Reversibility
             Reversible (Two-Way)     Irreversible (One-Way)
          ┌─────────────────────────┬─────────────────────────┐
    High  │ TYPE 2: DELEGATE        │ TYPE 1: ARCHITECT CRITICAL
          │ - Rapid experimentation │ - Deep analysis         │
          │ - Automated rollbacks   │ - Multi-stakeholder ADR │
 Impact   │ - Fast decision cycles  │ - Red-team review       │
          ├─────────────────────────┼─────────────────────────┤
    Low   │ TYPE 2: AUTOMATE        │ TYPE 2: MINOR FRICTION  │
          │ - Team autonomy         │ - Document in ticket    │
          │ - Linting / Conventions │ - Fast consensus        │
          └─────────────────────────┴─────────────────────────┘
```

## 2. Concrete Examples in Software Architecture

| Category | Type 2 (Reversible / Two-Way Door) | Type 1 (Irreversible / One-Way Door) |
| :--- | :--- | :--- |
| **Data Storage** | Adding a caching tier (Redis); creating secondary indexes; changing serializer formats. | Core primary database engine (Relational ACID vs Distributed NoSQL); relational schema partitioning keys; multi-region active-active master topology. |
| **Integration** | HTTP payload format (JSON vs Protobuf); retry backoff jitter algorithms. | Synchronous RPC vs Asynchronous Event-Driven choreography across bounded contexts; global entity identity generation scheme (UUIDv7 vs distributed auto-increment). |
| **Compute** | Framework version upgrade (Spring Boot 3.1 -> 3.2); container base image OS. | Multi-tenant shared database vs database-per-tenant isolation model; monolithic database decomposition. |
| **Security** | Session timeout duration; token refresh interval. | Zero-Trust network boundary topology; KMS encryption key hierarchy and envelope encryption architecture. |

## 3. Decision Velocity Heuristics

1. **If the cost of reversing is low**, decide today. The fastest way to learn is via production telemetry.
2. **If the cost of reversing is massive**, buy optionality. Use architectural seams, interfaces, facades, and modular abstractions to defer the point of commitment until uncertainty decreases.
3. **Cost of Delay vs Cost of Mistake**: If `Cost of Delay > Cost of Fixing a Mistake`, move immediately with a reversible pattern.

## Related Modules
- [Cognitive Biases in Architecture](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/decision-making/cognitive-biases-in-architecture.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
