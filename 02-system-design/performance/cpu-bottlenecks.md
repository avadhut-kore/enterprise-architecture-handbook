# CPU Bottleneck Analysis

## 1. Identifying CPU Saturation
CPU bottlenecks occur when execution threads spend excessive time waiting for scheduling quantum slices or executing computationally intensive operations.

---

## 2. Common Sources of CPU Burn in Distributed Systems
1. **JSON & XML Serialization**: Deserializing multi-megabyte JSON payloads using reflection consumes up to $40\%$ of microservice CPU cycles. *Remedy*: Migrate to Protocol Buffers or FlatBuffers.
2. **Cryptographic TLS Handshakes**: Negotiating RSA/ECDSA keys during initial TCP connections. *Remedy*: Enable TLS Session Resumption and keep-alive connection pooling.
3. **Regular Expression Inefficiencies (ReDoS)**: Catastrophic backtracking in poorly constructed regexes consuming $100\%$ of a core.
4. **Context Switching & Thread Thrashing**: Running 2,000 OS threads on an 8-core machine forces the Linux kernel scheduler to spend more CPU time swapping thread register states than executing business code.
