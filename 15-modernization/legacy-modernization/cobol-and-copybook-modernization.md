# COBOL Copybooks & EBCDIC Data Modernization

## 1. The Binary Data Challenge
COBOL applications store records in **EBCDIC** format using fixed-width **Copybooks** with packed decimal structures (`COMP-3`):
- To modern Java/C# microservices, packed decimal fields look like corrupted binary noise.
- Deploy open-source parser libraries (e.g., JRecord, Camel COBOL, or AWS Blu Age) to unpack binary EBCDIC bytes directly into typed JSON/Protobuf objects in-flight.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
