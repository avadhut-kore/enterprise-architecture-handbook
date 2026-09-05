# Thread Pool Architecture & Sizing

## 1. Thread Pool Sizing Mathematics
Provisioning too few threads starves throughput; provisioning too many exhausts RAM and causes CPU scheduler thrash.

### The Brian Goetz Thread Pool Formula
$$N_{\text{threads}} = N_{\text{cpu}} \times U_{\text{cpu}} \times \left(1 + \frac{W}{C}\right)$$
Where:
* $N_{\text{cpu}}$ = Number of available CPU cores
* $U_{\text{cpu}}$ = Target CPU utilization ($0 \le U_{\text{cpu}} \le 1$, typically $0.70$)
* $W$ = Average wait time per task (I/O, database, network)
* $C$ = Average compute time per task (CPU processing)

#### Example:
* An 8-core server processing requests with $10\text{ ms}$ compute and $40\text{ ms}$ database wait:
  $$\frac{W}{C} = \frac{40}{10} = 4$$
  $$N_{\text{threads}} = 8 \times 0.70 \times (1 + 4) = 5.6 \times 5 = 28\text{ threads}$$

---

## 2. Queue Sizing & Rejection Policies

```mermaid
flowchart LR
    Tasks[Incoming Tasks] --> Queue[Bounded Queue: Max 500 Items]
    Queue --> Pool[Worker Threads: 28 Threads]
    Queue -->|Queue Full!| Rejection{Rejection Handler}
    Rejection -->|CallerRunsPolicy| Caller[Execute on Submitting Thread (Backpressure!)]
    Rejection -->|AbortPolicy| Throw[Throw RejectedExecutionException]
```

*Architectural Rule*: **Never use unbounded task queues (`LinkedBlockingQueue` without capacity)**. Under traffic surges, unbounded queues accumulate millions of waiting tasks, triggering out-of-memory crashes before rejection policies can protect the service.
