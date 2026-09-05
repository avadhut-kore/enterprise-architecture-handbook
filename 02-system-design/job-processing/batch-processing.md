# Batch Processing Architecture

## 1. Chunking & Streaming Large Datasets
Processing 10 million database rows in a single in-memory collection triggers catastrophic JVM/Node.js Out-Of-Memory crashes.

```mermaid
flowchart TD
    LargeDataset[10 Million Records in Database] --> Chunker[Chunker Cursor: 1,000 Rows per Batch]
    Chunker --> Batch1[Batch 1: 1k Rows]
    Chunker --> Batch2[Batch 2: 1k Rows]
    Chunker --> BatchN[Batch 10,000: 1k Rows]
    
    Batch1 & Batch2 & BatchN --> ParallelWorkers[Parallel Worker Pool]
```

---

## 2. Checkpointing & Resume Capability
Save processing progress in durable storage:
`checkpoint = { last_processed_id: 4892100, completed_at: ... }`.
If the batch worker crashes at record $4,892,100$, the replacement worker resumes from the checkpoint rather than restarting from record 0.
