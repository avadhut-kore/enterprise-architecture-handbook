# Enterprise Modernization Architectural Patterns Library

## 1. Overview
Modernization patterns provide proven, repeatable architectural solutions to the recurring challenges of legacy transformation: maintaining system availability during rewrites, preventing domain contamination, breaking monolithic databases, and synchronizing state across distributed boundaries.

## 2. Patterns Catalog
- [strangler-fig-pattern.md](strangler-fig-pattern.md): Incremental legacy replacement via an intercepting routing facade.
- [anti-corruption-layer-pattern.md](anti-corruption-layer-pattern.md): Domain boundary isolation and translation adapters.
- [branch-by-abstraction.md](branch-by-abstraction.md): In-code abstraction layer allowing concurrent implementation swaps.
- [parallel-run-pattern.md](parallel-run-pattern.md): Running legacy and modern systems simultaneously with output validation.
- [shadow-traffic-pattern.md](shadow-traffic-pattern.md): Asynchronous live traffic mirroring for risk-free soak testing.
- [api-facade-pattern.md](api-facade-pattern.md): Stabilizing legacy endpoints behind a unified OpenAPI contract.
- [event-interception-pattern.md](event-interception-pattern.md): Capturing legacy events to feed modern distributed platforms.
- [database-strangler-pattern.md](database-strangler-pattern.md): Incremental schema splitting and query migration.
- [cdc-migration-pattern.md](cdc-migration-pattern.md): Log-based Change Data Capture for continuous data synchronization.
- [dual-read-pattern.md](dual-read-pattern.md): Reading from primary, reading from secondary, comparing diffs.
- [dual-write-with-outbox-pattern.md](dual-write-with-outbox-pattern.md): Transactional outbox pattern avoiding distributed dual-writes.
- [modular-monolith-pattern.md](modular-monolith-pattern.md): Internal boundary enforcement without distributed complexity.
- [capability-extraction-pattern.md](capability-extraction-pattern.md): Carving out a single vertical business capability end-to-end.
