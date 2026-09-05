# Managed vs Self-Managed Infrastructure

## Executive Summary

Architects frequently face the decision of whether to adopt a cloud provider's proprietary managed service (e.g., AWS Aurora, DynamoDB, Google Cloud Spanner) or self-host an open-source alternative (e.g., PostgreSQL, Cassandra, Kafka) on virtual machines or Kubernetes. This decision is fundamentally about **Total Cost of Ownership (TCO)**, **operational risk**, and **team capability**.

---

## 1. Decision Matrix: Managed Service vs Self-Managed OSS

| Dimension | Fully Managed Cloud Service | Self-Managed on VMs / Kubernetes |
| :--- | :--- | :--- |
| **Upfront Setup** | Minutes via IaC / Cloud API | Days/Weeks: Cluster provisioning, network tuning, storage allocation |
| **Day-2 Operations** | Automated OS/engine patching, automated backups, automated point-in-time recovery | Manual patching, custom backup scripts, manual restore validation, custom failover logic |
| **High Availability** | 1-click Multi-AZ replication with automated health checks and DNS failover | Complex quorum configuration (Raft/Paxos), split-brain prevention, custom sentinel scripts |
| **Scalability** | Automated storage auto-expansion, read-replica scaling, serverless scaling | Manual disk volume expansion, partition rebalancing, cluster resizing |
| **Customizability** | Constrained to provider-supported flags and extensions | Full access to source code, kernel tuning, custom third-party plugins |
| **Portability** | Lower (proprietary APIs, specialized features) | High (identical container image/version across any cloud or on-prem) |
| **Unit Cost** | Higher nominal cloud infrastructure cost (markup covers operational management) | Lower nominal infrastructure cost, but **substantially higher engineering labor cost** |

---

## 2. Total Cost of Ownership (TCO) Architectural Model

$$	ext{TCO}_{	ext{Managed}} = 	ext{Cloud Infrastructure Fee} + 	ext{Minimal Configuration Labor}$$

$$	ext{TCO}_{	ext{Self-Managed}} = 	ext{Raw Cloud VMs/Storage} + 	ext{SRE Headcount Labor} + 	ext{Custom Tooling} + 	ext{Outage Risk Cost}$$

### SRE Headcount Math Example
- Managing a highly available, multi-node self-hosted Kafka or PostgreSQL cluster across 3 AZs requires a dedicated SRE rotation (minimum 2–3 skilled engineers for 24/7 on-call coverage).
- In North America/Europe, fully burdened cost per senior distributed systems SRE is $\$200,000 - \$300,000/	ext{year}$.
- 2 SREs = $\$500,000/	ext{year}$ in labor overhead alone.
- A managed database or streaming service (AWS RDS / MSK / Confluent Cloud) costing $\$5,000 - $\$15,000/	ext{month}$ ($\$60,000 - \$180,000/	ext{year}$) is **substantially cheaper** than self-hosting when true labor costs are included.

---

## 3. When Self-Managed is Architecturally Justified

1. **Extreme Scale**: At massive scale (petabytes of streaming data, millions of IOPS), provider markups may exceed multiple millions of dollars annually, justifying a dedicated internal platform team.
2. **Proprietary Extensions**: Workloads requiring custom database extensions (e.g., bleeding-edge C plugins for PostgreSQL) not certified by the cloud vendor.
3. **Strict Air-Gapped / Sovereign Environments**: On-premises private clouds or sovereign enclaves where public cloud managed APIs are unavailable.
