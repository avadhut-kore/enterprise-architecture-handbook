# Architecture Comparison: Apache Kafka vs RabbitMQ

## 1. Architectural Trade-Off Matrix

```
+--------------------------+---------------------------------+---------------------------------+
| Architectural Dimension  | Apache Kafka                    | RabbitMQ                        |
+--------------------------+---------------------------------+---------------------------------+
| Architecture Model       | Distributed Append-Only Log     | Smart Broker, Dumb Consumer AMQP|
| Storage & Retention      | Persistent disk log (Time/Size) | Transient (Purged post-ACK)     |
| Event Replayability      | Full historical rewind & replay | No native replay (Purged)       |
| Routing Flexibility      | Static topic / partition routing| Complex dynamic exchange routing|
| Throughput Capacity      | Millions of events / sec        | Tens of thousands msgs / sec    |
| Message Ordering         | Guaranteed strictly per-partition| FIFO within single queue only   |
| Consumer Model           | Pull (Consumer polls batch)     | Push (Broker pushes to workers) |
| Best Use Case            | Event streaming, CDC, Big Data  | Complex task queues & workflows |
+--------------------------+---------------------------------+---------------------------------+
```

---

## 2. Architectural Comparison Blueprint

```
Kafka (Dumb Broker, Smart Consumer):
Topic Partition: [ Msg 0 | Msg 1 | Msg 2 | Msg 3 | Msg 4 ]
                      ▲                   ▲
                      │ Consumer Group 1  │ Consumer Group 2 (Independent offsets)

RabbitMQ (Smart Broker, Dumb Consumer):
Producer ──► [ Exchange ] ──Routing Keys──► [ Queue A ] ──Push──► Worker 1
                                       └──► [ Queue B ] ──Push──► Worker 2
                                            (Messages deleted upon ACK)
```

---

## 3. Decision Framework

- **Select Apache Kafka if**: You require event sourcing, CDC data pipelines, high-volume log aggregation, multi-consumer independent processing, or the ability to replay historical data.
- **Select RabbitMQ if**: You require complex message routing (topic wildcards, header routing), granular per-message TTL/priority queues, or standard transactional task-queue worker patterns.
