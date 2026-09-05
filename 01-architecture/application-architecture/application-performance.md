# Application Performance Engineering

## 1. Allocation & Garbage Collection Optimization

In high-throughput services (10k+ QPS):
- **Object Allocations**: Frequent allocation of short-lived objects triggers CPU-intensive garbage collection cycles (JVM young-gen GC, .NET Gen 0/1 GC pauses).
- **Techniques**:
  - Pool memory buffers (`ArrayPool<T>`, Netty `ByteBuf`).
  - Use value types / structs where appropriate to avoid heap allocations.
  - Stream large I/O payloads directly to network sockets instead of buffering in memory.

---

## 2. Non-Blocking Asynchronous I/O

- Never execute blocking synchronous I/O (`Thread.sleep()`, `.Result`, `.GetAwaiter().GetResult()`) inside worker threads.
- Blocking worker threads starves thread pools, causing cascading request latency spikes.
