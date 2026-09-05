# HTTP Caching & Conditional Requests

## 1. Directives: `Cache-Control`
* `Cache-Control: public, max-age=3600, s-maxage=86400`: Browsers cache for 1 hour; CDN caches for 24 hours.
* `Cache-Control: no-cache`: Client must revalidate with origin using `ETag` before serving cached content.
* `Cache-Control: no-store`: Sensitive PII / payment data; never write to disk or cache.

---

## 2. Conditional Requests via ETags (HTTP 304 Not Modified)

```mermaid
sequenceDiagram
    autonumber
    Client->>Server: GET /v1/products/42
    Server-->>Client: 200 OK (ETag: "w/33a2f4", Body: 100KB JSON)
    
    Note over Client: Later Request: Revalidate Cache!
    Client->>Server: GET /v1/products/42 (If-None-Match: "w/33a2f4")
    alt Resource Unchanged
        Server-->>Client: HTTP 304 Not Modified (Zero Body: 0KB Transferred!)
    else Resource Modified
        Server-->>Client: HTTP 200 OK (New ETag: "w/99b1c2", Fresh Body)
    end
```
