# Technology Comparison: Celery vs. Sidekiq vs. BullMQ

## 1. Comparison Matrix

| Architectural Vector | Celery (Python) | Sidekiq (Ruby) | BullMQ (Node.js / TypeScript) |
| :--- | :--- | :--- | :--- |
| **Runtime Language** | Python | Ruby | Node.js / TypeScript |
| **Broker Backend** | RabbitMQ / Redis / SQS | Redis | Redis / Dragonfly |
| **Concurrency Model** | Multi-process (prefork) / Gevent | Multi-threaded (Celluloid / Actor) | Single-threaded Async Event Loop |
| **Delayed Jobs** | Celery Beat (External scheduler) | Native in Redis ZSET | Native in Redis ZSET |
| **Memory Efficiency**| Moderate (Process fork overhead) | High (Shared heap multi-threaded) | High (V8 lightweight event loop) |
| **UI Dashboard** | Flower | Sidekiq Web UI (Built-in) | Bull-Board / Arena |
| **Job Chaining** | Canvas (Chains, Groups, Chords) | Batches (Enterprise edition) | FlowProducer (Parent-Child trees) |

---

## 2. Technology Selection
* **Choose Celery**: Heavy ML, data science, Python-based enterprise microservices.
* **Choose Sidekiq**: High-throughput Ruby on Rails platforms; exceptional thread memory efficiency.
* **Choose BullMQ**: Modern Node.js/TypeScript microservices; ultra-fast Redis performance with complex parent-child job workflows.
