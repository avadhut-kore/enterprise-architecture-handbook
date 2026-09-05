# Cloud Cutover Execution and DNS Traffic Switching

## 1. Lowering DNS Time-to-Live (TTL)
7 days prior to cutover weekend, reduce DNS TTL from 86,400 seconds (24 hours) to 300 seconds (5 minutes). This ensures that when DNS records are switched to cloud load balancer IPs, customer traffic shifts globally within minutes.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
