# Chaos Engineering: Injecting Failure to Verify Resilience

## Executive Summary

Chaos engineering is the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production.

---

## 1. Chaos Experimentation Workflow

```mermaid
graph LR
    SteadyState[1. Define Steady State SLI: Error Rate < 0.1%] --> Hypo[2. Form Hypothesis: If AZ1 Dies, Traffic Reroutes in 15s with Zero 5xx Errors]
    Hypo --> Inject[3. Inject Failure: AWS FIS / Chaos Mesh Terminates All AZ1 Nodes]
    Inject --> Verify{Steady State Maintained?}
    Verify -->|Yes| Confirmed[Confidence Confirmed!]
    Verify -->|No: Outage Occurs| Fix[Identify Bug & Refactor Architecture]
```
