# Case Study: 500-Partition Kafka Consumer Rebalance Storm in AdTech

> **Metadata**: ID: `CS-SCALE-04` | Domain: Scalability / Event Streaming | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
A real-time advertising analytics platform processing 450,000 ad impressions/second deployed an Apache Kafka topic with 500 partitions consumed by 100 containerized worker pods. During a live streaming sporting event, a downstream partner API slowed down, causing message processing times to exceed the consumer's configured `max.poll.interval.ms` (300,000ms / 5 minutes). The Kafka Group Coordinator assumed the lagging consumer had died, evicted it from the consumer group, and triggered a **Cluster-Wide Consumer Rebalance**. The rebalance stopped message processing across all 100 pods. When pods resumed, they re-read the same uncommitted messages, exceeded the poll interval again, and entered an infinite **Cascading Rebalance Storm**, completely halting ad revenue attribution for 7 hours.

---

## 02. Business & System Context
- **Organization**: Real-Time Programmatic Advertising Platform ($1.4B Annual Billing).
- **Core Workflow**: Ad Impression Attribution, Click Fraud Detection, and Publisher Bidding Settlement.
- **Scale**: 450,000 events/second across a 500-partition Kafka topic.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Principal Streaming Data Architect.
- **Key Teams**: Ad Ingestion Engineering, Kafka Platform SRE, Data Science Pipeline Squad.
- **Impacted Systems**: Core Ad Attribution Pipeline and Real-Time Billing Engine.

---

## 04. Requirements & NFRs
- **Attribution Latency**: Process ad impressions within $< 3.0\text{ seconds}$ to update real-time bidder budgets.
- **High Throughput**: Sustain 500,000 events/second without consumer lag accumulation.
- **Cluster Stability**: Single pod slowness must never disrupt event consumption across healthy peers.

---

## 05. Constraints & Assumptions
- **The "Eager Rebalance" Default**: The organization used the default **Eager Rebalance Protocol**, which revokes all 500 partitions from all 100 consumers whenever a single consumer joins or leaves the group.

---

## 06. Architecture Before: The Cascading Rebalance Storm
```mermaid
graph TD
    Publishers[Ad Publishers: 450k Events/sec] --> KafkaTopic[Kafka Topic: ad.impressions / 500 Partitions]
    
    subgraph Eager Consumer Group (100 Pods)
        KafkaTopic --> Consumer1[Consumer Pod 1: Slow Partner API]
        KafkaTopic --> Consumer2[Consumer Pod 2..100]
        
        Consumer1 -->|Exceeds max.poll.interval.ms| Coord[Kafka Broker Group Coordinator]
        Coord -->|EVICTS POD 1 & TRIGGERS FULL REBALANCE!| Stop[ALL 100 CONSUMERS REVOKED & FROZEN!]
        Stop --> Resign[Rebalance Takes 45 Seconds -> Lag Accumulates]
        Resign --> Repeat[Next Pod Times Out -> REPEAT REBALANCE LOOP!]
    end
    
    Note[Total Pipeline Paralysis for 7 Hours!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **Heavy Synchronous Processing inside `poll()` Loop** | Simple sequential code: consumer fetched records, called external fraud API, and committed offset. | If external API slowed down, processing time exceeded `max.poll.interval.ms`, causing the broker to classify healthy consumers as dead. |
| **Default Eager Rebalance Protocol** | Default setting in Kafka client library. | "Stop-the-world" rebalances revoked all 500 partitions every time a rebalance occurred; prevented any processing while assignments were negotiated. |

---

## 08. Timeline
```mermaid
timeline
    title Kafka Rebalance Storm Timeline
    19:00 UTC : Super Bowl live stream begins; ad impression volume surges to 450,000 events/sec
    19:05 UTC : Downstream fraud detection API latency rises from 15ms to 850ms
    19:12 UTC : Consumer Pod #12 spends 5.2 minutes processing 500 records; exceeds `max.poll.interval.ms`
    19:12 UTC : Broker evicts Pod #12; initiates cluster-wide eager rebalance
    19:13 UTC : All 100 pods stop consumption; partitions revoked; rebalance takes 48 seconds
    19:14 UTC : Pods restart; partitions accumulate 25M lagged messages; pods fetch max records and freeze again
    19:20 UTC : Rebalance loop enters infinite cycle: a rebalance occurs every 3 minutes
    02:30 UTC : SREs deploy emergency hotfix enabling Cooperative Sticky Assignor & decoupling poll loop
```

---

## 09. Incident Event
At 19:05 UTC, during a major sporting broadcast, an external third-party fraud scoring API degraded, with latency climbing from 15ms to 850ms. A consumer pod that had polled 500 records in a single batch began processing them sequentially ($500 \times 850\text{ms} = 425\text{ seconds}$). This exceeded the default `max.poll.interval.ms` of 300 seconds (5 minutes). The Kafka broker assumed the pod had crashed and triggered an eager rebalance. All 100 pods were forced to pause processing, drop their assigned partitions, and rejoin the group. Because processing was paused, consumer lag exploded. When pods rejoined, they pulled even larger batches, timed out again, and triggered another rebalance, paralyzing the entire pipeline for 7 hours.

---

## 10. Symptoms & Evidence
- **Fact**: Total Kafka consumer group lag surged from 10,000 messages to **185 Million unread messages**.
- **Fact**: Broker logs recorded 142 consumer group rebalances within a 3-hour window (normally $< 1$ per week).
- **Fact**: Throughput dropped from 450,000 events/sec to **zero** during active rebalance negotiations.
- **Inference**: Synchronously coupling heavy I/O operations inside the single-threaded Kafka `poll()` loop guarantees rebalance storms under downstream latency.

---

## 11. Failure Forensics
```
[External Fraud API latency spikes to 850ms]
                     │
                     ▼
[Consumer Pod #12 takes 425s to process batch -> Exceeds max.poll.interval.ms (300s)]
                     │
                     ▼
[Broker marks Pod #12 dead -> Kicks off Eager Group Rebalance]
                     │
                     ▼
[STOP-THE-WORLD: All 100 Consumers Revoke Partitions & Rejoin]
                     │
                     ▼
[Rebalance negotiation takes 48 seconds -> 21M new messages accumulate]
                     │
                     ▼
[Pods resume -> Fetch massive backlogged batches -> TIME OUT AGAIN!]
                     │
                     ▼
   [INFINITE CASCADING REBALANCE STORM FOR 7 HOURS]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why did the advertising pipeline stop processing events?** -> The Kafka consumer group was trapped in continuous rebalance cycles.
2. **Why were rebalances triggered continuously?** -> Consumer pods were repeatedly evicted for missing the `poll()` deadline.
3. **Why did pods miss the poll deadline?** -> Worker threads were blocked making synchronous HTTP calls to a slow external fraud API.
4. **Why did slow HTTP calls block the poll loop?** -> Polling and message processing executed synchronously on the exact same thread.
5. **Why was consumption designed this way?** -> Developers treated Kafka like an active-mq message queue rather than decoupling the ingestion loop from the worker thread pool.

---

## 13. Contributing Factors
- **`max.poll.records` Sizing**: Default setting fetched 500 records per poll, guaranteeing timeout whenever per-record processing exceeded 600ms.
- **Legacy Eager Assignor**: Using `RangeAssignor` instead of `CooperativeStickyAssignor` forced all partitions to be revoked on every rebalance.

---

## 14. Architecture After: Cooperative Sticky Assignor & Decoupled Workers
```mermaid
graph TD
    Kafka[Kafka Topic: 500 Partitions] --> PollThread[Dedicated Poll Thread: Fast & Lightweight]
    
    subgraph Resilient Decoupled Consumer Pod
        PollThread -->|Calls poll() every 100ms: ALWAYS HEALTHY| InternalQueue[Disruptor / LinkedBlockingQueue]
        InternalQueue --> WorkerPool[Thread Pool: 16 Async Worker Threads]
        WorkerPool --> ExternalAPI[External Fraud API]
        WorkerPool --> CommitMgr[Async Offset Commit Manager]
    end
    
    subgraph Non-Blocking Rebalance
        Protocol[CooperativeStickyAssignor: Rebalance takes < 50ms without stopping healthy partitions!]
    end
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: Scaled down Kafka consumer group to zero; restarted with `max.poll.records = 50` and `max.poll.interval.ms = 900000` (15 minutes), allowing the cluster to stabilize and drain the 185M message backlog over 4 hours.
- **Permanent Architectural Fix**:
  - **Decoupled Polling Architecture**: Completely decoupled the Kafka `poll()` loop from business processing. The polling thread does *nothing* except fetch records and push them into an internal in-memory **Disruptor ring buffer**, calling `poll()` continuously every 100ms. Worker threads process records asynchronously.
  - **Cooperative Sticky Rebalance Protocol**: Migrated to **`CooperativeStickyAssignor`**. Rebalances are now incremental: only partitions being reassigned are paused; healthy consumers processing other partitions continue running without interruption.
  - **Right-Sized Batch Limits**: Capped `max.poll.records` at **100 records**.

---

## 16. Business & Technical Impact
- **Financial**: $2.2M in un-attributed ad impressions that could not be contractually billed to advertisers.
- **Pipeline Stability**: Zero consumer group rebalance storms recorded since the architectural refactoring.
- **Rebalance Duration**: Rebalance negotiation time dropped from 48 seconds to **12 milliseconds**.

---

## 17. What Went Well
- Kafka brokers safely persisted all 185 Million backlog events on disk without a single byte of message loss.
- Once the decoupled consumer hotfix was deployed, the cluster processed the massive backlog at 650,000 events/second.

---

## 18. Lessons Learned
- **Architecture**: Never execute blocking I/O, heavy computation, or third-party network calls inside the Kafka `poll()` loop thread.
- **Protocol Standard**: The Eager Rebalance protocol is an architectural relic. Always use `CooperativeStickyAssignor` for large partition counts.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Enable `CooperativeStickyAssignor` across all enterprise Kafka consumers | Stream Arch | Zero eager rebalances |
| **30 Days** | Mandate decoupled worker thread pools for any consumer calling external APIs | Lead EA | 100% thread decoupling |
| **60 Days** | Configure alerts on `rebalance_latency_avg` and `rebalance_rate` in Prometheus | SRE Lead | Instant storm detection |
