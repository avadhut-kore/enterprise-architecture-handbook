# Data Lineage: Data Lineage in Regulatory Audits & Compliance (BCBS 239, GDPR)

## 1. Architectural Purpose & Problem Context
Providing mathematically verifiable audit trails for financial regulators: proving data origin, reconciliation integrity, and transformation correctness.

---

## 2. End-to-End Lineage Flow

```mermaid
flowchart LR
    Source[OLTP Database: orders.total_amount] --> ETL[dbt Transformation: currency_conv]
    ETL --> Lake[Lakehouse Table: fact_orders.usd_amount]
    Lake --> Agg[Data Mart: monthly_revenue]
    Agg --> Report[Executive BI Dashboard]
```

---

## 3. Production Invariants
- Automated column-level lineage extraction must be instrumented across all production ETL and lakehouse pipelines.
- Lineage graphs must be queryable via APIs to support automated pre-deployment schema change blast-radius analysis.
