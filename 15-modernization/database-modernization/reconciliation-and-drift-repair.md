# Continuous Data Reconciliation & Drift Repair

## 1. Automated Parity Auditing
Even with CDC, data divergence will occur due to network dropped packets or manual DBA interventions:
- **Nightly Row Count & Hash Checks**: Compute MD5/SHA-256 hashes of table partitions across legacy and modern databases.
- **Automated Drift Repair**: When a break is detected, fetch the authoritative row and publish a repair event to the outbox queue.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
