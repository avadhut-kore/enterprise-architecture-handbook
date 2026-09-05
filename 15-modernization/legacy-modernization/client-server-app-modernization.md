# Client-Server Modernization: VB6, Delphi, PowerBuilder

## 1. Migrating Fat Clients to Web Architecture
Legacy two-tier client-server applications bundle UI, business logic, and direct SQL queries:
- **Phase 1**: Extract direct SQL queries into a modern REST API backend.
- **Phase 2**: Rebuild the UI as a responsive single-page application (React / Angular).

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
