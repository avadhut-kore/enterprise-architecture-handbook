# Post-Migration FinOps and Cost Optimization

## 1. Eliminating Cloud Sprawl
Immediately following cutover:
- **Compute Rightsizing**: Analyze CloudWatch/Azure Monitor 14-day utilization metrics; downsize over-provisioned instances from `r5.4xlarge` to `r5.xlarge`.
- **Commitment Discounts**: Purchase 1-year or 3-year Compute Savings Plans or Reserved Instances for predictable baseline workloads.
- **Storage Tiering**: Configure S3 Lifecycle policies moving unaccessed logs to Glacier Instant Retrieval after 30 days.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
