# Distributed Event Streaming: Apache Kafka & Redpanda

## 1. The Append-Only Immutable Log
Unlike message queues, event streaming platforms persist events in an immutable, partition-ordered log across a configurable retention window (e.g., 30 days or infinite):
- Multiple independent consumer groups read from the same topic at their own pace.
- Events can be replayed from any offset in the past for disaster recovery or bug remediation.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
