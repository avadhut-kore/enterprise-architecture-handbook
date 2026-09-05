# Resource Exhaustion in Distributed Systems

## 1. Taxonomy of Critical Resource Exhaustion

Distributed services operate on bounded hardware resources. When one critical resource is exhausted, the process either crashes violently (OOM) or stops responding to traffic.

```
+--------------------------+----------------------------+----------------------------+
| Resource Type            | Symptom                    | Architectural Defense      |
+--------------------------+----------------------------+----------------------------+
| Memory (RAM)             | JVM OutOfMemoryError / OOMK| Strict Object Size Limits, |
|                          |                            | Streamed Processing (Chunks|
| File Descriptors         | "Too many open files"      | Connection Pooling, OS     |
|                          | Socket bind failures       | ulimit Tuning              |
| Thread Pools             | Worker Thread Exhaustion   | Async Non-Blocking I/O,    |
|                          | Request Timeout Cascades   | Reactive Streams (Epoll)   |
| Database Connections     | Connection Pool Starvation | External Proxies (PgBouncer|
|                          |                            | Connection Multiplexing    |
| Disk Space & Inodes      | Write Failures, Log Halts  | Automated Log Rotation,    |
|                          |                            | Disk Capacity Thresholds   |
+--------------------------+----------------------------+----------------------------+
```

---

## 2. Architectural Guardrails

- **Cap Concurrency Everywhere**: Never use unbounded queues or thread pools. Every queue must be bounded; when full, apply immediate backpressure or load shedding.
- **Stream, Never Buffer Full Payloads**: Process large payloads (file uploads, large JSON exports) as byte streams rather than reading entire gigabyte payloads into heap memory.
