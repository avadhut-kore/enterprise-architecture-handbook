# Caching Strategies & Topologies

## 1. Topologies: In-Process vs. Distributed Cache

```mermaid
flowchart TD
    subgraph In-Process Local Cache [L1: Caffeine / Guava]
        AppNode1[App Pod 1: RAM <1 microsecond]
        AppNode2[App Pod 2: RAM <1 microsecond]
    end

    subgraph Distributed Remote Cache [L2: Redis Cluster]
        Redis[(Redis Cluster: Network 1ms RTT)]
    end

    AppNode1 & AppNode2 --> Redis
    Redis --> Database[(PostgreSQL Database)]
```

| Dimension | In-Process (L1) Cache | Distributed (L2) Cache |
| :--- | :--- | :--- |
| **Access Latency** | Nanoseconds to Microseconds ($<1\ \mu\text{s}$) | Milliseconds ($0.5\text{--}2.0\text{ ms}$) |
| **Consistency** | Risk of split cache across pods | Single shared source of truth |
| **Capacity** | Constrained by JVM/process RAM | Terabytes across clustered shards |
| **Network Overhead**| Zero | Network hop required |
