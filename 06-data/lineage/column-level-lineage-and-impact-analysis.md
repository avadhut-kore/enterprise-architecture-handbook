# Data Lineage: Column-Level Lineage & Blast Radius Analysis

## 1. Architectural Purpose & Problem Context
Tracing single column mutations across multi-stage ETL joins, evaluating schema migration impact, and identifying downstream broken reports.

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
