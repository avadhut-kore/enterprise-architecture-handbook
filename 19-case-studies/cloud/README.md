# Enterprise Cloud Architecture Case Studies & Outage Post-Mortems

## Executive Summary

This directory contains a comprehensive portfolio of **Enterprise Cloud Architecture Case Studies**, spanning both large-scale cloud migrations/transformations and deep-dive forensic post-mortems of mission-critical cloud outages. Drawn from Fortune 500 enterprises, hyper-scale cloud providers, and global retail/banking platforms, each case study documents the complete decision-making journey, failure mechanisms, and permanent architectural remediations.

---

## 1. Cloud Outage Forensic Post-Mortems (P0 Incident Analyses)

Deep-dive forensic post-mortems analyzing major cloud availability breakdowns, network partitions, identity control-plane deadlocks, and multi-cloud routing loops.

| Incident ID | Title | Primary Architectural Breakdown | Financial & Operational Impact |
| :--- | :--- | :--- | :--- |
| **[`cs-cloud-01`](cs-cloud-01-global-bgp-routing-leak.md)** | **Global BGP Anycast Route Leak & Multi-Region Black Hole** | BGP community tag omitted in automation; global transit overload | $42M direct SLA breach penalties; 42 cloud regions offline |
| **[`cs-cloud-02`](cs-cloud-02-iam-policy-lockout-blast-radius.md)** | **Corrupted Global IAM Policy Push & Control Plane Lockout** | Corrupted AWS SCP applied to Root OU; administrative deadlock | $65M lost revenue; 450 AWS accounts deadlocked for 14 hours |
| **[`cs-cloud-03`](cs-cloud-03-multi-az-network-partition-cascade.md)** | **Multi-AZ Network Partition Cascade & Synchronous Lockup** | Cross-AZ synchronous dependencies; packet loss in one AZ froze all 3 AZs | $18M e-commerce checkout loss during peak shopping weekend |
| **[`cs-cloud-04`](cs-cloud-04-wildcard-tls-cert-expiration-blackout.md)** | **Wildcard Edge TLS Certificate Expiration & Mobile Blackout** | Manually managed wildcard certificate expired at 00:00 UTC | $11M operational loss; 6 Million mobile banking users locked out |
| **[`cs-cloud-05`](cs-cloud-05-multi-region-split-brain-divergence.md)** | **Multi-Region Active-Active Database Divergence & Split-Brain** | Multi-master LWW with NTP clock drift during replication lag | $9.5M flight rebooking and hotel compensations; 14,000 double-booked seats |
| **[`cs-cloud-06`](cs-cloud-06-multi-cloud-failover-dns-routing-loop.md)** | **Multi-Cloud Failover DNS Routing Loop & Cold Standby Collapse** | Un-warmed 5% Azure standby crushed by 45k QPS failover | $24M in lost flight bookings; 11-hour oscillating DNS death loop |

---

## 2. Enterprise Cloud Transformation Case Studies (18 Real-World Migrations)

Comprehensive case studies documenting strategic cloud migrations, landing zones, FinOps turnarounds, and compliance enclaves.

| # | Case Study Title | Transformation Scope | Key Architectural Technologies |
| :-: | :--- | :--- | :--- |
| **01** | **[On-Premises Data Center to AWS](01-on-premises-to-aws.md)** | Full Datacenter Eviction | AWS Organizations, Direct Connect, MGN, Aurora, EKS |
| **02** | **[On-Premises Windows to Azure](02-on-premises-to-azure.md)** | Microsoft Enterprise Migration | Azure Landing Zones, ExpressRoute, Azure SQL, Entra ID |
| **03** | **[On-Premises Analytics to GCP](03-on-premises-to-gcp.md)** | Planetary Big Data Migration | Google BigQuery, Cloud Interconnect, GKE, Cloud Storage |
| **04** | **[Monolith to Cloud Microservices](04-monolith-to-cloud.md)** | Strangler Fig Decomposition | Envoy Proxy, Domain Decomposition, Kafka, Cloud Run |
| **05** | **[VM Application to Containers](05-vm-to-containers.md)** | Replatforming to Containers | Docker Multi-Stage, AWS ECS Fargate, CI/CD Pipelines |
| **06** | **[Containers to Kubernetes](06-containers-to-kubernetes.md)** | Complex Platform Scaling | Amazon EKS, Helm, Ingress-NGINX, Horizontal Autoscaling |
| **07** | **[Self-Hosted to Managed K8s](07-kubernetes-to-managed-kubernetes.md)**| Eliminating K8s Ops Toil | DIY K8s on EC2 to GKE Autopilot, Karpenter, OTel |
| **08** | **[Traditional App to Serverless](08-traditional-to-serverless.md)** | Event-Driven Refactoring | Java Spring Boot Monolith to AWS Lambda SnapStart + DynamoDB |
| **09** | **[Single-Region to Multi-Region](09-single-region-to-multi-region.md)** | High-Resiliency Transformation | Single-AZ PostgreSQL to Multi-Region Aurora Global DB |
| **10** | **[Single-Cloud to Hybrid Cloud](10-single-cloud-to-hybrid.md)** | Mainframe Latency Integration | AWS Direct Connect, Hybrid DNS, Anti-Corruption Layer |
| **11** | **[Hybrid to Cloud-First Enterprise](11-hybrid-to-cloud-first.md)** | Complete Datacenter Retirement | Replatforming Core Ledgers, Decommissioning Legacy SANs |
| **12** | **[Cloud Cost Optimization (FinOps)](12-cloud-cost-optimization.md)**| Slashing 45% of Cloud Spend | Right-Sizing, Savings Plans, Egress Optimization, S3 Tiering |
| **13** | **[Enterprise Landing Zone Build](13-enterprise-landing-zone.md)** | Multi-Account Foundation | AWS Control Tower, 120 Accounts, Transit Gateway, SCPs |
| **14** | **[Regulated Workload Migration](14-regulated-workload-migration.md)** | PCI-DSS / HIPAA Compliance | Dedicated Enclaves, Cloud HSM, Air-Gapped WORM Logging |
| **15** | **[Legacy Database Migration](15-legacy-database-migration.md)** | 14 TB Oracle to Aurora PG | AWS SCT, DMS CDC Replication, Dual-Write Cutover |
| **16** | **[Large-Scale Data Migration](16-large-scale-data-migration.md)** | 8 PB Hadoop to Cloud Lake | AWS Snowball Edge, Apache Iceberg, Apache Parquet |
| **17** | **[Cloud DR Implementation](17-cloud-dr-implementation.md)** | Sub-15 Minute Cross-Region DR | Pilot Light to Warm Standby, Automated Route 53 ARC |
| **18** | **[Multi-Tenant SaaS Architecture](18-multi-tenant-saas-cloud.md)** | B2B SaaS Tenant Isolation | Pooled Compute on EKS, Siloed DB per Enterprise Client |
