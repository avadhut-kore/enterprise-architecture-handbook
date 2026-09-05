# .NET Framework to .NET 8/9 Migration Playbook

## 1. Architectural Strategy
Migrating from Windows-locked .NET Framework 4.8 to cross-platform .NET 8:
- Use the **.NET Upgrade Assistant** tool to automate project file format conversion (`<Project Sdk="Microsoft.NET.Sdk">`).
- Target `.NET Standard 2.0` for shared class libraries during the dual-run transition phase so they can be referenced by both legacy .NET Framework and modern .NET 8 services.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
