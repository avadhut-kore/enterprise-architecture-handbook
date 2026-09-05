# Serverless Cost Economics & The Crossover Curve

## Executive Summary

Serverless FaaS is billed strictly per invocation and per millisecond of compute time. While serverless is virtually free at low or unpredictable volumes, **at hyper-scale steady traffic, serverless unit costs diverge sharply from provisioned compute**.

---

## 1. The Financial Crossover Curve

```mermaid
graph LR
    subgraph Low / Spiky Traffic
        FreeTier[Low Traffic: 0 - 1M requests/mo] --> FaaSWins[Serverless FaaS is 90% Cheaper than Provisioned VMs]
    end

    subgraph The Crossover Point: ~10M to 50M requests/month sustained
        Cross[Crossover Point] --> Equal[FaaS Cost == Container / VM Cost]
    end

    subgraph Hyper-Scale Sustained Traffic
        HighScale[High Steady Traffic: > 100M requests/mo 24/7] --> VMSSWins[Managed Containers / Spot VMs are 70% Cheaper than FaaS]
    end
```

---

## 2. Architectural Cost Modeling Formula

$$\text{Monthly Cost}_{\text{FaaS}} = (\text{Requests} \times \text{Price}_{\text{req}}) + (\text{Requests} \times \text{Duration}_{\text{sec}} \times \text{Memory}_{\text{GB}} \times \text{Price}_{\text{GB-sec}})$$

$$\text{Monthly Cost}_{\text{Containers}} = (\text{Worker Nodes Count} \times \text{Hourly VM Rate} \times 730\text{ hrs}) + \text{Cluster Fee}$$

### SRE Rule of Thumb
- If a service processes continuous, high-concurrency requests 24 hours a day with $> 70\%$ sustained CPU utilization, migrating from Lambda to containerized fleets on EKS/Karpenter or ECS Fargate yields substantial financial savings.
