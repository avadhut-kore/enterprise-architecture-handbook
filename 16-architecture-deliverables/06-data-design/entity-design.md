# Entity Design & Aggregate Boundaries

## 1. Domain Aggregate Roots
* Enforce transactions strictly within aggregate boundaries.
* Never use cross-database distributed two-phase commit (2PC) transactions; use the Saga pattern with asynchronous domain events.
