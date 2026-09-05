# Circuit Breaker Architecture in Enterprise Integration

## 1. Finite State Machine (FSM)

```
        ┌──────────────────────────────────────────────┐
        │                                              │
        ▼                                              │
   ┌─────────┐   Failure Threshold Exceeded (e.g. 50%) ┌──────────┐
   │ CLOSED  │────────────────────────────────────────>│   OPEN   │
   └─────────┘                                         └──────────┘
        ▲                                              │
        │ Success Rate >= 90%        Cooldown Timeout  │
        │                            Elapsed           ▼
   ┌───────────┐                     (e.g. 30s)    ┌───────────┐
   │ HALF-OPEN │<──────────────────────────────────│ HALF-OPEN │
   └───────────┘    Test with Probe Traffic        └───────────┘
        │
        │ Probe Fails
        └──────────────────────────────────────────────>
```

## 2. Circuit Breaker Metrics and Configurations
- **Sliding Window Size**: Number of calls (count-based, e.g., 100 calls) or duration (time-based, e.g., 60s) evaluated.
- **Failure Rate Threshold**: Percentage of failed or slow calls triggering the circuit trip (typically 50%).
- **Slow Call Duration**: Calls exceeding this latency threshold (e.g., 2000ms) are categorized as failures.
- **Wait Duration in Open State**: Cool-off window before attempting probe traffic in HALF-OPEN state (typically 10s - 30s).
- **Permitted Calls in Half-Open**: Number of probe calls allowed to evaluate downstream health (typically 5 - 10 calls).

## 3. Fallback Strategies
When the circuit trips `OPEN`, the integration layer must execute an architectural fallback:
1. **Cache Fallback**: Return the last known good response from a local Redis cache.
2. **Graceful Degradation**: Return a partial response with non-critical components omitted.
3. **Asynchronous Stashing**: Save the mutation request to a durable local dead-letter queue or outbox table for delayed processing.
4. **Fast Fail**: Immediately return `HTTP 503 Service Unavailable` with a descriptive message, relieving pressure on the network.
