# Data Lineage: Data Lineage Overview & Extraction Architecture

## 1. Architectural Purpose & Problem Context
Automated lineage capture via query log parsing (OpenLineage, SQLGlot), execution engine instrumentation (Spark, dbt), and lineage graph visualization.

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
