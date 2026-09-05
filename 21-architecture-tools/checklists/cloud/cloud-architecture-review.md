# Cloud Architecture Review Checklist

## Executive Summary

This checklist provides the formal governance gate used by the Architecture Review Board (ARB) to evaluate enterprise systems prior to production cloud deployment.

---

## 1. Business Alignment & Classification
- [ ] **Criticality Tier Defined**: Workload explicitly classified (Tier 1 Mission-Critical, Tier 2 Business-Critical, Tier 3 Operational, Tier 4 Non-Critical).
- [ ] **RTO & RPO Documented**: Recovery Time Objective and Recovery Point Objective signed off by business product owner.
- [ ] **Compliance & Regulatory Boundaries**: Data residency, GDPR, HIPAA, PCI-DSS, or national sovereignty constraints identified.
- [ ] **Approved Cloud Service Validation**: All proposed cloud services are on the Enterprise Approved Service List.

---

## 2. Architecture & Resilience
- [ ] **Multi-AZ by Default**: Compute, datastores, and message brokers deployed across a minimum of 3 Availability Zones.
- [ ] **Static Stability Verified**: The data plane continues processing existing transactions if the cloud provider control plane fails.
- [ ] **Decoupled Asynchronous Processing**: Long-running or heavy operations decoupled via message queues or event streaming.
- [ ] **Circuit Breakers & Retries**: Downstream dependency calls implement timeouts, circuit breakers, and exponential backoff with full jitter.
- [ ] **Stateless Compute**: Zero state pinned to local virtual machines or container ephemeral filesystems; state externalized to managed DBs/caches.

---

## 3. Infrastructure & Network Security
- [ ] **Zero Public Databases**: No managed database or internal API has a public IP address or public route table entry.
- [ ] **Subnet Tiering Enforced**: Public (ALB/NAT), Private (Compute), and Isolated (Database) subnets strictly partitioned.
- [ ] **Least-Privilege Security Groups**: Ingress rules restricted to specific source Security Group IDs; no open `0.0.0.0/0` internal rules.
- [ ] **Zero Standing Credentials**: Workload Identity Federation (EKS Pod Identity / Managed Identity) used; zero hardcoded IAM access keys.
- [ ] **Envelope Encryption at Rest**: All block volumes, object storage buckets, and relational databases encrypted with KMS Customer Managed Keys.

---

## 4. Disaster Recovery & Operations
- [ ] **Disaster Recovery Strategy Validated**: Backup/Restore, Pilot Light, or Warm Standby automated in secondary region.
- [ ] **Automated Snapshot Lifecycle**: Automated cross-region replication of database snapshots with immutable WORM retention.
- [ ] **Verified Rollback Plan**: Deterministic cutover and reverse-replication rollback runbook documented and tested.
- [ ] **SLO Burn-Rate Alerting**: Multi-window burn-rate alerts configured in PagerDuty; zero raw CPU-only high-priority pages.

---

## 5. FinOps & Cost Governance
- [ ] **Mandatory Tagging Applied**: 100% of resources tagged with `CostCenter`, `OwnerEmail`, `Environment`, and `DataClassification`.
- [ ] **Upfront TCO Modeled**: Monthly run-rate calculated, including cross-AZ and internet egress data transfer fees.
- [ ] **Savings Plans Applied**: Baseline compute mapped to 1-Year or 3-Year Compute Savings Plans; Spot instances used for batch.
