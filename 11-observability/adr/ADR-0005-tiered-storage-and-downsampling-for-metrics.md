# ADR-0005: Multi-Tiered Storage & Automated Downsampling for Time-Series Data

* **Status**: Accepted
* **Date**: 2026-05-02
* **Deciders**: Infrastructure Architect, Storage Engineering Lead, SRE Lead
* **Technical Story**: [ARCH-OBS-005] Metrics Long-Term Retention & FinOps

---

## Context and Problem Statement
Storing raw 10-second scraped Prometheus metrics for 12 months requires hundreds of terabytes of expensive SSD storage. Historical 6-month capacity planning queries in Grafana frequently time out due to scanning millions of un-compacted time-series chunks.

## Decision Drivers
* Cost-effective 13-month historical retention for seasonal capacity planning.
* Sub-second Grafana dashboard rendering for multi-month queries.
* Automated compaction and downsampling lifecycle.

## Considered Options
1. **Option 1**: Limit Prometheus retention to 15 days; discard historical data.
2. **Option 2**: Retain 100% of raw metrics in SSD-backed persistent volumes.
3. **Option 3**: Deploy **Thanos / Cortex with Automated 3-Tier Storage and Downsampling**.

## Decision Outcome
**Chosen Option**: **Option 3: Thanos with Tiered Storage and Downsampling**.

### Positive Consequences
* **Hot Tier (0-7 Days)**: Retained at 10s raw resolution in local NVMe memory/disk for real-time incident triage.
* **Warm Tier (8-30 Days)**: Compacted and downsampled to 5-minute resolution in cloud object storage (S3).
* **Cold Tier (31-395 Days)**: Downsampled to 1-hour resolution; reduces historical data volume by 99.7%.
* **Cost Savings**: Slashing metrics storage costs by 94% while enabling instantaneous 1-year Grafana trend queries.

### Negative Consequences
* Introduces Thanos Sidecar, Compactor, and Store Gateway operational components to the telemetry cluster.

---

## Links
* Architecture Spec: [`../cost-and-capacity/data-lifecycle.md`](../cost-and-capacity/data-lifecycle.md)
