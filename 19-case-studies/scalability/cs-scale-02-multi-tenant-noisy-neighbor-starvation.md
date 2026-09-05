# Case Study: B2B SaaS Multi-Tenant Noisy Neighbor Database Starvation

> **Metadata**: ID: `CS-SCALE-02` | Domain: Scalability / Multi-Tenancy | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
A high-growth B2B CRM SaaS provider with 4,200 enterprise tenants operated a pooled multi-tenancy model sharing an Amazon Aurora PostgreSQL database cluster. A newly onboarded Fortune 50 enterprise tenant executed an unindexed automated Python script that performed 250,000 full-table scans to export 5 years of historical contact interactions. The script exhausted all database read IOPS and filled the shared buffer pool with cold data, evicting the hot caches of all other 4,199 tenants. The resulting **Noisy Neighbor Cascade** elevated API response times from 45ms to 18 seconds across the entire SaaS platform, locking 85,000 sales professionals out of their accounts for 3 hours during normal business hours.

---

## 02. Business & System Context
- **Organization**: B2B CRM SaaS Provider ($90M ARR).
- **Architecture Paradigm**: Pooled Multi-Tenancy (All tenants share the same PostgreSQL database schema with a `tenant_id` column).
- **Scale**: 4,200 paying enterprise tenants; 85,000 active concurrent sales reps.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Director of Core Infrastructure.
- **Key Teams**: SaaS Platform Engineering, PostgreSQL DBAs, Customer Success Leadership.
- **Impacted Customers**: 4,199 non-offending enterprise tenants whose operations were paralyzed.

---

## 04. Requirements & NFRs
- **Tenant Isolation**: Heavy usage by one tenant must *never* degrade latency or availability for other tenants.
- **API Latency SLA**: P95 $< 100\text{ ms}$.
- **Fair Resource Allocation**: Enforce proportional compute and I/O consumption per tenant.

---

## 05. Constraints & Assumptions
- **The "Pooled is Cheapest" Decision**: Early architects chose a single shared database for all tenants to minimize AWS infrastructure costs, but failed to implement tenant-aware rate limiting or query resource governors.

---

## 06. Architecture Before: The Ungoverned Pooled Database
```mermaid
graph TD
    NormalTenants[4,199 Normal Tenants: 85,000 Reps] --> APIGW[API Gateway]
    NoisyTenant[1 Mega-Tenant: Runaway Bulk Export Script] --> APIGW
    
    subgraph The Shared Un-Governed Database (Aurora PostgreSQL)
        APIGW --> SharedDB[(Shared PostgreSQL Cluster)]
        NoisyTenant -->|250,000 Full-Table Scans!| SharedDB
        SharedDB --> IOPS[IOPS 100% Saturated!]
        SharedDB --> CacheEvict[Buffer Cache Evicted! Cache Hit: 99% -> 12%]
    end
    
    SharedDB --> Failure[4,199 Tenants Frozen: P95 Latency = 18 Seconds!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **Fully Pooled Shared Database Model** | Highly cost-effective; eliminated need to manage 4,200 separate database schemas. | Zero physical resource isolation; a single tenant's unindexed queries could consume 100% of underlying disk IOPS. |
| **Global API Rate Limiting (No Tenant Dimension)** | Global token bucket prevented total site DDoS attacks. | Blind to tenant identities: the mega-tenant stayed within global API limits while consuming 98% of database I/O resources. |

---

## 08. Timeline
```mermaid
timeline
    title Noisy Neighbor Collapse Timeline
    13:00 UTC : Enterprise Tenant #4299 kicks off custom bulk contact export script
    13:05 UTC : Script issues 50 concurrent unindexed SQL queries scanning 45M rows
    13:10 UTC : PostgreSQL buffer cache hit ratio plunges from 99.4% to 12.1%
    13:15 UTC : Aurora storage read IOPS maxes out at 80,000 IOPS; disk latency spikes to 45ms
    13:20 UTC : API P95 latency across all 4,200 tenants climbs from 45ms to 18,000ms
    13:45 UTC : Customer support inundated with 1,200 escalation tickets from Fortune 500 accounts
    15:30 UTC : DBAs identify runaway `tenant_id = 4299` in `pg_stat_activity`; terminate connections
```

---

## 09. Incident Event
At 13:00 UTC, an IT integration engineer at a newly signed enterprise customer ran an unoptimized data extraction tool against the SaaS REST API. The script queried customer interactions using an unindexed JSON metadata filter: `SELECT * FROM activities WHERE tenant_id = 4299 AND metadata->>'source' = 'legacy'`. Each query forced PostgreSQL to perform a sequential scan of a 45-Million-row table. As 50 concurrent query threads read hundreds of gigabytes of cold disk blocks, PostgreSQL's shared memory buffer pool was flushed, evicting the active working sets of all other tenants. The entire database entered an I/O thrashing death spiral.

---

## 10. Symptoms & Evidence
- **Fact**: Aurora storage read IOPS pegged at the provisioned maximum of **80,000 IOPS**.
- **Fact**: Database buffer cache hit ratio collapsed from **99.4% to 12.1%** in under 10 minutes.
- **Fact**: Active database connection monitoring (`pg_stat_activity`) revealed that 92 out of 100 active connections were executing queries on behalf of a single tenant (`tenant_id = 4299`).
- **Inference**: In shared multi-tenant databases, logical separation (a `tenant_id` column) provides zero physical resource isolation.

---

## 11. Failure Forensics
```
[Mega-Tenant executes: SELECT * FROM activities WHERE metadata->>'source' = 'legacy']
                                │
                                ▼
         [No GIN index exists -> Sequential Table Scan of 45M Rows]
                                │
                                ▼
         [Reads 220GB of cold data directly from Aurora storage]
                                │
                                ▼
         [Buffer Pool completely evicts hot data of other 4,199 tenants]
                                │
                                ▼
  [Every single normal query across ALL tenants now requires a PHYSICAL DISK READ]
                                │
                                ▼
              [Disk Latency Spikes to 45ms -> Total Platform Paralysis]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why did all 4,200 tenants experience 18-second timeouts?** -> The database was overwhelmed by physical disk I/O reads.
2. **Why was disk I/O so high?** -> The database buffer cache was cleared by sequential scans from a single tenant.
3. **Why did that tenant's query run unindexed?** -> The customer's script queried an unindexed JSONB field.
4. **Why was that query permitted to run for hours?** -> The database lacked a statement timeout (`statement_timeout`) or tenant-level concurrency limits.
5. **Why were all tenants sharing the exact same resources without quotas?** -> The architecture team implemented multi-tenancy without building **Tenant-Aware Resource Governance**.

---

## 13. Contributing Factors
- **Missing `statement_timeout`**: Long-running analytical queries were permitted to run indefinitely in the primary transactional database.
- **Lack of Read Replicas for Exports**: Bulk export API requests were routed to the primary read-write database instead of dedicated read-only analytical replicas.

---

## 14. Architecture After: Hybrid Multi-Tenancy & Tenant Resource Governors
```mermaid
graph TD
    MegaTenants[Tier 1 Enterprise Tenants] --> DedicatedSilo[(Dedicated RDS Instances: 100% Isolation)]
    NormalTenants[Standard SMB Tenants] --> APIGW[API Gateway]
    
    subgraph Multi-Tenant Guarded Pool (Standard Tenants)
        APIGW --> TenantLimiter[Per-Tenant Token Bucket: Max 50 QPS]
        APIGW --> Router{Route by Query Type}
        Router -->|Transactional Reads/Writes| PrimaryDB[(Pooled Aurora Primary: statement_timeout = 2s)]
        Router -->|Bulk Export / Analytics| ReadReplica[(Dedicated Export Read Replicas)]
    end
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: Terminated the runaway queries using `SELECT pg_terminate_backend(pid)`; temporarily blocked API tokens for `tenant_id = 4299`.
- **Permanent Architectural Fix**:
  - **Hybrid Silo-Pool Multi-Tenancy**: Migrated top-tier enterprise accounts ($> 100\text{k}$ MRR) onto **Dedicated Silo Database Instances**, physically isolating them from the shared pool.
  - **Per-Tenant Token-Bucket Rate Limiting**: Enforced rate limits at the API Gateway using Redis, capping each tenant at **50 requests/sec** and **5 concurrent database queries**.
  - **Aggressive `statement_timeout`**: Enforced a non-negotiable **2,000ms statement timeout** on the transactional cluster; long-running queries are aborted automatically.
  - **Dedicated Analytical Read Replicas**: Routed all bulk data export and reporting queries to isolated Aurora read replicas.

---

## 16. Business & Technical Impact
- **Financial**: Paid $240,000 in SLA breach penalty credits to enterprise customers.
- **Sales Conversion**: The dedicated silo architecture became a premium enterprise upsell feature ("Enterprise Dedicated Isolation Tier"), generating $4.2M in new ARR.
- **Platform Resilience**: Re-tested under simulated noisy neighbor load: zero latency degradation for pooled tenants when a single tenant misbehaves.

---

## 17. What Went Well
- The `pg_stat_activity` system view provided immediate visibility into the exact offending SQL query and tenant identifier.
- The incident accelerated the monetization of a dedicated enterprise tier.

---

## 18. Lessons Learned
- **Architecture**: In multi-tenant systems, never trust tenants to write efficient queries. Without automated resource quotas, your largest tenant will eventually destroy your smallest tenants.
- **Segregation**: Separate transactional online workloads from bulk analytical export workloads.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Set `statement_timeout = 2000ms` on all pooled transactional DBs | Lead DBA | Zero runaway scans |
| **30 Days** | Route all export/reporting API calls to dedicated read replicas | Platform Arch | Zero export load on primary |
| **90 Days** | Build automated tenant-silo provisioning in Terraform for VIP accounts | Cloud Lead | 100% silo automation |
