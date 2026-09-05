# ADR-0004: Relational PostgreSQL vs. NoSQL DynamoDB for Financial Ledger

## Metadata
- **Status**: Accepted
- **Date**: 2026-09-05
- **Author(s)**: Lead Data Architect & Solution Architect
- **Deciders**: Architecture Review Board (ARB), Chief Information Security Officer (CISO)
- **Technical Story**: [ARCH-1102] Financial Ledger Persistence Selection

---

## 1. Context and Problem Statement

The enterprise is building a new real-time multi-currency digital wallet and ledger service. The system must process fund deposits, withdrawals, transfers between accounts, and currency exchanges.

The system has the following non-negotiable operational requirements:
1. **Absolute Data Integrity (Zero Overdrafts)**: Under no circumstances can two concurrent transactions double-spend or overdraft an account balance.
2. **Double-Entry Accounting Invariant**: Every monetary transfer must consist of an immutable balanced pair of entries: a `DEBIT` to one account and an equal `CREDIT` to another account ($\sum \text{Debits} = \sum \text{Credits}$).
3. **Auditing & Regulatory Invariants**: Complete financial auditability is legally mandated by banking regulatory authorities.
4. **Projected Scale**: Baseline throughput of **500 write transactions/second**, peaking at **2,500 TPS** during holiday promotional campaigns. Total ledger volume projected at **400 million transactions/year (~250 GB/year)**.

We must determine the primary persistence technology for the core Ledger database: **Relational (PostgreSQL / AWS Aurora)** vs. **Managed NoSQL (Amazon DynamoDB)**.

---

## 2. Decision Drivers

- **Driver 1: Strict Multi-Row ACID Transactions**: Atomicity across double-entry debits and credits is non-negotiable.
- **Driver 2: Complex Relational Constraints & Invariants**: Enforcing non-negative balance checks and foreign keys directly at the database engine level.
- **Driver 3: Rich Financial Auditing & Reconciliation Queries**: Ability to execute complex aggregate queries (`SUM`, `GROUP BY`, reconciliation scans) across dates and currencies.
- **Driver 4: Manageability & Team Competency**: Leverage existing database administration expertise without requiring deep NoSQL single-table design mastery.

---

## 3. Considered Options

- **Option A**: **Relational Database — Amazon Aurora PostgreSQL (Multi-AZ)**.
- **Option B**: Managed Distributed NoSQL — Amazon DynamoDB (Single-Table Design with DynamoDB Transactions).
- **Option C**: Distributed SQL — CockroachDB.

---

## 4. Comparative Evaluation Matrix

| Evaluation Criteria | Option A: Aurora PostgreSQL | Option B: Amazon DynamoDB | Option C: CockroachDB |
|:---|:---:|:---:|:---:|
| **Multi-Row ACID Guarantees** | **Native / Strict Serializable** | Limited (25-item transaction limit) | Native Distributed ACID |
| **Integrity Constraints (CHECK, FK)**| **Native DB Constraints (`CHECK (balance >= 0)`)** | Application-level logic only | Native DB Constraints |
| **Complex Analytical Reconciliation**| **High (Standard ANSI SQL / Window Functions)** | Extremely Poor (Requires scan or export to S3) | High (Standard SQL) |
| **Write Throughput Scalability** | **Sufficient (Handles up to 25k TPS)** | Unbounded Horizontal Scale | High Distributed Scale |
| **Operational Simplicity** | **High (Standard enterprise paved road)** | Very High (Serverless managed) | Medium (New technology learning curve)|
| **Cost Predictability** | **Predictable Provisioned / Reserved** | Can be volatile under heavy transactions | High |

---

## 5. Decision Outcome

**Chosen Option**: **Option A: Amazon Aurora PostgreSQL (Multi-AZ)**

### Rationale and Justification
For a financial double-entry ledger, **correctness and data integrity vastly outweigh unbounded horizontal scalability**. 

1. **Database-Level Invariant Enforcement**: PostgreSQL allows defining database-level constraints such as:
   ```sql
   CONSTRAINT positive_balance CHECK (available_balance >= 0)
   ```
   Even if an application developer introduces a concurrency race condition in application code, the database engine physically rejects the transaction, making overdrafts mathematically impossible.
2. **Double-Entry Atomicity**: Relational transactions guarantee that the debit to Account A and credit to Account B succeed or fail together as an atomic unit with zero risk of partial execution.
3. **Capacity Realities**: At 2,500 peak write TPS, a modern Aurora PostgreSQL instance (e.g., `db.r6g.4xlarge`) operates at under **35% CPU utilization**. Adopting DynamoDB to solve a "scale problem" that does not exist at 2,500 TPS would needlessly sacrifice SQL reconciliation queries and relational constraint safety.

---

## 6. Consequences & Trade-Offs

### Positive Consequences
- **Rock-Solid Financial Safety**: Full ACID compliance with `SERIALIZABLE` or `READ COMMITTED` isolation with row-level locks (`SELECT FOR UPDATE`).
- **Seamless Financial Auditing**: Internal auditors and finance teams can run standard SQL reconciliation queries directly against read-replicas.
- **Enterprise Tooling**: Pre-integrated with corporate backup solutions, encryption standards (AWS KMS), and replication pipelines.

### Negative Consequences
- **Vertical Scaling Ceiling**: Unlike DynamoDB, a single PostgreSQL primary cannot scale writes infinitely across 50 nodes. 
- **Storage Maintenance**: Large transaction tables will eventually require automated monthly table partitioning (`pg_partman`) by transaction date to maintain indexing performance over a 5-year horizon.

---

## 7. Compliance & Schema Guidelines

- All transaction insertions must be strictly append-only (No `UPDATE` on transaction journal rows).
- Schema must enforce strict non-negative balance checks:

```sql
CREATE TABLE account_balances (
    account_id UUID PRIMARY KEY,
    currency VARCHAR(3) NOT NULL,
    settled_balance NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    available_balance NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    version BIGINT NOT NULL DEFAULT 0,
    CONSTRAINT chk_positive_available CHECK (available_balance >= 0)
);
```
