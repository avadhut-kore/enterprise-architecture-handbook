# Architectural Calculator: High Availability & Downtime

## 1. SLA to Downtime Conversion Table

```
+--------------------+-----------------------+-----------------------+-----------------------+
| Availability %     | Downtime / Year       | Downtime / Month      | Downtime / Week       |
+--------------------+-----------------------+-----------------------+-----------------------+
| 99.0% (Two Nines)  | 3.65 days             | 7.30 hours            | 1.68 hours            |
| 99.9% (Three Nines)| 8.76 hours            | 43.8 minutes          | 10.1 minutes          |
| 99.99% (Four Nines)| 52.6 minutes          | 4.38 minutes          | 1.01 minutes          |
| 99.999% (Five Nines| 5.26 minutes          | 26.3 seconds          | 6.05 seconds          |
+--------------------+-----------------------+-----------------------+-----------------------+
```

---

## 2. Series vs Parallel Availability Modeling

### A. Components in Series (Failure in ANY breaks the system)
$$A_{\text{series}} = A_1 \times A_2 \times A_3 \times \dots \times A_n$$
*Example*: Gateway ($99.9\%$) $\times$ Service ($99.9\%$) $\times$ Database ($99.9\%$) = $0.999^3 = 99.7\%$ availability!

### B. Components in Parallel (Redundant failover)
$$A_{\text{parallel}} = 1 - (1 - A_1) \times (1 - A_2)$$
*Example*: Primary DB ($99.9\%$) with Standby Replica ($99.9\%$):
$$A_{\text{parallel}} = 1 - (0.001 \times 0.001) = 1 - 0.000001 = 99.9999\% \text{ (Six Nines)}$$
