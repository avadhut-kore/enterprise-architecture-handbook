# Database Cloud Migration: Zero-Downtime Replication & Cutover

## Executive Summary

Migrating multi-terabyte transactional databases to managed cloud engines (PostgreSQL, Aurora, Azure SQL) without business downtime requires **Change Data Capture (CDC)** replication.

---

## 1. CDC-Driven Zero-Downtime Migration Architecture

```mermaid
graph LR
    subgraph Source On-Premises DB
        SourceDB[(Production Oracle / SQL Server)] --> LogReader[Transaction Log Reader: WAL / Redo Logs]
    end

    subgraph Replication Engine
        LogReader ==> DMS[AWS Database Migration Service / Qlik Replicate]
    end

    subgraph Target Cloud DB
        DMS ==>|Continuous CDC Replication: Lag < 2s| TargetDB[(Target Aurora / Cloud SQL)]
    end

    Cutover[Cutover Window: 5 Mins] --> StopWrites[1. Stop Source App Writes]
    StopWrites --> CatchUp[2. DMS Applies Final In-Flight Transactions]
    CatchUp --> PointApp[3. Point Application Connection String to Target Cloud DB]
```

---

## 2. The Reverse Replication Safety Net
- During cutover, immediately configure **Reverse CDC Replication** from the target cloud database back to the on-premises database.
- If an unexpected critical bug emerges 6 hours post-cutover, traffic can be failed back to on-premises with **zero data loss**, because every transaction executed in the cloud was replicated back to on-prem.
