# Non-Retryable Errors

## 1. Fail-Fast Failures
Never retry:
- HTTP 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 422 (Unprocessable Entity).
- Domain validation failures.
- Non-idempotent operations without an idempotency key.
