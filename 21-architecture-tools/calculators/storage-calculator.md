# Architectural Calculator: Storage Capacity & Growth

## 1. Mathematical Formulation

```
Raw Daily Storage = Daily Writes * Average Payload Size (Bytes)
Effective Daily Storage = Raw Daily Storage * Replication Factor (e.g., 3x) * Indexing Overhead (1.3x)
Annual Storage Requirement = Effective Daily Storage * 365 days * (1 + Annual Growth Rate)
```

$$\text{Total Storage} = \sum_{t=1}^{Y} (\text{Daily Writes} \cdot \text{Size} \cdot R \cdot I \cdot 365) \cdot (1 + g)^{t-1}$$

---

## 2. Reference Worksheet (5-Year Projection, 3x Replication, 30% Index Overhead)

```
Assumptions: Payload Size = 2 KB, Writes/Day = 10,000,000 (10M), Annual Growth = 20%
Raw Daily: 10M * 2 KB = 20 GB / day
Effective Daily: 20 GB * 3 (Replication) * 1.3 (Index/Logs) = 78 GB / day
Year 1 Storage: 78 GB * 365 = 28.47 TB
Year 2 Storage: 28.47 TB * 1.20 = 34.16 TB (Cumulative: 62.63 TB)
Year 3 Storage: 34.16 TB * 1.20 = 41.00 TB (Cumulative: 103.63 TB)
Year 5 Cumulative Storage Requirement = ~212 TB
```

---

## 3. Production Safety Buffers

- **High-Water Mark (HWM)**: Never plan storage past 75% raw disk capacity. Once disks exceed 80%, file system write performance drops dramatically and compaction fails.
