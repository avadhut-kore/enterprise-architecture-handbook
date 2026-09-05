# Distributed Chat System Architecture

## 1. End-to-End Chat Topology

```mermaid
flowchart TD
    User1[Sender: User 1] -->|WebSocket: Send Message| GW1[Chat Gateway 1]
    GW1 --> ChatSvc[Chat Service / Message Sequencer]
    ChatSvc --> MsgDB[(Message Store: Cassandra / ScyllaDB)]
    ChatSvc --> Kafka[Kafka Broker: Event Bus]
    
    Kafka --> PushWorker[Push Notification Worker]
    PushWorker --> APNS_FCM[Apple APNS / Google FCM]
    
    Kafka --> Router[Gateway Router]
    Router -->|User 2 Connected to GW 2| GW2[Chat Gateway 2]
    GW2 -->|WebSocket: Deliver Message| User2[Recipient: User 2]
```

---

## 2. Storage Engine: Why Cassandra / ScyllaDB?
* **Write Optimization**: Chat messages are immutable, append-only records with a $1:1$ read-to-write ratio. LSM-tree stores write at memory speed.
* **Partition Key Design**:
  ```sql
  CREATE TABLE messages (
      conversation_id UUID,
      message_id      TIMEUUID,
      sender_id       UUID,
      content         TEXT,
      PRIMARY KEY (conversation_id, message_id)
  ) WITH CLUSTERING ORDER BY (message_id DESC);
  ```
  * All messages for a conversation reside on the same partition, ordered by timestamp in reverse for instant $O(1)$ channel history retrieval.
