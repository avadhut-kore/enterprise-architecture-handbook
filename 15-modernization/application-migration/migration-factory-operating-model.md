# Migration Factory Operating Model & Team Topologies

## 1. Factory Organization (Team Topologies)
- **Core Steering & Governance**: Program Director, Lead Enterprise Architect, Head of Security.
- **Factory Pods (Cross-Functional)**: Lead Cloud Architect, DevOps Engineer, Database Migration Specialist, QA/Test Lead, Application SME.
- Each factory pod owns an average velocity of 5 to 10 applications per monthly migration wave.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
