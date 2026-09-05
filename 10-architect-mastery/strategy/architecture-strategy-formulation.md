# Architecture Strategy Formulation

A technical strategy is not a list of technologies to adopt. It is a cohesive response to a significant business challenge.

## 1. Strategy Kernel (Rumelt Framework)

Every sound architectural strategy contains three essential components:
1. **The Diagnosis**: A clear, blunt explanation of the nature of the challenge (e.g., "Our checkout stack is tightly coupled to legacy mainframe billing, resulting in 4-month release cycles and lost conversion").
2. **A Guiding Policy**: An overall approach chosen to overcome the obstacles identified in the diagnosis (e.g., "Decouple cart checkout via an asynchronous event buffer and real-time inventory cache").
3. **Coherent Actions**: Coordinated steps, resource allocations, and architectural initiatives designed to carry out the guiding policy.

```
┌────────────────────────────────────────────────────────┐
│ 1. DIAGNOSIS                                           │
│ "Monolithic database contention caps peak orders at    │
│  2,000 TPS while Black Friday demand requires 10,000"  │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. GUIDING POLICY                                      │
│ "Move order placement to an ephemeral, in-memory queue │
│  with idempotent async persistence into sharded DBs"   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. COHERENT ACTIONS                                    │
│ - Q1: Implement Kafka ingestion buffer                 │
│ - Q2: Refactor order API into stateless Go microservice│
│ - Q3: Implement Aurora PostgreSQL sharded storage      │
└────────────────────────────────────────────────────────┘
```

## Related Modules
- [Wardley Mapping](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/strategy/wardley-mapping-for-architects.md)
- [Technology Strategy](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/technology-strategy/README.md)
