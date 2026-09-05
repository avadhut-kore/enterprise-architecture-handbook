# Data Architecture Starter Template

Production-ready boilerplate template for modeling enterprise data topologies, operational databases, caching layers, and analytical pipelines.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph OperationalTier ["1. Operational Transaction Tier"]
        App["Operational Microservice"]
        Cache[("Redis Cache Tier")]
        PrimaryDB[("Primary OLTP Database<br/>(PostgreSQL HA Cluster)")]

        App --> Cache
        App --> PrimaryDB
    end

    subgraph IntegrationAndCDC ["2. Streaming & Change Data Capture"]
        CDC["Debezium CDC Engine"]
        Kafka["Kafka Event Stream"]

        PrimaryDB -.->|"WAL Stream"| CDC
        CDC --> Kafka
    end

    subgraph AnalyticalTier ["3. Curated Analytical Lakehouse"]
        SparkJob["PySpark Aggregation Job"]
        DataLake[("Lakehouse Storage (S3 / Iceberg)<br/>[Bronze -> Silver -> Gold]")]
        BI["Executive BI & Analytics"]

        Kafka --> SparkJob
        SparkJob --> DataLake
        DataLake --> BI
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Operational Tier" {
  [App Service] --> [Redis Cache]
  [App Service] --> [Postgres DB]
}
package "CDC Pipeline" {
  [Postgres DB] ..> [Debezium CDC]
  [Debezium CDC] --> [Kafka Topic]
}
package "Analytical Tier" {
  [Kafka Topic] --> [Lakehouse Storage]
  [Lakehouse Storage] --> [BI Analytics]
}
@enduml
```

## Architectural Design Considerations

* **Separation of OLTP and OLAP**: Never run complex reporting queries against the operational OLTP database; stream mutations to an analytical store.
* **Standard Starting Baseline**: Use this template when documenting the complete data lifecycle for an enterprise solution.
* **Annotate Storage Formats**: Clearly state whether tables are row-oriented (B-Tree) or columnar (Parquet/Iceberg).

## Related Documentation & Patterns

* [Data Mesh](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/data-mesh.md)
* [Database Clustering](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/database-clustering.md)
* [Data Architecture Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/checklists.md)
