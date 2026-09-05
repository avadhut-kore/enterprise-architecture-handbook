# Anatomy of Critical HL7 Segments

## 1. Segment Overview
- **MSH (Message Header)**: Declares sender/receiver applications, facility, timestamp, and message type.
- **PID (Patient Identification)**: Name, MRN, date of birth, gender, address.
- **PV1 (Patient Visit)**: Hospital location, room, attending physician, admission type.
- **OBR (Observation Request)**: Order metadata, ordering clinician, specimen details.
- **OBX (Observation / Result)**: Numerical or textual test result, reference ranges, abnormal flags.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
