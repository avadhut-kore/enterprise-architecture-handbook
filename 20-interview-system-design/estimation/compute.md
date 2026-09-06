# Compute Sizing: CPU Cores, Memory & Worker Density

> Practical approaches to sizing CPU compute, RAM working sets, container density, thread pools, and async I/O worker concurrency.

---

## 1. The Myth of Universal Formulas

Never present a simplistic equation like *"1 core = 1,000 RPS"* as an absolute law. Real-world compute capacity is strictly dictated by:
1. **Workload Type**: CPU-bound (cryptography, image rendering, ML inference) vs. I/O-bound (CRUD APIs waiting on database queries or external REST calls).
2. **Concurrency Architecture**: Thread-per-request (traditional Java Spring / Tomcat) vs. Event-driven non-blocking async I/O (Node.js, Go goroutines, Java Netty / Virtual Threads).
3. **Internal Processing Latency**: A service that executes in $5\text{ms}$ can process $200\text{ req/sec}$ per single thread; a service that blocks for $200\text{ms}$ can only process $5\text{ req/sec}$ per thread.

---

## 2. Deriving Application Server Fleet Sizing

```
                          Peak RPS Required
                                 ÷
                     RPS Supported per Server Core
                                 =
                        Total CPU Cores
                                 ÷
                       Cores per Node (e.g., 8)
                                 =
                        Baseline Node Count
                                 ×
                 Safety Headroom Multiplier (1.5x - 2x)
                                 =
                   Target Production Server Fleet
```

### Concrete Sizing Example: I/O-Bound Stateless Microservice
* **Target Throughput**: $20,000\text{ Peak RPS}$.
* **Average Service Execution Latency**: $20\text{ms}$ (doing light validation, Redis check, and DB write).
* **Language Runtime**: Go or Java 21+ Virtual Threads (non-blocking I/O).

#### Step 1: Calculate Throughput per Core
* In a non-blocking asynchronous runtime, a single modern cloud vCPU (e.g., AWS Graviton3 or AMD EPYC) spending $2\text{ms}$ of actual on-CPU instruction time per request (with the remaining $18\text{ms}$ spent waiting on network I/O without blocking the thread) can handle:
  $$\text{Throughput per Core} = \frac{1,000\text{ms}}{2\text{ms on-CPU}} \approx \mathbf{500\text{ RPS per vCPU}}$$

#### Step 2: Calculate Required vCPUs
$$\text{Total Cores Needed} = \frac{20,000\text{ RPS}}{500\text{ RPS/core}} = \mathbf{40\text{ vCPUs}}$$

#### Step 3: Map to Container Pods and Nodes
* Deploying as Kubernetes Pods sized at $2\text{ vCPU / 4 GB RAM}$:
  $$\text{Pods Required} = \frac{40}{2} = \mathbf{20\text{ Pods}}$$
* Add **$50\%$ Headroom** for unexpected surges, rolling updates, and AZ failover:
  $$20 \times 1.5 = \mathbf{30\text{ Pods}}$$
* Node Instance Mapping: If hosting on `c6g.4xlarge` worker nodes ($16\text{ vCPU, 32 GB RAM}$), you need:
  $$\frac{60\text{ vCPUs total}}{16\text{ vCPUs/node}} \approx \mathbf{4\text{ Worker Nodes}}$$

---

## 3. Sizing RAM Working Sets & In-Memory Caches

Memory is primarily dictated by **Active Working Set**, not total disk storage.

### The 80/20 Working Set Rule (Pareto Principle)
* In almost all production systems, **$20\%$ of the data generates $80\%$ of the read traffic**.
* To achieve a $95\%+$ cache hit ratio, ensure your in-memory cache (Redis / Memcached) holds at least the **top 20% of daily active entities**.

### Working Set Sizing Example: Social Post Metadata
* Total posts stored on disk: $1\text{ Billion posts}$.
* Total active daily posts queried: $50\text{ Million posts}$.
* Size of cached post metadata: $500\text{ bytes}$.
* Cache Working Set Required:
  $$\text{RAM} = 50,000,000 \times 500\text{ bytes} = 25,000,000,000\text{ bytes} \approx \mathbf{25\text{ GB}}$$
* Add $100\%$ overhead for Redis jemalloc fragmentation, key indexes, and replication buffers:
  $$\text{Provisioned Cache RAM} = 25\text{ GB} \times 2 = \mathbf{50\text{ GB of RAM}}$$
* *Hardware Selection*: A 3-node Redis cluster with $3 \times 32\text{ GB instances}$ easily fulfills this requirement with high availability.

---

## 4. Compute Architecture Comparison

| Model | Concurrency Limit | Memory Overhead | Best Suited For |
| :--- | :--- | :--- | :--- |
| **Process-per-request** (Old Apache / CGI) | Low (~100s) | Extremely High (~10–50 MB per process) | Legacy applications, isolated sandboxes. |
| **Thread-per-request** (Java Tomcat, C# IIS) | Medium (~1,000–5,000) | High (~1 MB thread stack in RAM) | Enterprise business logic, compute-heavy workflows. |
| **Event-Driven / Non-Blocking** (Node.js, Netty) | High (~50,000+) | Low (~few KBs per socket) | High-concurrency I/O proxies, WebSockets, API gateways. |
| **Lightweight Green Threads** (Go goroutines, Java Project Loom) | Very High (~100,000+) | Ultra-Low (~2–4 KB stack, dynamically growing) | Modern cloud-native microservices, streaming pipelines. |

---

## 5. Cross-References

* **Database Connection & IOPS**: [`database.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/database.md)
* **Full Capacity Synthesis**: [`capacity.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/capacity.md)
* **Cloud Infrastructure Cost Modeling**: [`cost.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/cost.md)
