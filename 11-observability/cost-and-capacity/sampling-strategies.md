# Distributed Trace Sampling Strategies: Head vs Tail

## 1. Executive Summary
Storing 100% of distributed trace spans in an enterprise processing billions of requests per day is economically infeasible and operationally unnecessary. 99% of requests are nominal, low-latency successes that contain zero interesting diagnostic data.

Trace sampling is the architectural mechanism used to preserve **100% of high-value traces (errors, extreme latency, business VIPs)** while capturing just enough nominal traces to calculate baseline performance.

---

## 2. Head Sampling vs Tail Sampling

```mermaid
graph TD
    subgraph Head_Sampling ["Head Sampling (Edge / Gateway)"]
        H1["Request arrives at API Gateway"]
        H2{"Random Dice Roll\n(e.g., 5% Probability)"}
        H3["Sample = True\n(Record entire trace)"]
        H4["Sample = False\n(Drop trace immediately)"]
        H1 --> H2
        H2 -->|5%| H3
        H2 -->|95%| H4
        H_Note["Flaw: If a dropped trace subsequently fails at the database\nlayer 500ms later, THE ERROR TRACE IS LOST FOREVER!"]
    end

    subgraph Tail_Sampling ["Tail Sampling (OpenTelemetry Collector Buffer)"]
        T1["Collect 100% of spans in-memory buffer for 30s"]
        T2{"Analyze Completed Trace DAG:\n- Did any span emit status=ERROR?\n- Did duration exceed 2,000ms?\n- Is customer_tier == 'VIP'?"}
        T3["Retain 100% of Errors & Outliers"]
        T4["Probabilistically sample nominal successes at 1%"]
        T1 --> T2
        T2 -->|Matches Anomaly| T3
        T2 -->|Nominal Success| T4
        T_Note["Result: 100% of failure context captured with zero blind spots;\nReduces total trace volume by 90%+!"]
    end
```

---

## 3. Tail Sampling Policy Configuration

```yaml
# /etc/otelcol-contrib/config.yaml
processors:
  tail_sampling:
    decision_wait: 10s       # Wait 10 seconds for all asynchronous spans to arrive
    num_traces: 50000        # In-memory buffer size
    expected_new_traces_per_sec: 2000
    policies:
      # POLICY 1: Preserve 100% of traces with errors
      - name: drop_or_keep_errors
        type: status_code
        status_code: { status_codes: [ ERROR ] }

      # POLICY 2: Preserve 100% of slow traces (> 1.5 seconds)
      - name: latency_outliers
        type: latency
        latency: { threshold_ms: 1500 }

      # POLICY 3: Drop 100% of health check probes
      - name: drop_health_checks
        type: string_attribute
        string_attribute:
          key: http.target
          values: [ "/healthz", "/ready", "/metrics" ]
          enabled_regex_matching: false
          invert_match: true

      # POLICY 4: Probabilistic sample of remaining nominal traces (1%)
      - name: probabilistic_nominal
        type: probabilistic
        probabilistic: { sampling_percentage: 1.0 }
```
