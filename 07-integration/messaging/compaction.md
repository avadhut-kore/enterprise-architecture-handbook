# Kafka Log Compaction

## 1. Key-Based State Retention
By default, Kafka deletes log segments based on time (e.g., 7 days) or size. **Log Compaction** provides a different retention guarantee: **Kafka guarantees to retain the latest known value for every single primary key indefinitely**.

```mermaid
flowchart TD
    subgraph Dirty Log Segment [Before Compaction]
        K1_V1[Key: K1, Val: V1]
        K2_V1[Key: K2, Val: V1]
        K1_V2[Key: K1, Val: V2]
        K1_V3[Key: K1, Val: V3]
    end

    subgraph Clean Log Segment [After Compaction]
        K2_Final[Key: K2, Val: V1]
        K1_Final[Key: K1, Val: V3 - Latest Value Retained!]
    end
    
    Dirty Log Segment -->|Background Cleaner Thread| Clean Log Segment
```

---

## 2. Deleting Data: Tombstone Records
To permanently delete a key in a compacted topic, a producer writes a **Tombstone Record** (a message with the target key and a `null` payload).
* Consumers receiving the tombstone delete the key from their local caches.
* After `delete.retention.ms` elapses, Kafka's background cleaner permanently erases the tombstone and key from disk.
