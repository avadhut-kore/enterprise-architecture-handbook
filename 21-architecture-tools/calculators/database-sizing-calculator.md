# Architectural Calculator: Database IOPS, CPU & Shards

## 1. Mathematical Formulation

```
Read IOPS = (Read QPS * (1 - Cache Hit Ratio)) * Disk Reads per Query (B-tree depth)
Write IOPS = Write QPS * (1 + Write Amplification Factor from WAL/Indexes)
Total IOPS Required = (Read IOPS + Write IOPS) * IOPS Safety Factor (1.5x)
```

$$\text{Number of Shards} = \max\left(\left\lceil \frac{\text{Total IOPS}}{\text{Max IOPS per Node}} \right\rceil, \left\lceil \frac{\text{Total Storage}}{\text{Max Storage per Node}} \right\rceil\right)$$

---

## 2. Reference Sizing Example

```
Input Requirements:
- Write QPS: 15,000 writes/sec
- Secondary Indexes on Table: 3
- Write Amplification: 4x (1 heap insert + 3 index updates + WAL)
- Required Write IOPS: 15,000 * 4 = 60,000 IOPS
- Cloud EBS gp3 Max IOPS per Volume: 16,000 IOPS

Shard Sizing Calculation:
- Required Nodes = ceil(60,000 IOPS * 1.5 safety / 16,000 IOPS) = ceil(5.625) = 6 Shards
```

---

## 3. Memory & Buffer Pool Sizing

- Size database RAM such that the **active table indexes fit completely in the buffer pool** (`innodb_buffer_pool_size` or Postgres `shared_buffers`).
