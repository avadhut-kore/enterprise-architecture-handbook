# Data Architecture & Pipeline Review Checklist

This checklist provides a structured 35-point verification framework for Data Architects, Enterprise Architects, and the Architecture Review Board (ARB) to ensure data pipeline reliability, throughput scalability, and compliance integrity.

## 1. Pipeline Architecture & Reliability
- [ ] Are data ingestion boundaries decoupled via distributed streaming buffers (e.g., Kafka, Kinesis) to handle source spikes?
- [ ] Are processing pipelines idempotent (safe to re-execute without creating duplicate records or corrupting state)?
- [ ] Are delivery guarantees explicitly documented (At-Least-Once, Exactly-Once)?
- [ ] Is dead-letter queuing (DLQ) configured for malformed or unprocessable records?
- [ ] Are backpressure handling mechanisms implemented between rapid producers and slower downstream databases?
- [ ] Is stateful stream processing backed by asynchronous incremental checkpointing to durable cloud storage?

## 2. Data Modeling & Storage Strategy
- [ ] Is storage decoupled from analytical compute (e.g., Snowflake, BigQuery, Apache Iceberg over S3)?
- [ ] Are analytical datasets stored in optimized columnar formats (Parquet / ORC) with Snappy compression?
- [ ] Is the data partitioning strategy aligned with dominant query filter predicates to prevent full-table scans?
- [ ] Are historical changes tracked using appropriate Slowly Changing Dimension (SCD Type 2) patterns?
- [ ] Are dimension tables backed by integer surrogate keys rather than volatile operational natural keys?

## 3. Performance, Scalability & SLAs
- [ ] Are end-to-end data latency SLAs defined (e.g., streaming < 2 seconds, batch < 4 hours)?
- [ ] Can batch ETL jobs complete reliably within allocated overnight off-peak maintenance windows?
- [ ] Are connection pools (e.g., PgBouncer, HikariCP) sized to prevent database connection starvation?
- [ ] Are vector search retrieval latencies bounded under 150ms for hybrid AI/RAG applications?

## 4. Governance, Lineage & Metadata
- [ ] Is automated column-level data lineage captured using OpenLineage standards across all pipeline tasks?
- [ ] Are data contracts and schemas version-controlled in an enterprise Schema Registry (Avro / Protobuf)?
- [ ] Are automated schema validation and backward compatibility rules enforced before deployment?
- [ ] Is an enterprise data catalog (DataHub, Collibra) synchronized with pipeline metadata?
- [ ] Are data quality tests (e.g., Great Expectations, dbt tests) executed prior to promoting data to production serving layers?

## 5. Security, Privacy & Compliance
- [ ] Is all data encrypted in flight with TLS 1.3 and at rest with Customer-Managed Keys (CMKs) in KMS?
- [ ] Is sensitive PII, PCI, or PHI data tokenized or masked at the ingestion gateway before entering data lakes?
- [ ] Is there an automated pipeline to fulfill GDPR Article 17 (Right-to-be-Forgotten) deletion requests?
- [ ] Are cross-region replication streams filtered to comply with international data residency regulations?
- [ ] Are database transaction logs (WAL/CDC) protected with strict access controls and audited continuously?
