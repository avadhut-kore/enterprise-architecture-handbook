# Data Migration: Online vs Offline Data Migration Strategies

## 1. Architectural Purpose & Problem Context
Maintenance-window cold offline exports vs zero-downtime hot online continuous replication with incremental catch-up.

---

## 2. Zero-Downtime CDC Migration Topology

```mermaid
flowchart TD
    Legacy[(Source Legacy Database)] --> Snapshot[1. Initial Bulk Snapshot]
    Snapshot --> Target[(Target Modern Database)]
    Legacy -->|2. Continuous WAL Mining CDC| Catchup[CDC Catch-up Engine]
    Catchup --> Target
    Catchup -->|3. Lag Reaches Zero| Cutover[4. Execute Traffic Cutover]
    Target -.->|5. Reverse CDC Replication| Legacy
```

---

## 3. Production Invariants
- Every database migration must have an active reverse replication pipeline enabled for at least 72 hours post-cutover to allow instant zero-loss rollback.
- Never declare a migration complete without running automated 100% row count and checksum reconciliation across all migrated entities.
