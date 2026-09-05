# Enterprise Cloud Architecture Case Studies

## Executive Summary

This section contains 18 real-world enterprise cloud architecture case studies. Drawn from Fortune 500 migrations, global banking transformations, hyper-scale SaaS modernizations, and regulated infrastructure projects, each case study documents the complete decision-making journey across 15 structured sections.

---

## Catalog of Cloud Case Studies

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
