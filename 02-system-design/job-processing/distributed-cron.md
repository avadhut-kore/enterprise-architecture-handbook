# Distributed Cron Architecture

## 1. High-Availability Scheduled Execution
Distributed cron ensures that a scheduled job executes **exactly once per scheduled interval**, even across a cluster of 50 servers.

```mermaid
flowchart TD
    subgraph Clustered Servers
        Node1[Server 1: Tries to fire cron at 00:00]
        Node2[Server 2: Tries to fire cron at 00:00]
        Node3[Server 3: Tries to fire cron at 00:00]
    end
    
    Node1 & Node2 & Node3 --> Lock{Distributed Lock: Redis / DB}
    Lock -->|Winner: Node 2 Claims Lock| Fire[Enqueues Single Job to Queue]
    Lock -.->|Node 1 & Node 3 Lose Lock| Skip[Skipped]
```

---

## 2. Distributed Lock with Lease
```sql
-- PostgreSQL Atomic Leader Election for Cron
UPDATE cron_jobs 
SET last_executed_at = NOW(), locked_by = 'node_2'
WHERE job_name = 'nightly_billing' 
  AND (last_executed_at < NOW() - INTERVAL '23 hours' OR last_executed_at IS NULL);
```
* Only one node updates the row atomically, guaranteeing exactly-once scheduling.
