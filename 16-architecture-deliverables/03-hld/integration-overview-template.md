# HLD Integration & Interface Overview

## 1. Upstream & Downstream Dependencies
| Integration Point | Type | Protocol | Payload | SLA Target |
|---|---|---|---|---|
| **Client Gateway** | Inbound | HTTPS / REST | JSON (OpenAPI 3.1) | 99.95% Availability |
| **Inventory Service** | Outbound | gRPC / HTTP/2 | Protobuf v3 | p95 < 25ms |
| **Payment Gateway** | Outbound | HTTPS / REST | JSON | p95 < 800ms |
| **Event Stream** | Outbound | Kafka Producer | Avro with Schema Registry | Guaranteed Delivery |

## 2. Sequence Diagram: Order Placement Flow
Reference UML Sequence specs from [[17-diagrams/02-uml/02-sequence-diagrams.md](../../17-diagrams/sequence/order-processing.md)].

```mermaid
sequenceDiagram
    autonumber
    actor User as Client
    participant GW as API Gateway
    participant OS as Order Service
    participant DB as Order DB
    participant K as Kafka Broker

    User->>GW: POST /api/v1/orders
    GW->>OS: Forward with X-User-ID & Trace ID
    OS->>OS: Validate items & idempotency key
    critical Transactional Outbox
        OS->>DB: INSERT into orders (status: PENDING)
        OS->>DB: INSERT into outbox_table (OrderCreatedEvent)
    end
    OS-->>GW: 201 Created { order_id: "ord-123" }
    GW-->>User: 201 Created
    
    par Async Outbox Relay
        OS->>DB: Poll uncommitted outbox rows
        OS->>K: Publish to topic: order-lifecycle
        OS->>DB: Mark outbox row as PUBLISHED
    end
```
