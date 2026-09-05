# ADR-0049: Adoption of Amazon Aurora PostgreSQL as Standard Relational Engine

## Metadata
```yaml
id: ADR-0049
title: Adoption of Amazon Aurora PostgreSQL as Standard Relational Engine
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Traditional self-managed PostgreSQL on EC2 suffered from replication lag, complex multi-AZ failover scripts, and disk I/O bottlenecks.

---

## 2. Decision
We adopt Amazon Aurora PostgreSQL with log-structured distributed storage replicated 6 ways across 3 Availability Zones as the default enterprise relational engine.

---

## 3. Positive Consequences
- Up to 3x throughput improvement over standard PostgreSQL.
- Sub-10ms read replica replication lag.
- Automated failover in under 30 seconds with zero data loss.

---

## 4. Negative Consequences & Trade-offs
- Incurs premium Aurora storage and I/O pricing.
- Proprietary storage engine creates cloud provider lock-in.

---

## 5. Alternatives Considered & Rejected
- **Self-Managed PostgreSQL on EC2**: Rejected due to SRE maintenance overhead.
- **Standard RDS PostgreSQL**: Rejected due to higher replication lag and slower failover times.
