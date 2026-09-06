# Architecture Estimation Case Studies & Practice Exercises

> 8 fully worked, production-grade estimation case studies covering consumer internet, enterprise platforms, real-time messaging, video streaming, enterprise search, GenAI, and observability economics.

---

## Exercise Catalog

1. [Exercise 1: Design for 1M Daily Active Users (B2C SaaS)](#exercise-1-design-for-1m-daily-active-users-b2c-saas)
2. [Exercise 2: Design for 100M Requests / Day (API Platform)](#exercise-2-design-for-100m-requests--day-api-platform)
3. [Exercise 3: 5-Year Storage Sizing for Global E-Commerce Orders](#exercise-3-5-year-storage-sizing-for-global-e-commerce-orders)
4. [Exercise 4: Global Real-Time Notification Engine](#exercise-4-global-real-time-notification-engine)
5. [Exercise 5: Video Streaming Platform (Egress & CDN)](#exercise-5-video-streaming-platform-egress--cdn)
6. [Exercise 6: Enterprise Search Platform (Elasticsearch / OpenSearch)](#exercise-6-enterprise-search-platform-elasticsearch--opensearch)
7. [Exercise 7: Enterprise GenAI / LLM Assistant Platform](#exercise-7-enterprise-genai--llm-assistant-platform)
8. [Exercise 8: Centralized Observability & Telemetry Costs](#exercise-8-centralized-observability--telemetry-costs)

---

### Exercise 1: Design for 1M Daily Active Users (B2C SaaS)

* **Prompt**: Estimate the traffic, compute, database, and cache requirements for a productivity SaaS application with 1 Million DAU.
* **Assumptions**:
  * Users visit 3 times/day. Each session executes 15 reads and 2 writes.
  * Average read payload: 4 KB. Average write payload: 1 KB.
* **Calculations**:
  * **Daily Requests**: $1\text{M} \times 17 = 17\text{ Million requests/day}$.
  * **Average RPS**: $\frac{17,000,000}{86,400} \approx \mathbf{200\text{ RPS}}$.
  * **Peak RPS (3x)**: $200 \times 3 = \mathbf{600\text{ Peak RPS}}$ (530 Read RPS, 70 Write RPS).
  * **Ingress Bandwidth**: $70 \times 1\text{ KB} = 70\text{ KB/sec} \approx 0.56\text{ Mbps}$.
  * **Egress Bandwidth**: $530 \times 4\text{ KB} = 2,120\text{ KB/sec} \approx 17\text{ Mbps}$.
  * **Daily Storage**: $2\text{M writes} \times 1\text{ KB} \approx 2\text{ GB/day} \rightarrow \mathbf{730\text{ GB/year}}$.
  * **Cache Working Set (20%)**: $2\text{ GB} \times 0.20 \times 30\text{ days} \approx \mathbf{12\text{ GB RAM}}$ (Easily fits in a single Redis instance).
* **Architectural Implication**:
  * A single managed relational database (e.g., PostgreSQL on AWS RDS `db.m6g.large`) with one read replica can easily handle 600 Peak RPS and 730 GB/year. **No sharding or complex NoSQL needed!**

---

### Exercise 2: Design for 100M Requests / Day (API Platform)

* **Prompt**: Size an enterprise B2B API gateway receiving 100 Million daily calls.
* **Assumptions**:
  * Uniform distribution during business hours (12-hour active window).
  * Payload: 2 KB request, 10 KB response.
* **Calculations**:
  * **Average RPS during active window**: $\frac{100,000,000}{12 \times 3,600} = \frac{100,000,000}{43,200} \approx \mathbf{2,315\text{ RPS}}$.
  * **Peak RPS (2x)**: $\approx \mathbf{4,630\text{ Peak RPS}}$.
  * **Network Egress**: $4,630 \times 10\text{ KB} = 46.3\text{ MB/sec} = \mathbf{370\text{ Mbps}}$.
  * **Compute Sizing**: At 600 RPS per vCPU for a lightweight proxy (Kong / Envoy), we need $\frac{4,630}{600} \approx 8\text{ vCPUs}$.
* **Architectural Implication**:
  * 3 Gateway pods (2 vCPU each) behind an Application Load Balancer can comfortably process this load with $N+1$ redundancy.

---

### Exercise 3: 5-Year Storage Sizing for Global E-Commerce Orders

* **Prompt**: Estimate 5-year storage for an e-commerce platform processing 10 Million orders per day.
* **Assumptions**:
  * Each order record is 1 KB (order lines, customer ID, payment status, shipping address).
  * 4 secondary indexes per order table (adds 100% index overhead).
  * Triple replication (3 AZs).
* **Calculations**:
  * **Daily Raw Ingestion**: $10\text{M} \times 1\text{ KB} = \mathbf{10\text{ GB/day}}$.
  * **With Index Overhead (2x)**: $10\text{ GB} \times 2 = \mathbf{20\text{ GB/day}}$.
  * **1-Year Storage**: $20\text{ GB} \times 365 = \mathbf{7.3\text{ TB/year}}$.
  * **5-Year Raw Storage**: $7.3\text{ TB} \times 5 = \mathbf{36.5\text{ TB}}$.
  * **Total Replicated Disk (3x)**: $36.5\text{ TB} \times 3 = \mathbf{109.5\text{ TB}}$.
* **Architectural Implication**:
  * $36.5\text{ TB}$ of transactional order data exceeds optimal performance boundaries for a single PostgreSQL instance. Partitioning strategy: Partition by `order_date` (monthly partitions) and shard by `customer_id` or `order_id`. Migrate orders older than 90 days to a historical warehouse (Snowflake / BigQuery).

---

### Exercise 4: Global Real-Time Notification Engine

* **Prompt**: Size a notification system sending 500 Million push notifications and SMS per day.
* **Assumptions**:
  * Peak event: Flash sale where 50 Million notifications must be dispatched within 10 minutes.
* **Calculations**:
  * **Peak Dispatch Throughput**:
    $$\text{Peak RPS} = \frac{50,000,000\text{ notifications}}{600\text{ seconds}} \approx \mathbf{83,333\text{ notifications/second}}$$
  * **Queue Buffering**: Downstream providers (Apple APNs, Google FCM, Twilio) throttle ingestion. If downstream limits us to 20,000/sec, the queue must buffer $50\text{M} - (20,000 \times 600) = 38\text{ Million pending messages}$.
  * **Queue Storage**: $38\text{M} \times 500\text{ bytes} \approx \mathbf{19\text{ GB of queue buffer}}$.
* **Architectural Implication**:
  * A partitioned Kafka topic or RabbitMQ cluster with dedicated worker pools and token-bucket rate limiters is mandatory to buffer spikes without dropping transactional alerts.

---

### Exercise 5: Video Streaming Platform (Egress & CDN)

* **Prompt**: Calculate egress bandwidth and monthly CDN costs for 1 Million concurrent 4K/1080p viewers.
* **Assumptions**:
  * 70% 1080p (4 Mbps), 30% 4K (15 Mbps). Average blended bitrate: $(0.7 \times 4) + (0.3 \times 15) = 7.3\text{ Mbps}$.
* **Calculations**:
  * **Total Egress Bandwidth**: $1,000,000 \times 7.3\text{ Mbps} = \mathbf{7.3\text{ Tbps}}$.
  * **Monthly Data Transferred**:
    $$7.3\text{ Tbps} \times \frac{1\text{ TB}}{8\text{ Tb}} \times 3,600 \times 24 \times 30 \approx \mathbf{2.36\text{ Petabytes/day}} \approx \mathbf{70.8\text{ PB/month}}$$
  * **CDN Cost (at negotiated enterprise rate of $0.008/GB)**:
    $$70,800,000\text{ GB} \times \$0.008 \approx \mathbf{\$566,400/\text{month}}$$
* **Architectural Implication**:
  * Serving this from cloud origin is impossible. Multi-CDN routing (combining Akamai, Fastly, Cloudflare) with edge caching and adaptive bitrate streaming (HLS/DASH) is required.

---

### Exercise 6: Enterprise Search Platform (Elasticsearch / OpenSearch)

* **Prompt**: Size an OpenSearch cluster indexing 2 Billion enterprise documents with sub-second full-text search.
* **Assumptions**:
  * Document size: 2 KB. Indexing overhead (analyzers, inverted index, doc values): 1.8x.
  * Primary shards + 1 replica (2x).
* **Calculations**:
  * **Raw Document Data**: $2\text{B} \times 2\text{ KB} = \mathbf{4\text{ TB}}$.
  * **Indexed Data Size**: $4\text{ TB} \times 1.8 = \mathbf{7.2\text{ TB}}$.
  * **With 1 Replica**: $7.2\text{ TB} \times 2 = \mathbf{14.4\text{ TB}}$.
  * **Storage Headroom (30% free space for Lucene merges)**: $\frac{14.4}{0.70} \approx \mathbf{20.5\text{ TB SSD}}$.
  * **RAM Sizing (Filesystem cache for fast queries)**: Target 50% of indexed primary data in OS page cache: $7.2\text{ TB} \times 0.50 \approx \mathbf{3.6\text{ TB RAM}}$.
* **Architectural Implication**:
  * Cluster Topology: 30 data nodes, each with 128 GB RAM and 1 TB NVMe SSD (`r6gd.4xlarge`).

---

### Exercise 7: Enterprise GenAI / LLM Assistant Platform

* **Prompt**: Estimate compute and token economics for an enterprise AI assistant serving 50,000 employees.
* **Assumptions**:
  * 10,000 daily queries.
  * RAG prompt payload: 2,000 input tokens (system instructions + retrieved vector chunks).
  * Generation payload: 500 output tokens.
* **Calculations**:
  * **Daily Token Volume**:
    * Input Tokens: $10,000 \times 2,000 = \mathbf{20\text{ Million input tokens/day}}$.
    * Output Tokens: $10,000 \times 500 = \mathbf{5\text{ Million output tokens/day}}$.
  * **Hosted LLM API Cost (e.g., GPT-4o / Claude 3.5 Sonnet)**:
    * Input: $20\text{M} \times \$2.50/\text{M} = \$50/\text{day}$.
    * Output: $5\text{M} \times \$10.00/\text{M} = \$50/\text{day}$.
    * Total API Cost: $\$100/\text{day} \approx \mathbf{\$3,000/\text{month}}$.
  * **Self-Hosted Open Weights Alternative (Llama 3 70B on 4x A100/H100 GPUs)**:
    * Dedicated GPU instance run rate: $\approx \$5,000/\text{month}$ per instance.
* **Architectural Implication**:
  * At 10,000 queries/day, **hosted SaaS LLMs are significantly cheaper** than maintaining dedicated self-hosted GPU clusters. Self-hosting only becomes cost-effective when daily volume exceeds 100,000 queries or strict data isolation prohibits public APIs.

---

### Exercise 8: Centralized Observability & Telemetry Costs

* **Prompt**: Size log ingestion and metric storage for a 200-microservice fleet generating telemetry.
* **Assumptions**:
  * 200 microservices running 2,000 total pods.
  * Each pod emits 50 log lines/sec (average line: 500 bytes).
* **Calculations**:
  * **Log Throughput**: $2,000\text{ pods} \times 50\text{ lines/sec} = 100,000\text{ lines/sec}$.
  * **Ingestion Rate**: $100,000 \times 500\text{ bytes} = 50\text{ MB/sec} = \mathbf{400\text{ Mbps}}$.
  * **Daily Log Volume**: $50\text{ MB/sec} \times 86,400 \approx \mathbf{4.32\text{ TB/day}}$.
  * **30-Day Retention**: $4.32\text{ TB} \times 30 \approx \mathbf{130\text{ TB/month}}$.
  * **SaaS Telemetry Bill (Datadog @ $0.10/GB indexed)**:
    $$130,000\text{ GB} \times \$0.10 \approx \mathbf{\$13,000/\text{month}}$$
* **Architectural Implication**:
  * Ingesting 100% of raw debug logs into commercial SaaS will blow the budget. Introduce an **Observability Gateway (OpenTelemetry Collector / Vector)** to sample successful 200 OK logs at 1%, index only warning/error logs, and stream raw logs directly to low-cost S3 Glacier for compliance.

---

## Cross-References

* **Formulas & Conversions**: [`capacity.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/capacity.md)
* **TCO Modeling**: [`cost.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/cost.md)
* **System Design Cases**: [`architecture-interviews/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/architecture-interviews/README.md)
