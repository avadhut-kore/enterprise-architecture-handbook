# Portfolio Triage and Wave Design

## 1. Triage Classification
Sort candidate applications into three distinct operational tracks:
- **Track 1 (Fast-Track Rehost)**: Commodity internal applications; low complexity, standard operating systems.
- **Track 2 (Replatform / Containerize)**: Standard web/API applications suitable for containerization on Kubernetes.
- **Track 3 (Complex Modernization / Rearchitect)**: Core revenue-generating databases and tightly coupled monoliths requiring custom engineering.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
