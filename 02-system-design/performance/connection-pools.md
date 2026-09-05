# Database Connection Pooling

## 1. Why Connection Pooling Is Critical
Opening a raw database connection is expensive:
1. TCP 3-way handshake ($1\text{ RTT}$).
2. TLS negotiation handshake ($2\text{ RTTs}$).
3. Database authentication and role verification.
4. Server OS spawns backend worker process and allocates private memory buffers ($5\text{--}10\text{ MB}$).
*Total Cost*: $25\text{--}80\text{ ms}$ per query! Connection pools maintain pre-authenticated sockets, reducing query connection latency to zero.

---

## 2. Pool Sizing: The Universal PostgreSQL / HikariCP Formula

A dangerous anti-pattern is configuring massive connection pools (e.g., 500 connections per app instance across 20 pods = 10,000 connections). This forces the database server into massive CPU context switching thrash.

$$\text{Max Pool Connections} = (\text{CPU Cores} \times 2) + \text{Disk Spindle / Channel Count}$$

```mermaid
flowchart TD
    subgraph Anti-Pattern: 1,000 Open DB Connections
        Bad[1,000 Waiting Backend Processes -> CPU Context Switching -> 504 Timeouts]
    end

    subgraph Best Practice: 32 Tuned Connections
        Good[32 Active Connections -> CPU Saturates at 100% Useful Work -> Sub-5ms p99!]
    end
```

---

## 3. Connection Leak Prevention
* **Leak Detection Threshold**: Set `leakDetectionThreshold = 5000ms`. HikariCP prints a stack trace if a thread holds a connection for longer than 5 seconds without releasing it.
* **Max Lifetime**: Set `maxLifetime = 30 minutes` to periodically recycle connections and avoid memory leaks in database backend daemons.
