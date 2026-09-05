# Database Architecture Comparison: AWS vs Azure vs GCP

## Executive Summary

Data architectures range from traditional managed relational engines to planetary-scale globally distributed transactional ledgers.

---

## 1. Managed Relational & Cloud-Native SQL

| Capability | Amazon Aurora | Azure SQL Hyperscale | Google Cloud SQL / AlloyDB |
| :--- | :--- | :--- | :--- |
| **Engine Support** | PostgreSQL, MySQL | Microsoft SQL Server (T-SQL) | PostgreSQL, MySQL, SQL Server / AlloyDB |
| **Storage Architecture** | 6-way replicated log-structured shared storage | Distributed Page Servers + Log Service | Persistent Disk Mirroring / Log-based (AlloyDB) |
| **Maximum Volume Size** | 128 TB | 100 TB | 64 TB |
| **Global Disaster Recovery**| Aurora Global Database (Sub-second lag) | Auto-Failover Groups (Geo-Replication) | Cross-region read replicas |
| **Serverless Scaling** | Aurora Serverless v2 (Instant scaling by ACUs)| Serverless compute tier (Auto-pause/resume) | Autoscale CPU/Memory (Requires restart on standard) |

---

## 2. Globally Distributed & Planetary NoSQL

| Capability | Amazon DynamoDB | Azure Cosmos DB | Google Cloud Spanner |
| :--- | :--- | :--- | :--- |
| **Database Category** | Key-Value / Document NoSQL | Multi-Model NoSQL (Document, Graph, Key-Value)| **Planetary Distributed Relational (ACID)** |
| **Consistency Models** | Eventual or Strongly Consistent | **5 Tunable Consistency Levels** | **External Consistency (Strict Serializability)** |
| **Distributed Consensus** | Paxos per partition | Paxos consensus | **TrueTime API + Paxos Consensus** |
| **Multi-Region Writes** | Supported (Global Tables / Last-Writer-Wins)| Supported (Multi-region writes with conflict policy) | Supported natively across continental regions |
| **Availability SLA** | 99.999% (Global Tables) | 99.999% (Multi-region active writes) | 99.999% (Multi-region instances) |
