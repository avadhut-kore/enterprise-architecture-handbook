# Asynchronous Event-Driven Sequence Diagram

Asynchronous patterns decouple the producer from the consumer using message brokers, ensuring fast acknowledgment and non-blocking background processing.

```mermaid
sequenceDiagram
    autonumber
    actor User as Mobile User
    participant Gateway as Edge API Gateway
    participant OrderSvc as Order Processing Service
    participant Queue as Kafka Cluster (orders.incoming)
    participant Worker as Fulfillment Worker
    participant Inventory as Inventory DB
    participant Notify as Notification Service

    User->>Gateway: POST /v1/orders (OrderPayload)
    activate Gateway
    Gateway->>OrderSvc: CreateOrder(OrderPayload)
    activate OrderSvc
    OrderSvc->>Queue: Publish(OrderCreatedEvent, IdempotencyKey)
    activate Queue
    Queue-->>OrderSvc: Ack (Partition 2, Offset 8192)
    deactivate Queue

    OrderSvc-->>Gateway: 202 Accepted (OrderID: ord_987, Status: PENDING)
    deactivate OrderSvc
    Gateway-->>User: 202 Accepted (Check status at /orders/ord_987)
    deactivate Gateway

    Note over Queue,Worker: Asynchronous Consumer Polling
    Worker->>Queue: PollBatch()
    activate Worker
    Queue-->>Worker: OrderCreatedEvent(ord_987)
    Worker->>Inventory: DecrementStock(SKU_44, Qty: 1)
    activate Inventory
    Inventory-->>Worker: Stock Reserved (Commit ACID)
    deactivate Inventory

    Worker->>Notify: SendPushNotification(ord_987, "Confirmed")
    Worker->>Queue: CommitOffset(Offset 8192)
    deactivate Worker
```
