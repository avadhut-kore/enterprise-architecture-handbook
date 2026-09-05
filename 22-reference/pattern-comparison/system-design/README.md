# Architectural Pattern & Technology Comparisons

Enterprise architecture is fundamentally the discipline of managing trade-offs. No single architectural style, communication protocol, or storage engine is universally optimal across all dimensions.

This section provides comparative trade-off analyses, feature matrices, decision trees, and selection frameworks for critical system design choices.

---

## Pattern Comparison Catalog

| Comparison | Core Architectural Dilemma | Primary Selection Factor |
| :--- | :--- | :--- |
| [REST vs gRPC vs GraphQL](rest-vs-grpc-vs-graphql.md) | API Protocol Paradigm | Inter-service performance vs Client flexibility |
| [Kafka vs RabbitMQ](kafka-vs-rabbitmq.md) | Event Streaming vs Smart Broker Queueing | Replayability & ordering vs Complex AMQP routing |
| [SQL vs NoSQL](sql-vs-nosql.md) | Relational ACID vs Distributed Scalability | Schema rigidity & ACID joins vs Partition elasticity |
| [Push vs Pull Models](push-vs-pull.md) | Data Delivery & Polling Inversion | Real-time latency vs Consumer backpressure control |
| [Batch vs Streaming Processing](batch-vs-streaming.md) | High-Volume Latency Trade-Off | Computational completeness vs Millisecond freshness |
| [Redis vs Memcached](redis-vs-memcached.md) | In-Memory Data Store Architecture | Rich data structures & persistence vs Pure multithread cache |
| [Monolith vs Microservices](monolith-vs-microservices.md) | Topology & Organizational Alignment | Development velocity & simplicity vs Independent scaling |
| [Polling vs WebSockets vs SSE](polling-vs-websockets-vs-sse.md) | Client-Server Push Mechanisms | Full-duplex bidirectional vs Lightweight server-push |
| [Strong vs Eventual Consistency](strong-vs-eventual-consistency.md) | CAP / PACELC Trade-Off Profile | Absolute financial correctness vs Planetary availability |
