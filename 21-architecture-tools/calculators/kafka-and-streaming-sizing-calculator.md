# Apache Kafka & Stream Sizing Calculator

## 1. Formulas & Sizing Methodology

### A. Partition Count Formula
$$\text{Partitions} = \max\left(\frac{\text{Target Producer Throughput (MB/s)}}{\text{Single Partition Write Speed (~10 MB/s)}}, \frac{\text{Target Consumer Throughput (MB/s)}}{\text{Single Consumer Read Speed (~25 MB/s)}}\right)$$

### B. Cluster Retention Disk Storage Formula
$$\text{Total Storage} = \text{Ingress Rate (MB/s)} \times 86,400 \times \text{Retention Days} \times \text{Replication Factor} \times 1.20$$
*(The $1.20$ multiplier reserves 20% disk headroom for OS and compaction overhead).*

---

## 2. Reference Benchmark Sizing Table

| Tier | Msg Rate (msgs/sec) | Avg Msg Size | Ingress MB/s | Partitions | 7-Day Storage (RF=3) |
|---|---|---|---|---|---|
| **Standard Service** | 5,000 | 2 KB | 10 MB/s | 6 | ~22 TB |
| **High-Throughput Bus** | 50,000 | 1 KB | 50 MB/s | 24 | ~108 TB |
| **Clickstream & Telemetry**| 250,000 | 1.5 KB | 375 MB/s | 96 | ~815 TB |
