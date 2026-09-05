# Terminal Systems & Green Screen Modernization

## 1. De-risking Screen Scraping (TN3270 / TN5250)
Screen scraping is brittle. Modernize by:
- Inspecting the underlying CICS transaction definitions behind the terminal screen.
- Exposing the CICS transaction directly via IBM z/OS Connect EE as a REST/JSON endpoint, eliminating terminal emulation entirely.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
