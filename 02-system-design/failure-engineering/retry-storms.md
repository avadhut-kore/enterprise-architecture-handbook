# Retry Storms & Self-Inflicted Outages

## 1. Anatomy of a Retry Storm

A retry storm is a positive feedback loop where client or service retries multiply traffic volume against an already struggling downstream dependency, driving it into complete failure.

```
Normal Traffic: 10,000 QPS
Downstream experiences 10% latency bump
Clients timeout at 1s and retry 3 times
Traffic Surges: 10,000 + (10,000 * 3) = 40,000 QPS!
Downstream completely collapses under 4x traffic.
```

---

## 2. The Golden Rules of Distributed Retries

1. **Exponential Backoff**: Never retry at fixed intervals. Increase delay exponentially:
   $$t_{\text{wait}} = t_{\text{base}} \cdot 2^{\text{attempt}}$$
2. **Full Jitter**: Synchronized retries cause periodic wave spikes. Introduce full randomization:
   $$t_{\text{sleep}} = \text{random}(0, t_{\text{wait}})$$
3. **Retry Budgets**: Limit retries to a maximum percentage of total requests (e.g., retries cannot exceed 10% of total outbound calls across a service).
4. **Never Retry Non-Idempotent Writes Without Keys**: Avoid duplicating charges or records.
