# Real-Time Data Reconciliation During Cutover

## 1. In-Flight Verification Checklist
During the cutover maintenance window:
- **Row Count Parity**: Verify $\Delta 	ext{Rows} == 0$ across all primary and child tables.
- **Hash Checksums**: Compare MD5/SHA-256 digests of balance fields across legacy and modern stores.
- **Orphaned Record Scan**: Scan for child records whose parent foreign keys failed replication.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
