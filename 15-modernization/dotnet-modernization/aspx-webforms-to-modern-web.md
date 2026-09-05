# ASP.NET WebForms to Modern Web Architectures

## 1. Breaking the ViewState Monolith
ASP.NET WebForms (`.aspx`) tightly couples UI controls, server-side events, and ViewState into the DOM:
- **Strangler Approach**: Extract backend database operations into REST Web APIs.
- Rebuild user interface screens progressively using modern single-page applications (React, Angular) or server-side component models (**Blazor**).

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
