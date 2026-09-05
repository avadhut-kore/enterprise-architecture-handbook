# Reliability Engineering Architecture (`reliability-engineering/`)

## Executive Summary

Reliability engineering designs software systems that anticipate failure, prevent cascading collapse, and maintain acceptable user experiences during severe infrastructure degradation.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`fault-tolerance-and-graceful-degradation.md`](fault-tolerance-and-graceful-degradation.md) | Degradation | Fallback UI, cached stale reads, asynchronous queue offloading |
| [`circuit-breakers-bulkheads-and-load-shedding.md`](circuit-breakers-bulkheads-and-load-shedding.md) | Isolation | Netflix Hystrix / Resilience4j, connection pools, priority queues |
| [`backpressure-and-rate-limiting.md`](backpressure-and-rate-limiting.md) | Flow Control | Reactive Streams, TCP window exhaustion, consumer lag controls |
| [`chaos-engineering-and-game-days.md`](chaos-engineering-and-game-days.md) | Chaos Ops | Chaos Mesh / Litmus, latency injection, AZ kill game days |
