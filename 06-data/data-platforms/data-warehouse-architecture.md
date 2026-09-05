# Data Platforms: Enterprise Data Warehouse Architecture (Snowflake, BigQuery, Redshift)

## 1. Architectural Purpose & Problem Context
Columnar storage engines, massively parallel processing (MPP), schema-on-write, workload isolation, and dimensional data modeling.

---

## 2. Modern Lakehouse Platform Architecture

```mermaid
flowchart TD
    Sources[Operational DBs / Kafka / Files] --> Ingest[Batch & Streaming Ingestion]
    Ingest --> Bronze[Raw / Bronze Zone: Immutable Event Log]
    Bronze --> Silver[Cleansed / Silver Zone: Conformed Iceberg Tables]
    Silver --> Gold[Curated / Gold Zone: Dimensional Aggregations]
    Gold --> BI[BI Dashboards / SQL Queries]
    Gold --> ML[ML Feature Store / AI Pipelines]
```

---

## 3. Production Invariants
- Prefer modern open table formats (Apache Iceberg / Delta Lake) over proprietary locked warehouse formats.
- Maintain immutable raw audit layers to allow full historical recomputation of downstream silver/gold tables.
