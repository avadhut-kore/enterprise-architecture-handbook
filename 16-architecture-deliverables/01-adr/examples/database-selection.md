# ADR-0002: Distributed SQL (CockroachDB) for Multi-Region Ledger

---
**Metadata**:
* **ADR ID**: ADR-0002
* **Title**: Selection of CockroachDB for Multi-Region Financial Ledger
* **Status**: Accepted
* **Date**: 2026-01-20
* **Decision Owners**: Data Architect, Lead Payment Engineer
* **Decision Reviewers**: Security Architect, Infrastructure Lead, ARB
* **Related Requirements**: REQ-FIN-012, NFR-AVAIL-001, NFR-LAT-003
* **Related ADRs**: Supersedes ADR-0001
---

## 1. Context & Problem Statement
The Global Payment Platform requires expanding from a single AWS region (us-east-1) to three active regions (us-east-1, eu-west-1, ap-southeast-1). The core financial ledger must guarantee strict serializable isolation (ACID), zero balance corruption, and resilient survivability against entire cloud region outages while maintaining read latencies under 20ms for local accounts.

## 2. Business & Technical Drivers
* Regulatory compliance (PCI-DSS, European GDPR data residency) requiring transactions to settle locally.
* Zero tolerance for double-spend or split-brain inconsistencies during inter-region network splits.
* Recovery Point Objective (RPO) = 0; Recovery Time Objective (RTO) < 30 seconds.

## 3. Options Considered

### Option 1: Sharded PostgreSQL with Asynchronous Cross-Region Replication
* **Pros**: Deep team expertise, rich ecosystem, lower software cost.
* **Cons**: Asynchronous replication guarantees data loss during regional failover (RPO > 0). Manual sharding logic adds extreme application complexity.

### Option 2: CockroachDB (Distributed SQL)
* **Pros**: Raft-based consensus per range guarantees strict serializability and zero data loss (RPO = 0). Automatic horizontal range splitting and rebalancing. Native table and row-level geo-partitioning to enforce GDPR residency.
* **Cons**: Higher write latency for cross-region transactions due to multi-phase commit roundtrips. Significant enterprise licensing costs.

### Option 3: AWS Aurora Global Database
* **Pros**: Fully managed by AWS, fast physical replication.
* **Cons**: Single active write region; failover requires promoting secondary region with 1-2 minute downtime (RTO > 30s). Vendor lock-in.

## 4. Decision & Rationale
**Chosen Option**: Option 2 (CockroachDB Dedicated / Self-Hosted Multi-Region).

CockroachDB is selected because it is the only viable option providing true Active-Active multi-region transactions with strict serializable consistency (RPO=0) and automated regional failover without operator intervention. Row-level data locality ensures 95% of domestic transactions achieve local consensus in <15ms.

## 5. Consequences & Trade-offs
* **Accepted Trade-off**: Cross-region money transfers that span continents will incur a p99 latency of 250-350ms due to multi-region Raft consensus. This is accepted and mitigated via client-side asynchronous progress updates.
* **Operational Impact**: SRE team must be trained on CockroachDB range diagnostics, Raft follower reads, and node rebalancing.

## 6. Security & Operational Characteristics
* Node-to-node and client-to-node communication strictly encrypted via mTLS using HashiCorp Vault PKI.
* Full Prometheus metrics integrated into Grafana with alerts on under-replicated ranges.
