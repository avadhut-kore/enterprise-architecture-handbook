# Architecture Cost Estimation & Financial Modeling (FinOps)

> How to calculate Total Cost of Ownership (TCO), unit economics (Cost per Active User, Cost per Transaction), and avoid cloud billing disasters.

---

## 1. The Real Cost of Architecture

Senior architects must think like Chief Technology Officers and VP of Engineering. An elegant distributed architecture that satisfies all technical criteria but costs $\$300,000/\text{month}$ for a $\$50,000/\text{month}$ revenue product is an architectural failure.

```
Total Cost of Ownership (TCO):
  ├── Cloud Infrastructure Run Rate (Compute, Storage, Network, DB)
  ├── SaaS & Third-Party Licensing (Datadog, Snowflake, Auth0, Confluent)
  ├── Network Egress & Cross-AZ Penalties
  ├── Operational & Engineering Headcount (FTEs to maintain system complexity)
  └── Cost of Downtime & SLA Penalties
```

---

## 2. Standard Cloud Cost Benchmarks (Order of Magnitude)

| Resource Category | Specification | Typical Cloud Cost (AWS / GCP / Azure) |
| :--- | :--- | :--- |
| **Compute (General Purpose)** | 8 vCPU, 32 GB RAM (e.g., `m6i.2xlarge`) | $\approx \$0.38/\text{hr} \approx \mathbf{\$280/\text{month}}$ |
| **Compute (ARM / Graviton)** | 8 vCPU, 32 GB RAM (e.g., `m7g.2xlarge`) | $\approx \$0.29/\text{hr} \approx \mathbf{\$210/\text{month}}$ ($25\%$ cheaper) |
| **Serverless Compute** | AWS Lambda ($1\text{M invocations} \times 200\text{ms}, 512\text{ MB}$) | $\approx \mathbf{\$1.80/\text{Million invocations}}$ |
| **Block Storage (SSD)** | AWS EBS `gp3` | $\approx \mathbf{\$0.08\text{ per GB/month}}$ |
| **High-Performance IOPS** | Provisioned IOPS `io2` | $\approx \mathbf{\$0.125\text{ per GB}} + \mathbf{\$0.065\text{ per provisioned IOPS}}$ |
| **Object Storage (Standard)** | AWS S3 Standard | $\approx \mathbf{\$0.023\text{ per GB/month}}$ ($\approx \$23/\text{TB}$) |
| **Object Storage (Archive)** | AWS S3 Glacier Deep Archive | $\approx \mathbf{\$0.00099\text{ per GB/month}}$ ($\approx \$1/\text{TB}$) |
| **Distributed In-Memory Cache** | Redis Cluster ($3 \times 16\text{ GB nodes}$) | $\approx \mathbf{\$450/\text{month}}$ |
| **Managed Kafka Cluster** | AWS MSK ($3 \times \text{kafka.m5.xlarge}$) | $\approx \mathbf{\$650/\text{month}} + \text{storage}$ |
| **Public Internet Egress** | Data transferred out to internet | $\approx \mathbf{\$0.08\text{ per GB}}$ ($\approx \$80/\text{TB}$) |
| **Cross-AZ Data Transfer** | Data transferred between AZs in same region | $\approx \mathbf{\$0.01\text{ per GB}}$ ($\approx \$10/\text{TB}$) |

---

## 3. End-to-End Monthly TCO Sizing Example

### Scenario: Mid-Sized Enterprise SaaS Platform
* **User Base**: $2\text{ Million MAU}$, $200,000\text{ DAU}$.
* **Throughput**: $2,000\text{ Average RPS}$, $6,000\text{ Peak RPS}$.
* **Data Volume**: $10\text{ TB}$ OLTP database, $50\text{ TB}$ S3 documents, $50\text{ TB/month}$ public egress.

### Line-Item Cost Breakdown

```text
1. COMPUTE TIER (Kubernetes EKS Fleet)
   - 12 x m7g.xlarge worker nodes (4 vCPU, 16 GB RAM)
   - 12 * $105/mo .................................................. $1,260 / month

2. MANAGED RELATIONAL DATABASE (AWS Aurora PostgreSQL Multi-AZ)
   - Primary + Read Replica (db.r6g.2xlarge: 8 vCPU, 64 GB RAM)
   - Compute: 2 * $550/mo = $1,100
   - Storage: 10 TB Aurora storage * $0.10/GB = $1,000
   - I/O requests: 500M requests * $0.20/M = $100
   - Total Database ................................................ $2,200 / month

3. DISTRIBUTED CACHING (ElastiCache Redis Multi-AZ)
   - 2-node cluster (cache.m6g.xlarge: 13 GB RAM)
   - Total Cache ................................................... $320 / month

4. STORAGE & ARCHIVE (AWS S3)
   - 50 TB S3 Standard * $23/TB .................................... $1,150 / month

5. NETWORK EGRESS & CDN (CloudFront + AWS Egress)
   - 50 TB egress via CloudFront CDN @ $0.04/GB .................... $2,000 / month

6. OBSERVABILITY & TELEMETRY (SaaS Datadog / OpenTelemetry)
   - 12 hosts + APM tracing + log ingestion ......................... $1,800 / month

-----------------------------------------------------------------------------
TOTAL DIRECT INFRASTRUCTURE RUN RATE:                               $8,730 / month
ANNUALIZED INFRASTRUCTURE COST:                                     $104,760 / year
-----------------------------------------------------------------------------
```

### Unit Economics Calculation
$$\text{Cost per Monthly Active User} = \frac{\$8,730}{2,000,000\text{ MAU}} = \mathbf{\$0.00436\text{ per user/month} (< \text{half a cent})}$$
$$\text{Cost per 1,000 Requests} = \frac{\$8,730}{2,000\text{ RPS} \times 2.59\text{M sec}} \approx \mathbf{\$0.00168\text{ per 1,000 requests}}$$

> [!TIP]
> **Executive Presentation Tip**: In senior interviews, quoting the unit economic metric (*"This architecture operates at less than half a cent per active user per month"*) demonstrates immediate executive financial competence.

---

## 4. Cross-References

* **Bandwidth Sizing**: [`bandwidth.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/bandwidth.md)
* **Compute Capacity**: [`compute.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/compute.md)
* **Complete Capacity Synthesis**: [`capacity.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/capacity.md)
* **Trade-Off Analyses**: [`tradeoffs/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/README.md)
