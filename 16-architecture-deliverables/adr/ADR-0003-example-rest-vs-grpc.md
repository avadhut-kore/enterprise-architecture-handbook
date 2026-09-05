# ADR-0003: gRPC vs. REST for Internal Microservice Communication

## Metadata
- **Status**: Accepted
- **Date**: 2026-09-05
- **Author(s)**: Principal Systems Architect
- **Deciders**: Architecture Review Board (ARB), Platform Engineering Team
- **Technical Story**: [ARCH-1088] Inter-Service Communication Standard

---

## 1. Context and Problem Statement

Our platform consists of 14 backend microservices executing on AWS EKS (Kubernetes). Currently, all inter-service communication utilizes REST over HTTP/1.1 with JSON serialization. 

During our recent peak load tests (12,000 incoming user requests/sec), single user transactions resulted in deep internal service call chains (averaging 5–7 hops). Profiling revealed:
1. **Serialization Bottleneck**: CPU profiling showed application servers spending **28% of total CPU cycles** serializing and deserializing large JSON text payloads.
2. **Network Latency & Thread Blocking**: HTTP/1.1 connection limits caused TCP handshake overhead and head-of-line blocking, inflating internal inter-service p99 latency to **450ms**.
3. **Contract Drift**: Teams frequently made breaking changes to JSON fields without detection, leading to runtime null-pointer exceptions in downstream services.

We must establish a standardized, high-performance inter-service communication protocol for all internal synchronous RPC calls.

---

## 2. Decision Drivers

- **Driver 1: Performance & Low Latency**: Internal inter-service hop latency must be $\le 10\text{ms}$ at p99.
- **Driver 2: Efficient Resource Utilization**: Reduce CPU serialization overhead to decrease cloud container compute costs.
- **Driver 3: Strict Contract Governance**: Strongly typed, compiled API contracts with automated backwards-compatibility verification.
- **Driver 4: Streaming Support**: Ability to support bidirectional telemetry and event streaming between services.

---

## 3. Considered Options

- **Option A**: Continue with REST over HTTP/1.1 with JSON (Enhanced with connection keep-alive pools).
- **Option B**: REST over HTTP/2 with JSON.
- **Option C**: **gRPC over HTTP/2 with Protocol Buffers (Protobuf)**.
- **Option D**: Apache Thrift over TCP.

---

## 4. Comparative Evaluation Matrix

| Decision Criteria | Option A: REST (HTTP/1.1) | Option B: REST (HTTP/2) | Option C: gRPC (HTTP/2) | Option D: Apache Thrift |
|:---|:---:|:---:|:---:|:---:|
| **Serialization Performance** | Poor (Bulky JSON text) | Poor (Bulky JSON text) | **Exceptional (Binary Protobuf)** | Exceptional (Binary) |
| **Connection Multiplexing** | No (HOL blocking) | Yes | **Yes (Single TCP connection)** | Custom |
| **Strict Schema Enforcement** | Weak (OpenAPI optional) | Weak | **Strict (Compiled `.proto` files)**| Strict (`.thrift` files) |
| **CPU Efficiency** | Low | Low | **High (Up to 7x faster than JSON)**| High |
| **Ecosystem & Cloud Support** | Ubiquitous | High | **Native EKS / Envoy / Istio integration**| Moderate |
| **Developer Ergonomics (Debugging)**| High (curl / Postman) | High | **Moderate (Requires grpcurl / schemas)**| Low |

---

## 5. Decision Outcome

**Chosen Option**: **Option C: gRPC over HTTP/2 with Protocol Buffers**

### Rationale and Justification
Benchmarking in our staging environment demonstrated that switching from REST/JSON to gRPC/Protobuf reduced inter-service p99 latency from **450ms to 42ms** and reduced CPU consumption by **22%**. 

Furthermore, Protocol Buffers enforce contract-first engineering. By checking `.proto` files into a centralized schema repository (`buf.build` or internal Git repository), CI/CD pipelines automatically generate strongly typed client SDKs for Go, Java, and .NET, while breaking pull requests that introduce non-backward-compatible schema changes.

> [!NOTE]
> Public ingress APIs facing web browsers and third-party partners will continue to expose standard **REST/JSON via the API Gateway** (using Envoy / grpc-gateway for protocol translation). gRPC is mandated strictly for **internal, service-to-service communication**.

---

## 6. Consequences & Trade-Offs

### Positive Consequences
- **Sub-Millisecond Payload Serialization**: Compact binary format drastically reduces memory allocation and CPU cycles.
- **HTTP/2 Multiplexing**: Eliminates TCP connection exhaustion by multiplexing thousands of concurrent RPC calls across a single persistent TCP socket.
- **Contract Safety**: Eliminates accidental runtime field mismatch bugs; compiler guarantees contract conformance.

### Negative Consequences
- **Debugging Complexity**: Payload bytes cannot be read directly in Wireshark or browser network logs without decoding through the protobuf definition.
- **Load Balancing Complexity**: HTTP/2 persistent connections break traditional L4 round-robin load balancers. Mitigated by deploying Envoy proxy sidecars to perform L7 client-side RPC load balancing.

---

## 7. Compliance & Enforcement

1. **Central Schema Repository**: All internal service definitions must reside as `.proto` files in the `enterprise-proto-contracts` repository.
2. **Automated Breaking Change Detection**: The `buf breaking --against` linter runs on every pull request to reject breaking changes:

```yaml
# Example buf.yaml configuration
version: v1
lint:
  use:
    - DEFAULT
breaking:
  use:
    - FILE
```
