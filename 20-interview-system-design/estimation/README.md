# Architecture Estimation & Capacity Planning

> Practical back-of-the-envelope calculations, order-of-magnitude reasoning, latency numbers every architect must know, and financial capacity modeling.

---

## 1. The Purpose of Back-of-the-Envelope Estimation

In an architecture interview, estimation is **not** an arithmetic test. The interviewer does not care whether your calculation yields $11.57\text{ TB}$ or $12.1\text{ TB}$.

The purpose of estimation is:
1. **Prove Architectural Plausibility**: Can this system fit on a single database node, or does it require a distributed, horizontally sharded cluster?
2. **Identify Bottlenecks Before Designing**: Is the system bound by network bandwidth, disk IOPS, RAM working set, or CPU compute?
3. **Ground Financial Feasibility**: Will this architecture cost $500/month or $500,000/month?

---

## 2. Numbers Every Architect Must Know

### Latency Numbers (Order of Magnitude)

| Operation | Approximate Latency | Real-World Analog (Human Scale: 1 CPU Cycle = 1 sec) |
| :--- | :--- | :--- |
| **L1 CPU Cache reference** | $0.5\text{ ns}$ | 1 second |
| **Branch mispredict** | $5\text{ ns}$ | 10 seconds |
| **L2 CPU Cache reference** | $7\text{ ns}$ | 14 seconds |
| **Mutex lock/unlock** | $25\text{ ns}$ | 50 seconds |
| **Main memory (RAM) reference** | $100\text{ ns}$ | 3.3 minutes |
| **Compress 1 KB with Zstandard** | $2,000\text{ ns} = 2\ \mu\text{s}$ | 1 hour |
| **Read 1 MB sequentially from RAM** | $3,000\text{ ns} = 3\ \mu\text{s}$ | 1.5 hours |
| **Send 2 KB over 1 Gbps network** | $20,000\text{ ns} = 20\ \mu\text{s}$ | 10 hours |
| **Read 1 MB sequentially from NVMe SSD** | $250,000\text{ ns} = 250\ \mu\text{s}$ | 5.8 days |
| **Read 4 KB random from NVMe SSD** | $10,000\text{ ns} = 10\ \mu\text{s}$ | 5.5 hours |
| **Read 1 MB sequentially from Spinning Disk (HDD)** | $20,000,000\text{ ns} = 20\text{ ms}$ | ~8 months |
| **HDD seek time (Random I/O)** | $10,000,000\text{ ns} = 10\text{ ms}$ | ~4 months |
| **Round trip intra-datacenter (same AZ)** | $500,000\text{ ns} = 0.5\text{ ms}$ | 12 days |
| **Round trip cross-AZ (same region)** | $1,000,000\text{ ns} = 1\text{ ms}$ | 24 days |
| **Round trip US East to US West** | $60,000,000\text{ ns} = 60\text{ ms}$ | ~2 years |
| **Round trip transatlantic (NY to London)** | $100,000,000\text{ ns} = 100\text{ ms}$ | ~3.3 years |
| **Round trip transpacific (SF to Sydney)** | $160,000,000\text{ ns} = 160\text{ ms}$ | ~5.3 years |

---

## 3. Powers of Two & Storage Reference

| Power of 2 | Exact Value | Order of Magnitude (Decimal) | Prefix |
| :--- | :--- | :--- | :--- |
| $2^{10}$ | $1,024$ | $\approx 1\text{ Thousand } (10^3)$ | Kilobyte (KB) |
| $2^{20}$ | $1,048,576$ | $\approx 1\text{ Million } (10^6)$ | Megabyte (MB) |
| $2^{30}$ | $1,073,741,824$ | $\approx 1\text{ Billion } (10^9)$ | Gigabyte (GB) |
| $2^{40}$ | $1,099,511,627,776$ | $\approx 1\text{ Trillion } (10^{12})$ | Terabyte (TB) |
| $2^{50}$ | $1,125,899,906,842,624$ | $\approx 1\text{ Quadrillion } (10^{15})$ | Petabyte (PB) |

### Seconds in Time
* 1 minute = $60\text{ seconds}$
* 1 hour = $3,600\text{ seconds}$
* 1 day = $86,400\text{ seconds} \approx \mathbf{100,000\text{ seconds}}$ *(Use $100,000$ for fast mental math!)*
* 1 month = $2.59 \times 10^6\text{ seconds} \approx \mathbf{2.5\text{ Million seconds}}$
* 1 year = $3.15 \times 10^7\text{ seconds} \approx \mathbf{30\text{ Million seconds}}$

---

## 4. The 10-Second Mental Math Rules

1. **Calculate RPS from Daily Volume**:
   $$\text{Average RPS} = \frac{\text{Daily Requests}}{100,000}$$
   * *Example*: 100 Million requests/day $\rightarrow \frac{100,000,000}{100,000} \approx \mathbf{1,000\text{ Average RPS}}$.
2. **Calculate Peak RPS**:
   $$\text{Peak RPS} = \text{Average RPS} \times 2 \text{ to } 5$$
   * *Example*: $1,000 \times 3 = \mathbf{3,000\text{ Peak RPS}}$.
3. **Calculate Daily Storage**:
   $$\text{Daily Storage} = \text{Daily Writes} \times \text{Average Payload Size}$$
   * *Example*: $50\text{M writes/day} \times 2\text{ KB} = 100\text{ GB/day}$.
4. **Calculate 5-Year Storage with Replication ($3\times$)**:
   $$100\text{ GB/day} \times 365 \times 5 \times 3 \approx 100\text{ GB} \times 2,000 \times 3 \approx \mathbf{600\text{ TB}}$.

---

## 5. Submodule Guide

* **[`traffic.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/traffic.md)**: Sizing user concurrency, WebSocket connections, and peak traffic multipliers.
* **[`storage.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/storage.md)**: Sizing disk volume, index bloat, write amplification, and tiering.
* **[`bandwidth.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/bandwidth.md)**: Network throughput, wire formats (JSON vs Protobuf), and egress bandwidth.
* **[`compute.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/compute.md)**: CPU cores, RAM working sets, container density, and runtime sizing.
* **[`database.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/database.md)**: IOPS estimation, connection pools, sharding key boundaries, and read replica count.
* **[`capacity.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/capacity.md)**: The unified end-to-end checklist for synthesizing all capacity dimensions.
* **[`cost.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/cost.md)**: Modeling cloud infrastructure run rate and FinOps unit economics.
* **[`exercises/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/exercises/README.md)**: 8 fully solved real-world estimation case studies.
