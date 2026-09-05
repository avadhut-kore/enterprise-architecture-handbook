# Job Monitoring & Observability

## 1. Key Performance Indicators (KPIs)
* **Queue Latency (Wait Time)**: Time a job spends waiting in queue before being touched by a worker.
* **Execution Duration**: Time required to process the job.
* **Failure Rate**: Percentage of jobs failing per unit time.
* **Queue Depth / Lag**: Number of unconsumed jobs in the backlog.

---

## 2. KEDA: Queue-Depth Autoscaling
Integrate **KEDA (Kubernetes Event-driven Autoscaling)** to scale worker pods from 0 to 100 based on backlog queue depth:
$$\text{Desired Pods} = \left\lceil \frac{\text{Queue Backlog Depth}}{\text{Target Jobs per Worker}} \right\rceil$$
