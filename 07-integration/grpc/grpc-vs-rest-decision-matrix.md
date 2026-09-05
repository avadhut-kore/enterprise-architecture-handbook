# gRPC Architecture: gRPC vs REST Comprehensive Decision Matrix

## 1. Architectural Purpose & Problem Context
Payload efficiency (Protobuf binary vs JSON), browser support challenges (gRPC-Web), latency benchmarks, and enterprise adoption rules.

---

## 2. gRPC Call Lifecycle & Load Balancing Flow

```mermaid
flowchart LR
    Client[gRPC Client Service] -->|HTTP/2 Multiplexed| Envoy[Envoy L7 Load Balancer]
    Envoy -->|mTLS Stream| Server1[Backend Service Instance 1]
    Envoy -->|mTLS Stream| Server2[Backend Service Instance 2]
```

---

## 3. Production Invariants
- Never use L4 (TCP) load balancers for gRPC backends; always use L7 reverse proxies (e.g., Envoy) or client-side round-robin.
- Always attach and propagate gRPC deadlines across all downstream service calls.
- Never change or reuse field numbers in `.proto` files once published to production.
