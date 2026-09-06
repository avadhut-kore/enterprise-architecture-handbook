# Bandwidth Estimation: Ingress, Egress & Wire Protocols

> How to calculate network throughput, evaluate wire serialization efficiencies (JSON vs. Protobuf), and design for cloud egress bandwidth economics.

---

## 1. Network Throughput Formulas

$$\text{Ingress Throughput (Bytes/sec)} = \text{Write RPS} \times \text{Average Ingress Request Size}$$

$$\text{Egress Throughput (Bytes/sec)} = \text{Read RPS} \times \text{Average Egress Response Size}$$

$$\text{Network Bandwidth in Gbps} = \frac{\text{Throughput in Bytes/sec} \times 8}{1,000,000,000}$$

> [!TIP]
> **Remember the Bits vs. Bytes factor**: Network cards, cloud interconnects, and ISPs measure in **Bits per second (bps, Gbps)**, while application payloads, storage, and databases measure in **Bytes (B, MB, GB)**. Always multiply Bytes by **8** when sizing network bandwidth!

---

## 2. Wire Serialization Overhead: JSON vs. Protobuf vs. Avro

The serialization protocol chosen for high-throughput microservice communication directly impacts both CPU consumption and network bandwidth.

```
Representation of an Order Payload:
  - Formatted JSON:      ~ 450 bytes
  - Minified JSON:       ~ 280 bytes
  - Protocol Buffers:    ~ 75 bytes  (3.7x smaller than minified JSON)
  - Apache Avro:         ~ 60 bytes  (Schema separate from binary payload)
```

| Serialization Format | Schema Enforcement | Binary / Text | Network Footprint | CPU Serialization Overhead | Ideal Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **JSON** | Schema-optional / dynamic | Text | High (verbose keys repeated in every payload) | Moderate (string parsing, UTF-8 decoding) | Public HTTP REST APIs, developer-facing endpoints. |
| **Protocol Buffers (Protobuf)** | Strict `.proto` contract | Binary | Very Low (integer tag keys, packed varints) | Very Low (efficient binary encoding) | Internal microservice RPCs (gRPC), high-throughput service meshes. |
| **Apache Avro** | Strict schema registry | Binary | Ultra-Low (no field tags in record; schema sent once per batch) | Very Low | High-volume event streaming (Kafka), analytics data lakes (Parquet/ORC). |

---

## 3. End-to-End Bandwidth Calculation Example

### Scenario: High-Volume Video Streaming Platform
* **Read Traffic**: 500,000 concurrent video streams.
* **Average Video Bitrate**: 1080p HD stream encoded at $4\text{ Mbps}$ ($500\text{ KB/sec}$).
* **API Metadata Traffic**:
  * $50,000\text{ Read RPS}$ for video catalogs, recommendations, and search.
  * Average API response payload: $10\text{ KB}$ (minified JSON).

### 1. Video Streaming Egress:
$$\text{Video Bandwidth} = 500,000 \times 4\text{ Mbps} = 2,000,000\text{ Mbps} = \mathbf{2,000\text{ Gbps} = 2\text{ Tbps}}$$

### 2. API Metadata Egress:
$$\text{API Egress} = 50,000\text{ RPS} \times 10\text{ KB} = 500,000\text{ KB/sec} = 500\text{ MB/sec}$$
$$\text{In Gbps} = \frac{500\text{ MB/sec} \times 8}{1,000} = \mathbf{4\text{ Gbps}}$$

### Architectural Takeaway
* The API metadata ($4\text{ Gbps}$) can easily be handled by a standard fleet of cloud application load balancers (ALBs) and API gateways.
* The video stream ($2\text{ Tbps}$) **CANNOT and MUST NOT** be served from origin application servers. Attempting to route 2 Tbps through an internal VPC would saturate cloud interconnects and result in millions of dollars in egress penalties.
* **Solution**: 100% of video static chunks must be offloaded to a **Tier-1 Content Delivery Network (Cloudflare, Akamai, AWS CloudFront)** with point-of-presence (PoP) edge caching. Origin servers only see cache misses ($< 5\%$).

---

## 4. Cloud Egress Cost Reality Check

Cloud providers charge significant premiums for data leaving their network:
* AWS Internet Egress: $\approx \$0.05\text{ to }\$0.09\text{ per GB}$.
* Cross-Region Data Transfer: $\approx \$0.01\text{ to }\$0.02\text{ per GB}$.
* Cross-Availability-Zone Data Transfer: $\approx \$0.01\text{ per GB}$.

*If your system transfers $1\text{ PB/month}$ of uncompressed data directly to the public internet:*
$$\text{Monthly Egress Bill} = 1,000,000\text{ GB} \times \$0.08 = \mathbf{\$80,000/\text{month}}$$
*By introducing gzip/brotli compression ($3\times$ reduction) and a CDN with negotiated tiering ($50\%$ discount), egress cost drops from $\$80,000$ to $\approx \$13,000/\text{month}$.*

---

## 5. Cross-References

* **Traffic & RPS Estimation**: [`traffic.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/traffic.md)
* **Compute & Worker Concurrency**: [`compute.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/compute.md)
* **Financial TCO Modeling**: [`cost.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/estimation/cost.md)
