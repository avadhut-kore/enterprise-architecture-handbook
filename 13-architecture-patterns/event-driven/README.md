# Event-Driven Architecture (EDA) Pattern

## Overview

Event-Driven Architecture (EDA) is a distributed software architecture paradigm wherein system components communicate primarily by producing, detecting, consuming, and reacting to state changes known as **Events**. An Event represents an immutable, factual occurrence in the past (e.g., `OrderPlaced`, `PaymentFailed`, `InventoryReserved`).

Unlike traditional synchronous request-response architectures (REST/gRPC) where the caller blocks waiting for the callee to execute work, EDA enforces **extreme temporal and spatial decoupling**: event producers publish events without knowing or caring who consumes them, how many consumers exist, or when they will process the message.

---

## Architectural Topology

```mermaid
flowchart TD
    subgraph Producers["Event Producers"]
        OrderSvc["Order Service"]
        PaymentSvc["Payment Service"]
    end

    subgraph EventBrokers["Event Streaming Backbone (Kafka / EventBridge)"]
        TopicOrders[("Topic: orders.events<br/>[OrderCreated, OrderCancelled]")]
        TopicPayments[("Topic: payments.events<br/>[PaymentCaptured, PaymentDeclined]")]
    end

    subgraph Consumers["Autonomous Event Consumers"]
        NotifSvc["Notification Service<br/>(Sends SMS/Email)"]
        InvenSvc["Inventory Service<br/>(Deducts physical stock)"]
        FraudSvc["Fraud Analytics Engine<br/>(Real-time ML scoring)"]
        DataLake["Data Lake Ingest<br/>(ClickHouse / Snowflake)"]
    end

    OrderSvc -->|Publish Event| TopicOrders
    PaymentSvc -->|Publish Event| TopicPayments
    
    TopicOrders -->|Subscribe| InvenSvc
    TopicOrders -->|Subscribe| NotifSvc
    TopicOrders -->|Subscribe| FraudSvc
    TopicOrders -->|Subscribe| DataLake
    TopicPayments -->|Subscribe| NotifSvc
```

---

## Core Concepts: Events vs. Commands vs. Messages

| Primitive | Intent & Semantics | Directionality | Temporal Nature | Example |
|:---|:---|:---|:---|:---|
| **Command** | Directive to perform an action. Can be rejected by receiver. | Targeted to 1 specific handler | Synchronous / Expects immediate feedback | `ProcessPaymentCommand`, `CreateUser` |
| **Event** | Statement of an immutable historical fact. Cannot be rejected or undone. | Broadcast / Multi-consumer | Asynchronous / Past tense | `OrderPlacedEvent`, `SensorReadingRecorded` |
| **Message** | Raw envelope containing either a Command or an Event payload. | Point-to-Point or Pub/Sub | Agnostic | AMQP packet, SQS message |

---

## Event Broker Paradigms: Queue vs. Stream

```mermaid
flowchart LR
    subgraph MessageQueue["1. Message Queue (AMQP / RabbitMQ / AWS SQS)"]
        Q1["Message published"]
        Q2["Worker consumes message"]
        Q3["Worker acknowledges (ACK)"]
        Q4["Message is DELETED from queue permanently!"]
    end

    subgraph EventLog["2. Distributed Event Log (Apache Kafka / Apache Pulsar)"]
        L1["Event appended to partition log"]
        L2["Consumers read independently using private offsets"]
        L3["Events remain PERSISTED in log for days/months"]
        L4["Supports replaying historical events from offset 0!"]
    end
```

- **Use Message Queues (RabbitMQ/SQS)**: When individual discrete tasks need to be processed by workers and forgotten (e.g., "resize image", "send password reset email").
- **Use Event Streams (Kafka/Pulsar)**: When events represent an immutable audit trail, require multi-subscriber fanout, require temporal replayability, or power streaming analytics (e.g., financial ledger transactions, e-commerce order streams).

---

## Coordination Models: Choreography vs. Orchestration

```mermaid
flowchart TD
    subgraph Choreography["1. Event Choreography (Decentralized)"]
        C_Order["Order Svc: Publishes OrderCreated"] --> C_Pay["Payment Svc: Listens & Publishes PaymentProcessed"]
        C_Pay --> C_Inv["Inventory Svc: Listens & Reserves Stock"]
        Note1["Pros: Zero central SPOF, high autonomy.<br/>Cons: Flow logic is implicit; hard to visualize full workflow."]
    end

    subgraph Orchestration["2. Event Orchestration (Centralized)"]
        O_Mgr["Saga Orchestrator (Temporal / AWS Step Functions)"]
        O_Mgr -->|Execute| O_Order["Order Svc"]
        O_Mgr -->|Execute| O_Pay["Payment Svc"]
        O_Mgr -->|Execute| O_Inv["Inventory Svc"]
        Note2["Pros: Explicit workflow state, simple compensation.<br/>Cons: Central orchestrator can become coupled bottleneck."]
    end
```

---

## The Transactional Outbox Pattern

A fatal failure in EDA occurs when a service saves state to its database, but crashes before publishing the event to Kafka ("Dual-Write Failure"). Architects eliminate this with the **Transactional Outbox Pattern**:

```mermaid
sequenceDiagram
    autonumber
    participant App as Order Application Service
    participant DB as PostgreSQL Database
    participant CDC as Debezium CDC Relay
    participant Kafka as Apache Kafka Broker

    rect rgb(230, 245, 255)
    Note over App,DB: ATOMIC LOCAL DATABASE TRANSACTION
    App->>DB: INSERT INTO orders (id, total, status) VALUES (...)
    App->>DB: INSERT INTO outbox_table (event_type, payload) VALUES (...)
    App->>DB: COMMIT TRANSACTION (Both succeed or both fail!)
    end

    CDC->>DB: Read PostgreSQL Write-Ahead Log (WAL)
    CDC->>Kafka: Publish OrderCreated event to 'orders.events' topic
    CDC->>DB: Mark outbox row as processed (or purge)
```

---

## Production Realities & Trade-Offs

- **Eventual Consistency**: Consumers process events asynchronously. A customer may submit an order and refresh their page before the inventory consumer has updated the UI. Systems must be designed with optimistic client UIs and asynchronous polling.
- **Idempotent Consumers**: Networks duplicate messages. Every event handler must check an `idempotency_key` or message UUID before executing side effects to prevent charging customers twice.
- **Schema Evolution**: Schemas change over time. Enforce strict backwards and forwards compatibility using an Avro/Protobuf **Schema Registry**.
