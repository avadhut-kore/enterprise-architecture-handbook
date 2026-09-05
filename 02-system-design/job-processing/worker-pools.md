# Worker Pools & Concurrency Sizing

## 1. Concurrency Models: Multi-Threading vs. Multi-Processing
* **I/O-Bound Jobs (Calling external APIs, DB exports)**: Use multi-threaded or async event loop worker pools (1 worker process runs 50â€“100 concurrent threads).
* **CPU-Bound Jobs (Image compression, PDF rendering, ML inference)**: Use multi-processing pools where concurrency matches physical CPU cores:
  $$\text{Worker Processes} = \text{Total CPU Cores} - 1$$

---

## 2. Graceful Worker Shutdown (SIGTERM Handling)
When Kubernetes scales down worker pods or deploys new code:
1. Orchestrator sends `SIGTERM`.
2. Worker stops accepting new jobs from the queue.
3. Worker is granted a grace period (e.g., $60\text{ seconds}$) to finish active jobs.
4. If time expires, worker re-queues uncompleted jobs before `SIGKILL`.
