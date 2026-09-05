# Retry & Idempotency Algorithms
* Use exponential backoff with full jitter: `sleep = rand(0, min(max_sleep, base_sleep * (2 ^ attempt)))`.
