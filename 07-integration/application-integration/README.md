# Application Integration Architecture

Application integration patterns dictate how software boundaries interact reliably, securely, and evolvably across disparate sub-systems, services, and legacy platforms.

---

## Architectural Taxonomy

```mermaid
flowchart TD
    subgraph Synchronous Integration
        REST[REST / HTTP Client]
        gRPC[gRPC / Protobuf]
        Facade[Integration Facade]
    end
    subgraph Asynchronous Integration
        Outbox[Transactional Outbox]
        Broker[Message Broker / Kafka / RabbitMQ]
        Inbox[Transactional Inbox / Idempotent Consumer]
    end
    subgraph Domain Isolation
        ACL[Anti-Corruption Layer ACL]
        Adapter[Domain Adapter]
    end

    Facade --> REST
    Outbox --> Broker --> Inbox
    REST --> ACL --> Adapter
```

---

## Knowledge Index
- [Service Client Pattern](service-client-pattern.md)
- [API Client Pattern](api-client-pattern.md)
- [Adapter Pattern](adapter-pattern.md)
- [Facade Pattern](facade-pattern.md)
- [Anti-Corruption Layer (ACL)](anti-corruption-layer.md)
- [Integration Service Pattern](integration-service.md)
- [Transactional Outbox Pattern](transactional-outbox.md)
- [Transactional Inbox Pattern](inbox-pattern.md)
- [Idempotent Consumer Pattern](idempotent-consumer.md)
- [Synchronous Integration Architecture](synchronous-integration.md)
- [Asynchronous Integration Architecture](asynchronous-integration.md)
