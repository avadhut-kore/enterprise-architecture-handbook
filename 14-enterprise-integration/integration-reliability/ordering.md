# Message Ordering and Partitioning in Integration

## 1. The Distributed Ordering Dilemma
In distributed systems, achieving total global ordering across multiple nodes requires single-threaded processing, creating an severe throughput bottleneck. Enterprise integration architectures achieve scale by enforcing **per-partition ordering** rather than global ordering.

## 2. Partition Key Architecture (Kafka / Message Queues)

```
Incoming Stream of Transactions:
[Acct 1: Deposit] ──┐
[Acct 2: Debit]   ──┼──> [Partition Key: account_id] 
[Acct 1: Transfer]──┘           │
                                ├─ Hash(Acct 1) ──> Partition 0 (Strict FIFO for Acct 1)
                                └─ Hash(Acct 2) ──> Partition 1 (Strict FIFO for Acct 2)
```

## 3. Resequencer Pattern
When asynchronous networks route packets over divergent paths, messages may arrive out of chronological order:
- **Resequencer**: Buffers out-of-sequence messages in an in-memory or Redis sorted set using an incrementing sequence number or business timestamp, emitting messages downstream only when previous gaps are filled.
