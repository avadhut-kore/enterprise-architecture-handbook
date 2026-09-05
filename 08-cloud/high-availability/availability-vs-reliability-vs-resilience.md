# Availability vs Reliability vs Resilience vs Disaster Recovery

## Executive Summary

Enterprise architects must use precise engineering terminology. Conflating **Availability**, **Reliability**, **Resilience**, and **Disaster Recovery** leads to flawed NFR specifications and misallocated infrastructure budgets.

---

## 1. Architectural Taxonomy

```mermaid
graph TD
    Taxonomy[System Dependability Taxonomy]
    Taxonomy --> Avail[1. Availability: Proportion of time system is functional (Uptime %)]
    Taxonomy --> Rel[2. Reliability: Probability of performing error-free for a time period (MTBF)]
    Taxonomy --> Res[3. Resilience: Ability to absorb, adapt to, and recover from failures (MTTR)]
    Taxonomy --> DR[4. Disaster Recovery: Re-establishing operations after catastrophic events (RTO/RPO)]
```

---

## 2. Comparative Engineering Definitions

| Attribute | Mathematical / Engineering Definition | Primary Architectural Mechanism | Example Scenario |
| :--- | :--- | :--- | :--- |
| **Availability** | $\text{Uptime} / (\text{Uptime} + \text{Downtime}) \times 100$ | Redundant active compute fleets, Multi-AZ load balancing | A system maintains 99.99% uptime over a 30-day window. |
| **Reliability** | Mean Time Between Failures ($\text{MTBF}$) | Defensive coding, input validation, circuit breakers | An API processes 50 million consecutive transactions without a single 5xx error. |
| **Resilience** | Mean Time To Recovery ($\text{MTTR}$) | Automated self-healing, graceful degradation, bulkheads | An entire data center loses power; the system shifts traffic in 15 seconds without user impact. |
| **Disaster Recovery** | Recovery Time Objective ($\text{RTO}$) & Recovery Point Objective ($\text{RPO}$) | Out-of-region asynchronous data replication, cold/warm secondary sites | A hurricane destroys an entire AWS region; operations resume in secondary region within 1 hour. |
