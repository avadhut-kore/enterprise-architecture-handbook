# Latency Engineering

## 1. Anatomical Breakdown of End-to-End Latency
Latency is the total elapsed time between when a client initiates an action and when the result is fully rendered. In distributed architectures, latency is composite:
$$T_{\text{total}} = T_{\text{DNS}} + T_{\text{TCP\_TLS}} + T_{\text{transit}} + T_{\text{gateway}} + T_{\text{compute}} + T_{\text{db}} + T_{\text{serialization}}$$

```mermaid
sequenceDiagram
    autonumber
    Client->>DNS: Resolve IP (10-50ms)
    Client->>Gateway: TCP Handshake + TLS 1.3 Negotiate (15-60ms)
    Client->>Gateway: HTTP Request Transmission
    Gateway->>App: Microservice Routing (0.5ms)
    App->>Cache: Redis Query (1ms)
    App->>DB: PostgreSQL Query (12ms)
    App->>App: JSON Serialization (2ms)
    App-->>Gateway: HTTP 200 OK
    Gateway-->>Client: Payload Egress Transit (15-50ms)
```

---

## 2. Mathematical Models & Latency Budgeting
When an endpoint's SLO specifies $p99 < 100\text{ ms}$, latency budgeting apportions millisecond allowances across the distributed dependency tree:
$$\sum_{i=1}^{k} \text{Budget}_i \le \text{Target SLO} \times 0.75\text{ (25% Headroom)}$$

### Sample Budget Distribution for $100\text{ ms}$ SLO:
* **Network & Edge CDN**: $35\text{ ms}$ (Speed of light, TLS, last-mile ISP)
* **API Gateway / WAF**: $5\text{ ms}$
* **Application Business Logic**: $10\text{ ms}$
* **Persistence / Cache Tier**: $25\text{ ms}$
* **Buffer Safety Cushion**: $25\text{ ms}$
