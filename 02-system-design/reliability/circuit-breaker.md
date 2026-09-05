# Circuit Breaker Pattern

## 1. Purpose & States
The Circuit Breaker pattern (Michael Nygard) prevents an application from repeatedly attempting an operation that is almost certain to fail, saving CPU threads and preventing cascading failure across the enterprise.

```mermaid
stateDiagram-v2
    [*] --> Closed
    
    Closed --> Open : Failure Rate > 50% in 10s Window
    Open --> HalfOpen : Sleep Window Elapsed (e.g., 30s)
    
    HalfOpen --> Closed : Trial Requests Succeed (100% Success)
    HalfOpen --> Open : Any Trial Request Fails!
    
    note right of Closed : Traffic passes through normally.
    note right of Open : Requests fail fast immediately with fallback!
    note right of HalfOpen : Limited trial requests allowed to test downstream vitality.
```

---

## 2. Configuration Parameters (Resilience4j / Envoy Standard)
* **Failure Rate Threshold**: $50\%$ (if $50\%$ of calls fail over the evaluation window, trip to OPEN).
* **Slow Call Rate Threshold**: Trip to OPEN if $>50\%$ of calls exceed $2000\text{ ms}$.
* **Sliding Window Size**: 100 requests (or 10 seconds).
* **Wait Duration in Open State**: $30\text{ seconds}$ before transitioning to HALF-OPEN.
* **Permitted Number of Calls in Half-Open**: 10 trial requests.
