# Synchronous RPC vs Asynchronous Events Trade-off Model

Architectural decision framework comparing synchronous request-response (REST/gRPC) against asynchronous publish-subscribe messaging.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph SyncRPC ["Synchronous Request-Response (REST / gRPC)"]
        Caller1["Client / Upstream"]
        Callee1["Target Service"]
        Caller1 -->|"1. Blocking Request"| Callee1
        Callee1 -->>|"2. Immediate Response"| Caller1
        note1["Coupling: HIGH<br/>Temporal: MUST BE ONLINE<br/>Latency: IMMEDIATE<br/>Failure: CASCADING RISKS"]
    end

    subgraph AsyncEvents ["Asynchronous Publish-Subscribe (Kafka / RabbitMQ)"]
        Producer["Producer Service"]
        Broker["Event Broker (Queue/Topic)"]
        Consumer["Consumer Service"]
        Producer -->|"1. Fire & Forget"| Broker
        Broker -->|"2. Decoupled Delivery"| Consumer
        note2["Coupling: LOOSE<br/>Temporal: FULLY DECOUPLED<br/>Latency: EVENTUAL<br/>Failure: BUFFERED & RESILIENT"]
    end
```

## PlantUML Specification

```plantuml
@startuml
rectangle "Synchronous RPC (REST/gRPC)" as rpc {
  [Caller] -> [Callee] : Blocks until response
  note bottom : Tight temporal coupling
Direct dependency
}
rectangle "Asynchronous Messaging" as async {
  [Producer] -> [Queue / Broker] : Non-blocking publish
  [Queue / Broker] -> [Consumer] : Pull/Push delivery
  note bottom : Loose temporal coupling
Resilient to consumer downtime
}
@enduml
```

## Architectural Design Considerations

* **When to use Sync RPC**: Queries requiring real-time answers (e.g., user login verification, real-time balance checks).
* **When to use Async Events**: Side-effects, long-running operations, or workflows spanning multiple independent bounded contexts.
* **Cascading Failures**: Deep synchronous call chains ($A ightarrow B ightarrow C ightarrow D$) multiply unavailability; keep sync call depths $\le 2$ hops.

## Related Documentation & Patterns

* [Event-Driven Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/eda.md)
* [Modern API Gateway](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/integration/api-gateway.md)
* [Trade-off Matrix](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/tradeoff-matrix.md)
