# API Gateway Technology Comparison: Envoy vs. Kong vs. AWS API Gateway

## 1. Enterprise Selection Matrix

| Architectural Dimension | Envoy Proxy | Kong Gateway | AWS API Gateway |
| :--- | :--- | :--- | :--- |
| **Core Architecture** | C++ High Performance, Asynchronous Event Loop | Lua / OpenResty (Nginx base) | Multi-tenant AWS Managed Serverless |
| **Throughput / Latency**| Ultra-High ($<1\text{ ms}$ overhead) | High ($1\text{--}3\text{ ms}$) | Moderate ($15\text{--}40\text{ ms}$) |
| **Configuration Model** | Dynamic xDS gRPC APIs / YAML | REST Admin API / Declarative YAML | CloudFormation / CDK / Console |
| **Extensibility** | WebAssembly (Wasm) filters, C++ plugins | Lua plugins, Go/Python plugins | AWS Lambda Authorizers / Integrations |
| **Service Mesh Synergy**| Native Data Plane (Istio, Consul) | Kong Mesh (Kuma) | AWS App Mesh |
| **Operational Overhead**| High (Self-hosted or via Istio/Envoy Gateway) | Medium (Self-managed or Kong Konnect) | Zero (Fully managed cloud service) |
| **Cost Model** | Infrastructure VM / Compute cost | Open-Source free / Enterprise license | Per-million invocations + data transfer |

---

## 2. Decision Tree
* **Choose AWS API Gateway**: Serverless applications (AWS Lambda), low-to-medium volume ($<5,000\text{ RPS}$), rapid prototyping.
* **Choose Kong**: Rich API management requirements (developer portal, billing plugins, API productization) with straightforward Lua extensibility.
* **Choose Envoy**: Ultra-high scale ($>50,000\text{ RPS}$), microsecond latency requirements, Kubernetes-native service mesh architectures.
