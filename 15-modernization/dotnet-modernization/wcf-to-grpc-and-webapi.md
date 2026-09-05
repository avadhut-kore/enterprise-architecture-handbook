# WCF Modernization: Migrating to gRPC and REST Web APIs

## 1. Replacing Windows Communication Foundation (WCF)
WCF is not supported on non-Windows modern .NET runtimes:
- **Inter-Service Microservices**: Migrate WCF TCP/Binary bindings to high-performance **gRPC** using Protocol Buffers.
- **External Public Clients**: Migrate SOAP `BasicHttpBinding` to standard **ASP.NET Core Web API** with OpenAPI/Swagger.
- **Drop-in Transmit Fallback**: Utilize `CoreWCF` open-source port if complete rewrites are commercially impossible.

## Operational Guidelines & Failure Modes
- **Idempotency & Safe Retries**: Ensure operations are idempotent by tagging mutations with unique correlation IDs and deduplication keys.
- **Circuit Breakers & Timeouts**: Enforce strict connection and socket timeouts on all network calls; trip circuit breakers if downstream errors exceed 50% over a 30-second window.
- **Rollback Checkpoints**: Always maintain backward compatibility and automated rollback scripts to recover safely without data corruption.

## Security & Architecture Checklist
- [ ] Are all cross-system calls authenticated via mutual TLS (mTLS) with short-lived tokens?
- [ ] Is asynchronous data replication verified using automated continuous reconciliation?
- [ ] Are non-transient message failures isolated to a Dead Letter Queue with operational alerting?
