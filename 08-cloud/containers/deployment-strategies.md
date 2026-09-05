# Container Deployment Strategies

## Executive Summary

Selecting a container deployment strategy balances **downtime tolerance**, **resource cost**, and **blast radius risk**.

---

## 1. Deployment Strategies Comparison

```mermaid
graph TD
    subgraph Recreate: Downtime Required / Minimal Cost
        Old1[Version 1] --> Kill[Terminate V1 Completely]
        Kill --> Start1[Start Version 2]
    end

    subgraph Rolling Update: Zero Downtime / Shared Capacity
        R1[V1 Instance A] --> ReplaceA[Replace with V2 Instance A]
        R2[V1 Instance B] --> ReplaceB[Replace with V2 Instance B]
    end

    subgraph Blue-Green: Zero Downtime / Instant Rollback / 2x Cost
        Blue[Blue Fleet: 100% Active Production V1]
        Green[Green Fleet: 100% Staged V2]
        Router[Load Balancer Router] ==>|Instant Switch| Green
    end

    subgraph Canary: Minimum Blast Radius / Incremental Validation
        CanaryRouter[Load Balancer] -->|95% Traffic| MainFleet[V1 Fleet]
        CanaryRouter -->|5% Traffic| CanaryPod[V2 Canary Pod]
    end
```

---

## 2. Comparative Decision Matrix

| Strategy | Downtime | Infrastructure Cost Multiplier | Rollback Speed | Backward Compatibility Requirement |
| :--- | :---: | :---: | :---: | :---: |
| **Recreate** | Yes ($1 - 5\text{ mins}$) | $1.0\times$ | Slow (Re-pull and restart) | Not required |
| **Rolling Update** | Zero | $1.25\times$ (maxSurge) | Moderate (Roll back pods sequentially) | **Mandatory** (V1 and V2 run concurrently) |
| **Blue/Green** | Zero | $2.0\times$ (Double capacity during deployment) | **Instantaneous** (Switch load balancer target) | **Mandatory** (Shared database during swap) |
| **Canary** | Zero | $1.1\times$ | Fast (Route traffic away from canary) | **Mandatory** |
