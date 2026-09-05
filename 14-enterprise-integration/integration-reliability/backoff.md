# Backoff Algorithms and Jitter in Integration Systems

## 1. Mathematical Analysis of Jitter Strategies

```
Attempt 1 -> Base: 100ms
Attempt 2 -> Base: 200ms
Attempt 3 -> Base: 400ms
Attempt 4 -> Base: 800ms
Attempt 5 -> Base: 1600ms
```

Without jitter, 1,000 parallel clients that fail simultaneously will all retry at exactly the same milliseconds (200ms, 400ms, etc.), synchronizing their request spikes and repeatedly crashing the target service.

## 2. Comparison of Backoff Approaches
1. **No Jitter**: Deterministic wait times. Worst performance during outages.
2. **Equal Jitter**: Half deterministic, half random. Keeps minimum floor while smoothing spikes.
3. **Full Jitter (Recommended)**: Completely uniform distribution between 0 and calculated exponential ceiling. Provides optimal de-synchronization across distributed clients.
4. **Decorrelated Jitter**: Next sleep is calculated based on previous sleep. Excellent queue drainage characteristics.
