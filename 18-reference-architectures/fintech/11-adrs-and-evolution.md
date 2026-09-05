# Architecture Decision Records & Evolution Roadmap: Fintech

## 1. Canonical Architecture Decision Records

### ADR-001: Adoption of Immutable Double-Entry Ledger Model
- **Status**: Accepted
- **Context**: Mutable balance updates in relational databases make historical financial auditing impossible and create race conditions.
- **Decision**: All financial movements must be recorded as balancing double-entry journal lines in an append-only ledger table.
- **Consequences**: Guarantees mathematical auditability; requires indexed materialized views for real-time balance queries.

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x)**: Single-region PostgreSQL with strict double-entry triggers.
- **Stage 2 (10x)**: Dedicated card authorization cache; Kafka event mesh; CloudHSM integration.
- **Stage 3 (100x)**: Globally distributed multi-region Spanner ledger; sub-30ms global authorization.
