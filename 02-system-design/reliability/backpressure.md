# Backpressure & Flow Control

## 1. Push vs. Pull Paradigms
* **Uncontrolled Push**: Producers stream data as fast as possible. If consumers cannot keep pace, consumer memory buffers overflow, causing out-of-memory crashes.
* **Reactive Pull (Backpressure)**: Consumers explicitly signal demand to upstream producers, dictating processing volume.

```mermaid
flowchart LR
    Producer[Fast Producer] <-->|Signal: request(n=100) Demand| Consumer[Consumer: Processes 100 items at sustainable rate]
```

---

## 2. Backpressure Signaling Mechanics
1. **TCP Flow Control**: The receiver advertises its available socket buffer size via the TCP Receive Window (`RCV.WND`). When buffer fills, window shrinks to 0, pausing sender transmission.
2. **Reactive Streams Protocol (`request(n)`)**: In Project Reactor / RxJava, consumers request $n$ elements at a time. Producers never push data without explicit consumer credit.
3. **Queue-Depth Pausing**: Kafka consumer fleet pauses partition polling (`consumer.pause()`) when internal downstream queues exceed high-water mark thresholds.
