# Enterprise Data Architecture Review Checklist

This checklist provides a structured 25-point evaluation for data tier design, storage technologies, clustering topologies, and governance.

## 1. Storage Selection & Sizing
- [ ] Is the database engine chosen appropriately for the workload (Relational ACID vs Document vs Timeseries vs Graph)?
- [ ] Are estimated data growth rates calculated for 1, 3, and 5-year horizons?
- [ ] Is appropriate indexing defined for all dominant query predicates, avoiding redundant or unindexed foreign keys?
- [ ] Are read replicas decoupled from write-heavy primary nodes?

## 2. High Availability & Resilience
- [ ] Is the database deployed in a high-availability cluster spanning at least 3 availability zones?
- [ ] Is an odd number of consensus nodes configured to prevent split-brain leader elections?
- [ ] Is Recovery Point Objective (RPO) and Recovery Time Objective (RTO) documented and tested via automated failover drills?
- [ ] Are continuous automated backups and point-in-time recovery (PITR) configured and regularly verified?

## 3. Sharding & Scalability
- [ ] If sharding is required, is the shard key chosen with high cardinality and even write distribution?
- [ ] Are cross-shard queries eliminated or strictly bounded to administrative operations?
- [ ] Is consistent hashing implemented to support non-disruptive cluster expansion?

## 4. Governance, Security & Lineage
- [ ] Is encryption at rest enabled with customer-managed keys (CMKs) in KMS?
- [ ] Is sensitive personal data (PII) tokenized or masked before propagating into analytical data lakes?
- [ ] Are data contracts established between operational domain producers and downstream analytical consumers?
