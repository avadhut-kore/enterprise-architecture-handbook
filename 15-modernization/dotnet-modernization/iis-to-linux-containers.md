# Windows IIS to Linux Containers on Kubernetes

## 1. Operating System License Elimination
Hosting applications on Windows Server IIS requires expensive Windows Server licensing per virtual CPU core:
- Modern .NET runs natively on Linux Alpine/Debian Docker containers using Kestrel web server.
- Deploy containerized .NET workloads on Linux Kubernetes nodes (EKS/AKS/GKE), reducing cloud compute costs by up to 50%.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
