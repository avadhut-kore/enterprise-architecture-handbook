# Migration Factory Governance & Architecture Review Gates

## 1. The 5 Quality Gates
- **Gate 1: Strategy Approval**: Formal sign-off on 11 Rs strategy mapping.
- **Gate 2: Landing Zone Verification**: Security and networking compliance check.
- **Gate 3: Test Cutover Sign-off**: Successful dry-run migration in staging environment.
- **Gate 4: Production Go/No-Go**: Final checklist execution 24 hours prior to cutover.
- **Gate 5: Operational Handover**: Hypercare exit and transition to business-as-usual operations.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
