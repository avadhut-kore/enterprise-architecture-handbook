# Modern Open Lakehouse Architecture (Apache Iceberg & Delta Lake)

Converged storage architecture bringing ACID transactions, schema enforcement, time-travel queries, and zero-copy cloning to open cloud object storage.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph IngestionEngines ["Multi-Engine Ingestion"]
        SparkIngest["Apache Spark (Batch ELT)"]
        FlinkIngest["Apache Flink (Streaming CDC)"]
        KafkaConnect["Kafka Connect (Iceberg Sink)"]
    end

    subgraph LakehouseMetadataLayer ["Lakehouse Table Format (Apache Iceberg / Delta Lake)"]
        IcebergCatalog["Iceberg Catalog (AWS Glue / Nessie / REST)"]
        
        subgraph SnapshotHierarchy ["Metadata Architecture"]
            SnapFile["Snapshot File (Current Manifest List Pointer)"]
            ManifestList["Manifest List (Summary of Manifest Files)"]
            ManifestFile["Manifest File (File Paths, Min/Max Stats)"]
            DataFiles["Data Files (Snappy Parquet on Cloud Object Store)"]

            SnapFile --> ManifestList
            ManifestList --> ManifestFile
            ManifestFile --> DataFiles
        end

        IcebergCatalog --> SnapFile
    end

    subgraph UnifiedQueryEngines ["Decoupled Analytical Compute Engines"]
        Trino["Trino (Ad-Hoc SQL Queries)"]
        DuckDB["DuckDB (Embedded In-Memory)"]
        Snowflake["Snowflake (External Iceberg Table Engine)"]
        SparkML["Spark MLlib (AI/ML Feature Training)"]

        Trino --> IcebergCatalog
        DuckDB --> IcebergCatalog
        Snowflake --> IcebergCatalog
        SparkML --> IcebergCatalog
    end

    SparkIngest -->|"ACID Commit"| LakehouseMetadataLayer
    FlinkIngest -->|"Micro-Batch Commit"| LakehouseMetadataLayer
    KafkaConnect -->|"Stream Writes"| LakehouseMetadataLayer

    classDef eng fill:#e8f4f8,stroke:#007791,stroke-width:2px;
    classDef meta fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef qry fill:#edf7ed,stroke:#2e7d32,stroke-width:2px;
    class SparkIngest,FlinkIngest,KafkaConnect eng;
    class IcebergCatalog,SnapFile,ManifestList,ManifestFile,DataFiles meta;
    class Trino,DuckDB,Snowflake,SparkML qry;
```

## PlantUML Specification

```plantuml
@startuml
package "Compute Engines" {
  [Apache Spark]
  [Trino Engine]
  [Snowflake External Tables]
}
package "Lakehouse Table Layer (Apache Iceberg)" {
  component "Iceberg Catalog (AWS Glue)" as cat
  file "Snapshot Pointer" as snap
  file "Manifest Files (Metadata & Partition Stats)" as meta
}
package "Cloud Object Storage" {
  folder "Parquet Data Files" as data
}

[Apache Spark] --> cat : Commit ACID Write
cat --> snap : Atomic Pointer Swap
snap --> meta : Reference Manifests
meta --> data : Point to Parquet Files
[Trino Engine] --> cat : Read Table Metadata
@enduml
```

## Architectural Design Considerations

* **Open Table Formats**: Apache Iceberg and Delta Lake eliminate vendor lock-in by allowing multiple disparate compute engines (Trino, Spark, Snowflake) to read the same storage.
* **Metadata Pruning**: Iceberg manifest files store column min/max statistics, allowing engines to skip entire Parquet files without reading them from object storage.
* **Time Travel and Rollback**: Every mutation generates an immutable snapshot, enabling exact historical query reproduction and zero-downtime rollback.

## Related Documentation & Patterns

* [Data Lake](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lake.md)
* [Data Warehouse](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-warehouse.md)
* [Modern ELT](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/elt.md)
