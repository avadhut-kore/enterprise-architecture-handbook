# High-Volume Duplicate Prevention Patterns

## 1. Distributed In-Flight Locking
To prevent race conditions where two identical payment requests arrive within milliseconds:
```python
import redis

r = redis.Redis(host='redis-cluster.internal')

def acquire_payment_lock(idempotency_key: str) -> bool:
    # Set NX with a 60-second TTL
    return r.set(f"lock:payment:{idempotency_key}", "LOCKED", nx=True, ex=60)
```

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
