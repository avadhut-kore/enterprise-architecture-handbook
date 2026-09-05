# Database Scaling Architecture

## 1. The Scaling Hierarchy for Persistence Tiers
Scaling relational and distributed databases requires a disciplined progression. Attempting complex distributed sharding before exhausting simpler optimizations introduces catastrophic complexity prematurely.

```mermaid
flowchart TD
    Step1[1. Query & Index Optimization: Eliminate Full Table Scans] --> Step2[2. Caching Tier: Offload 80-95% Reads to Redis]
    Step2 --> Step3[3. Vertical Scale-Up: Maximize CPU, RAM & NVMe IOPS]
    Step3 --> Step4[4. Read-Replicas: Offload Analytical & Secondary Reads]
    Step4 --> Step5[5. Functional Decomposition: Microservice Polyglot DBs]
    Step5 --> Step6[6. Horizontal Sharding: Partition Primary Writes by Shard Key]
```

---

## 2. Read-Replica Topology & Replication Lag

```mermaid
flowchart LR
    App[Application Fleet] -->|All Writes: INSERT/UPDATE/DELETE| Primary[(Primary DB: Master)]
    Primary == Asynchronous WAL Stream ==> Replica1[(Read Replica 1)]
    Primary == Asynchronous WAL Stream ==> Replica2[(Read Replica 2)]
    
    App -->|Read Queries: SELECT| Replica1
    App -->|Read Queries: SELECT| Replica2
```

### The Replication Lag Dilemma
Because WAL replication is asynchronous for performance, read replicas lag behind the primary by $\Delta t$ milliseconds:
$$\text{Replication Lag} = t_{\text{replica\_commit}} - t_{\text{primary\_commit}}$$

*Failure Scenario (Write-then-Read)*:
1. User updates shipping address (writes to Primary).
2. Page refreshes immediately; read request routes to Replica 2.
3. Replica 2 has $150\text{ ms}$ lag; user sees their old shipping address!

### Mitigation Strategies
* **Read-Your-Own-Writes Consistency**: Pin the updating user's reads to the Primary database for 5â€“10 seconds post-mutation.
* **Monotonic Read Routing**: Ensure session affinity routes a specific user to the same replica, preventing time-travel anomalies.
* **GTID / LSN Tracking**: Client tracks the Global Transaction ID (GTID); replica waits until its applied GTID $\ge$ client GTID before serving the read.
