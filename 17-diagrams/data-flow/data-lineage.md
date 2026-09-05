# Data Lineage & Column-Level Governance Architecture

OpenLineage metadata tracing architecture capturing complete end-to-end data provenance from raw ingestion to column-level analytical outputs.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph PipelineNodes ["Instrumented Pipeline Steps"]
        Job1["Airflow: ingest_stripe_charges"]
        Job2["Spark: cleanse_and_mask_pii"]
        Job3["dbt: build_fct_monthly_revenue"]
    end

    subgraph OpenLineageEmitters ["OpenLineage Standardized Events"]
        E1["START / COMPLETE Event<br/>(Inputs: Stripe API, Outputs: s3://raw/charges)"]
        E2["START / COMPLETE Event<br/>(Inputs: s3://raw, Outputs: s3://silver/charges)"]
        E3["START / COMPLETE Event<br/>(Inputs: s3://silver, Outputs: snowflake.fct_revenue)"]

        Job1 -.-> E1
        Job2 -.-> E2
        Job3 -.-> E3
    end

    subgraph MetadataHub ["Lineage & Catalog Hub (Marquez / Apache Atlas)"]
        LineageAPI["OpenLineage Ingestion HTTP API"]
        GraphDB[("Lineage Metadata Graph DB<br/>(Dataset & Job Dependency DAG)")]
        CatalogUI["Enterprise Governance UI (DataHub / Collibra)"]

        E1 --> LineageAPI
        E2 --> LineageAPI
        E3 --> LineageAPI
        LineageAPI --> GraphDB
        GraphDB --> CatalogUI
    end

    subgraph ImpactAnalysis ["Architectural Governance Use Cases"]
        U1["Column-Level Impact Analysis (Upstream Schema Change)"]
        U2["Regulatory Audit (GDPR Article 30 Compliance Proof)"]
        U3["Data Quality Incident Root Cause Tracing"]

        CatalogUI --> U1
        CatalogUI --> U2
        CatalogUI --> U3
    end

    classDef job fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef evt fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef hub fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    class Job1,Job2,Job3 job;
    class E1,E2,E3 evt;
    class LineageAPI,GraphDB,CatalogUI hub;
```

## PlantUML Specification

```plantuml
@startuml
package "ETL Execution" {
  component "Airflow DAG" as dag
  component "Spark Job" as spark
  component "dbt Model" as dbt
}
package "Lineage Telemetry" {
  component "OpenLineage Collector" as col
  database "Lineage Graph (Marquez)" as graph
}
package "Enterprise Catalog" {
  component "DataHub / Collibra" as ui
}

dag -> col : Emit Run Event
spark -> col : Emit Dataset In/Out Event
dbt -> col : Emit Column Lineage Event
col -> graph : Store Lineage DAG
graph -> ui : Visualize End-to-End Data Journey
@enduml
```

## Architectural Design Considerations

* **Standardized Metadata**: Adopt the OpenLineage open standard to ensure lineage instrumentation is portable across Airflow, Spark, dbt, and Flink.
* **Column-Level Lineage**: Capture precise column transformations (e.g., `revenue = price * quantity - discount`) to allow comprehensive impact analysis before altering upstream tables.
* **Automated Failure Alerting**: Automatically notify downstream data consumers whenever upstream ingestion pipelines fail or experience significant schema drift.

## Related Documentation & Patterns

* [Modern ELT](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/elt.md)
* [PII Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/pii-flow.md)
* [Data Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/checklists.md)
