# Asynchronous Processing & Non-Blocking I/O

## 1. Concurrency Models Comparison
Synchronous blocking architectures allocate one operating system thread per connection. Under massive concurrency ($10^5+$ connections), this model collapses due to thread stack memory consumption and OS context-switching overhead.

```mermaid
flowchart TD
    subgraph Synchronous Blocking [Apache / Classic Java]
        C1[Client 1] --> T1[Thread 1: Blocks on DB 50ms]
        C2[Client 2] --> T2[Thread 2: Blocks on DB 50ms]
        C3[Client 3] --> WaitQueue[No Threads Available -> Connection Refused!]
    end

    subgraph Non-Blocking Reactive [Netty / Node / Go / Java Loom]
        AllClients[100,000 Clients] --> Epoll[Linux Epoll / Kqueue Event Loop]
        Epoll --> Workers[Small Worker Pool = Number of CPU Cores]
        Workers -->|Asynchronously Dispatched| DB[(Non-Blocking Async DB)]
    end
```

---

## 2. Java Virtual Threads (Project Loom) vs. Reactive Streams
* **Reactive Programming (Project Reactor, RxJava)**: Delivers exceptional resource efficiency but introduces steep cognitive complexity, fragmented call stacks, and difficult debugging.
* **Virtual Threads (JDK 21+)**: Restores simple imperative code (`thread-per-request` syntax) while executing over lightweight user-space fibers mounted dynamically to carrier OS threads.
