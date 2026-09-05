# Transactional Outbox Pattern

## 1. Solving the Dual-Write Problem
When an application must update a database and publish an event to Kafka:
```sql
-- Atomic local database transaction
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 'ACC-1';
  INSERT INTO outbox (id, event_type, payload) VALUES (uuid(), 'DEBITED', '{...}');
COMMIT;
-- CDC engine (Debezium) tails outbox table and streams events to Kafka
```
Guarantees events are published if and only if the database transaction commits.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
