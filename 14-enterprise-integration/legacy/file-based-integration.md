# File-Based Integration and Managed File Transfer (MFT)

## 1. Managed File Transfer Architecture
Mainframes generate multi-gigabyte flat files overnight:
- **MFT Engine**: Coordinates SFTP / Connect:Direct transmission, file integrity verification (MD5/SHA-256), and PGP encryption.
- **Chunking Pipeline**: Splits large flat files into streaming micro-batches for parallel cloud ingestion.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
