# Architecture Decision Records & Evolution Roadmap: E-Commerce

## 1. Canonical Architecture Decision Records

### ADR-001: Adoption of Redis Atomic Lua Scripts for Flash-Sale Reservations
- **Status**: Accepted
- **Context**: Relational database row-level locking (`SELECT ... FOR UPDATE`) causes severe connection exhaustion and database crashes under 20,000 concurrent checkout attempts.
- **Decision**: Manage active inventory reservation counters in Redis using atomic Lua scripts with 10-minute auto-expiring keys.
- **Consequences**: Enables 50,000 TPS inventory reservations; requires out-of-band reconciliation with warehouse master databases.

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x)**: Modular monolith with embedded cache.
- **Stage 2 (10x)**: Headless Next.js frontend, microservices, and Redis reservation layer.
- **Stage 3 (100x)**: Multi-region active-active deployment with global edge inventory replication.
