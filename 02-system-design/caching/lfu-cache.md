# Least Frequently Used (LFU) Cache

## 1. Algorithmic Mechanics
LFU evicts keys with the lowest access frequency. It protects popular items that may not have been accessed in the last few minutes from being flushed out by sudden bursts of transient data.

```mermaid
flowchart TD
    Freq1[Freq 1: New Keys] --> NodeX[Key C]
    Freq10[Freq 10: Regulars] --> NodeY[Key B]
    Freq1000[Freq 1000: Viral Item] --> NodeZ[Key A - Protected from Eviction]
```

---

## 2. Frequency Decay (Morris Counter)
In Redis LFU, each key stores an 8-bit logarithmic counter coupled to an access timestamp.
* **Logarithmic Increment**: Counter increments probabilistically; higher values require exponentially more hits to increment.
* **Decay Pacing**: If a key has not been accessed for $N$ minutes, its frequency counter is halved (`lfu-decay-time`), preventing older historical spikes from permanently squatting in RAM.
