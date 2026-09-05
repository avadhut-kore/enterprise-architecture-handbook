# Real-Time vs. Batch Data Synchronization Patterns

## 1. Synchronization Matrix

| Pattern | Trigger | Mechanism | Latency | Volume |
| :--- | :--- | :--- | :--- | :--- |
| **Real-Time** | User saves record | Platform Event / Apex Callout | $< 1	ext{s}$ | Low (< 10k/day) |
| **Near Real-Time** | DB Commit | Change Data Capture (CDC) | 1s - 5s | Medium (< 1M/day) |
| **Batch** | Scheduled night | Bulk API 2.0 / ETL Tool | Hours | Massive (> 1M/day) |

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
