# Designing Applications for Testability

## 1. Architectural Seams

An **architectural seam** is a place where you can alter system behavior without editing source code. Seams are created by programming to interfaces and utilizing dependency injection.

---

## 2. Elimination of Non-Deterministic State

To prevent flaky tests, decouple application code from non-deterministic primitives:
- **System Clock**: Inject a `TimeProvider` or `Clock` interface; never call `DateTime.UtcNow` or `System.currentTimeMillis()` directly in domain logic.
- **ID Generation**: Inject a `GuidGenerator` or pass generated IDs as parameters.
- **Randomness**: Inject seedable random abstractions.
