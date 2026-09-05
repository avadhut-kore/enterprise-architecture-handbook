# Data Streaming: Stream Joins, Lookups & Temporal Enrichment

## 1. Architectural Purpose & Problem Context
Stream-stream joins (interval joins), stream-table joins (dimension lookups), and managing temporal consistency across asymmetric arrival rates.

---

## 2. Stream Processing Architecture & Windowing Topology

```mermaid
flowchart LR
    SourceStream[Continuous Unbounded Event Stream] --> Watermark[Watermark & Timestamp Extractor]
    Watermark --> WindowEngine[Windowing & State Engine: Flink / Kafka Streams]
    StateStore[(Embedded Local State Store: RocksDB)] <--> WindowEngine
    WindowEngine --> SinkStream[Materialized Analytical Output / Alert]
    WindowEngine -->|Allowed Lateness Exceeded| SideOutput[Late Events Dead-Letter Queue]
```

---

## 3. Production Invariants
- Always use Event Time with realistic watermarking for financial, billing, and analytical computations.
- Ensure stateful stream processing checkpoints are saved to highly durable cloud object storage (S3/GCS).
- Design stream consumers to be idempotent; network rebalances will cause redeliveries of uncommitted batches.
