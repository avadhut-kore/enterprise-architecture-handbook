# Migration Automation Tooling Catalog

## 1. Tooling Landscape
- **Discovery**: AWS Application Discovery Service, Azure Migrate, Device42.
- **Data Replication**: AWS DMS, Debezium, Qlik Replicate, Oracle GoldenGate.
- **Server Migration**: AWS Application Migration Service (MGN), Azure Site Recovery (ASR).
- **Configuration & Infrastructure**: Terraform, Ansible, HashiCorp Packer.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
