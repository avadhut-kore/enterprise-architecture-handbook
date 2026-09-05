# Case Study: Redis Large-Key Single-Thread Meltdown in Social Gaming

> **Metadata**: ID: `CS-PERF-04` | Domain: Performance / Gaming | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
A global multiplayer mobile gaming platform with 15 Million daily active users suffered an unexpected cascading service failure across its real-time matchmaking cluster. The outage was traced to an architectural anti-pattern: storing the global player leaderboard inside a **single Redis Hash key (`leaderboard:global`) containing 5.2 Million fields (250 Megabytes)**. When a background cron job executed `HGETALL` to calculate hourly seasonal rankings, Redis's single-threaded event loop blocked completely for **4.8 seconds**. The blocked thread caused thousands of concurrent player heartbeat requests to queue up, triggering Redis connection timeouts, pod crash-loops, and disconnecting 2.2 million active gaming sessions.

---

## 02. Business & System Context
- **Organization**: Mobile Social Gaming Studio ($600M Annual Revenue).
- **Core System**: Global Matchmaking, Session Heartbeat, and Leaderboard Service.
- **Scale**: 85,000 operations per second against a 6-node Redis Cluster.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Lead Game Backend Architect.
- **Key Teams**: Game Server Engineering, LiveOps Infrastructure, Cache Reliability Team.
- **Technology Stack**: Go Microservices, AWS ElastiCache for Redis (Cluster Mode Enabled).

---

## 04. Requirements & NFRs
- **Session Latency**: P99 Redis response time $< 2.5\text{ ms}$.
- **Matchmaking SLA**: Match generation completed within $< 3.0\text{ seconds}$.
- **Availability**: 99.95% continuous player connectivity.

---

## 05. Constraints & Assumptions
- **The "Redis is Lightning Fast" Fallacy**: The engineering team assumed that because Redis operates entirely in-memory, querying large data structures would carry zero operational risk.

---

## 06. Architecture Before: The Single-Key Chokepoint
```mermaid
graph TD
    Clients[2.2M Active Players] --> GameServers[Game Server Pods: Go]
    
    subgraph AWS ElastiCache Cluster (6 Shards)
        Shard1[Shard 1: 15% Load]
        Shard2[Shard 2: 12% Load]
        Shard3[Shard 3: 10% Load]
        Shard4[Shard 4: HOT SHARD! 100% CPU]
        Shard5[Shard 5: 14% Load]
        Shard6[Shard 6: 11% Load]
    end
    
    GameServers -->|Normal Heartbeats: 85k QPS| Shard1
    CronJob[Hourly Seasonal Ranking Cron] -->|HGETALL leaderboard:global (250MB!)| Shard4
    
    Note[Single-Threaded Event Loop Frozen for 4.8 Seconds!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **Single Monolithic Key for Leaderboards** | Simple atomic lookups; allowed easy ranking updates using standard Redis hash commands. | Violates Redis single-thread mechanics; a 250MB key cannot be read without monopolizing the CPU core for seconds. |
| **Unbounded `HGETALL` in Production** | Quickest way for the analytics service to dump ranking snapshots. | `HGETALL` is an $O(N)$ command; running it against 5.2M fields blocks the entire Redis shard. |

---

## 08. Timeline
```mermaid
timeline
    title Redis Large-Key Meltdown Timeline
    18:59:50 : Cluster operating normally; Redis P99 latency is 1.1ms
    19:00:00 : Hourly cron job executes: `HGETALL leaderboard:global`
    19:00:01 : Shard 4 CPU core spikes to 100%; event loop ceases processing other commands
    19:00:03 : 18,000 player heartbeat requests queue up in Shard 4 TCP backlog
    19:00:04 : Go game servers reach 3,000ms Redis connection timeout; begin dropping player sessions
    19:00:05 : Redis finally finishes HGETALL (4.8s duration); floods network with 250MB payload
    19:00:10 : 2.2 Million players disconnected globally; client reconnect storm begins
```

---

## 09. Incident Event
At 19:00:00 UTC, a scheduled hourly LiveOps background job issued `HGETALL leaderboard:global` to compute regional badge awards. The key had grown to 5.2 Million fields, weighing 250 Megabytes. Because Redis executes commands sequentially on a single thread, the engine spent 4.8 seconds serializing 5.2 Million hash entries and writing them to the network socket. During those 4.8 seconds, Shard 4 could not process a single read or write. Over 18,000 real-time player heartbeat pings timed out, causing game servers to assume players had disconnected, kicking 2.2 million active gamers out of ongoing competitive matches.

---

## 10. Symptoms & Evidence
- **Fact**: Redis `SLOWLOG` output recorded: `1) (integer) 1042 / 2) (integer) 1711911604 / 3) (integer) 4812040 / 4) 1) "HGETALL" 2) "leaderboard:global"`.
- **Fact**: AWS ElastiCache metric `EngineCPUUtilization` spiked to 100% on Shard 4 while remaining at 12% on all other 5 shards.
- **Inference**: A single large key in Redis destroys horizontal scaling because that key is pinned to exactly one shard's single thread.

---

## 11. Failure Forensics
```
[19:00:00: Background cron executes HGETALL on 250MB Key]
                           │
                           ▼
[Redis Shard 4 Single Thread begins serializing 5.2M elements]
                           │
                           ▼
  [EVENT LOOP COMPLETELY BLOCKED FOR 4,812 MILLISECONDS]
                           │
                           ▼
[18,000 Player Heartbeat Pings arrive on Shard 4 -> QUEUED IN OS BUFFER]
                           │
                           ▼
[Game Servers reach 3,000ms timeout -> Drop Player TCP Sockets]
                           │
                           ▼
  [2.2 Million Active Players Disconnected -> Reconnect Storm]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why did 2.2 million players disconnect?** -> Game servers timed out communicating with the Redis session cache.
2. **Why did Redis time out?** -> Shard 4 was completely unresponsive for 4.8 seconds.
3. **Why was it unresponsive?** -> The single-threaded engine was executing a blocking `HGETALL` command.
4. **Why was `HGETALL` executed?** -> A background analytics cron job needed to calculate hourly tournament winners.
5. **Why was the key so large?** -> The architecture stored the entire global player population in a single un-sharded Redis Hash key instead of partitioned buckets.

---

## 13. Contributing Factors
- **Forbidden Commands in Production**: The operations team had not disabled high-risk $O(N)$ commands like `KEYS`, `HGETALL`, or `FLUSHALL` via Redis configuration.
- **Missing Large-Key Telemetry**: The enterprise did not run automated `redis-cli --bigkeys` scans to audit key size growth.

---

## 14. Architecture After: Sharded Buckets & Non-Blocking Scans
```mermaid
graph TD
    Client[Players / LiveOps] --> GameSvc[Game Microservices]
    
    subgraph Sharded Redis Architecture (Zero Large Keys!)
        GameSvc --> HashRouter{Hash Slot Router: CRC16}
        HashRouter --> Bucket1[Key: leaderboard:bucket:001]
        HashRouter --> Bucket2[Key: leaderboard:bucket:002]
        HashRouter --> BucketN[Key: leaderboard:bucket:128]
    end
    
    subgraph Safe Iteration & Guardrails
        CronJob[Background Analytics] -->|HSCAN: 500 items per cursor tick| ShardedKeys[Sharded Buckets]
        Config[Redis Config] --> Rename[RENAME-COMMAND: HGETALL Disabled!]
    end
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: SREs manually killed the cron job, applied client-side jitter to manage the 2.2M reconnect storm, and renamed `HGETALL` in the Redis configuration to prevent further invocations.
- **Permanent Architectural Fix**:
  - **Bucket Sharding**: Partitioned the monolithic leaderboard into **128 discrete bucketed keys** (`leaderboard:{bucket_id}`) using consistent hashing on player IDs, ensuring no single key exceeds **2 Megabytes**.
  - **Incremental Iteration**: Replaced all $O(N)$ operations with cursor-based **`HSCAN` iterations** processing 500 fields per tick with 2ms pauses, guaranteeing the event loop is never blocked for $> 1\text{ ms}$.
  - **Automated Big-Key Monitoring**: Configured a nightly audit job running `redis-cli --bigkeys` and alerting on Slack if any key exceeds 5MB.

---

## 16. Business & Technical Impact
- **Financial**: Lost estimated $420,000 in in-game microtransaction revenue during the outage.
- **Performance**: Shard 4 CPU dropped from 100% to **14%**; P99 Redis latency stabilized at **1.2ms**.
- **Player Retention**: App Store rating recovered after players were compensated with free in-game currency.

---

## 17. What Went Well
- Redis Cluster did not crash or corrupt memory; it recovered immediately once the blocking operation finished.
- ElastiCache CloudWatch metrics cleanly isolated the issue to Shard 4 within minutes.

---

## 18. Lessons Learned
- **Architecture**: In Redis, your data model *must* account for single-threaded execution. A single massive key will take down an entire cluster regardless of how many shards you provision.
- **Operational Guardrail**: Disable `KEYS`, `HGETALL`, and `SMEMBERS` in production. Always use cursor-based `SCAN` commands.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Disable `HGETALL` and `KEYS` via ElastiCache parameter groups | Lead DBA | 100% parameter lock |
| **30 Days** | Refactor all collections with $> 10,000$ elements to sharded buckets | Game Arch | Max key size $< 2	ext{MB}$ |
| **60 Days** | Deploy automated nightly big-key scanners with Prometheus alerting | SRE Lead | Instant alert if $> 5	ext{MB}$ |
