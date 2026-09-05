# Data Lifecycle Architecture: Tiered Storage & Downsampling

## 1. Executive Summary
The operational value of telemetry data decays exponentially over time:
- **0 to 24 Hours**: Maximum value (active triage, high-resolution debugging, immediate incident response).
- **1 to 7 Days**: Moderate value (post-incident reviews, weekly capacity planning).
- **30 to 365 Days**: Low operational value (compliance, historical trend reporting, seasonal capacity analysis).

Paying high-performance NVMe SSD prices to store 90-day-old debug logs is an architectural failure. Telemetry pipelines must enforce automated **Tiered Storage Lifecycles**.

---

## 2. The 3-Tier Storage Topology

```mermaid
graph LR
    Ingest["Telemetry Ingest"] --> Hot["1. Hot Tier (NVMe SSD)\n- Resolution: Raw (10s / Full Logs)\n- Retention: 3 to 7 Days\n- Fast Lucene / Memory Queries"]
    Hot -->|Lifecycle Policy (Day 7)| Warm["2. Warm Tier (Standard HDD / Compaction)\n- Resolution: Downsampled (5m step)\n- Retention: 7 to 30 Days\n- Read-Only Indices"]
    Warm -->|Lifecycle Policy (Day 30)| Cold["3. Cold Tier (S3 / GCS / Glacier)\n- Format: Parquet / Zstandard Chunks\n- Retention: 30 to 365 Days\n- Cost: $0.015/GB/month"]
```

---

## 3. Downsampling Mathematics (Prometheus / Thanos)

To preserve multi-month metric trends without retaining billions of raw samples, Thanos and Cortex apply automated compaction and downsampling:

```
Raw Data (10s scrape interval):
[•]--10s--[•]--10s--[•]--10s--[•]--10s--[•]--10s--[•]  (8,640 samples/day/series)

Downsampled 5m Resolution (Retained for 180 Days):
[   • Min / Max / Avg / Count over 5 minutes   ]       (288 samples/day/series -> 96.6% Reduction!)

Downsampled 1h Resolution (Retained for 2 Years):
[   • Min / Max / Avg / Count over 1 hour      ]       (24 samples/day/series -> 99.7% Reduction!)
```

This ensures an engineer querying a 1-year trend in Grafana downloads only 8,760 pre-computed data points instead of 3,153,600 raw samples, rendering graphs instantly while slashing storage costs by $98\%$.
