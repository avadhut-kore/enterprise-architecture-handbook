# Case Study: 1M WebSocket Epoll File Descriptor & Memory Exhaustion

> **Metadata**: ID: `CS-SCALE-05` | Domain: Scalability / Real-Time Web | Type: Synthetic Forensic Case Study | Complexity: Advanced

---

## 01. Executive Summary
A cloud-based real-time collaborative whiteboard platform ($150M ARR) designed to support 1 Million concurrent enterprise users suffered a catastrophic infrastructure collapse during a global virtual corporate keynote. As 650,000 users connected their browsers to the live collaborative whiteboard, the Node.js WebSocket gateway servers crashed in rapid succession. The root cause was an alignment of operating system and network architecture limits: the Linux system default **File Descriptor (FD) limit (`nofile = 1024`)** was exhausted, TCP socket receive/send buffers consumed all physical kernel RAM (**Socket Buffer Memory Exhaustion**), and Node.js single-threaded event loops froze processing raw TLS framing packets, terminating all active collaboration sessions.

---

## 02. Business & System Context
- **Organization**: SaaS Collaborative Whiteboard & Digital Workspaces.
- **Core Workflow**: Real-Time Cursor Tracking, Canvas Vector Sync, and Collaborative Chat.
- **Scale**: 650,000 active concurrent WebSocket connections.

---

## 03. Scope & Stakeholders
- **Incident Commander**: Principal Edge Systems Architect.
- **Key Teams**: Real-Time Gateway Team, Linux Systems Operations, Platform SRE.
- **Impacted Systems**: 40 Node.js WebSocket Gateway EC2 Instances.

---

## 04. Requirements & NFRs
- **Concurrent Connections**: Maintain 1,000,000 persistent, bi-directional WebSocket connections.
- **Message Latency**: P95 cursor broadcast latency $< 50\text{ ms}$.
- **Memory Footprint**: Average RAM overhead $< 15\text{ KB}$ per idle WebSocket connection.

---

## 05. Constraints & Assumptions
- **The "WebSockets are Cheap" Assumption**: Engineers assumed that an idle WebSocket connection consumes virtually zero resources, neglecting the OS kernel TCP memory (`rmem`/`wmem`) and application-level session object memory.

---

## 06. Architecture Before: The Fragile Node.js WebSocket Tier
```mermaid
graph TD
    Clients[650,000 Enterprise Browsers] --> NLB[AWS Network Load Balancer]
    NLB --> Gateways[40 Node.js WebSocket Gateway Nodes: m5.4xlarge]
    
    subgraph Operating System & Runtime Collapse (Per Gateway Node)
        Gateways --> FD_Limit[Linux OS Limit: nofile = 1024 (EXHAUSTED!)]
        Gateways --> TCP_Mem[TCP Buffer Allocation: 128KB per socket x 16k conns = Kernel OOM!]
        Gateways --> NodeLoop[Single-Threaded Event Loop: 100% CPU on TLS Framing]
    end
    
    Gateways --> Crash[Kernel Panic & Node.js CrashLoop -> 650k Connections Dropped!]
```

---

## 07. Architecture Decisions
| Decision | Rationale | Downstream Failure |
| :--- | :--- | :--- |
| **Node.js (`ws` Library) on Default Linux AMI** | Rapid prototyping; event-driven model felt natural for WebSockets. | Default Linux kernel tuning (`ulimit -n 1024`, default TCP window sizes) prevented scaling beyond 1,000 sockets per server; Node's single-threaded event loop choked on TLS crypto. |
| **Termination of TLS Inside Application Process** | Kept architecture simple by avoiding a separate edge reverse proxy layer. | Saturated the single Node.js V8 execution thread with SSL/TLS record parsing, starving cursor broadcast processing. |

---

## 08. Timeline
```mermaid
timeline
    title 1M WebSocket Collapse Timeline
    14:00 UTC : Global virtual keynote begins; attendees connect to collaborative canvas
    14:05 UTC : Concurrent connections surge from 50,000 to 450,000 across 40 gateway servers
    14:08 UTC : Gateway nodes hit OS file descriptor ceiling: `EMFILE: too many open files`
    14:12 UTC : Linux kernel memory exhaustion: `TCP: out of memory -- consider increasing sysctl_tcp_mem`
    14:15 UTC : All 40 Node.js gateway processes crash; NLB health checks fail; complete connection blackout
    14:30 UTC : SREs attempt restart; instant thundering herd of 650,000 reconnecting clients crashes servers again
```

---

## 09. Incident Event
At 14:05 UTC, as a Fortune 500 company began an all-hands interactive keynote, 650,000 enterprise users clicked into the live whiteboard canvas. Inbound WebSocket upgrades flooded the 40 Node.js gateway instances. Within 3 minutes, servers began throwing fatal `EMFILE: too many open files` errors because the system administrator had not increased the default Linux `ulimit -n` of 1024. On servers where file limits were higher, the Linux kernel allocated default 128KB read and write buffers for each TCP socket ($16,000 \times 256\text{KB} = 4.1\text{GB}$ of non-swappable kernel slab memory per server), causing out-of-memory kernel panics. When the servers rebooted, a massive thundering herd of 650,000 clients attempting to reconnect crashed the gateways instantly.

---

## 10. Symptoms & Evidence
- **Fact**: Gateway application logs were flooded with `Error: accept EMFILE`.
- **Fact**: Linux kernel log (`dmesg`) output: `Out of Socket memory` and `TCP: too many orphaned sockets`.
- **Fact**: Memory profiling revealed that each idle Node.js WebSocket connection consumed **72 Kilobytes of V8 heap memory**, plus **64 Kilobytes of kernel TCP memory** (136 KB total per connection).
- **Inference**: High-concurrency persistent connection architectures are operating-system and kernel-networking problems, not just application code problems.

---

## 11. Failure Forensics
```
[650,000 Users connect simultaneously]
                  │
                  ▼
[16,250 WebSocket connections arrive per server node]
                  │
  ┌───────────────┴───────────────┐
  ▼                               ▼
[ulimit -n 1024 hit: EMFILE]     [Kernel TCP Buffers allocate 128KB/socket]
  │                               │
  ▼                               ▼
[New connections dropped]        [Kernel Slab Memory Exhaustion: OOM]
  │                               │
  └───────────────┬───────────────┘
                  ▼
[Node.js Single-Threaded Event Loop Frozen on TLS Parsing]
                  │
                  ▼
[All 40 Gateway Instances Crash -> Complete Blackout]
```

---

## 12. Root Cause Analysis (5-Whys)
1. **Why did the whiteboard disconnect for 650,000 users?** -> All 40 WebSocket gateway instances crashed.
2. **Why did the gateway instances crash?** -> They ran out of operating system file descriptors and kernel TCP memory.
3. **Why did they run out of resources?** -> Default Linux OS kernel parameters were left un-tuned for high-concurrency connection density.
4. **Why was per-socket memory so high?** -> TCP receive/send socket buffers were sized for bulk data transfer rather than tiny, high-frequency JSON cursor updates.
5. **Why was this not tested beforehand?** -> Scalability load tests simulated message throughput (bytes/sec) rather than connection concurrency (open sockets).

---

## 13. Contributing Factors
- **Thundering Herd Reconnects**: Client mobile and web apps re-attempted connections immediately upon disconnect without randomized exponential backoff.
- **Monolithic Process Role**: The same Node.js process terminated TLS, managed WebSocket state, and executed canvas synchronization logic.

---

## 14. Architecture After: Kernel-Tuned Envoy Edge with Go Gateway
```mermaid
graph TD
    Clients[1,000,000 Enterprise Browsers] --> Cloudflare[Cloudflare Edge: Connection Throttling]
    Cloudflare --> EnvoyFleet[Envoy Proxy Fleet (C++): TLS Termination & Epoll Optimization]
    
    subgraph Kernel-Tuned High-Density Cluster (sysctl tuned)
        EnvoyFleet -->|Cleartext Local WebSockets| GoGateway[Go WebSocket Gateway Fleet]
        GoGateway -->|epoll / netpoll: Zero-Copy| Kernel[Linux Kernel: tcp_rmem/wmem tuned to 4KB!]
        GoGateway --> RedisMesh[(Redis Cluster: Cursor Pub/Sub)]
    end
    
    Note[Memory Per Connection Drops from 136KB to 9.2KB!]
```

---

## 15. Recovery & Remediation
- **Immediate Mitigation**: Scaled out 120 new gateway instances; applied emergency `sysctl` updates; deployed a client-side update with **exponential backoff and full jitter** to disperse the reconnect storm.
- **Permanent Architectural Fix**:
  - **Linux Kernel Network Tuning**: Tuned kernel socket parameters across all gateway AMIs:
    ```bash
    # Enforce 2 Million open file descriptors
    fs.file-max = 2097152
    * soft nofile 1048576
    * hard nofile 1048576
    # Minimize TCP buffer sizes for small real-time messages (min, default, max)
    net.ipv4.tcp_rmem = 4096 87380 16777216
    net.ipv4.tcp_wmem = 4096 65536 16777216
    ```
  - **Decoupled TLS Termination**: Offloaded all TLS handshakes to an **Envoy Proxy fleet**, freeing gateway compute nodes from cryptographic math.
  - **Migrated Gateway to Go (netpoll)**: Rewrote the WebSocket gateway in Go using the **`gorilla/websocket` and `epoll`-based event loops**, reducing per-connection memory overhead from 136KB to **9.2 Kilobytes**.

---

## 16. Business & Technical Impact
- **Financial**: Retained key Fortune 50 enterprise client by providing a comprehensive forensic RCA and SLA compensation.
- **Connection Capacity**: Single-node capacity increased from 1,000 to **75,000 concurrent WebSockets per node**.
- **System Footprint**: Safely supported **1.2 Million concurrent connections** during subsequent load tests using only 16 instances.

---

## 17. What Went Well
- The Linux kernel telemetry (`/proc/net/sockstat`) immediately highlighted that socket memory consumption was the underlying trigger.
- Rewriting the gateway in Go dramatically improved memory predictability and eliminated garbage collection latency spikes.

---

## 18. Lessons Learned
- **Architecture**: In high-density persistent connection architectures, the operating system kernel is part of your architecture. Default OS parameters are sized for general servers, not million-connection gateways.
- **Memory Math**: Always calculate: $\text{Memory} = \text{Connections} \times (\text{App Heap} + \text{Kernel Sockets})$.

---

## 19. Architectural Recommendations
| Horizon | Action Item | Owner | Target |
| :--- | :--- | :--- | :--- |
| **Immediate** | Codify `sysctl` and `nofile` socket limits in base Terraform/Packer AMIs | Infra Lead | `nofile` $\ge 1,048,576$ |
| **30 Days** | Mandate randomized jitter in all client WebSocket reconnection libraries | Client Arch | Zero reconnect storms |
| **90 Days** | Decouple TLS termination from WebSocket application gateways | Edge Lead | Offload crypto to Envoy |
