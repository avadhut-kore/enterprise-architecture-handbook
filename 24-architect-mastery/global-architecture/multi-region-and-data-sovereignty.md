# Multi-Region and Data Sovereignty Architecture

Global enterprises must respect the physical and legal reality of data borders. Data residency laws (GDPR, Saudi PDPL, China PIPL) prohibit citizen PII from leaving territorial jurisdictions.

## 1. Regional Sharding Topology

```
┌─────────────────────────────────────────────────────────────┐
│                    GLOBAL ANYCAST EDGE                      │
│       Cloudflare / AWS Global Accelerator (Geo-Routing)     │
├──────────────────────────────┬──────────────────────────────┤
│      EU REGION (Frankfurt)   │      US REGION (Virginia)    │
│  - EU Kubernetes Cluster     │  - US Kubernetes Cluster     │
│  - Local RDS PostgreSQL (PII)│  - Local RDS PostgreSQL (PII)│
│  - Local Encryption Keys     │  - Local Encryption Keys     │
├──────────────────────────────┴──────────────────────────────┤
│                    REPLICATED NON-PII TIERS                 │
│      Product Catalog / Global Config / Anonymized Analytics │
└─────────────────────────────────────────────────────────────┘
```

## 2. Architectural Rules for Global Compliance
1. **Geo-Partitioned Databases**: Use databases with native row-level geo-partitioning (CockroachDB, Spanner) or application-level regional database shards.
2. **Isolated Key Management (KMS)**: Regional encryption keys must be held in regional HSMs to prevent extraterritorial subpoena compliance.
3. **Anonymized Telemetry**: Strip IP addresses and PII before streaming observability logs to centralized global observability hubs.

## Related Modules
- [Regulated Enterprise Architecture](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/regulated-enterprise/README.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
