# Case Study: DynamoDB Hot-Partition Throttling in High-Heat Sneaker Drop

> **Metadata**: ID: `CS-SCALE-01` | Domain: Scalability / NoSQL | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
A global streetwear and sneaker marketplace launched a highly anticipated limited-edition sneaker drop (5,000 pairs available). Over 450,000 sneakerheads attempted to purchase the item within 60 seconds, generating 52,000 inventory reservation requests per second. The architecture team provisioned 80,000 Write Capacity Units (WCUs) on Amazon DynamoDB, confident that capacity was more than sufficient. However, the database design used the Product SKU as the **Partition Key (`PK = SKU#JORDAN4-RETRO`)**. Because DynamoDB distributes provisioned throughput evenly across underlying physical storage partitions (each capped at a physical limit of **1,000 WCUs/sec**), 98% of the provisioned 80,000 WCUs were wasted on empty partitions, while the single hot partition throttled 98% of shoppers, causing checkout failures, bot exploitation, and a massive brand relations disaster.

---

## 02. Business & System Context
- **Organization**: Global E-Commerce & Sneaker Marketplace ($2B Annual GMV).
- **Core Workflow**: Limited-Release "Flash Drop" Inventory Reservation and Order Placement.
- **Scale**: 450,000 concurrent mobile shoppers; 52,000 reservation attempts/second at T+0.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Principal Data Architect.
- **Key Teams**: Flash Sale Platform Engineering, Cloud Infrastructure, Fraud & Bot Operations.
- **Technology Stack**: AWS Lambda, API Gateway, Amazon DynamoDB (Provisioned Mode).

---

## 04. Requirements & NFRs
- **Peak Throughput**: Process 50,000 reservations/second without throttling.
- **Reservation Latency**: P95 $< 100\text{ ms}$.
- **Zero Overselling**: Exactly 5,000 units sold; absolute inventory accuracy.

---

## 05. Constraints & Assumptions
- **The "Aggregate Throughput" Fallacy**: The engineering team assumed that provisioning 80,000 WCUs globally on a DynamoDB table meant that *any single record* could absorb up to 80,000 writes per second.

---

## 06. Architecture Before: The Single Hot Partition Trap
```mermaid
graph TD
    Shoppers[450,000 Shoppers: 52,000 QPS] --> APIGW[API Gateway]
    APIGW --> Lambda[Checkout Lambda Workers: 5,000 Concurrency]
    
    subgraph DynamoDB Table (80,000 Total Provisioned WCUs across 80 Partitions)
        Lambda -->|PK = SKU#JORDAN4-RETRO (ALL 52,000 QPS)| Partition1[Partition 1: HARD LIMIT = 1,000 WCUs!]
        Empty1[Partition 2: 1,000 WCUs]
        Empty2[Partition 3..80: 78,000 WCUs IDLE]
    end
    
    Partition1 -->|Throttled: 51,000 QPS Dropped!| Error[ProvisionedThroughputExceededException]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **`PK = ProductID / SKU`** | Natural domain key; allowed simple atomic decrements (`ADD inventory -1`). | Concentrated 100% of the flash-sale write volume onto a single physical DynamoDB partition, which has a non-negotiable physical hardware ceiling of 1,000 writes/sec. |
| **Provisioned Capacity Mode (80k WCUs)** | Avoided on-demand throttling during sudden traffic spikes. | The 80,000 WCUs were divided equally across 80 physical partitions ($80,000 / 80 = 1,000\text{ WCU/partition}$). The remaining 79 partitions sat completely idle while Partition 1 burned. |

---

## 08. Timeline
```mermaid
timeline
    title Sneaker Drop Hot Partition Timeline
    09:55 UTC : 80,000 WCUs provisioned on `Inventory` table in preparation for 10:00 drop
    10:00:00 : Drop goes live; 450,000 mobile clients submit reservations simultaneously
    10:00:02 : Write throughput on `PK = SKU#JORDAN4-RETRO` hits 52,000 writes/sec
    10:00:03 : DynamoDB begins throwing `ProvisionedThroughputExceededException` (51k/sec throttled)
    10:00:15 : Lambda worker queues saturate; API Gateway returns HTTP 504 Timeouts
    10:00:45 : Scripted bot networks, retrying at millisecond intervals, capture 85% of the 5,000 pairs
    10:01:30 : Legitimate human shoppers receive "Network Error"; sneakerhead outrage explodes on Twitter
```

---

## 09. Incident Event
At 10:00:00 UTC, the sneaker drop went live. Within 2 seconds, 5,000 Lambda execution environments concurrently invoked `UpdateItem` with an atomic conditional expression decrementing available stock on the single record `SKU#JORDAN4-RETRO`. Because DynamoDB partitions are bounded by a strict internal partition limit of 1,000 WCUs, the storage engine rejected 51,000 requests per second. While legitimate users experienced loading spinners and HTTP 504 timeouts, automated bot networks executing thousands of retries per millisecond slipped through the narrow 1,000 WCU aperture, scooping up 4,200 of the 5,000 pairs.

---

## 10. Symptoms & Evidence
- **Fact**: CloudWatch metric `ThrottledRequests` on the `Inventory` table spiked to **51,200 per second**, while `ConsumedWriteCapacityUnits` hovered at a pathetic **1,000 WCUs**.
- **Fact**: Table utilization efficiency was a dismal **1.25%** ($1,000 / 80,000\text{ WCUs}$), meaning 98.75% of paid cloud capacity was completely idle.
- **Inference**: Distributed NoSQL systems achieve horizontal scalability solely through high-cardinality partition keys. A single hot partition bottlenecks the entire distributed system.

---

## 11. Failure Forensics
```
[450,000 Shoppers hit "Buy Now" at 10:00:00]
                     │
                     ▼
[5,000 Lambda functions execute concurrently]
                     │
                     ▼
[All 5,000 Lambdas hash to SAME partition: Hash(SKU#JORDAN4-RETRO)]
                     │
                     ▼
[DynamoDB Partition 1 physical hardware limit: 1,000 writes/sec]
                     │
  ┌──────────────────┴──────────────────┐
  ▼                                     ▼
[1,000 Writes Succeeded]       [51,000 Writes Throttled / Exception]
                                        │
                                        ▼
                       [HTTP 504 Timeout on Shopper Phones]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why did checkouts fail during the drop?** -> The DynamoDB table returned `ProvisionedThroughputExceededException`.
2. **Why was it throttled when 80,000 WCUs were provisioned?** -> All write requests targeted a single partition key.
3. **Why did all writes target one key?** -> The inventory count for the sneaker was stored in a single database record.
4. **Why was it a single record?** -> The data model used a monolithic counter to prevent overselling.
5. **Why was a distributed counter or partition-sharding pattern not used?** -> Architects misunderstood DynamoDB's internal partition mechanics, assuming provisioned capacity was an unconstrained global pool.

---

## 13. Contributing Factors
- **Bot Amplification**: Un-throttled bot networks flooded the API with retries, consuming the scarce 1,000 WCU capacity and starving human shoppers.
- **Absence of a Virtual Waiting Room**: Traffic hit the transactional database directly rather than passing through an upstream queue (e.g., AWS SQS or Cloudflare Waiting Room).

---

## 14. Architecture After: Write-Sharded Counters & Virtual Waiting Room
```mermaid
graph TD
    Shoppers[450,000 Shoppers] --> Queue[Virtual Waiting Room: Cloudflare / Queue-It]
    Queue -->|Controlled Admission: 800 Users/sec| APIGW[API Gateway]
    
    APIGW --> Lambda[Reservation Service]
    
    subgraph Write-Sharded Inventory (50 Distinct Partitions!)
        Lambda --> ShardRouter{Random Shard ID: 1..50}
        ShardRouter --> Shard1[PK = SKU#JORDAN4_01 (100 units)]
        ShardRouter --> Shard2[PK = SKU#JORDAN4_02 (100 units)]
        ShardRouter --> Shard50[PK = SKU#JORDAN4_50 (100 units)]
    end
    
    subgraph In-Memory Atomic Reservation
        Lambda --> RedisCluster[(Redis Enterprise: Atomic Decr)]
    end
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: Cancelled suspicious bot orders flagged by shipping address clustering; re-released stock via an unannounced raffle.
- **Permanent Architectural Fix**:
  - **Write-Sharded Counters**: Decomposed single inventory records into **50 distributed shards** (`SKU#JORDAN4-RETRO_01` through `_50`), multiplying write throughput capacity by 50x to **50,000 writes/sec** across 50 independent physical partitions.
  - **Redis Atomic In-Memory Reservations**: Shifted the primary flash reservation lock into an in-memory **Redis Cluster** executing atomic Lua scripts, using DynamoDB strictly for asynchronous post-reservation persistence.
  - **Virtual Waiting Room**: Deployed **Cloudflare Waiting Room**, admitting users to checkout in smooth, controlled batches that never exceed downstream capacity.

---

## 16. Business & Technical Impact
- **Brand Reputation**: Negative viral press covered across sneaker blogs and social media.
- **Throughput Multiplier**: Re-tested drop with 50-shard write architecture: achieved **48,000 successful reservations/second with zero throttling**.
- **Bot Mitigation**: Virtual waiting room reduced bot capture rate from 85% to **$< 2\%$**.

---

## 17. What Went Well
- DynamoDB partition auto-splitting algorithms prevented table corruption or data loss despite the intense load.
- SRE dashboards cleanly visualized the hot-partition metric, allowing architects to prove the diagnosis within 10 minutes.

---

## 18. Lessons Learned
- **Architecture**: In distributed NoSQL databases, capacity is not a global pool; it is divided across partitions. If your access pattern is not evenly distributed across partition keys, your effective capacity is limited to that of a single partition.
- **Traffic Shaping**: Never allow raw, unbuffered flash traffic to strike a transactional database. Use virtual waiting rooms to shape the ingress curve.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Audit all DynamoDB tables for single-key write hotspots | Data Arch | Identify hot PKs |
| **30 Days** | Implement write sharding (`key_suffix = rand(1, N)`) on all flash inventory | Commerce Arch | 50k writes/sec capacity |
| **60 Days** | Deploy Cloudflare Waiting Room on all promotional marketing entry points | Edge Lead | 100% traffic shaping |
