# GCP Planetary Database Architecture: Cloud Spanner

## Executive Summary

Google Cloud Spanner is the world's first globally distributed relational database service that delivers both **external consistency (serializability)** and **high availability (99.999% SLA)** at planetary scale, mathematically solving the distributed ACID problem via **TrueTime**.

---

## 1. TrueTime & External Consistency Architecture

```mermaid
graph TD
    subgraph Google Data Centers Worldwide
        GPS[GPS Atomic Clocks] <--> Satellites[GPS Satellite Constellation]
        Rubidium[Rubidium Atomic Oscillator Backup Clocks]
        TrueTime[TrueTime API: Provides Time [t.earliest, t.latest]]
        GPS --> TrueTime
        Rubidium --> TrueTime
    end

    TrueTime --> SpannerNodes[Spanner Paxos Leader Nodes Worldwide]
    SpannerNodes -->|Deterministic Commit Wait: Guarantees Global Ordering| ACID[(Global ACID State)]
```

---

## 2. Spanner Split Architecture & Scaling

- **Splits**: Spanner automatically partitions tables into chunks called "splits" based on row count and data size (typically 4 GB).
- **Paxos Groups**: Each split is replicated across zones/regions via an independent Paxos consensus group.
- **Zero Schema Maintenance Lockout**: Execute live DDL schema migrations (adding columns, creating secondary indexes) on multi-terabyte production tables without locking reads or writes.
- **When to Choose Spanner**: Global financial ledgers, global inventory reservations, or core banking systems requiring strict ACID consistency with multi-region active-active read/write access.
