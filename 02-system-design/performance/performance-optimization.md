# Performance Optimization Methodology

## 1. The 6-Step Scientific Optimization Framework
Performance optimization must follow a rigorous, empirical methodology. Optimizing code based on intuition or subjective opinions almost always optimizes non-critical code paths while introducing bugs.

```mermaid
flowchart TD
    M1[1. Profile & Measure: Capture Flamegraphs & Traces] --> M2[2. Identify the Amdahl Bottleneck: Where is 80% time spent?]
    M2 --> M3[3. Formulate Falsifiable Hypothesis: e.g., 'Covering index will reduce p99 by 70%']
    M3 --> M4[4. Apply Single Isolated Optimization]
    M4 --> M5[5. Re-Benchmark under Identical Synthetic Workload]
    M5 --> M6{Did p99 Improve Without Regressing Other Metrics?}
    M6 -->|Yes| Ship[Document ADR & Ship Canary]
    M6 -->|No| Revert[Revert Code & Formulate New Hypothesis]
```

---

## 2. Profiling Tools & Techniques
* **CPU Flamegraphs (Async-profiler / Linux `perf`)**: Visualizes call stack sample frequencies to pinpoint CPU-burning functions.
* **Database Query Profiling**: PostgreSQL `pg_stat_statements`, MySQL Performance Schema, and slow query logs.
* **Distributed Tracing (OpenTelemetry)**: Analyzes waterfall charts across microservice boundaries to locate cross-network latency bottlenecks.
