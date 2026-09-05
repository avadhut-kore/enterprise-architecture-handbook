# Job Prioritization Architecture

## 1. Priority Inversion & Queue Starvation
If a single queue processes both high-priority transactional emails (password reset) and low-priority bulk marketing blasts (1,000,000 promotional emails), password resets are delayed by hours.

```mermaid
flowchart TD
    subgraph Multi-Queue Strict Priority
        Q_High[High Priority Queue: Password Reset] --> WorkerPool[Worker Pool: Evaluates High First]
        Q_Med[Medium Priority Queue: Order Confirmations] --> WorkerPool
        Q_Low[Low Priority Queue: Marketing Blast] --> WorkerPool
    end
```

---

## 2. Fair-Share Weighted Worker Allocation
Rather than starving low-priority queues completely:
* Assign dedicated worker ratios: $60\%$ workers to High, $30\%$ to Medium, $10\%$ to Low.
