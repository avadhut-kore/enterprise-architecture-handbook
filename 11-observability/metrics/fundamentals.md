# Metrics Fundamentals: Counters, Gauges, Histograms & Summaries

## 1. Executive Summary
Understanding the mathematical characteristics of metric types is required to prevent incorrect calculations during incident triage. Time-series databases store metrics as streams of timestamped floating-point values identified by a metric name and key-value label pairs:

$$\text{Time Series} = \big( \text{Metric Name}, \{\text{label}_1=\text{val}_1, \dots\}, \big[(t_0, v_0), (t_1, v_1), \dots\big] \big)$$

---

## 2. The 4 Core Metric Types

```mermaid
graph TD
    M[OpenTelemetry / Prometheus Metric Types] --> C[1. Counter\nMonotonically Increasing\nResets to 0 on restart\nUse: rate(), irate()]
    M --> G[2. Gauge\nVariable Real-Time Value\nCan increase or decrease\nUse: Instant value, avg_over_time()]
    M --> H[3. Histogram\nClient-Side Bucketing\nAggregatable across instances\nUse: histogram_quantile()]
    M --> S[4. Summary\nClient-Side Quantiles\nNon-Aggregatable across pods\nUse: Pre-calculated P99]
```

### 1. Counter
* **Behavior**: Cumulative metric representing a single monotonically increasing counter. Its value can only increase or be reset to zero on process restart.
* **Never query raw Counter values directly**: Querying the raw value of `http_requests_total` is meaningless because it depends entirely on how long the container has been running.
* **Correct Mathematical Usage**: Always wrap counters in rate functions:
  $$\text{Per-Second Rate} = \text{rate}(http\_requests\_total[5m])$$
  Prometheus automatically detects counter resets (when the current value is less than the previous value) and adjusts the rate calculation smoothly.

### 2. Gauge
* **Behavior**: Represents a single numerical value that can arbitrarily rise and fall over time.
* **Examples**: Memory usage in bytes (`node_memory_Active_bytes`), active concurrent HTTP connections, Kafka consumer lag, queue depth.
* **Correct Mathematical Usage**: Never apply `rate()` to a Gauge. To smooth out noisy gauge spikes, use moving averages:
  $$\text{Moving Average} = \text{avg\_over\_time}(queue\_depth[10m])$$

### 3. Histogram
* **Behavior**: Samples observations (usually request durations or payload sizes) and counts them into configurable bucket counters, alongside a cumulative count and sum.
* **Bucket Mechanics**: Each bucket is a counter tracking the number of observations $\le$ upper bound ($le$ label).
  ```
  http_request_duration_seconds_bucket{le="0.05"} 1204
  http_request_duration_seconds_bucket{le="0.1"}  3489
  http_request_duration_seconds_bucket{le="0.5"}  8910
  http_request_duration_seconds_bucket{le="+Inf"} 9214
  http_request_duration_seconds_sum               1492.4
  http_request_duration_seconds_count             9214
  ```
* **Aggregation**: Histograms are **fully aggregatable across multiple instances and clusters**. To compute the cluster-wide 99th percentile:
  $$P_{99} = \text{histogram\_quantile}\Big(0.99, \sum \text{rate}(http\_request\_duration\_seconds\_bucket[5m]) \text{ by } (le)\Big)$$

### 4. Summary
* **Behavior**: Calculates configurable $\phi$-quantiles (e.g., P50, P90, P99) directly in-process on the client side over a sliding time window.
* **The Fatal Architectural Flaw**: **Quantiles cannot be mathematically aggregated!**
  $$\text{Average}(P_{99}(\text{Pod A}), P_{99}(\text{Pod B})) \ne P_{99}(\text{Cluster})$$
* **Enterprise Policy**: **Banned for distributed microservices**. Use Histograms instead of Summaries across all distributed multi-instance services.
