# The Strangler Fig Pattern in Enterprise Modernization

## 1. Step-by-Step Modernization Lifecycle
1. **Intercept**: Route all incoming traffic through a facade routing gateway.
2. **Carve Out**: Implement a single vertical domain slice in modern cloud microservices.
3. **Shadow Run**: Call both legacy and cloud services, comparing output for consistency.
4. **Switch**: Cut traffic over to the cloud service; decommission legacy routine.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
