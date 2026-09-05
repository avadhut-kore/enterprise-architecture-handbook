# Multi-Region High Availability Architecture

## Executive Summary

Multi-region architectures distribute applications across distant geographic territories to survive catastrophic regional failures or satisfy strict data residency regulations.

---

## 1. Active-Active vs Active-Passive Multi-Region

```mermaid
graph TD
    subgraph Multi-Region Active-Passive [RECOMMENDED FOR OLTP]
        R1[Region A: Active Production 100% Traffic] --> DB1[(Primary ACID Database Master)]
        R2[Region B: Warm Standby Pilot Light] --> DB2[(Read-Only Replica: Async Replication Lag < 1s)]
        DB1 -.->|Asynchronous Replication| DB2
    end

    subgraph Multi-Region Active-Active [STATELESS / GLOBAL TABLES ONLY]
        R3[Region A: 50% Traffic] --> DynamoA[(DynamoDB Global Table A)]
        R4[Region B: 50% Traffic] --> DynamoB[(DynamoDB Global Table B)]
        DynamoA <==>|Bi-directional Eventual Consistency| DynamoB
    end
```

---

## 2. The Speed of Light Constraint
- Continental cross-region latency is bounded by physics ($60 - 80\text{ ms}$ round-trip time).
- Attempting synchronous cross-region commits stalls transactional databases. Multi-region architectures **must embrace asynchronous replication and eventual consistency**.
