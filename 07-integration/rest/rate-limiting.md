# API Rate Limiting Headers

## 1. Standard IETF RateLimit Headers
When an API Gateway enforces rate limiting, it informs the caller of their quota consumption using standard response headers:

```http
HTTP/1.1 200 OK
RateLimit-Limit: 1000
RateLimit-Remaining: 842
RateLimit-Reset: 15
```

---

## 2. Breached Quota (HTTP 429) Response
When a client exceeds their allocated token bucket rate limit:

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/problem+json
Retry-After: 30

{
  "type": "https://api.enterprise.com/errors/rate-limit-exceeded",
  "title": "Too Many Requests",
  "status": 429,
  "detail": "Quota of 1000 requests per minute exceeded. Retry after 30 seconds."
}
```
