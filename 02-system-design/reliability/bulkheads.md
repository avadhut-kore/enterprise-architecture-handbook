# Bulkhead Architecture

## 1. The Nautical Analogy
In naval architecture, bulkheads are watertight partitions dividing a ship's hull. If one compartment is breached by an iceberg, water fills only that single section; the remaining watertight compartments keep the vessel afloat.

```mermaid
flowchart TD
    subgraph Without Bulkheads [Catastrophic Failure]
        SlowAPI[Slow Recommendation API] --> SharedPool[Shared App Thread Pool: 200 Threads]
        SharedPool --> Starve[Core Payment & Checkout Threads Starved -> Total Outage!]
    end

    subgraph With Bulkheads [Resilient Partitioning]
        RecAPI[Recommendation API] --> PoolRec[Bulkhead Pool A: 20 Threads]
        PayAPI[Payment Checkout API] --> PoolPay[Bulkhead Pool B: 100 Dedicated Threads]
    end
```

---

## 2. Bulkhead Implementations
1. **Thread Pool Bulkheads**: Dedicating isolated thread pools with bounded task queues per external dependency.
2. **Semaphore Bulkheads**: Bounding concurrent in-flight requests without thread context switching overhead.
3. **Hardware / Pod Bulkheads**: Isolating Tier-1 enterprise tenants on dedicated Kubernetes node pools.
