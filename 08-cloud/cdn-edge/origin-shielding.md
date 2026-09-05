# Origin Shielding & Protecting Backends from Cache Stampedes

## Executive Summary

When a popular cached object expires across 450 edge locations simultaneously, hundreds of edge PoPs issue simultaneous backend origin fetches. This **Cache Stampede (Thundering Herd)** can overwhelm origin load balancers and crash databases.

---

## 1. Origin Shield Architecture

```mermaid
graph TD
    subgraph Edge PoPs Worldwide
        PoP1[Edge PoP: Tokyo]
        PoP2[Edge PoP: Sydney]
        PoP3[Edge PoP: London]
        PoP4[Edge PoP: Frankfurt]
    end

    subgraph Mid-Tier Regional Cache
        Shield[Origin Shield: Centrally Located in Virginia]
    end

    subgraph Cloud Origin
        Origin[Production Origin: ALB / Aurora Database]
    end

    PoP1 --> Shield
    PoP2 --> Shield
    PoP3 --> Shield
    PoP4 --> Shield

    Shield ==>|SINGLE Consolidated Request to Origin!| Origin
```

---

## 2. Collapse Forwarding / Request Coalescing

- **Collapse Forwarding**: When 100 concurrent requests for the identical uncached URL hit an Origin Shield simultaneously, the shield holds 99 requests in memory and sends **exactly one request** to the origin server.
- Once the origin responds, the single response satisfies all 100 waiting client requests, reducing origin traffic spikes by 99%.
