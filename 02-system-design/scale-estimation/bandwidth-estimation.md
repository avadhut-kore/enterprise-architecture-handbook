# Bandwidth Estimation

## 1. Concept & Criticality
Bandwidth estimation calculates the inbound (ingress) and outbound (egress) network throughput across application gateways, internal microservice fabrics, and persistence tiers. Sizing bandwidth accurately ensures network interface cards (NICs), virtual private cloud (VPC) NAT gateways, and edge CDNs do not saturate, causing packet drops and latency spikes.

---

## 2. Bandwidth Formulas

### Ingress Bandwidth
$$\text{BW}_{\text{ingress}} = \text{QPS}_{\text{write}} \times \text{Avg Ingress Payload Size} \times 8\text{ bits/byte}$$

### Egress Bandwidth
$$\text{BW}_{\text{egress}} = \text{QPS}_{\text{read}} \times \text{Avg Egress Payload Size} \times 8\text{ bits/byte}$$

### Origin Egress with CDN Offloading
$$\text{BW}_{\text{origin\_egress}} = \text{BW}_{\text{total\_egress}} \times (1 - \text{CDN Cache Hit Ratio})$$

---

## 3. Worked Enterprise Example: E-Commerce Product Catalog

### System Parameters
* **Peak Read Traffic**: $50,000\text{ QPS}$
* **Peak Write Traffic (Orders/Updates)**: $1,500\text{ QPS}$
* **Average Product Page Payload (JSON + HTML)**: $120\text{ KB}$
* **Average Write Payload**: $4\text{ KB}$
* **CDN Offload Target**: $92\%$ hit ratio for static/catalog read responses.

### Calculation

#### 1. Ingress Bandwidth
$$\text{BW}_{\text{ingress}} = 1,500\text{ QPS} \times 4,000\text{ bytes} \times 8 = 48,000,000\text{ bps} \approx 48\text{ Mbps}$$

#### 2. Total User Egress Bandwidth
$$\text{BW}_{\text{egress, total}} = 50,000\text{ QPS} \times 120,000\text{ bytes} \times 8 = 48,000,000,000\text{ bps} \approx 48\text{ Gbps}$$

#### 3. Origin Server Egress (Post-CDN Offload)
$$\text{BW}_{\text{origin}} = 48\text{ Gbps} \times (1 - 0.92) = 48 \times 0.08 = 3.84\text{ Gbps}$$

```mermaid
flowchart LR
    Users[Global Users] <-->|48 Gbps Egress| CDN[Edge CDN Network: 92% Cached]
    CDN <-->|3.84 Gbps Origin Egress| LB[Application Load Balancers]
    LB <-->|Internal Service Mesh: ~12 Gbps East-West| AppFleet[Microservice Fleet]
```

---

## 4. Internal East-West vs. North-South Bandwidth
North-South traffic enters the data center from the public internet. East-West traffic circulates internally between microservices, caches, and databases.
* In microservice architectures, the **East-West Bandwidth Multiplier** typically ranges from $3\times$ to $8\times$ North-South ingress volume.
* If origin ingress is $3.84\text{ Gbps}$, internal East-West traffic routinely reaches $12\text{--}30\text{ Gbps}$.

---

## 5. Architectural Implications & Network Bottlenecks
* **NIC Saturation Limits**: Standard cloud virtual machines are capped at 10 Gbps, 25 Gbps, or 100 Gbps network bandwidth. Sizing compute nodes without reviewing cloud provider bandwidth allocations leads to silent packet throttling.
* **NAT Gateway Cost & Bandwidth Traps**: In public cloud environments (AWS/Azure), managed NAT gateways charge per-GB processed. Pushing gigabits of telemetry or database replication through public NAT gateways creates astronomical cloud invoices. Use internal VPC endpoints.
* **Serialization Protocols**: Protocol Buffers (gRPC) or FlatBuffers yield a $60\%\text{--}80\%$ bandwidth reduction compared to verbose JSON payloads, directly scaling network throughput.
