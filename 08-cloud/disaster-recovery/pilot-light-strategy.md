# Pilot Light Disaster Recovery Strategy

## Executive Summary

In a **Pilot Light** architecture, the core data tier is continuously replicated to a secondary region in real time, while the compute tier (containers, virtual machines) is kept dormant or scaled to zero.

---

## 1. Pilot Light Architecture Blueprint

```mermaid
graph TD
    subgraph Primary Region
        AppProd[Production App Fleet: 50 Containers]
        MasterDB[(Primary Aurora Database)]
    end

    subgraph Secondary Region [Pilot Light: Core Data Active]
        StandbyDB[(Aurora Global DB Replica: Lag < 1s)]
        AppStandby[Compute Scaled to Zero Pods / Dormant]
    end

    MasterDB ==>|Continuous Asynchronous Storage Replication| StandbyDB

    Disaster[Disaster Triggered] --> Promote[1. Promote StandbyDB to Primary Master]
    Promote --> ScaleCompute[2. Terraform / Karpenter Scales AppStandby: 0 -> 50 Pods in 15 Mins]
    ScaleCompute --> CutoverDNS[3. Shift Route 53 Traffic to Secondary Region]
```

---

## 2. Performance Profile
- **RTO**: 30 to 60 minutes (time required to scale up container clusters and warm caches).
- **RPO**: Sub-second (continuous asynchronous storage replication).
- **Cost**: Moderate ($1.2\times - 1.3\times$ of primary infrastructure spend).
