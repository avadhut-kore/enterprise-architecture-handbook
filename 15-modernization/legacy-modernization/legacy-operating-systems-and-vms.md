# Unsupported Operating Systems & Virtual Machines

## 1. Triage for EOL Platforms (Windows 2008 / AIX / Solaris)
- **Containerization**: Package legacy apps in Windows Server 2022 containers.
- **Microsegmentation**: Isolate unpatched legacy VMs in quarantined subnets behind reverse proxies with strict firewall rules and no internet access.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
