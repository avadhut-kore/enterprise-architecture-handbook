# Integrating AI with REST, gRPC & Apache Kafka

## 1. Multi-Protocol Integration Matrix

Enterprise architectures demand different protocols depending on the AI workload's interaction model:

```mermaid
flowchart TD
    Client["Client / Upstream Producer"] --> Dec{"Integration Pattern?"}
    
    Dec -->|Real-Time Interactive Chat / Copilot| REST["1. REST / HTTP/2 with SSE\n- Best for web/mobile browsers\n- Standard streaming token delivery (TTFT < 800ms)"]
    
    Dec -->|Internal Low-Latency Microservice RPC| gRPC["2. gRPC / Protobuf\n- Binary serialization, zero overhead\n- Sub-5ms transport between backend services & model servers"]
    
    Dec -->|High-Volume Asynchronous Batch Ingestion| Kafka["3. Apache Kafka Event Streams\n- Backpressure resilient, durable queuing\n- Batch document summarization, anomaly detection"]
```

---

## 2. Invariant: Circuit Breaking on Model Endpoints
When exposing synchronous REST/gRPC endpoints wrapping foundation models, always configure Resilience4j / Envoy circuit breakers with a maximum timeout of 10 seconds. Unbounded HTTP thread pool consumption during upstream LLM latency spikes will crash the calling microservice.
