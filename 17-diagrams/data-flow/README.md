# Enterprise Data-Flow Architecture Diagrams

This directory provides standardized, copy-pasteable architectural diagrams and modeling patterns for enterprise data pipelines, streaming topologies, ingestion boundaries, change data capture (CDC), data lakehouse tiers, and compliance-governed flows.

## Data-Flow Diagram Catalog

| Diagram Specification | Primary Focus | Key Technologies / Paradigms |
|:----------------------|:--------------|:-----------------------------|
| [Logical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/logical-data-flow.md) | Business domain flows & boundary transitions | Domain entities, inputs/outputs, business stores |
| [Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md) | Network paths, wire protocols, storage engines | TCP/IP, Kafka, gRPC, JDBC, S3, NVMe |
| [Batch ETL Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/etl.md) | Extract-Transform-Load staging & curation | Apache Spark, Airflow, dbt, staging tables |
| [Modern ELT Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/elt.md) | Extract-Load-Transform in cloud warehouses | Snowflake, BigQuery, dbt, cloud object store |
| [Real-Time Streaming Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/streaming.md) | Low-latency stream processing & windowing | Apache Flink, Apache Kafka, Spark Streaming |
| [Event-Driven Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/event-driven.md) | Choreography, event sourcing & CQRS | Apache Kafka, EventBridge, CloudEvents |
| [Change Data Capture (CDC)](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/cdc.md) | Log-based replication & zero-impact sync | Debezium, Kafka Connect, PostgreSQL WAL |
| [Data Lake Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lake.md) | Multi-tier object storage curation | Raw (Bronze), Standardized (Silver), Curated (Gold) |
| [Data Warehouse Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-warehouse.md) | Dimensional modeling, facts & dimensions | Star schema, Snowflake schema, Data Marts |
| [Modern Lakehouse Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/lakehouse.md) | ACID transactions over cloud storage | Apache Iceberg, Delta Lake, Trino |
| [Operational Data Store (ODS)](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/operational-data-store.md) | Near-real-time operational integration store | MongoDB, PostgreSQL, low-latency sync |
| [Master Data Management (MDM)](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/master-data.md) | Golden record deduplication & survival rules | Entity resolution, master golden catalog |
| [Data Migration Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-migration.md) | Dual-write, shadow verification & cutover | Canary writes, reconciliation engine, rollback |
| [Data Synchronization Topology](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-synchronization.md) | Active-active replication & conflict resolution | CRDTs, last-write-wins (LWW), vector clocks |
| [Data Lineage & Governance](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lineage.md) | Metadata provenance & column-level tracing | OpenLineage, Marquez, Apache Atlas |
| [PII Data Flow & Redaction](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/pii-flow.md) | Sensitive data isolation & field tokenization | GDPR Article 30, Format-Preserving Encryption |
| [Financial Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/financial-data-flow.md) | Double-entry ledger & idempotency pipeline | Exactly-once semantics, strict audit trails |
| [AI / RAG Data Ingestion Pipeline](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/ai-rag-data-flow.md) | Document parsing, chunking, embedding & vectorization | LangChain, LlamaIndex, Pinecone, Milvus |
| [Data-Flow Diagram Template](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/template.md) | Reusable boilerplate for data pipeline modeling | Ingestion -> Processing -> Storage -> Egress |
| [Data Architecture Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/checklists.md) | 35-point audit for throughput, durability & SLA | ARB / Data Governance Sign-off |

## Visual Modeling Conventions
1. **Flow Directionality**: Standardize horizontal flow (Left-to-Right `graph LR`) for pipelines moving from ingestion sources to analytical sinks.
2. **Storage Tier Demarcation**: Group storage tiers (Bronze/Silver/Gold or Raw/Enriched/Serving) within nested subgraphs.
3. **Throughput & Protocol Annotations**: Explicitly document transport semantics (`gRPC`, `Kafka Topic [3x Replication]`, `Parquet / S3`) along connection lines.
