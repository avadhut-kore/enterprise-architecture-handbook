# Low-Level Design Review Checklist

Use this 20-point checklist before marking an LLD ready for engineering code implementation.

---

## 1. Structure & Architecture
- [ ] Package and directory layout adheres to Clean / Hexagonal Architecture.
- [ ] Domain logic has zero dependencies on external frameworks or databases.
- [ ] Dependency injection graph has no circular dependencies.

## 2. Invariants & Data Integrity
- [ ] Domain invariants and state machine transitions are mathematically airtight.
- [ ] Money calculations strictly utilize arbitrary-precision arithmetic (`BigDecimal`).
- [ ] Database locking strategy (Optimistic/Pessimistic) is explicitly documented.

## 3. Concurrency & Performance
- [ ] Thread safety of singletons and shared caches is verified.
- [ ] Database queries utilize covering indexes with no unindexed full table scans.
- [ ] Cache invalidation and TTL policies prevent memory leaks.

## 4. Resilience & Testing
- [ ] Exceptions map directly to standard RFC 7807 HTTP / gRPC status codes.
- [ ] Database rollbacks occur automatically on uncaught domain exceptions.
- [ ] Test strategy covers unit tests ($\ge 85\%$) and integration tests with Testcontainers.
