# Mapping HL7 v2 Segments to Modern JSON and FHIR

## 1. Normalization Pipeline
1. Ingest raw MLLP socket packet.
2. Strip MLLP framing bytes (`0x0B`, `0x1C`, `0x0D`).
3. Parse pipe-delimited segments into an Abstract Syntax Tree (AST).
4. Map segments to target FHIR resources (`PID` -> `Patient`, `OBR/OBX` -> `DiagnosticReport`/`Observation`).
5. Emit normalized JSON payload to Kafka.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
