# Enterprise Message Queue Throughput Calculator

## 1. Queue Backlog & Drain Time Formula

$$\text{Drain Time (Seconds)} = \frac{\text{Queue Backlog Depth}}{\text{Consumer Workers} \times \text{Msgs/Sec per Worker} - \text{Incoming Ingestion Rate}}$$

---

## 2. Sizing Guidelines
* Set consumer concurrency high enough that `Drain Rate > 2x Peak Ingestion Rate`.
* Configure queue memory high watermark alerts at 70% RAM utilization to prevent disk paging.
