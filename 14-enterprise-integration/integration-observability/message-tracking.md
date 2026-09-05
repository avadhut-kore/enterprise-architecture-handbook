# End-to-End Message Lifecycle Tracking

## 1. The Tracking Problem in Asynchronous Choreography
In complex event-driven architectures, a message may branch, split, merge, and transform across 15 different topics, queues, and database tables. Without centralized message lifecycle tracking, tracing whether a message was delivered, dropped, or delayed is impossible.

## 2. Message State Machine

```
[PRODUCED] ──> [BUFFERED] ──> [CONSUMED] ──> [TRANSFORMED] ──> [DELIVERED]
     │                                                               │
     └─────────────────────────> [DEAD_LETTERED] <───────────────────┘
```

## 3. Dedicated Tracking Store Pattern
Store high-level state transitions in an indexed, low-latency datastore (e.g., Elasticsearch, ClickHouse, or DynamoDB) using the message's unique `Message-ID`. Each integration processor emits lightweight status pings to the tracking store upon receipt and completion.
