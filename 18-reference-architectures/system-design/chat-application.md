# Reference Architecture: Real-Time Chat Application (WhatsApp / Slack)

## 1. System Overview
A globally scalable, real-time messaging platform supporting 1-on-1 direct messaging, group conversations, presence tracking (online/last seen), message receipts (sent, delivered, read), and media attachments.

## 2. Business Context
Serves as the mission-critical communication fabric for consumers and enterprise collaboration platforms.

## 3. Functional Requirements
* Real-time 1-on-1 and group messaging (up to 1,000 members per group).
* Presence tracking (Online, Away, Offline).
* Delivery status ticks: Sent ($\checkmark$), Delivered ($\checkmark\checkmark$), Read (Blue $\checkmark\checkmark$).
* Push notifications for offline users.
* Media attachment uploads (images, audio, videos).

## 4. Non-Functional Requirements
* **End-to-End Latency**: Sub-100ms message delivery for online users globally.
* **Concurrency**: 10 Million concurrent WebSocket connections.
* **Durability**: Zero message loss.
* **Security**: End-to-End Encryption (E2EE) using the Signal Protocol.

## 5. Constraints & Assumptions
* Mobile devices frequently transition between cellular networks and offline states.
* Read-to-write ratio: $pprox 1:1$ (each message sent is typically read once or twice).

## 6. Scale Estimation
* 50 Million Daily Active Users.
* 40 messages per user/day = 2 Billion messages/day.
* Average Message Rate: $rac{2 	imes 10^9}{86,400} pprox 23,150	ext{ msgs/sec}$.
* Peak Rate ($3	imes$): $pprox 70,000	ext{ msgs/sec}$.

## 7. Capacity Planning
* Average message size: 200 bytes.
* Daily Message Storage: $2 	imes 10^9 	imes 200	ext{ bytes} pprox 400	ext{ GB/day}$.
* 5-Year Storage ($	ext{RF}=3$): $400	ext{ GB} 	imes 365 	imes 5 	imes 3 pprox \mathbf{2.19	ext{ PB}}$.
* Concurrent WebSocket Connections: $10,000,000$ active sockets.

## 8. High-Level Architecture
```mermaid
flowchart TD
    UserA[User A: Online] -->|WebSocket| GW1[WebSocket Gateway 1]
    GW1 --> ChatSvc[Chat Routing Service]
    ChatSvc --> MsgDB[(Message Store: ScyllaDB)]
    ChatSvc --> RedisPresence[(Redis Presence / Session Store)]
    
    ChatSvc --> Router{Is Recipient Online?}
    Router -->|Yes: Connected to GW 2| GW2[WebSocket Gateway 2]
    GW2 -->|WebSocket| UserB[User B: Online]
    
    Router -->|No: Offline| Kafka[Kafka Push Stream]
    Kafka --> PushSvc[Push Notification Service (APNS/FCM)]
    PushSvc --> UserB_Phone[User B Mobile Notification]
```

## 9. Component Architecture
* **WebSocket Gateway Fleet**: Manages 10M long-lived TCP sockets; terminates TLS.
* **Session & Presence Service**: Maps `user_id` $ightarrow$ `gateway_instance_id`.
* **Chat Message Sequencer**: Assigns strictly monotonic sequence numbers per conversation.
* **Media Service**: S3 object storage for image/video attachments.

## 10. Data Flow
1. User A sends message to User B over WebSocket.
2. Gateway forwards to Chat Service.
3. Service persists to ScyllaDB and queries Redis for User B session.
4. If User B is online on Gateway 2: dispatch over internal mesh $ightarrow$ delivered via Gateway 2 socket.
5. If User B is offline: emit to Kafka $ightarrow$ Trigger push notification.

## 11. API Design
WebSocket binary frame protocol (Protobuf):
```protobuf
message ChatMessage {
  string conversation_id = 1;
  string message_id = 2;
  string sender_id = 3;
  bytes encrypted_payload = 4;
  int64 timestamp = 5;
}
```

## 12. Data Model
```sql
CREATE TABLE conversation_messages (
    conversation_id UUID,
    message_id      TIMEUUID,
    sender_id       UUID,
    payload         BLOB,
    PRIMARY KEY (conversation_id, message_id)
) WITH CLUSTERING ORDER BY (message_id DESC);
```

## 13. Storage Architecture
ScyllaDB / Apache Cassandra. LSM-Tree storage delivers linear write throughput for immutable append-only chat streams.

## 14. Caching Architecture
Redis stores active user session locations (`user:101` $ightarrow$ `gateway-node-4`) and last 50 messages per active conversation.

## 15. Messaging & Async Processing
Kafka handles offline push notification queues, group message fan-out, and search indexing pipelines.

## 16. Scalability Strategy
* **Connection Multiplexing**: Linux epoll-based gateway nodes (Go/Netty) support $100,000$ open sockets per node $ightarrow$ 100 gateway nodes handle 10M connections.
* **Group Fan-out**: For small groups (<100 members), fan out on write; for massive channels (Slack #general), fan out on read.

## 17. Performance Optimization
* Binary Protobuf serialization reduces payload size by $70\%$ compared to JSON over WebSocket.
* TCP Socket buffer tuning (`tcp_rmem` / `tcp_wmem`) bounds kernel memory to 4KB per socket.

## 18. Reliability & Fault Tolerance
* Ephemeral socket recovery: When a mobile device reconnects, it sends its `last_received_message_id`; the gateway streams missed messages immediately.

## 19. Consistency & Transactions
Strict FIFO ordering enforced per conversation via TimeUUIDs. Cross-conversation transactions are not required.

## 20. Security Architecture
End-to-End Encryption (Signal Protocol: Double Ratchet algorithm). The server relays encrypted binary blobs and has zero ability to decrypt message contents.

## 21. Observability Strategy
Metrics: `websocket_active_connections`, `message_e2e_delivery_latency_ms`, `dropped_socket_count`.

## 22. Disaster Recovery
Multi-region ScyllaDB replication across 3 cloud regions.

## 23. Cost Optimization
Pre-signed direct S3 uploads for media files offload multi-gigabyte media bandwidth from gateway servers.

## 24. Trade-off Analysis
* **Fan-Out on Write vs. Fan-Out on Read**: Fan-out on write delivers instant notification for 1-on-1 chat but collapses on massive groups. Hybrid model switches to read-fanout for groups $>500$ members.

## 25. Failure Scenarios
* **Gateway Node Crash**: $100,000$ mobile sockets disconnect simultaneously; client reconnect exponential backoff with full jitter prevents thundering herd on remaining gateways.

## 26. Production Considerations
* Set up automated heartbeats (ping/pong every 30s) to detect dead cellular sockets and prevent NAT timeouts.
