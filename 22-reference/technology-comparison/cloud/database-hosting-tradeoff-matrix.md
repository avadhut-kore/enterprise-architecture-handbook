# Technology Comparison: Database Hosting Trade-Off Matrix

## Executive Summary
This reference matrix evaluates the architectural trade-offs between managed cloud database vs self-managed on iaas.

---

## Architectural Comparison Matrix

| Dimension | Managed Cloud DB (Aurora / Azure SQL) | Self-Managed on EC2 / K8s |
| :--- | :--- | :--- |
| **Setup & Provisioning** | Minutes via Terraform / Console | Days (OS, disk partitioning, clustering) |
| **Patching & Maintenance**| Automated zero-downtime OS/engine updates | Manual scheduling and execution |
| **High Availability** | 1-Click Multi-AZ replication & failover | Complex manual clustering and sentinels |
| **Total Cost of Ownership**| Higher nominal infrastructure fee, ZERO SRE toil| Lower nominal cloud fee, $500k+ in SRE labor |
