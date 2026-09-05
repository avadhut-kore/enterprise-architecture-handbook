# Enterprise Data-Flow Architecture Diagram Template

Standardized, copy-pasteable starter template for modeling enterprise data flow pipelines from multi-source ingestion through processing, storage tiers, and egress.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph SourceTier ["1. Data Producers & Ingestion Sources"]
        SourceA["Operational API / App"]
        SourceB["Third-Party Webhook"]
        SourceC["Relational Database (CDC)"]
    end

    subgraph IngestionTier ["2. Ingestion & Streaming Buffer"]
        Buffer["Event Broker / Ingestion Proxy<br/>(Kafka / Kinesis / SQS)"]
        SourceA --> Buffer
        SourceB --> Buffer
        SourceC --> Buffer
    end

    subgraph ProcessingTier ["3. Stream & Batch Processing Tier"]
        Processor["Processing Engine<br/>(Spark / Flink / dbt)"]
        Buffer -->|"Pull Stream / Batch"| Processor
    end

    subgraph StorageTier ["4. Persistent Storage & Lakehouse"]
        RawStore[("Raw Landing Store (Bronze)")]
        CuratedStore[("Curated Analytics Store (Gold)")]
        Processor --> RawStore
        Processor --> CuratedStore
    end

    subgraph ConsumptionTier ["5. Data Consumers & Sinks"]
        BIApp["BI & Analytical Dashboards"]
        MLApp["Machine Learning Feature Store"]
        ExternalSync["Reverse ETL / Downstream SaaS"]

        CuratedStore --> BIApp
        CuratedStore --> MLApp
        CuratedStore --> ExternalSync
    end

    classDef src fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef buf fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef prc fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef str fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef cns fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class SourceA,SourceB,SourceC src;
    class Buffer buf;
    class Processor prc;
    class RawStore,CuratedStore str;
    class BIApp,MLApp,ExternalSync cns;
```

## PlantUML Specification

```plantuml
@startuml
package "Ingestion Sources" {
  [Application DB]
  [Third-Party APIs]
}
package "Streaming Buffer" {
  queue "Kafka Broker" as kafka
}
package "Transformation" {
  component "Processing Cluster" as spark
}
package "Storage Tiers" {
  database "Raw Store" as raw
  database "Curated Mart" as gold
}
package "Consumption" {
  [BI Reporting]
  [ML Models]
}

[Application DB] --> kafka
[Third-Party APIs] --> kafka
kafka --> spark
spark --> raw
spark --> gold
gold --> [BI Reporting]
gold --> [ML Models]
@enduml
```

## Architectural Design Considerations

* **Start with the Flow**: Map inputs on the left, processing in the center, storage tiers along the boundary, and consumption sinks on the right.
* **Clarify Guarantees**: Annotate whether connections provide At-Least-Once, At-Most-Once, or Exactly-Once delivery semantics.
* **Standardize Color Tokens**: Coral (#fbe9e7) for sources, Yellow (#fff8e1) for streaming buffers, Blue (#e1f5fe) for compute, Purple (#f3e5f5) for storage, and Green (#e8f5e9) for consumers.

## Related Documentation & Patterns

* [Logical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/logical-data-flow.md)
* [Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md)
* [Data Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/checklists.md)
