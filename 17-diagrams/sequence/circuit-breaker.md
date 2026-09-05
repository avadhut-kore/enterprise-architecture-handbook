# Circuit Breaker & Retry Sequence Diagram

Illustrates client resilience using exponential backoff retry and transitioning to an **Open Circuit** state when downstream failures exceed thresholds.

```mermaid
sequenceDiagram
    autonumber
    participant Client as Order Service
    participant CB as Circuit Breaker (Resilience4j)
    participant PaymentAPI as Third-Party Payment API

    Note over Client,CB: State: CLOSED (Normal Operation)
    Client->>CB: Execute Call (Authorize Payment)
    CB->>PaymentAPI: POST /authorize
    PaymentAPI-->>CB: 504 Gateway Timeout
    CB-->>Client: Request Failed (Attempt 1)

    Note over Client: Exponential Backoff (Wait 100ms)
    Client->>CB: Execute Call (Retry Attempt 2)
    CB->>PaymentAPI: POST /authorize
    PaymentAPI-->>CB: 504 Gateway Timeout
    CB-->>Client: Request Failed (Attempt 2)

    Note over Client: Exponential Backoff (Wait 200ms)
    Client->>CB: Execute Call (Retry Attempt 3)
    CB->>PaymentAPI: POST /authorize
    PaymentAPI-->>CB: 504 Gateway Timeout
    CB->>CB: Failure Rate Exceeded (80% > Threshold 50%)
    Note over CB: Circuit Transitions to: OPEN
    CB-->>Client: Request Failed (Max Retries Exceeded)

    Note over Client,PaymentAPI: Subsequent Requests (Fast Fail)
    Client->>CB: Execute Call (New Order Payment)
    CB-->>Client: 503 CallNotPermittedException (Circuit OPEN - No Network Call)

    Note over CB: Sleep Window Expired (Wait 60s)
    Note over CB: Circuit Transitions to: HALF-OPEN
    Client->>CB: Probe Call (Authorize Payment)
    CB->>PaymentAPI: POST /authorize (Probe)
    PaymentAPI-->>CB: 200 OK (Payment Service Recovered)
    CB->>CB: Probe Succeeded
    Note over CB: Circuit Transitions to: CLOSED (Healed)
    CB-->>Client: 200 OK
```
