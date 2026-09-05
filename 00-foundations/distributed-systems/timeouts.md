# Timeouts & Cascading Failure Prevention

> **Domain**: `00-foundations/distributed-systems`  
> **Status**: Approved  
> **Target Audience**: Solution Architects, Principal Engineers, SREs

---

## 1. Simple Explanation

A **Timeout** is a non-negotiable deadline: if a remote network call or database query does not return an answer within a specified period of time, the client abruptly terminates the waiting connection and takes corrective action.

In software architecture, **a slow downstream dependency is far more dangerous than a dead one.** A dead service fails fast in 1 millisecond; a slow service holds server worker threads hostage for minutes, triggering cascading total system collapse.

---

## 2. Architect-Level Deep Dive: Anatomy of a Network Timeout

A single HTTP call traverses multiple distinct network layers, each requiring an explicit timeout setting:

```mermaid
flowchart LR
    Client["Client Application"] --> Connect["1. Connection Timeout\n(TCP 3-Way Handshake: SYN -> SYN-ACK -> ACK)\nTarget: 200ms - 500ms"]
    Connect --> TLS["2. TLS Handshake Timeout\n(Certificate exchange & key negotiation)\nTarget: 500ms"]
    TLS --> Read["3. Socket / Read Timeout\n(Waiting for server response bytes)\nTarget: 1,500ms - 3,000ms"]
```

### The Anatomy of the Three Timeouts
1. **Connection Timeout**: Time allowed to establish the underlying TCP socket. If the remote host is offline or a firewall silently drops packets, default OS kernel timeouts can wait **75 seconds**! (Must be capped at `500ms`).
2. **TLS Handshake Timeout**: Time allowed to negotiate encryption keys and validate certificates. (Must be capped at `1,000ms`).
3. **Socket / Read Timeout**: Time allowed between reading incoming data bytes from the socket. This governs how long the application waits for the server to process the query and send data.

---

## 3. The Thread Pool Starvation Disaster

What happens when an architect leaves timeouts at default values?

```mermaid
sequenceDiagram
    autonumber
    actor Users as 200 Concurrent Users
    participant App as Order Web Server (Pool: 200 Threads)
    participant Inventory as Slow Inventory Service (Takes 30s)

    Users->>App: Incoming Requests
    App->>Inventory: Call Inventory (No timeout configured!)
    Note over App: Thread 1 blocked...<br/>Thread 2 blocked...<br/>Thread 200 blocked!
    Note over App: THREAD POOL EXHAUSTION! Zero threads left to serve health checks!
    App--xUsers: Server 503 Out of Memory / Kubernetes restarts pod
```

---

## 4. Deadline Propagation (The Context Deadline Pattern)

In modern microservices with deep call chains ($A \to B \to C \to D$), individual static timeouts are insufficient:

```mermaid
flowchart LR
    Client["Client Budget = 2,000ms"] --> SvcA["Service A (Spends 800ms)"]
    SvcA -->|Pass Remaining Deadline: 1,200ms| SvcB["Service B (Spends 1,000ms)"]
    SvcB -->|Pass Remaining Deadline: 200ms| SvcC["Service C (Operation needs 500ms!)"]
    SvcC -- "Abort early! Deadline exceeded before starting" --> SvcB
```

### The Deadline Propagation Principle (gRPC / Go Context / W3C Baggage)
* Service A receives a request with a total latency budget of `2,000ms`.
* Service A spends `800ms` doing local work.
* When Service A calls Service B, it passes the **Remaining Deadline (`1,200ms`)** in the RPC metadata.
* When Service B calls Service C, only `200ms` remain.
* Service C knows its database query takes at least `500ms`. Instead of wasting database CPU on work that will arrive too late for the user anyway, **Service C rejects the call immediately**, saving enterprise compute resources!
