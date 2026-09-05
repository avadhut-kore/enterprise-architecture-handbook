# Log Routing, Buffering & Ingestion Architecture

## 1. Executive Summary
Application pods must never write logs directly over high-latency network connections to centralized storage. A network glitch on the logging cluster must never stall transaction worker threads.

The enterprise log routing architecture uses an **asynchronous out-of-process pipeline**: applications log to `stdout` -> node-level agents collect and buffer -> regional gateway collectors parse, redact, and route to tiered backends.

---

## 2. Ingestion Pipeline Architecture

```mermaid
graph TD
    subgraph K8s_Pod ["Kubernetes Application Pod"]
        App["App Process"] -->|Non-blocking write| Pipe["stdout / stderr pipe"]
    end

    subgraph Node_Host ["Node Host (DaemonSet Tier)"]
        Pipe --> Kubelet["Container Runtime\n(/var/log/pods/...)"]
        Agent["Node Log Agent\n(FluentBit / Vector / OTel Collector)\n- Reads local log files\n- In-memory ring buffer\n- Disk-backed buffer fallback"]
        Kubelet --> Agent
    end

    subgraph Gateway_Tier ["Regional Ingestion Gateway Fleet"]
        NLB["Network Load Balancer"]
        GW1["Collector Gateway Replica 1"]
        GW2["Collector Gateway Replica 2"]
        
        NLB --> GW1
        NLB --> GW2
    end

    subgraph Destinations ["Multi-Destination Routing"]
        Search[("OpenSearch / Elastic\n(Operational Search: 7d)")]
        Loki[("Grafana Loki / ClickHouse\n(Aggregated Logs: 30d)")]
        S3[("S3 / WORM Vault\n(Compliance Archive: 7yr)")]
    end

    Agent -->|gRPC / TLS Load-Balanced| NLB
    GW1 --> Search
    GW1 --> Loki
    GW1 --> S3
```

---

## 3. Backpressure & Failure Handling Policies

What happens when log volume spikes by $10\times$ during a cascading failure?

| Scenario | Agent Behavior | Application Impact | Architectural Rule |
| :--- | :--- | :--- | :--- |
| **Nominal Operation** | In-memory buffer flushes every 1s or 512KB. | Zero impact (< 0.1% CPU). | Target steady-state latency < 5s from log emission to searchability. |
| **Transient Network Blip** | Agent fails over to local disk-backed buffer (up to 5GB). | Zero impact. | Buffers absorb up to 2 hours of regional network partition. |
| **Catastrophic Pipeline Outage** | Disk buffer reaches 100% capacity. | **Agent drops logs via FIFO drop-oldest policy**. | **Non-Negotiable Rule**: The logging pipeline must drop logs rather than freezing or crashing the business application. |
