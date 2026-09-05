# Layer 4 vs Layer 7 Load Balancing Architecture

## Executive Summary

Choosing between **Layer 4 (Transport Layer)** and **Layer 7 (Application Layer)** load balancing dictates network throughput, protocol capabilities, and inspection depth.

---

## 1. Comparative Architecture Matrix

| Architectural Feature | Layer 4 Load Balancer (AWS NLB / Azure Basic LB) | Layer 7 Load Balancer (AWS ALB / Azure Application Gateway) |
| :--- | :--- | :--- |
| **OSI Model Layer** | Transport Layer (TCP, UDP, TLS) | Application Layer (HTTP, HTTPS, HTTP/2, gRPC, WebSockets) |
| **Inspection Depth** | Evaluates only IP headers and TCP/UDP port numbers. | Parses complete HTTP request: URL path, headers, cookies, query params. |
| **Throughput & Scale** | **Ultra-High**: Millions of requests/sec; handles extreme instantaneous bursts. | High; requires time to pre-scale or warm up for sudden massive surges. |
| **Latency Profile** | Sub-millisecond ($< 0.2\text{ ms}$). | Low ($1 - 5\text{ ms}$ processing overhead). |
| **Static IP Address** | Provides dedicated static Anycast IP addresses per AZ. | Dynamic IP addresses; requires CNAME / Alias DNS mapping. |
| **Routing Capabilities**| Round-Robin / Hash-based (5-tuple: IP, Port, Protocol). | Content-based routing: `/api/orders` vs `/api/payments`, host headers. |
| **Client IP Preservation**| Native client IP preserved at packet level. | Injects client IP via `X-Forwarded-For` HTTP header. |

---

## 2. Decision Rule
- **Use Layer 4 (NLB)**: For non-HTTP protocols (Kafka, MySQL, Redis, custom TCP); ultra-low-latency financial trading; workloads subject to sudden 10x traffic spikes (e.g., ticket sales).
- **Use Layer 7 (ALB)**: For microservices routing by HTTP path/host, gRPC microservices, WebSocket bidirectional streams, and WAF integration.
