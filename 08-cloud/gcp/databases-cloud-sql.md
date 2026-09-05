# GCP Relational Databases: Cloud SQL

## Executive Summary

Google Cloud SQL is a fully managed relational database service supporting PostgreSQL, MySQL, and SQL Server.

---

## 1. High-Availability Architecture

```mermaid
graph TD
    subgraph Primary Zone: us-central1-a
        App[Microservice Fleet] --> Master[Cloud SQL Primary]
        Master --> StorageM[(Persistent Disk: Synchronous Replicated)]
    end

    subgraph Secondary Zone: us-central1-b
        Standby[Cloud SQL Standby]
        StorageS[(Persistent Disk: Standby Mirror)]
    end

    StorageM <==>|Synchronous Block-Level Mirroring| StorageS
    Master -.->|Automated Failover < 60s| Standby
```

---

## 2. Cloud SQL Enterprise Plus Edition

For mission-critical enterprise workloads, select **Enterprise Plus**:
- **Data Cache**: Utilizes local NVMe SSDs to automatically cache hot relational data pages, delivering up to **3x read throughput** and reducing latency by 50%.
- **Maintenance Downtime**: Minimizes planned maintenance downtime to sub-10 seconds using fast failover orchestration.
- **99.99% Availability SLA**: Guaranteed multi-zone availability including scheduled maintenance windows.
