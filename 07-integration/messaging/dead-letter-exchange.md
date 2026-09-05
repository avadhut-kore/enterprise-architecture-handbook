# Dead Letter Exchange (DLX) Architecture

## 1. Routing Poison & Expired Messages
In RabbitMQ, a **Dead Letter Exchange (DLX)** is an exchange to which messages are automatically routed when they cannot be delivered or processed in their primary queue.

```mermaid
flowchart LR
    Q_Main[(Primary Orders Queue)] -->|basic.nack with requeue=false| DLX{Dead Letter Exchange}
    Q_Main -->|TTL Expiration in Queue| DLX
    Q_Main -->|Queue Max-Length Exceeded| DLX
    
    DLX --> Q_Dead[(Dead Letter Parking Queue)]
    Q_Dead --> SRE[SRE Diagnostic / Redrive Tool]
```

---

## 2. Configuration Directives (RabbitMQ)
```json
{
  "x-dead-letter-exchange": "orders.dlx",
  "x-dead-letter-routing-key": "orders.poison",
  "x-message-ttl": 86400000
}
```
* Messages rejected with `basic.reject(requeue=false)` bypass the main queue and are preserved durably in the dead letter parking lot.
