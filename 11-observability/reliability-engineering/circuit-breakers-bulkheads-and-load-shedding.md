# Circuit Breakers, Bulkheads & Load Shedding

## Executive Summary

1. **Circuit Breaker State Machine**:
   ```mermaid
   stateDiagram-v2
       [*] --> Closed: Normal Operation
       Closed --> Open: Error rate exceeds 50% in 10s
       Open --> HalfOpen: Sleep window (30s) expires
       HalfOpen --> Closed: 5 consecutive probe calls succeed
       HalfOpen --> Open: Any probe call fails
   ```
2. **Bulkhead Isolation**: Partition thread pools and database connections so that a slow reporting service cannot exhaust all threads needed for real-time payments.
3. **Load Shedding**: When CPU exceeds 85%, drop non-critical requests (analytics, search auto-complete) with HTTP 503 while preserving critical transactions (checkout).
