# Chaos Engineering & Resilience Testing

## 1. Principles of Chaos Engineering
Chaos Engineering (pioneered by Netflix Chaos Monkey) is the discipline of experimenting on a system in production to build confidence in its capability to withstand turbulent and unexpected conditions.

```mermaid
flowchart TD
    Hypothesis[1. Formulate Hypothesis: 'If Redis fails, DB will handle degraded load without 500 errors']
    Hypothesis --> Blast[2. Define Minimal Blast Radius: 5% of Canary Traffic]
    Blast --> Inject[3. Inject Fault via Chaos Mesh / LitmusChaos]
    Inject --> Observe[4. Observe Golden Signals: Did SLO Breach?]
    Observe --> Fix[5. Identify Weakness & Implement Hardening]
```

---

## 2. Core Chaos Injection Scenarios

| Experiment Type | Synthetic Fault Injected | Expected Architectural Behavior |
| :--- | :--- | :--- |
| **Pod / Instance Chaos** | Kill 20% of random microservice pods | Load balancer evicts dead pods in $<2\text{s}$; zero user 5xx errors. |
| **Network Latency** | Inject $+2000\text{ ms}$ latency to payment gateway | Circuit breaker trips; fallback returns graceful degradation. |
| **Packet Corruption** | Drop $15\%$ of packets across Availability Zones | TCP retransmissions handle traffic without connection resets. |
| **Database Failover** | Force primary database crash (`kill -9`) | Automated replica promotion succeeds in $<30\text{s}$ with zero data loss. |
