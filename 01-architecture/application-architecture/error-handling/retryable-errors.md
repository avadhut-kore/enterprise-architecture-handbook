# Identifying Retryable Errors

## 1. Criteria for Retries
Only retry when the operation is **idempotent** AND the failure is **transient**:
- HTTP 429 (Too Many Requests - check `Retry-After`).
- HTTP 503 (Service Unavailable).
- TCP connection reset / DNS timeout.
