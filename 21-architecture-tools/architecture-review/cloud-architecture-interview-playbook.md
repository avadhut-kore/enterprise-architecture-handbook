# Cloud Architecture Interview & Review Playbook

## Executive Summary

This playbook contains structured architectural answers to 14 high-stakes enterprise cloud system design interview questions. Every scenario follows the required architectural reasoning sequence:
$$\text{Requirements} \rightarrow \text{Constraints} \rightarrow \text{NFRs} \rightarrow \text{Options} \rightarrow \text{Trade-offs} \rightarrow \text{Decision} \rightarrow \text{Failure Modes} \rightarrow \text{Cost}$$

---

## 1. Design a Globally Available, Resilient API Platform
- **Requirements**: Sub-50ms latency for global users; survive regional cloud datacenter catastrophe.
- **NFRs**: 99.999% availability SLA, sub-minute RTO, near-zero RPO.
- **Architecture**: Global Anycast IP routing (Cloud Armor / AWS Global Accelerator) terminating at edge PoPs. Traffic directed to multi-region compute clusters (GKE / EKS) backed by Google Cloud Spanner or Aurora Global Database with asynchronous replication. Local read queries served by regional Redis clusters.
- **Trade-off**: High infrastructure cost and cross-region egress fees accepted to satisfy the 99.999% uptime mandate.

## 2. Kubernetes vs Serverless Decision for a High-Growth FinTech
- **Context**: 25 engineers building a high-growth consumer payment API.
- **Decision**: Adopt **Serverless Containers (Google Cloud Run / AWS ECS Fargate)**. Reject self-managed Kubernetes.
- **Rationale**: 25 developers cannot afford the operational tax of K8s cluster upgrades, CNI networking, and etcd maintenance. Cloud Run provides standard Docker packaging, sub-5 second autoscaling, and zero server maintenance, allowing the team to focus 100% of capacity on business payment features.

## 3. Migrate a 14 TB On-Premises Oracle Database to Cloud with Zero Downtime
- **Architecture**: Convert schema using AWS Schema Conversion Tool (SCT) to Amazon Aurora PostgreSQL. Seed initial baseline data via AWS Snowball. Establish continuous Change Data Capture (CDC) replication using AWS DMS.
- **Cutover & Rollback**: Once replication lag is < 2 seconds, enter a 5-minute maintenance window. Reconfigure DMS for **Reverse Replication** (Aurora back to on-prem Oracle). Promote Aurora to primary. If an unrecoverable bug emerges post-cutover, fail back to Oracle with zero data loss.

## 4. Design an Enterprise Multi-Account Landing Zone (150 Accounts)
- **Architecture**: AWS Control Tower with AWS Organizations. OUs partitioned into Core (Security, Log Archive, Network Transit), Workloads (Prod, Non-Prod per domain), and Sandbox.
- **Guardrails**: Service Control Policies (SCPs) deny root user usage, block public S3 buckets, enforce encryption at rest, and mandate `CostCenter` resource tags. Centralized inspection VPC handles all egress.

## 5. Slashing Cloud Invoices by 45% (FinOps Turnaround)
- **Actions**:
  1. Commit steady-state compute baseline to 3-Year Compute Savings Plans (66% discount).
  2. Implement S3 Intelligent-Tiering to eliminate cold storage spend.
  3. Migrate compute instances from x86 generation 5 (`m5`) to Graviton3 (`m7g`), delivering 40% better price-performance.
  4. Deploy automated nightly Lambda cleaners to snapshot and delete unattached EBS volumes and idle dev/test clusters.
