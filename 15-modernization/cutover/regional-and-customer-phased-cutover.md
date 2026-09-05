# Regional and Cohort-Based Phased Cutover

## 1. Blast Radius Containment
Migrate users by designated cohorts:
- **Internal Employees / Beta Users**: Week 1.
- **Low-Volume Geographic Region (e.g., APAC/Australia)**: Week 2.
- **Medium-Volume Region (e.g., EMEA/Europe)**: Week 3.
- **High-Volume Core Region (e.g., Americas/US)**: Week 4.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
