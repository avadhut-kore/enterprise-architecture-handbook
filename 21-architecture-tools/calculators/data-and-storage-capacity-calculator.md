# Database Storage & Capacity Planning Calculator

## 1. Formulas & Sizing Methodology

### A. Raw Storage Growth Formula
$$\text{Daily Storage} = \text{Rows/Day} \times \text{Avg Row Size (Bytes)} \times (1 + \text{Index Overhead Factor})$$
$$\text{Annual Raw Storage} = \text{Daily Storage} \times 365 \times (1 + \text{Annual Growth Rate})$$

*Typical Index Overhead Factor*: $0.40$ to $0.80$ (40% to 80% of data size).

### B. IOPS & Connection Pool Sizing Formula
$$\text{Target Connections} = (\text{CPU Cores} \times 2) + \text{Effective Spindle Count}$$
$$\text{Required Write IOPS} = \frac{\text{Peak Write TPS} \times \text{Pages Written per Tx}}{\text{Page Cache Hit Ratio Factor}}$$

---

## 2. Reference Benchmark Sizing Table

| Workload Tier | Daily Transactions | Avg Row Size | Daily Volume | 1-Year Storage (w/ Indexes) | Target IOPS |
|---|---|---|---|---|---|
| **Small Enterprise** | 500,000 | 1 KB | 500 MB | ~300 GB | 2,500 IOPS |
| **Medium Scale** | 5,000,000 | 2 KB | 10 GB | ~6 TB | 12,000 IOPS |
| **High-Volume OLTP** | 50,000,000 | 2 KB | 100 GB | ~60 TB | 45,000 IOPS |
| **Planetary Scale** | 500,000,000 | 1.5 KB | 750 GB | ~450 TB | 150,000+ IOPS |
