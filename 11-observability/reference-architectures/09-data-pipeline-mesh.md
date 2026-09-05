# Reference Architecture 09: Data Mesh & Analytical Lakehouse Observability

## 1. System Context & Overview
Modern data architectures rely on distributed pipelines (Apache Spark, Snowflake, Databricks, dbt) to process terabytes of analytical data. Standard application metrics (QPS and HTTP latency) are meaningless here.

**Data Observability** focuses on **Data Freshness, Volume Anomaly Detection, Schema Drift, and Lineage Tracking**.

---

## 2. Architecture Diagram

```mermaid
flowchart TD
    subgraph Data_Sources ["Operational Data Producers"]
        DB["OLTP Database (PostgreSQL)"]
        CDC["Debezium / Kafka CDC"]
        DB --> CDC
    end

    subgraph Pipeline_Processing ["ETL / ELT Pipeline Execution"]
        Spark["Apache Spark / Databricks Jobs"]
        dbt["dbt Transformation Models"]
        Lakehouse["Delta Lake / Snowflake Warehouse"]
        CDC --> Spark --> dbt --> Lakehouse
    end

    subgraph Data_Observability_Agent ["Data Observability Engine (Great Expectations / Monte Carlo)"]
        Freshness["Freshness Monitor\n(Alerts if table not updated in > 4 hours)"]
        Volume["Volume Anomaly Detector\n(Alerts if row count drops by > 30%)"]
        Schema["Schema Drift Detector\n(Detects dropped/renamed columns)"]
        Quality["Data Quality Assertions\n(Null percentage, unique constraints)"]
    end

    Lakehouse -. Inspect Metadata .-> Freshness
    Lakehouse -. Inspect Metadata .-> Volume
    Lakehouse -. Inspect Metadata .-> Schema
    Lakehouse -. Inspect Metadata .-> Quality

    subgraph Lineage_Store ["Data Lineage & Catalog"]
        OpenLineage["OpenLineage / Marquez\n(Tracks DAG dependencies from raw to mart)"]
        dbt --> OpenLineage
        Spark --> OpenLineage
    end
```

---

## 3. Key Architectural Decisions
1. **Metadata-Based Inspection**: Instead of scanning billions of raw data rows (which incurs huge Snowflake/Databricks query compute costs), freshness and volume monitors query internal database catalog metadata (`information_schema.tables`).
2. **Schema Drift Circuit Breaker**: When upstream application teams add, drop, or alter database columns, the schema monitor detects the change and pauses downstream reporting jobs before invalid data corrupts financial reports.
3. **OpenLineage Standards**: Data pipeline execution stages emit standard OpenLineage events, allowing automated end-to-end tracing from raw operational database tables to executive BI dashboards.
