# Enterprise Integration Decision Framework

## 1. Executive Purpose
This framework provides Solution Architects with an objective, trade-off-driven evaluation rubric for selecting integration topologies, protocols, and communication styles.

---

## 2. The Multi-Dimensional Integration Decision Matrix

| Integration Decision | Option A | Option B | Evaluation Criteria & Architectural Drivers |
|---|---|---|---|
| **API vs Event** | Synchronous REST / gRPC | Asynchronous Pub/Sub Event | Use API when caller requires immediate response; Event when publishing facts to multiple consumers |
| **Sync vs Async** | Synchronous Request/Reply | Asynchronous Message Queue | Use Async for temporal decoupling, burst absorption, and long-running operations |
| **Queue vs Stream** | Message Queue (RabbitMQ / SQS) | Event Stream (Kafka / Kinesis) | Use Queue for point-to-point task distribution; Stream for ordered event logs & replayability |
| **Batch vs Real-Time** | Scheduled Bulk ETL / Batch | Continuous Real-Time Streaming | Use Batch for heavy analytical aggregations; Real-Time when business SLA < 5 seconds |
| **Point-to-Point vs Platform** | Direct Service Integration | Enterprise Integration Platform / Mesh | Point-to-Point for isolated 1:1 services; Platform when integration web exceeds $O(N^2)$ |
| **REST vs gRPC** | REST / JSON / OpenAPI | gRPC / HTTP/2 / Protobuf | REST for public & browser clients; gRPC for high-throughput internal microservice RPC |
| **REST vs GraphQL** | Fixed Endpoint REST | Client-Driven GraphQL | REST for predictable caching & simplicity; GraphQL for composite UI data aggregation |
| **Webhook vs Polling** | Asynchronous Webhook Push | Scheduled HTTP Polling | Webhook for efficient real-time notification; Polling only when publisher lacks push capability |
| **CDC vs API Sync** | Database Log-Based CDC | Application-Level API Sync | CDC for transparent zero-dual-write sync; API Sync when domain logic validation is required |
| **File vs API** | Secure Batch File (SFTP) | Synchronous REST API | File for massive multi-million record legacy batch drops; API for granular real-time records |
| **Orchestration vs Choreography** | Central Workflow Engine | Decentralized Event Choreography | Orchestration for complex financial sagas; Choreography for loosely coupled notification flows |

---

## 3. Architecture Selection Guidelines
- Select based on non-functional requirements (latency, consistency, volume) rather than technology hype.
- Avoid introducing complex distributed streaming brokers when simple queues satisfy the SLA.
