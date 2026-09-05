# Feature Flags & Canary Traffic Shifting

## 1. Progressive Weight Shifting
Instead of switching 100% of traffic at midnight:
1. Shift **1%** of traffic to modern service. Monitor error rates for 1 hour.
2. Shift **5%** of traffic. Monitor for 2 hours.
3. Shift **25%** of traffic. Monitor for 4 hours.
4. Shift **100%** of traffic.

Automated canary analysis (Argo Rollouts, Flagger) trips an instant, automatic rollback if HTTP 5xx error rates exceed 0.5% or p99 latency spikes above 500ms.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
