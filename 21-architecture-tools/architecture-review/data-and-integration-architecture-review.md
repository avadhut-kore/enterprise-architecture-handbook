# Data & Integration Architecture Review Specification

## 1. Executive Purpose
This document establishes the mandatory Architecture Review Board (ARB) review questions and evaluation criteria for assessing enterprise data storage, persistence, APIs, messaging, and financial integration architectures.

---

## 2. ARB Review Dimensions & Inquiry Questions

### Section 1: Data Architecture & Governance
* **Data Ownership**: Who is the designated business domain owner and technical steward of this data?
* **Source of Truth**: What system is the single authoritative Source of Truth (SoT) and System of Record (SoR)?
* **Lifecycle & Retention**: What is the retention period, archival tiering strategy, and deletion policy?
* **Data Classification**: Is the data classified as Public, Internal, Confidential, or Restricted (PII/PCI/PHI)?
* **Data Quality**: What automated assertions verify accuracy, completeness, and freshness at ingestion?

### Section 2: Database Architecture & Selection
* **Workload Justification**: Why was this specific database engine selected over standard relational alternatives?
* **Query Patterns**: What are the top read and write query access patterns, and are they supported by indexes?
* **Scaling Strategy**: How does the database scale under 10x traffic spikes (read replicas, partitioning, sharding)?
* **Failure & Recovery**: What is the Recovery Point Objective (RPO) and Recovery Time Objective (RTO)?
* **Schema Evolution**: How will schema changes be deployed to production with zero downtime?

### Section 3: Data Mapping & Transformation
* **Source-to-Target Specification**: Is there a formal [Data Mapping Specification](../../16-architecture-deliverables/DATA-MAPPING-TEMPLATE.md)?
* **Code Translations**: How are mismatched enumeration codes and status values mapped and validated?
* **Null & Missing Data**: What are the explicit policies for missing optional vs missing mandatory fields?
* **Financial Precision**: Do monetary transformations use integer minor units or arbitrary-precision decimals?
* **Mapping Lineage**: How are mapping changes versioned, tested, and tracked for downstream blast radius?

### Section 4: Integration & Messaging
* **Communication Style**: Why was synchronous API chosen over asynchronous messaging (or vice-versa)?
* **Dependency Failure**: What happens to this service when downstream dependencies experience outages or latency spikes?
* **Idempotency**: Is the operation idempotent? How are duplicate network deliveries detected and mitigated?
* **Contract Evolution**: Are API/event schemas versioned and validated via schema registries in CI?
* **Poison Message Triage**: How are unprocessable messages routed, alerted, and replayed from DLQs?

### Section 5: Financial Transactions & Settlement
* **Idempotency Keys**: Are client-generated idempotency keys enforced on all financial mutations?
* **Transaction Lifecycle**: How are authorization holds, captures, refunds, and chargebacks tracked?
* **Settlement Source of Truth**: What bank or processor file is the authoritative source for settled funds?
* **Settlement Batches**: How are batch cut-off timestamps, control sums, and netting calculations verified?
* **Reversal Handling**: What automated and manual processes exist for failed or delayed settlements?

### Section 6: Financial Reconciliation
* **Systems Reconciled**: What exact systems are being matched (e.g., Internal DB ↔ Gateway ↔ Bank ↔ GL)?
* **Matching Criteria**: What composite keys, reference numbers, and amount tolerances are used?
* **Exception Management**: How are missing transactions, duplicate charges, and fee mismatches classified?
* **Investigation & Adjustment**: What four-eyes approval workflows govern financial adjustments and write-offs?
* **Auditability**: Are reconciliation matching results and manual adjustments permanently logged for auditors?
