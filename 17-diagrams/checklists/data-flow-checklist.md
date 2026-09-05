# Data-Flow Architecture Review Checklist

- [ ] Are ingestion buffers (Kafka / Kinesis) implemented to absorb source traffic spikes?
- [ ] Are data processing jobs idempotent and safe to re-run across historical data?
- [ ] Is columnar storage (Parquet / Iceberg) utilized for analytical storage tiers?
- [ ] Are field-level tokenization or redaction pipelines in place for PII/PCI data?
- [ ] Is column-level data lineage tracked using OpenLineage standards?
