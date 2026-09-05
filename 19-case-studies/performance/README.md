# Performance Engineering Forensic Case Studies

## 1. Domain Overview & Architectural Scope
Performance failures are rarely solved by simply "adding more CPU cores" or "enabling autoscaling." In enterprise distributed systems, performance collapse occurs at hidden bottlenecks: catastrophic ORM N+1 query amplification, database connection pool exhaustion under latency spikes, JVM Stop-The-World (STW) garbage collection pauses, Redis single-threaded CPU saturation from 250MB large keys, CPU-bound reflection in JSON serializers, and TLS handshake storms during connection re-establishment.

This category presents rigorous, data-driven forensic investigations following the scientific performance methodology:
$$\text{Baseline} \longrightarrow \text{Symptom} \longrightarrow \text{Measurement} \longrightarrow \text{Hypothesis} \longrightarrow \text{Experiment} \longrightarrow \text{Root Cause} \longrightarrow \text{Architectural Fix}$$

---

## 2. Case Study Portfolio Index

| Case Study ID | Title | Primary Performance Bottleneck | Systemic Consequence |
| :--- | :--- | :--- | :--- |
| **[`cs-perf-01`](cs-perf-01-orm-n-plus-one-query-black-friday.md)** | **ORM N+1 Query Explosion on Black Friday** | Hibernate EAGER loading fetching 50k queries/request | E-commerce database CPU pinned at 100%; $8.5M in lost flash-sale orders |
| **[`cs-perf-02`](cs-perf-02-connection-pool-thread-starvation.md)** | **HikariCP Connection Pool Thread Starvation** | Unbounded connection pool exhaustion in banking API | All core banking endpoints return HTTP 500 within 90 seconds of DB latency spike |
| **[`cs-perf-03`](cs-perf-03-jvm-garbage-collection-stop-the-world.md)** | **45-Second JVM Garbage Collection Pause** | Massive 128GB JVM heap on high-frequency trading gateway | G1GC Stop-The-World pause causing cluster ejection and split-brain trading |
| **[`cs-perf-04`](cs-perf-04-redis-large-key-hot-shard-meltdown.md)** | **Redis Large-Key Single-Thread Meltdown** | 250MB single Redis Hash key with 5M elements | Single-thread event loop blocked for 4.8 seconds; cascading game session timeouts |
| **[`cs-perf-05`](cs-perf-05-json-serialization-cpu-bottleneck.md)** | **Reflection JSON Serialization CPU Saturation** | Inefficient Java Jackson reflection on IoT telematics | Kubernetes pod fleet scaled to 800 pods at 100% CPU; $120k cloud waste |
| **[`cs-perf-06`](cs-perf-06-tls-handshake-connection-storm.md)** | **TLS Handshake Cryptographic CPU Storm** | Missing TLS session resumption & short keep-alives | Edge API Gateway CPU collapsed under 15,000 asymmetric RSA handshakes/sec |
