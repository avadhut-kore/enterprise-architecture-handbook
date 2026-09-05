# Reference Architecture 02: Serverless & FaaS Observability

## 1. System Context & Overview
Serverless compute environments (e.g., AWS Lambda, Google Cloud Run) introduce unique architectural challenges: ephemeral execution environments, frozen execution states, extreme cold starts, and the absence of persistent host agents.

This architecture leverages the **AWS Lambda Telemetry API Extension** to deliver asynchronous, non-blocking telemetry collection without increasing invocation latency.

---

## 2. Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    participant APIGW as API Gateway / Event Bridge
    participant Handler as Lambda Function Execution Loop
    participant Ext as OTel Lambda Telemetry Extension (In-Memory Buffer)
    participant Backend as Central Telemetry Backend

    APIGW->>Handler: HTTP Request / Event Trigger
    Note over Handler: Lambda Execution Unfreezes
    Handler->>Ext: Emit Trace Spans & Metrics (In-Memory IPC)
    Handler-->>APIGW: Return HTTP 200 OK Response
    Note over Handler: Invocation completes! Handler freezes immediately!
    
    Note over Ext: Lambda Execution Environment remains active for Extension phase
    Ext->>Backend: Asynchronous Batch Flush (OTLP HTTP/gRPC)
    Note over Ext: Extension Signals Done to Lambda Runtime API
```

---

## 3. Key Architectural Decisions
1. **Zero-Impact Response Latency**: The application handler flushes telemetry into the local extension memory buffer and returns the response to the user immediately. Telemetry is transmitted over the wire during the post-invocation runtime extension phase.
2. **Cold Start Instrumentation**: The OpenTelemetry layer wraps the initialization routine to record `faas.coldstart=true` and measure exact initialization duration in distributed traces.
3. **Connection Pooling**: Reusable HTTP keep-alive connections are maintained across warm invocations to eliminate repeated TLS handshake overhead.
