# 17 — Load Balancing & Traffic Routing Strategy

## Purpose

Load Balancing and Traffic Routing Strategy defines how incoming network traffic from client devices, web browsers, and external APIs is distributed across available compute instances, microservices, and geographic data centers.

The primary goal is to **prevent server overload, minimize latency, maximize hardware utilization, and ensure zero-downtime failover** when individual backend instances or entire availability zones fail.

---

## Problem It Solves

- **Server Hot-Spotting**: Prevents one application server from being overwhelmed with 10,000 connections while adjacent servers sit idle.
- **Single Points of Failure (SPOF)**: Automatically detects dying or unresponsive backend pods and reroutes traffic within milliseconds without user disruption.
- **Geographic Network Latency**: Routes global users to the nearest physical data center or cloud region using Anycast and geo-DNS routing.

---

## Inputs

- **Network Protocol Requirements**: TCP/UDP (L4) vs. HTTP/HTTPS/gRPC (L7).
- **Session State Requirements**: Stateless tokens (JWT) vs. Stateful sticky sessions.
- **Traffic Volume & Surge Multipliers**: Sizing calculations from Step 06.

---

## Decision Process: The Load Balancing Layer Hierarchy

```mermaid
flowchart TD
    User["Global Client Applications"] --> GeoDNS["1. Global Traffic Management (GTM)<br/>Anycast DNS / AWS Route 53<br/>Routes users to the closest healthy cloud region"]
    
    subgraph RegionalVPC["Regional Cloud Ingress (e.g., us-east-1)"]
        GeoDNS --> L4["2. Layer 4 Transport Load Balancer (NLB / IPVS)<br/>TCP / UDP level; handles millions of connections; ultra-high speed"]
        L4 --> L7["3. Layer 7 Application Load Balancer / API Gateway (ALB / Envoy / NGINX)<br/>HTTP/HTTPS / gRPC level; path routing, TLS termination, header inspection"]
        
        subgraph ComputeTier["Application Worker Pods"]
            L7 --> Pod1["Worker Pod 1"]
            L7 --> Pod2["Worker Pod 2"]
            L7 --> Pod3["Worker Pod 3"]
        end
    end
```

---

## Layer 4 vs. Layer 7 Load Balancing

| Architectural Vector | Layer 4 Load Balancing (NLB / IPVS) | Layer 7 Load Balancing (ALB / Envoy / Kong) |
|:---|:---|:---|
| **OSI Layer** | Layer 4 (Transport Layer: TCP / UDP) | Layer 7 (Application Layer: HTTP, HTTPS, gRPC, WebSockets) |
| **Payload Inspection**| None; packet bytes are routed blindly based on IP and port | Full inspection of HTTP headers, cookies, query parameters, path |
| **Throughput & Latency**| Extreme throughput; microsecond latency; ultra-low CPU | Higher CPU consumption; adds 1–5ms for TLS and header parsing |
| **Routing Intelligence**| Simple: IP hash, Round Robin, Least Connections | Sophisticated: Path-based (`/orders` vs `/billing`), Host-based, Canaries |
| **TLS Termination** | Passes raw encrypted TCP bytes to backends, or basic TLS offload | Full TLS 1.3 termination, certificate management, mTLS inspection |
| **gRPC Multiplexing** | Poor (Pins all multiplexed RPCs to a single backend pod) | Native (Distributes individual gRPC RPC streams across pods) |

---

## Load Balancing Algorithms Compared

```mermaid
mindmap
  root((Load Balancing Algorithms))
    Static Algorithms
      Round Robin (Sequential rotation across servers)
      Weighted Round Robin (Allocates traffic by server capacity/CPU)
      IP Hash (Pins client IP to specific server for session affinity)
    Dynamic Algorithms
      Least Connections (Routes to server with lowest active TCP count)
      Least Response Time (Routes to server with fastest TTFB latency)
      Peak EWMA (Exponentially Weighted Moving Average of latency)
    Distributed Routing
      Consistent Hashing (Minimizes cache thrashing during server add/remove)
```

1. **Round Robin**: Distributes requests sequentially. Ideal only when all backend servers have identical hardware and all requests require identical processing time.
2. **Least Connections**: Dynamically routes to the server currently handling the fewest active connections. **The recommended default for long-lived HTTP/1.1 or WebSocket connections.**
3. **Peak EWMA (Exponentially Weighted Moving Average)**: Tracks real-time latency percentiles; routes traffic away from servers experiencing garbage collection (GC) pauses or disk I/O wait.

---

## Health Checks & Graceful Drain Mechanics

A load balancer is only as effective as its health-checking mechanism:

```mermaid
sequenceDiagram
    autonumber
    participant LB as Application Load Balancer
    participant Pod as Worker Pod (K8s)

    loop Every 5 Seconds
        LB->>Pod: GET /health/ready
        Pod-->>LB: HTTP 200 OK (Ready to accept traffic)
    end

    Note over Pod: Deploying new release: SIGTERM received!
    Pod->>Pod: Switch /health/ready to return HTTP 503
    LB->>Pod: GET /health/ready
    Pod-->>LB: HTTP 503 Service Unavailable
    Note over LB,Pod: DEREGISTRATION DELAY (Draining Traffic)
    LB->>LB: Stop routing NEW requests to Pod!
    Note over Pod: Pod completes in-flight requests for 30s
    Pod->>Pod: Process terminates cleanly with zero 5xx errors!
```

---

## Important Probing Questions

- *Are client sessions strictly stateless (JWT), or does the architecture require sticky sessions? (Sticky sessions degrade load distribution).*
- *How does the load balancer handle gRPC over HTTP/2? (Requires L7 load balancing to avoid pinning all traffic to one pod).*
- *What is the configured health check timeout, retry count, and deregistration delay?*
- *Is Cross-Zone Load Balancing enabled to distribute traffic evenly across Availability Zones?*

---

## Common Mistakes

- **Routing gRPC over L4 Load Balancers**: Placing a TCP-level L4 load balancer in front of gRPC microservices. Because HTTP/2 multiplexes all requests across a single persistent TCP connection, L4 routes **100% of all client requests to a single backend pod**, leaving the rest completely idle.
- **Overly Aggressive Health Checks**: Setting health probes to execute every 500ms with a 1-strike failure threshold, causing transient network blips to eject healthy servers and trigger cascading cluster collapse.
- **Deep Health Check Cascades**: Writing health checks that query the primary database, Redis, and downstream payment APIs. If a downstream payment gateway goes down, the health check fails, **causing the load balancer to kill all application web pods**! (Health checks must evaluate only local pod readiness).

---

## Trade-offs

| Load Balancer Tier | Advantage | Trade-Off / Cost |
|:---|:---|:---|
| **Layer 4 (NLB)** | Massive throughput (millions of connections); ultra-low latency. | Zero application-layer routing intelligence; cannot inspect HTTP headers. |
| **Layer 7 (ALB / Envoy)**| Rich path routing, header-based canaries, TLS offloading, WAF integration. | Higher latency overhead; higher CPU and cloud infrastructure cost. |

---

## Production Considerations

- Deploy **Envoy / Service Mesh Sidecars** for internal microservice-to-microservice RPC to achieve client-side L7 load balancing with sub-millisecond overhead.
- Ensure all backend pods implement separate **`/health/live` (Liveness)** and **`/health/ready` (Readiness)** endpoints.
