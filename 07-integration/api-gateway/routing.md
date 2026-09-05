# Dynamic Routing & Traffic Splitting

## 1. Routing Modalities
* **Path-Based Routing**:
  * `/v1/orders/*` $\rightarrow$ Order Service Fleet
  * `/v1/users/*` $\rightarrow$ User Service Fleet
* **Host / SNI Routing**:
  * `api.enterprise.com` $\rightarrow$ Public API Gateway
  * `admin.enterprise.com` $\rightarrow$ Internal Admin Gateway

---

## 2. Canary Traffic Splitting (Weighted Routing)
API gateways facilitate zero-downtime canary deployments by dynamically partitioning traffic based on percentage weights:

```mermaid
flowchart LR
    Ingress[Client Traffic: 10,000 RPS] --> Router{Envoy Weighted Cluster}
    Router -->|95% Traffic: 9,500 RPS| V1[Stable Fleet: Version 1.4]
    Router -->|5% Canary: 500 RPS| V2[Canary Fleet: Version 1.5]
```
