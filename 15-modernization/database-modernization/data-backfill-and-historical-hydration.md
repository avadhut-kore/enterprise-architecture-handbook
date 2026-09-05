# High-Volume Data Backfill & Historical Hydration

## 1. Zero-Downtime Backfill Pipeline
Migrating 500 million historical rows without locking active production tables:
1. **Snapshot Phase**: Dump historical records in indexed primary-key chunks (`WHERE id BETWEEN 1 AND 100000`) using read-only secondary replicas.
2. **Streaming Catch-Up**: Start CDC replication *before* beginning the snapshot; buffer real-time updates in Kafka.
3. **Merge & Deduplicate**: Replay buffered CDC events on top of the restored historical snapshot using idempotent `UPSERT` operations.
