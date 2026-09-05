# Enterprise Migration Factory Model

## 1. Industrialized Factory Pipeline
The Migration Factory standardizes repeatable patterns across thousands of servers:
- **Discovery Pod**: Validates inventory and dependencies.
- **Build Pod**: Provisions target cloud landing zone resources via Terraform/Bicep.
- **Migration Pod**: Executes continuous block replication and test cutovers.
- **Cutover Pod**: Manages weekend change advisory board execution and DNS shift.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
