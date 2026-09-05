# Kafka Partitioning Strategy

## 1. Sizing Partitions for Throughput
In Apache Kafka, the **Partition** is the base unit of parallelism and physical disk storage. A single partition lives entirely on one broker and cannot be subdivided.

### Universal Throughput Benchmark
* **Write Throughput per Partition**: $\approx 10\text{ MB/s}\text{--}25\text{ MB/s}$.
* **Read Throughput per Partition**: $\approx 25\text{ MB/s}\text{--}50\text{ MB/s}$.

$$\text{Min Partitions Required} = \max\left( \frac{\text{Target Ingress MB/s}}{15\text{ MB/s}}, \frac{\text{Target Egress MB/s}}{30\text{ MB/s}} \right)$$

---

## 2. Partition Key Selection Hazards
* **The Null Key Trap**: If messages are produced with `key=null`, modern Kafka employs sticky partitioning (batching records into random partitions). Concurrency is high, but ordering guarantees are completely lost.
* **Celebrity Hot Partition**: If partitioning by `merchant_id`, a mega-merchant (Amazon / Walmart) generates $80\%$ of all volume, overloading a single partition while other partitions sit idle. *Mitigation*: Salt the partition key (`merchant_id + "_" + random(1, 10)`).
