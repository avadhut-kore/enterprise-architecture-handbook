# Zero-Downtime Deployment Strategies: Rolling, Blue/Green & Canary

## Executive Summary

Selecting a deployment strategy balances **infrastructure cost**, **rollback speed**, and **backward compatibility**.

---

## 1. Progressive Canary Delivery Architecture

```mermaid
graph LR
    Client[Production Traffic] --> Router[Argo Rollouts / Service Mesh Router]
    Router -->|90% Traffic| V1[Version 1 Fleet]
    Router -->|10% Traffic| V2[Version 2 Canary]

    V2 --> Prometheus[Prometheus Analysis: Latency & Error Rate]
    Prometheus --> Gate{Meets SLO Error Budget?}
    Gate -->|Yes| Advance[Advance Canary: 10% -> 25% -> 50% -> 100%]
    Gate -->|No| AutoRollback[ABORT & INSTANT ROLLBACK TO 100% V1!]
```

---

## 2. Strategy Trade-Offs

- **Rolling Updates**: Zero additional infrastructure cost, but rollbacks are slow and transient version mismatches (V1 and V2 running simultaneously) are guaranteed.
- **Blue/Green Deployments**: Instantaneous rollback (switch load balancer target), but requires doubling infrastructure capacity during deployment.
- **Canary Deployments**: Minimum blast radius; automated statistical validation prevents catastrophic regressions from reaching the broader customer base.
