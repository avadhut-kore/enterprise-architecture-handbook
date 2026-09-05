# Data Design Specification: [DATA SYSTEM NAME]

---
**Metadata**:
```yaml
document_id: "DATA-[SYSTEM-ID]-001"
title: "Data Design Specification — [System Name]"
version: "1.0.0"
status: "Draft" # Draft | In Review | Approved | Implemented
data_architect: "[Data Architect Name <email>]"
lead_engineer: "[Lead Engineer Name]"
database_engine: "PostgreSQL 16 / CockroachDB"
data_classification: "Restricted - Financial PII"
created_date: "YYYY-MM-DD"
```
---

## 1. Data System Scope & Objectives
* Business domain entities managed by this storage tier.
* Single Source of Truth (SSOT) boundaries.

## 2. Logical Data Model & Entity Relationships
Reference Entity-Relationship Diagrams (ERD) from [[17-diagrams/03-data-diagrams/01-erd.md](../../17-diagrams/data/README.md)].

## 3. Physical Storage & Schema Specification
* DDL table definitions, datatypes, primary keys, foreign keys, and check constraints.

## 4. Indexing & Query Access Patterns
* Top 5 critical read queries and their supporting composite B-Tree/GIN indexes.

## 5. Partitioning & Sharding Strategy
* Range or hash partition key (e.g., `PARTITION BY RANGE (created_at)`).

## 6. Consistency Model & Concurrency
* Isolation level: `READ COMMITTED` | `REPEATABLE READ` | `SERIALIZABLE`.
* Concurrency locking mechanism (Optimistic `@Version` vs Pessimistic row locks).

## 7. Caching Strategy
* Cache invalidation policy, TTLs, and cache stampede mitigations.

## 8. Data Protection, PII & Cryptography
* Column-level encryption for sensitive attributes (SSN, credit cards).
* Masking in non-production environments.

## 9. Retention, Archival & Pruning
* Active operational retention window (e.g., 90 days in fast storage).
* Long-term compliance archival (e.g., 7 years in Parquet format on S3).

## 10. Zero-Downtime Migration Strategy
* Backward-compatible migration sequence (Expand and Contract pattern).
