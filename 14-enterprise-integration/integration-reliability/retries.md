# Retry Strategies in Enterprise Integration

## 1. When to Retry and When NOT to Retry

| HTTP Status / Error | Retryable? | Architectural Rationale |
| :--- | :--- | :--- |
| **500 Internal Server Error** | Conditionally | Only if service is known to fail transiently; risk of overload |
| **502 Bad Gateway / 503 Unavailable** | Yes | Transient routing or restart condition; retry with backoff |
| **504 Gateway Timeout** | Dangerous | Downstream may have already processed state; requires idempotency |
| **400 Bad Request** | NO | Malformed payload; retrying will never succeed |
| **401 / 403 Forbidden** | NO | Authentication/authorization failure; will repeatedly fail |
| **404 Not Found** | NO | Resource does not exist |
| **409 Conflict** | Yes (with jitter)| Optimistic locking conflict; retrying may resolve concurrency |
| **429 Too Many Requests** | Yes | Rate limit hit; respect `Retry-After` header |

## 2. Exponential Backoff with Full Jitter
Linear or immediate retries create the "thundering herd" problem, hammering an already struggling service into complete failure. Retries must incorporate exponential backoff with randomized jitter:

$$t_{retry} = 	ext{random}(0, \min(T_{max}, T_{base} 	imes 2^{attempt}))$$

```python
import time
import random

def execute_with_jitter(attempt: int, base_delay: float = 0.5, max_delay: float = 30.0):
    delay = min(max_delay, base_delay * (2 ** attempt))
    jittered_delay = random.uniform(0, delay)
    time.sleep(jittered_delay)
```

## 3. Safe Retries Require Idempotency
Never configure retries on non-idempotent HTTP methods (`POST`) or state-mutating operations without passing an `Idempotency-Key` header verified by the receiver.
