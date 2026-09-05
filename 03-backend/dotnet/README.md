# Modern .NET Enterprise Architecture (.NET 8+)

This directory establishes architectural standards, engineering patterns, performance baselines, and production guidelines for modern enterprise applications running on the cross-platform **.NET 8 / 9 runtime**.

> [!IMPORTANT]
> **Architecture, Not Syntax**: This documentation analyzes runtime execution models, garbage collection characteristics, thread pool starvation, memory barriers, dependency injection lifetimes, and boundary enforcement—not elementary C# syntax.

---

## Subsystem Navigation

| Subsystem | Scope & Focus |
| :--- | :--- |
| [Architecture](architecture/) | Host lifecycle, ASP.NET Core pipelines, Clean/Hexagonal/.NET patterns |
| [Data Access](data/) | EF Core architecture, DbContext lifecycles, query performance & transactions |
| [API Engineering](api/) | Minimal APIs vs Controllers, problem details, idempotency & versioning |
| [Resilience](resilience/) | Polly policies, circuit breakers, rate limiting & fault tolerance |
| [Testing Architecture](testing/) | Testcontainers, WebApplicationFactory, NetArchTest architecture testing |
| [Performance](performance/) | Span<T>, Memory<T>, Gen 0/1/2 GC tuning, async-await state machines |
| [Security](security/) | ASP.NET Identity, OAuth2/OIDC, JWT validation, authorization policies |
