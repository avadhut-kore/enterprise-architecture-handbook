# Cloud & Data Migration Forensic Case Studies

## 1. Domain Overview & Architectural Scope
Enterprise migrations—moving from on-premises datacenters to public cloud, evacuating legacy SAN arrays, or refactoring proprietary databases (Oracle/SQL Server to PostgreSQL)—represent some of the highest-risk endeavors in software engineering. When migrations fail, the causes are rarely raw network throughput; they are architectural traps: buried PL/SQL stored procedure dependencies, flawed cutover sequencing that crosses the Point-of-No-Return without validation, silent Change Data Capture (CDC) replication drift, and unanticipated cloud egress networking fees.

This category presents rigorous forensic investigations of complex enterprise migrations, examining both high-profile failures and an industrialized migration factory success.

---

## 2. Case Study Portfolio Index

| Case Study ID | Title | Primary Architecture Issue | Systemic Consequence |
| :--- | :--- | :--- | :--- |
| **[`cs-mig-01`](cs-mig-01-oracle-to-postgres-stored-proc-trap.md)** | **Oracle to PostgreSQL Stored Procedure Trap** | 45,000 Lines of proprietary PL/SQL logic | 18-Month project delay, $22M budget overrun, and failed automated translation |
| **[`cs-mig-02`](cs-mig-02-point-of-no-return-cutover-disaster.md)** | **Point-of-No-Return Cutover Collapse** | Premature database DNS switch without rollback sync | 36-Hour airline flight cancellation crisis & stranded passengers |
| **[`cs-mig-03`](cs-mig-03-zero-downtime-cdc-replication-lag-drift.md)** | **CDC Replication Lag & Silent Data Drift** | Debezium CDC buffer overflow under peak write load | 84,000 Corrupted customer balances & emergency 48-hour manual rollback |
| **[`cs-mig-04`](cs-mig-04-cloud-lift-and-shift-egress-shock.md)** | **Lift-and-Shift Cloud Egress Shock** | Hybrid architecture splitting compute and database across cloud boundary | $450,000/month surprise AWS DirectConnect egress bills |
| **[`cs-mig-05`](cs-mig-05-failed-san-storage-data-evacuation.md)** | **Datacenter SAN Storage Evacuation Collapse** | Block storage IOPS mismatch during VM live migration | Critical healthcare imaging system freeze & emergency rollback |
| **[`cs-mig-06`](cs-mig-06-successful-800-workload-factory-migration.md)** | **Industrialized Migration Factory (Success)** | Repeatable wave planning, automated landing zones & dual-run | 800 Workloads migrated in 12 months with zero P1 incidents and 28% TCO savings |
