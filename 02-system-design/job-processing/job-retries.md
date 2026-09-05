# Job Retries & Failure Backoff

## 1. Transient vs. Fatal Failures
* **Transient (Retryable)**: Network timeout, third-party 503, database deadlock $\rightarrow$ Retry with exponential backoff.
* **Fatal (Non-Retryable)**: Invalid argument, null pointer exception, unauthorized API key $\rightarrow$ Fail fast directly to Dead Letter Queue.

---

## 2. Backoff Equation with Jitter
$$T_{\text{wait}} = \min(T_{\text{max}}, T_{\text{base}} \times 2^{\text{attempt}}) \pm \text{RandomJitter}$$
