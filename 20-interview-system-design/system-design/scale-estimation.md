# Scale Estimation & Capacity Math

## 1. Mental Math Cheat Sheet for System Design

```
+---------------------------+------------------------------------------------+
| Time Conversion           | Value                                          |
+---------------------------+------------------------------------------------+
| Seconds per Day           | 86,400 seconds ≈ 100,000 seconds (for math)    |
| 1 Million requests / day  | ≈ 10 to 12 QPS                                 |
| 100 Million requests / day| ≈ 1,000 to 1,200 QPS                           |
| 1 Billion requests / day  | ≈ 10,000 to 12,000 QPS                         |
+---------------------------+------------------------------------------------+
```

```
+---------------------------+------------------------------------------------+
| Data Storage Scale        | Multiplier                                     |
+---------------------------+------------------------------------------------+
| 1 KB                      | 1,000 Bytes                                    |
| 1 MB                      | 1,000,000 Bytes                                |
| 1 GB                      | 1,000,000,000 Bytes (10^9)                     |
| 1 TB                      | 1,000 GB (10^12)                               |
| 1 PB                      | 1,000 TB (10^15)                               |
+---------------------------+------------------------------------------------+
```

---

## 2. Standard 3-Minute Estimation Template

1. **Traffic**: $\text{DAU} \times \text{Requests per user} / 100,000 = \text{Avg QPS}$. Multiply by $3\times$ for Peak QPS.
2. **Storage**: $\text{Daily Writes} \times \text{Size} \times 365 \times 3 \text{ (replication)} = \text{Annual Storage}$.
3. **Bandwidth**: $\text{Read QPS} \times \text{Payload Size} \times 8 = \text{Egress (Mbps/Gbps)}$.
4. **Memory (Cache)**: $\text{Daily Reads} \times \text{Size} \times 0.20 = \text{RAM Working Set}$.
