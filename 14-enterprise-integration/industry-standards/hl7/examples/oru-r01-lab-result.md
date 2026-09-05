# Implementation Example: HL7 v2 ORU^R01 Lab Result Message

## 1. Production Raw HL7 v2 Message
```text
MSH|^~\&|LAB_SYS|COMMUNITY_HOSP|EHR_CORE|HEALTH_SYS|20260905120000||ORU^R01|MSG20260905001|P|2.5.1
PID|1||MRN881920^^^HOSP||DOE^JANE^E||19840615|F|||123 ELM ST^^METROPOLIS^IL^60601
PV1|1|I|3W^302^1|E|||1234^WELBY^MARCUS^^DR|||||||||||V10029
OBR|1|ORD9912|LAB8821|883-9^ABO GROUP^LN|||20260905113000|||||||||1234^WELBY^MARCUS^^DR
OBX|1|ST|883-9^ABO GROUP^LN||A POSITIVE||||||F|||20260905114500
```

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
