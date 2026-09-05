# Content Delivery Network (CDN) Scaling

## 1. The Edge Acceleration Paradigm
A Content Delivery Network (CDN) distributes hundreds of Points of Presence (PoPs) globally, positioning cached content within milliseconds of the end user. CDNs offload $80\%\text{--}95\%$ of internet traffic, shielding origin data centers from massive bandwidth and compute loads.

```mermaid
flowchart LR
    Client[User in Tokyo] -->|5ms Latency| PoP[Tokyo Edge PoP: 90% Cache Hit]
    PoP -.->|Cache Miss: Origin Transit| Shield[Origin Shield: Oregon]
    Shield -.->|Origin Request| Origin[Enterprise Origin DC: US-East]
```

---

## 2. Edge Caching Mechanics & Headers

### HTTP Caching Directives
* `Cache-Control: public, max-age=3600, s-maxage=86400`: Instructs browsers to cache for 1 hour, and shared CDN caches to cache for 24 hours.
* `stale-while-revalidate=60`: Serves stale cached content instantly to the user while asynchronously fetching a fresh copy from origin in the background.
* `stale-if-error=300`: Serves expired cached content if the origin application server returns an HTTP 5xx error.

---

## 3. Origin Shielding & Tiered Distribution
When $200$ global edge PoPs experience a cache miss for the same resource simultaneously, they can launch a "thundering herd" DDoS against origin servers.
* **Origin Shield**: A centralized edge caching layer sitting directly in front of the origin. All regional PoPs query the Origin Shield; only the Shield queries the origin application.
* **Bandwidth Offload Ratio**:
  $$\text{Origin Egress} = \text{Total Edge Egress} \times (1 - \text{PoP Hit Ratio}) \times (1 - \text{Shield Hit Ratio})$$
