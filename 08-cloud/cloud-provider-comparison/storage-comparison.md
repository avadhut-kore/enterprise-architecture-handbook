# Storage Architecture Comparison: AWS vs Azure vs GCP

## Executive Summary

Storage selection balances access latency, throughput, sharing requirements, durability, and cost optimization lifecycles.

---

## 1. Object Storage (S3 vs Blob vs GCS)

| Architectural Dimension | Amazon S3 | Azure Blob Storage | Google Cloud Storage (GCS) |
| :--- | :--- | :--- | :--- |
| **Global Consistency** | Strong Read-After-Write consistency | Strong Read-After-Write consistency | Strong Read-After-Write consistency |
| **Namespace Scope** | Globally unique across all AWS accounts | Unique per Storage Account (`account.blob.core.windows.net`) | Globally unique across all GCP projects |
| **Lifecycle Optimization**| S3 Intelligent-Tiering (Auto-moves based on access)| Blob Lifecycle Management (Rules-based) | **GCS Autoclass** (Moves down AND up without retrieval fees) |
| **Archive Retrieval** | S3 Glacier Flexible ($3-5\text{ hrs}$), Deep Archive ($12\text{ hrs}$) | Blob Archive ($15\text{ hrs}$) | GCS Archive ($< 1\text{ second}$ first-byte latency!) |
| **Compliance Immutability**| S3 Object Lock (WORM compliance) | Immutable Blob Storage with Legal Hold | GCS Bucket Lock (Retention policies) |

---

## 2. Block Storage (EBS vs Azure Managed Disks vs GCE Persistent Disks)

| Capability | AWS EBS (gp3 / io2) | Azure Managed Disks (Premium v2 / Ultra) | GCP Persistent Disks (PD-Balanced / Extreme) |
| :--- | :--- | :--- | :--- |
| **Decoupled IOPS/Throughput**| Yes (gp3 decouples baseline IOPS from volume size) | Yes (Premium SSD v2 allows independent provisioning) | Yes (PD-Extreme allows custom IOPS scaling) |
| **Multi-Attach Support** | Supported on io1/io2 (Clustered file systems) | Supported on Premium/Ultra SSD (Clustered SQL) | Supported (Read-only multi-attach across VMs) |
| **Cross-Zone Availability** | Strictly single-AZ; requires snapshot to replicate | Zone-Redundant Disks (ZRS) available! | Regional Persistent Disk (Synchronous 2-zone replication!) |
