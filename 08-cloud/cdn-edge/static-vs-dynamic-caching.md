# Static vs Dynamic Caching Architecture

## Executive Summary

Architects must distinguish between caching immutable static assets and caching dynamic, user-personalized API responses.

---

## 1. Caching Behavior Matrix

| Workload Type | Cacheability | Cache Key Components | Optimization Technique |
| :--- | :--- | :--- | :--- |
| **Static Assets (JS/CSS/Images)** | 100% Cacheable | URL path only (`/static/bundle.js`) | Long TTLs (1 year) + unique build hash in filename |
| **Catalog / Read-Heavy APIs** | Cacheable ($5\text{ s} - 5\text{ mins}$) | URL + Query Params (`?category=shoes`) | Micro-caching (5-second TTL eliminates database spikes) |
| **Personalized User APIs** | **Bypass Cache (`no-store`)** | Authorization header, Session cookie | Dynamic acceleration via persistent TCP connection reuse |
| **Authenticated Mutating APIs** | **Bypass Cache (`no-store`)** | POST / PUT / DELETE payloads | Terminate TLS at edge; route over private provider fiber |

---

## 2. Dynamic Content Acceleration

Even when an API payload is dynamic and non-cacheable (`Cache-Control: no-store`), routing traffic through a CDN delivers massive latency improvements:
1. **Edge TLS Termination**: The multi-packet TLS 1.3 handshake completes in $< 20\text{ ms}$ between the user and their local city edge PoP.
2. **Persistent Origin Connection Pools**: The CDN maintains warm, pre-negotiated HTTP/2 or HTTP/3 TCP connections across its private fiber backbone to the cloud origin, avoiding slow-start TCP window ramp-up.
