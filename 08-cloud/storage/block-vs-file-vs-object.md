# Block vs File vs Object Storage: Comparative Architecture

## Executive Summary

Selecting the incorrect storage abstraction results in either severe performance bottlenecks or exorbitant operational costs.

---

## 1. Deep Architectural Comparison

| Dimension | Block Storage (EBS / Azure Disk) | File Storage (EFS / Azure Files) | Object Storage (S3 / Blob / GCS) |
| :--- | :--- | :--- | :--- |
| **Primary Protocol** | SCSI, NVMe over Fabric (NVMe-oF) | NFS v4.1, SMB 3.0 | HTTP / HTTPS REST API |
| **Latency Profile** | **Sub-millisecond ($0.1 - 2\text{ ms}$)** | Low ($2 - 10\text{ ms}$) | High ($50 - 150\text{ ms}$ first-byte) |
| **Throughput Ceiling** | Up to $4\text{ GB/s}$ per volume | Up to $10\text{ GB/s}$ (Scales with storage) | **Virtually Unlimited (Scales per prefix)**|
| **Multi-Host Sharing** | Single VM attach (except clustered multi-attach)| **Shared by thousands of concurrent VMs/Pods**| Shared globally by any authorized HTTP client |
| **File Modification** | In-place byte-level modification | In-place byte-level modification | **Atomic Replacement Only (Write entire object)**|
| **Cost per GB/Month** | High ($\$0.08 - \$0.15/\text{GB}$) | Moderate ($\$0.15 - \$0.30/\text{GB}$) | **Ultra-Low ($\$0.00099 - \$0.023/\text{GB}$)** |
| **Primary Workloads** | Relational DBs (PostgreSQL, Oracle), OS Disks | Legacy CMS, legacy shared app shares, container PVs| Big Data lakes, document archives, media assets |
