# Traffic Estimation: RPS, Peak Factors & Concurrency

> How to translate Daily Active Users (DAU) and Monthly Active Users (MAU) into actionable Queries Per Second (QPS), Peak RPS, and concurrent network connections.

---

## 1. The Core Conversion Funnel

```
Users (DAU / MAU)
  ↓ [Requests per User per Day]
Total Requests / Day
  ↓ [Divide by 86,400 or 100,000 seconds]
Average Requests / Second (RPS)
  ↓ [Multiply by Peak Factor (2x to 5x)]
Peak Requests / Second (Peak RPS)
  ↓ [Read / Write Ratio Split (e.g., 90% Read, 10% Write)]
Read RPS & Write RPS
  ↓ [Average Session Duration / Heartbeat]
Concurrent Connections (WebSockets / HTTP Keep-Alive)
```

---

## 2. Deriving RPS Step-by-Step

### Example 1: B2C Social Application (e.g., Twitter / Instagram)
* **Given**: $500\text{ Million MAU}$, $250\text{ Million DAU}$.
* **Assumptions**:
  * Each active user visits the app $4\text{ times/day}$.
  * Each visit generates $25\text{ read queries}$ (timeline, profile, notifications) and $1\text{ write}$ (post, comment, like).
  * Total queries per active user per day: $100\text{ reads}$, $4\text{ writes} = 104\text{ requests/day}$.
* **Calculations**:
  * **Total Daily Requests**: $250\text{M} \times 104 \approx 26\text{ Billion requests/day}$.
  * **Average RPS**:
    $$\text{Average RPS} = \frac{26,000,000,000}{86,400\text{ sec}} \approx \mathbf{300,000\text{ RPS}}$$
  * **Peak RPS** (Using a $2.5\times$ peak factor for regional evening surges):
    $$\text{Peak RPS} = 300,000 \times 2.5 = \mathbf{750,000\text{ Peak RPS}}$$
  * **Read vs. Write Split**:
    * Read RPS: $750,000 \times \frac{100}{104} \approx \mathbf{720,000\text{ Read RPS}}$
    * Write RPS: $750,000 \times \frac{4}{104} \approx \mathbf{30,000\text{ Write RPS}}$

### Architectural Implication
* 30,000 write RPS exceeds what a single relational database instance can comfortably persist ($~5,000–15,000\text{ writes/sec}$ on standard cloud hardware). Therefore, write sharding, an asynchronous ingestion buffer (Kafka), or a distributed NoSQL datastore (DynamoDB / Cassandra) is **architecturally required**.
* 720,000 read RPS requires an aggressive multi-tiered caching strategy (Edge CDN + Redis Cluster) to prevent the storage tier from collapsing.

---

## 3. Estimating Concurrent Connections (WebSockets / Push)

When designing real-time systems (chat, collaborative editing, ride matching), server sizing is bound by **active open socket connections**, not just HTTP RPS.

### Formula for Concurrent Connections
$$\text{Concurrent Connections} = \text{DAU} \times \text{Peak Active Percentage}$$

* If an app has $50\text{ Million DAU}$, and at peak evening hours, $10\%$ of daily users are active simultaneously:
  $$\text{Peak Concurrency} = 50,000,000 \times 0.10 = \mathbf{5,000,000\text{ concurrent connections}}$$
* **Connection Memory Footprint**:
  * A single TCP connection with TLS and WebSocket framing takes between $10\text{ KB}$ and $30\text{ KB}$ of kernel RAM in Linux.
  * RAM required for $5\text{ Million}$ open connections:
    $$5,000,000 \times 20\text{ KB} = 100,000,000\text{ KB} \approx \mathbf{100\text{ GB of RAM}}$$
* **Server Fleet Sizing**:
  * If using a modern async networking runtime (Go `epoll`, Node.js `libuv`, or Netty on Java), a single 64 GB RAM server can reliably maintain $\approx 500,000\text{ idle WebSocket connections}$.
  * Fleet size required:
    $$\frac{5,000,000}{500,000} = \mathbf{10\text{ Gateway Connection Servers}} (+ 50\%\text{ redundancy for failover} = \mathbf{15\text{ nodes}})$$

---

## 4. Peak Factors & Traffic Multipliers

| System Archetype | Typical Peak Factor | Primary Driver of Spike |
| :--- | :--- | :--- |
| **B2B SaaS / Enterprise Portal** | $1.5\times$ to $2\times$ | Standard business hours (9 AM – 5 PM local time). |
| **Global Consumer Social / Video** | $2\times$ to $3\times$ | Regional evening prime-time relaxation (7 PM – 10 PM). |
| **Food Delivery / Ride Hailing** | $3\times$ to $5\times$ | Lunch rush (12 PM – 1 PM) and dinner rush (6 PM – 8 PM); rain/weather events. |
| **E-Commerce Flash Sale / Ticketing** | $10\times$ to $50\times$ | Exact drop time (e.g., 10:00:00 AM black Friday or concert ticket release). |

---

## 5. Cross-References

* **Bandwidth & Ingress/Egress**: [`bandwidth.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/bandwidth.md)
* **Compute & Server Sizing**: [`compute.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/compute.md)
* **Database & IOPS Sizing**: [`database.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/database.md)
* **Real-World Estimation Exercises**: [`exercises/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/exercises/README.md)
