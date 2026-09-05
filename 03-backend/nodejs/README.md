# Modern Node.js & TypeScript Enterprise Architecture (Node.js 20+ LTS)

This directory establishes architectural standards, runtime engineering rules, and design patterns for modern enterprise backends built with **Node.js (v20+ LTS) and TypeScript (v5+)**.

> [!IMPORTANT]
> **Architecture, Not Syntax**: This documentation focuses on the libuv event loop phases, microtask/macrotask queuing, worker thread offloading, stream backpressure, V8 heap allocation limits, and TypeScript type-safe architectural boundaries.

---

## Subsystem Navigation

| Subsystem | Scope & Focus |
| :--- | :--- |
| [Architecture](architecture/) | Node.js runtime internals, Fastify vs Express, Clean/Hexagonal TypeScript |
| [API Engineering](api/) | Zod schema validation, routing architecture, RFC 7807 problem details |
| [Data Access](data/) | Database connectivity, Prisma vs TypeORM vs Kysely, connection pooling |
| [Testing Architecture](testing/) | Vitest/Jest, Testcontainers node, dependency-cruiser boundary tests |
| [Performance](performance/) | Event loop monitoring, memory leak debugging, V8 heap snapshots, clustering |
| [Security](security/) | Prototype pollution, npm supply chain defense, OAuth2/OIDC, secret handling |
