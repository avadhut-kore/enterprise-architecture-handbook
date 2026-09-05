# Dual-Reads and Shadow Data Validation

## 1. Validating Query Equivalence Before Cutover
Before switching live read traffic to the modernized database, verify that queries return identical results:
1. Application reads from primary legacy database and services customer response.
2. Asynchronously, a worker fires the identical query against the modernized database.
3. A comparator diffs the records down to data types, timestamps, and floating-point precision, logging any mismatches to an analytics dashboard.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
