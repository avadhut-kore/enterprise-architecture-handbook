# Non-Blocking I/O & Java 21 Virtual Threads (Project Loom)

## 1. High-Throughput Concurrency Without Reactive Complexity
Reactive programming (Project Reactor / RxJava) introduces steep debugging complexity. In Java 21:
- Adopt **Virtual Threads**: Enable lightweight, cheap fibers (`Executors.newVirtualThreadPerTaskExecutor()`) that execute standard blocking synchronous code while scaling to millions of concurrent requests.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
