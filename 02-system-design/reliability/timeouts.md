# Timeout Architecture & Cascading Failures

## 1. The Peril of Missing Timeouts
In distributed systems, **a slow dependency is infinitely more dangerous than a dead dependency**.
* A dead dependency fails fast with `ECONNREFUSED` ($<1\text{ ms}$).
* A slow dependency holds open client connections for minutes. Upstream thread pools exhaust waiting, cascading backwards until the entire enterprise platform freezes.

```mermaid
flowchart LR
    Client[Incoming Request] --> SvcA[Service A: 200 Threads]
    SvcA -->|HTTP Call - NO TIMEOUT!| SvcB[Service B: Slow Third-Party API]
    SvcB -.->|Hangs for 60 seconds| SvcA
    Note over SvcA: All 200 Threads Blocked! Svc A Collapses!
```

---

## 2. Sizing Timeouts Mathematically
Timeouts must be sized according to empirical latency distributions:
$$T_{\text{timeout}} = T_{p99.9} + \text{Safety Buffer Margin}$$
* Set timeouts at **3Ã— the typical $p99$ response time**. If downstream $p99$ is $20\text{ ms}$, set timeout to $60\text{--}80\text{ ms}$.
* Never rely on runtime defaults (standard Java HTTP client defaults to infinite timeout!).

---

## 3. Deadline Propagation (gRPC / W3C Context)
Propagate the global timeout budget across microservice hops. If the frontend client allocates a $500\text{ ms}$ budget and $400\text{ ms}$ has already elapsed, downstream services receive a remaining budget of $100\text{ ms}$. If time expires, in-flight work is cancelled immediately.
