# Backpressure & Flow Control in Messaging

## 1. Flow Control Across Messaging Paradigms
Without backpressure, rapid message producers overwhelm slow consumers, causing out-of-memory crashes or runaway disk queues.

```mermaid
flowchart LR
    Broker[High-Throughput Broker: 100k msgs/s] -->|Fetch max.poll.records=50| Consumer[Consumer Worker: Bounded Memory]
    Consumer -->|Throttled / Busy: Executes pause()| Broker
```

---

## 2. Broker-Specific Controls
* **RabbitMQ Prefetch (`basic.qos`)**: Configures the maximum number of unacknowledged messages the broker sends to a channel. Sizing `prefetch_count = 50` guarantees the worker buffer never exceeds 50 messages.
* **Kafka Polling Limits**:
  * `max.poll.records = 100`: Bounds the batch size retrieved in each `poll()` invocation.
  * `max.poll.interval.ms = 300000` ($5\text{ mins}$): Maximum time the consumer can spend processing a batch before the coordinator marks it dead and triggers a rebalance.
