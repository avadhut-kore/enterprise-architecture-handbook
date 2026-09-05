# Case Study: HikariCP Connection Pool Starvation in Core Banking API

> **Metadata**: ID: `CS-PERF-02` | Domain: Performance / Banking | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
A digital banking API platform serving 8 Million retail users experienced a complete outage across all mobile and web banking services within 90 seconds of a minor downstream database latency blip. The root cause was an improperly tuned database connection pool (**HikariCP**) configured with an oversized pool size (100 connections per pod across 50 pods = 5,000 connections) combined with an unbounded connection acquisition timeout (`connectionTimeout = 30000ms`). When the PostgreSQL database experienced a transient 2-second I/O lock, application threads piled up waiting for connections, completely exhausting Tomcat worker thread pools and causing the entire microservices mesh to collapse under thread starvation.

---

## 02. Business & System Context
- **Organization**: Retail Banking & Payment Platform.
- **Core Workflow**: Mobile Account Inquiries, Card Freezes, and Fund Transfers.
- **Scale**: 8,000 HTTP requests/second; 50 containerized API gateway pods.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Lead Reliability Architect.
- **Key Teams**: Core Banking API Squad, PostgreSQL Database Operations, SRE.
- **Technology Stack**: Java 17, Spring Boot 3.1, HikariCP, PostgreSQL Aurora.

---

## 04. Requirements & NFRs
- **API Availability**: 99.99% ($< 4.3\text{ minutes}$ downtime/month).
- **Latency Budget**: Account balance retrieval p99 $< 120\text{ ms}$.
- **Graceful Degradation**: Individual endpoint slowness must never crash unrelated API endpoints.

---

## 05. Constraints & Assumptions
- **The "Bigger Pool is Better" Fallacy**: The engineering team believed that increasing HikariCP pool size from 10 to 100 connections per pod would increase concurrency and prevent connection queueing.

---

## 06. Architecture Before: The Thread Starvation Trap
```mermaid
graph TD
    Client[8,000 Mobile Requests/sec] --> Tomcat[Tomcat Worker Pool: 200 Threads/Pod]
    
    subgraph Application Pod (50 Pods Active)
        Tomcat --> WorkerThread[Thread 1..200]
        WorkerThread --> HikariCP[HikariCP Pool: 100 Connections / 30s Timeout!]
    end
    
    subgraph PostgreSQL Database (5,000 Demanded Connections)
        HikariCP --> Postgres[(Aurora PostgreSQL: Max 1,000 Connections)]
        Postgres -->|Context Switching Thrashing / Disk I/O Stall| Stall[Database Latency Rises to 2.5s]
    end
    
    WorkerThread -. Blocks for 30 seconds! .-> TomcatExhaust[All 200 Tomcat Threads Blocked -> Pod Crashes!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **`maximumPoolSize = 100` per Pod** | "Ensure we never run out of connections during traffic spikes." | 50 pods attempted to open 5,000 connections to a database sized for 1,000 connections; overwhelmed PostgreSQL process scheduler with context switching. |
| **`connectionTimeout = 30000ms`** | Prevented immediate exceptions if the pool was briefly busy. | Caused application worker threads to block for 30 seconds before failing; exhausted all Tomcat request threads, freezing health check endpoints. |

---

## 08. Timeline
```mermaid
timeline
    title Connection Pool Collapse Timeline
    14:00:00 : PostgreSQL initiates routine autovacuum on `TRANSACTION_LOGS` table
    14:00:15 : Disk I/O latency briefly rises from 0.8ms to 2,200ms
    14:00:25 : Database queries take 2.2 seconds; connections held 5x longer than normal
    14:00:40 : HikariCP connection pools exhaust across all 50 pods
    14:01:00 : All 200 Tomcat worker threads per pod blocked in `HikariPool.getConnection()`
    14:01:20 : Kubernetes readiness probes fail because health checks cannot acquire threads
    14:01:30 : Kubernetes terminates and restarts all 50 pods simultaneously; total blackout
```

---

## 09. Incident Event
At 14:00 UTC, a scheduled PostgreSQL autovacuum process created brief disk I/O lock contention, elevating query response times from 15ms to 2,200ms for 30 seconds. Because queries took longer, database connections were retained by threads for 2.2 seconds instead of 15ms. The HikariCP pool exhausted. New incoming HTTP requests blocked on `getConnection()` waiting for the 30-second timeout. Within 60 seconds, all 200 Tomcat worker threads in each pod were paralyzed. Kubernetes readiness probes timed out because no worker threads were free to respond to HTTP `/actuator/health`. Kubernetes declared all 50 pods unhealthy and killed them simultaneously, causing complete banking downtime.

---

## 10. Symptoms & Evidence
- **Fact**: JVM thread dumps (`jstack`) showed 198 out of 200 Tomcat threads in `TIMED_WAITING (parking)` state inside `com.zaxxer.hikari.pool.HikariPool.getConnection()`.
- **Fact**: Kubernetes events recorded 50 pod terminations within a 15-second window due to failed readiness probes.
- **Inference**: An oversized connection pool coupled with a long acquisition timeout converts a minor database latency hiccup into a total application container crash.

---

## 11. Failure Forensics
```
[Transient 2-second DB I/O latency blip]
                  │
                  ▼
[Queries hold DB connections for 2.2s instead of 15ms]
                  │
                  ▼
[HikariCP pool (100 conns) fully checked out]
                  │
                  ▼
[New requests block on getConnection() waiting 30 seconds!]
                  │
                  ▼
[All 200 Tomcat worker threads blocked waiting for DB]
                  │
                  ▼
[Kubernetes /actuator/health probe arrives -> NO FREE THREADS]
                  │
                  ▼
[Probe times out -> Kubernetes kills all 50 pods simultaneously!]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why did mobile banking crash completely?** -> All 50 API gateway pods were killed by Kubernetes.
2. **Why did Kubernetes kill the pods?** -> The HTTP health check endpoints stopped responding.
3. **Why did health checks stop responding?** -> All 200 Tomcat worker threads were blocked waiting to acquire database connections.
4. **Why were they waiting so long?** -> HikariCP `connectionTimeout` was set to 30,000ms (30 seconds).
5. **Why was the pool empty?** -> Connections were held by slow queries during an I/O spike, exacerbated by an oversized pool that throngs the PostgreSQL backend.

---

## 13. Contributing Factors
- **Shared Thread Pool for Health Checks**: The Kubernetes readiness probe endpoint shared the same Tomcat thread pool as user business transactions.
- **Violating the HikariCP Sizing Formula**: Architects ignored the canonical PostgreSQL sizing formula:
  $$\text{Connections} = ((\text{Core Count} \times 2) + \text{Effective Spindle Count})$$

---

## 14. Architecture After: Sized Pools, Fast Failure & Isolated Health Probes
```mermaid
graph TD
    Client[Mobile Requests] --> Tomcat[Tomcat Business Pool: 200 Threads]
    K8sProbe[K8s Readiness Probe] --> MgtServer[Dedicated Management Port 8081: Isolated Threads!]
    
    subgraph Optimized Sizing (Fast Failure)
        Tomcat --> HikariCP[HikariCP Pool: 10 Conns / 1,500ms Timeout!]
        HikariCP --> FastFail{Connection Available in 1.5s?}
        FastFail -->|Yes| Postgres[(PostgreSQL: 500 Total Conns)]
        FastFail -->|No| Shed[Immediate 503 Shed: Pod Stays ALIVE!]
    end
    
    MgtServer -->|Always Responds in < 5ms| Healthy[Pod Stays In Service!]
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: Scaled down pool size via environment variable override; restarted pods with staggered readiness grace periods.
- **Permanent Architectural Fix**:
  - **Sized Connection Pools**: Reduced `maximumPoolSize` from 100 to **10 connections per pod** ($50 \times 10 = 500$ total connections, well within Aurora's sweet spot).
  - **Aggressive Fast-Fail Timeout**: Reduced `connectionTimeout` from 30,000ms to **1,500ms**. If a connection cannot be acquired in 1.5s, the request immediately throws an exception and sheds load, preventing thread pool starvation.
  - **Isolated Management Port**: Configured Spring Boot Actuator on a **dedicated management port (8081)** with an independent thread pool, guaranteeing health checks never block on business traffic.

---

## 16. Business & Technical Impact
- **Downtime**: 45 minutes of complete banking unavailability.
- **Resiliency Verification**: Re-tested under simulated 5-second database freeze: instead of crashing, pods rejected 8% of transactions with immediate HTTP 503s while remaining healthy, recovering within 2 seconds once database I/O cleared.

---

## 17. What Went Well
- The dedicated management port pattern permanently eliminated cascading pod restarts across the enterprise.
- JVM thread dumps captured the exact line of lock contention, making the root cause indisputable.

---

## 18. Lessons Learned
- **Architecture**: In connection pools, less is more. Sizing connection pools larger than database CPU cores increases contention, context switching, and memory thrashing.
- **Fast Failure**: Never wait 30 seconds for a resource in a real-time web path. Fail fast, shed load, and protect the process.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Set `connectionTimeout = 1500ms` across all microservices | Lead SRE | Zero thread starvation |
| **30 Days** | Calculate and enforce strict connection budgets per database engine | Lead DBA | Max 60% of engine limit |
| **60 Days** | Isolate health check endpoints to independent network ports | Platform Arch | Zero false-positive kills |
