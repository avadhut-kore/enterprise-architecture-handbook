# Multi-Tier Data Lake Architecture (Bronze, Silver, Gold)

Hierarchical data lake storage pattern organizing raw landing assets into cleansed intermediate representations and aggregated business-ready data assets.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph IngestionSources ["Ingestion Sources"]
        S1["Microservices APIs"]
        S2["Third-Party SaaS"]
        S3["IoT Sensor Fleet"]
    end

    subgraph BronzeTier ["Tier 1: Bronze Layer (Raw Landing)"]
        BronzeS3["s3://datalake-bronze/<br/>- Unmodified Source Payloads<br/>- Preserved Schema Quirks<br/>- Append-Only, JSON/CSV/Avro<br/>- Retention: 7 Years"]
        S1 -->|"Batch/Stream"| BronzeS3
        S2 -->|"REST Extract"| BronzeS3
        S3 -->|"MQTT Dump"| BronzeS3
    end

    subgraph SilverTier ["Tier 2: Silver Layer (Standardized / Cleaned)"]
        SilverS3["s3://datalake-silver/<br/>- Deduplicated & Type-Casted<br/>- PII Masked / Anonymized<br/>- Converted to Parquet Format<br/>- Enforced Schema Validation"]
        BronzeS3 -->|"PySpark Cleansing Job"| SilverS3
    end

    subgraph GoldTier ["Tier 3: Gold Layer (Curated Business Marts)"]
        GoldS3["s3://datalake-gold/<br/>- Star Schema / Dimensional Tables<br/>- Pre-aggregated KPIs & Metrics<br/>- High-Performance Parquet/ORC<br/>- Partitioned by Year/Month/Region"]
        SilverS3 -->|"dbt / Spark Transformations"| GoldS3
    end

    subgraph QueryEngines ["Serving & Query Engines"]
        Trino["Trino / Presto Query Engine"]
        Athena["Amazon Athena Serverless"]
        BI["Executive BI Dashboards"]
        
        GoldS3 --- Trino
        GoldS3 --- Athena
        Trino --> BI
    end

    classDef brnz fill:#d7ccc8,stroke:#5d4037,stroke-width:2px;
    classDef slvr fill:#cfd8dc,stroke:#455a64,stroke-width:2px;
    classDef gld fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    class BronzeS3 brnz;
    class SilverS3 slvr;
    class GoldS3 gld;
```

## PlantUML Specification

```plantuml
@startuml
package "Raw Tier" {
  folder "Bronze (Raw Storage)" as bronze
}
package "Enriched Tier" {
  folder "Silver (Cleansed Parquet)" as silver
}
package "Business Tier" {
  folder "Gold (Aggregated Marts)" as gold
}
component "Spark Cleansing" as spark1
component "dbt Aggregations" as spark2
component "Athena / BI" as bi

bronze -> spark1 : Clean & Deduplicate
spark1 -> silver : Write Parquet
silver -> spark2 : Compute Business Metrics
spark2 -> gold : Star Schema
gold -> bi : Analytical Queries
@enduml
```

## Architectural Design Considerations

* **Immutability of Bronze**: Never modify raw data in the Bronze layer; it serves as the ultimate system of record for replaying transformations.
* **Columnar Storage**: Ensure Silver and Gold layers are stored in columnar formats (Apache Parquet or ORC) with Snappy compression for optimal query performance.
* **Partitioning Strategy**: Partition data by query-predicate dimensions (e.g., `date=YYYY-MM-DD`, `tenant_id=XYZ`) to prune unneeded files during scans.

## Related Documentation & Patterns

* [Modern Lakehouse](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/lakehouse.md)
* [Data Warehouse](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-warehouse.md)
* [Batch ETL](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/etl.md)
