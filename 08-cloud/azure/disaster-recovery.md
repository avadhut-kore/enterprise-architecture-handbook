# Azure Disaster Recovery: Paired Regions and Resiliency Patterns

## Executive Summary

Designing disaster recovery on Azure leverages **Availability Zones (AZs)** for intra-region high availability and **Azure Paired Regions** for geographic disaster recovery.

---

## 1. Regional Resiliency Hierarchy

```mermaid
graph TD
    subgraph Primary Region: East US
        AZ1[AZ 1: Independent Power/Cooling]
        AZ2[AZ 2: Independent Power/Cooling]
        AZ3[AZ 3: Independent Power/Cooling]
        SQLPrimary[(Azure SQL Primary)]
    end

    subgraph Secondary Paired Region: West US
        SQLSecondary[(Azure SQL Auto-Failover Group)]
    end

    SQLPrimary -.->|Asynchronous Geo-Replication: Lag < 5s| SQLSecondary

    FrontDoor[Azure Front Door: Global Anycast Routing] ==> EastUS[Primary: East US]
    FrontDoor -.->|Automated Failover| WestUS[Secondary: West US]
```

---

## 2. Azure Paired Region Advantages

1. **Sequential Updates**: Azure never updates platform software in both paired regions simultaneously; updates roll out sequentially to prevent global patch-induced outages.
2. **Physical Separation**: Paired regions are separated by at least 300 miles to survive regional disasters (weather events, civil disruption).
3. **Data Residency**: Regional pairs reside within the same geopolitical tax and legal boundary (with the exception of Brazil South).
