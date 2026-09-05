# ADR-0005: PostgreSQL vs MongoDB for Customer Profile Service

---
**Metadata**:
* **ADR ID**: ADR-0005
* **Title**: Data Store Selection — PostgreSQL for Customer Profile & Identity
* **Status**: Accepted
* **Date**: 2026-03-02
* **Decision Owners**: Lead Data Architect
---

## 1. Context & Problem Statement
Customer profile data includes structured demographic fields, dynamic arbitrary third-party attributes, authentication credentials, and strict regulatory consent records. We evaluated PostgreSQL vs MongoDB.

## 2. Decision & Rationale
Adopt **PostgreSQL** with native `JSONB` storage.
PostgreSQL provides robust relational integrity and ACID transactions for identity and consent audit logs, while its `JSONB` indexing provides the schemaless flexibility required for dynamic customer attributes without the operational overhead of managing a separate MongoDB cluster.
