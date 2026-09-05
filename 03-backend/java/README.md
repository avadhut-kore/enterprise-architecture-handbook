# Modern Java Enterprise Architecture (Java 21+ & Spring Boot 3+)

This directory establishes architectural baselines, runtime design rules, and performance engineering guidelines for modern enterprise applications running on the **Java 21+ Virtual Machine (JVM)** and **Spring Boot 3+**.

> [!IMPORTANT]
> **Architecture, Not Syntax**: This documentation focuses on the Java Memory Model, Virtual Threads (Project Loom), JVM Garbage Collection ergonomics (ZGC / G1), Hibernate session boundaries, transaction isolation, and boundary enforcement.

---

## Subsystem Navigation

| Subsystem | Scope & Focus |
| :--- | :--- |
| [Architecture](architecture/) | Spring framework internals, Bean lifecycles, Clean/Hexagonal Java |
| [Data Access](data/) | JPA/Hibernate architecture, entity lifecycle, N+1 query traps & pooling |
| [API Engineering](api/) | Spring MVC / WebFlux, RFC 7807 problem details, idempotency & validation |
| [Resilience](resilience/) | Resilience4j, circuit breakers, bulkheads, rate limiters & fallbacks |
| [Testing Architecture](testing/) | Testcontainers, MockMvc, ArchUnit architecture boundary enforcement |
| [Performance](performance/) | JVM memory layout, ZGC/G1 tuning, Virtual Threads, thread pools |
| [Security](security/) | Spring Security 6, OAuth2/OIDC, JWT filter chains, authorization |
