# Integration Architecture: HL7 v2 and FHIR Conversion

## 1. MLLP to FHIR Event Bridge
Hospital bedside monitors and EHRs transmit raw HL7 v2 pipes-and-hats messages over TCP sockets using Minimal Lower Layer Protocol (MLLP):
1. Ingress MLLP gateway buffers message in Kafka topic (`hl7v2.inbound`).
2. Gateway immediately responds with an MLLP `ACK` commit.
3. Transformation worker maps HL7 `PID` segment to FHIR `Patient` resource and `OBX` segment to FHIR `Observation`.
4. Upserts to FHIR CDR via transactional bundle.

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
