# RabbitMQ Architecture

## 1. The AMQP 0-9-1 Messaging Model
Unlike Kafka's dumb broker model, RabbitMQ is an intelligent routing broker built on Erlang and the Advanced Message Queuing Protocol (AMQP).

```mermaid
flowchart LR
    Producer[Producer] -->|Publish with Routing Key| Exchange{AMQP Exchange}
    Exchange -->|Binding Rule: *.orders| Queue1[(Orders Queue)]
    Exchange -->|Binding Rule: audit.#| Queue2[(Audit Log Queue)]
    
    Queue1 --> Consumer1[Worker Service]
    Queue2 --> Consumer2[Compliance Archiver]
```

---

## 2. Core Exchange Topologies
* **Direct Exchange**: Routes messages based on an exact match between routing key and binding key.
* **Fanout Exchange**: Broadcasts all incoming messages to every bound queue (pure pub/sub).
* **Topic Exchange**: Routes based on wildcard pattern matching (`*` matches one word; `#` matches zero or more words).
* **Headers Exchange**: Routes based on message header attributes rather than routing keys.

---

## 3. Quorum Queues (Raft-Based HA)
Modern RabbitMQ deployments utilize **Quorum Queues** (replicated via the Raft consensus algorithm) instead of legacy mirrored queues, delivering predictable data safety under network partitions.
