# Dashboard Design Principles & Cognitive Ergonomics

## 1. Executive Summary
During a high-severity production outage, engineers experience physiological stress: tunnel vision, elevated heart rate, and reduced working memory. Dashboards designed without cognitive ergonomics exacerbate this stress.

Effective dashboard architecture adheres to **The 5-Second Rule**: an on-call engineer glancing at a tier-1 dashboard must be able to determine whether the system is healthy within **5 seconds**, and isolate the failing component within **30 seconds**.

---

## 2. The 4 Principles of Operational Visualization

### 1. Visual Hierarchy (The Inverted Pyramid)
Organize panels strictly by operational urgency from top to bottom:

```
┌────────────────────────────────────────────────────────────────────────┐
│ TOP ROW: Overall Health & Status (Single-Stat Badges / SLO Burn Rate)  │
│ [ System Status: DEGRADED ]  [ Error Budget: 64% ]  [ P1 Active: 1 ]  │
├────────────────────────────────────────────────────────────────────────┤
│ SECOND ROW: Primary Service Symptoms (RED Metrics)                     │
│ [ Incoming QPS (Rate) ] [ Error Ratio % (Errors) ] [ P99 Latency (Dur) ]│
├────────────────────────────────────────────────────────────────────────┤
│ THIRD ROW: Core Infrastructure Saturation (USE Metrics)                │
│ [ CPU / RAM Utilization ] [ DB Pool Saturation ] [ Kafka Lag Records ]  │
├────────────────────────────────────────────────────────────────────────┤
│ BOTTOM ROW: Correlated Logs & Trace Exemplars                          │
│ [ Embedded Top Error Logs ] [ Recent Slow Trace Outliers ]             │
└────────────────────────────────────────────────────────────────────────┘
```

### 2. Semantic Color Consistency
- **Green**: Healthy, nominal operation ($SLO > 99.9\%$).
- **Yellow / Orange**: Warning threshold breached, degradation occurring, action needed during business hours.
- **Red**: Catastrophic failure, error budget fast burning, immediate page active.
- **Blue / Purple**: Contextual metrics (throughput, traffic, total volume) where higher or lower is not inherently good or bad.
- **Rule**: Never use Red for nominal traffic spikes or arbitrary label differentiation.

### 3. Avoid Misleading Scales & Zero-Baseline Invariant
- **Bar and Area charts must always start at zero**. Truncating the Y-axis to start at 95% makes a nominal 1% fluctuation look like a catastrophic 80% cliff.
- **Latency Histograms**: Use logarithmic scales ($y$-axis) only when displaying wide percentile distributions (e.g., comparing P50 at 20ms with P99.9 at 15,000ms).

### 4. Information Density & The "Rule of 12"
A dashboard containing more than **12 to 15 panels** creates cognitive paralysis. Decompose monolithic mega-dashboards into a primary health dashboard that links to specialized drill-down dashboards via dashboard links and template variables.
