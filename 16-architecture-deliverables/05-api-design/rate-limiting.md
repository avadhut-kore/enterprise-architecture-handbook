# API Rate Limiting Standards

## 1. IETF Standard Response Headers
When rate limits are enforced, the response MUST include:
* `RateLimit-Limit`: `1000` (Max allowed requests in window)
* `RateLimit-Remaining`: `942`
* `RateLimit-Reset`: `15` (Seconds until window resets)

When limit is exceeded, return `429 Too Many Requests` with a `Retry-After: 15` header.
