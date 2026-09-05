# COBOL Copybooks and EBCDIC Data Transformation

## 1. The EBCDIC Challenge
Mainframes do not store text in ASCII or UTF-8; they use **EBCDIC** (Extended Binary Coded Decimal Interchange Code) and packed decimal formats (`COMP-3`):
- `PIC 9(7)V99 COMP-3`: Encodes numbers in 4-bit nibbles with a trailing sign nibble.
- Integration engines must use specialized binary decoders (e.g., JRecord, Camel COBOL) to unpack binary EBCDIC records into JSON numbers.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
