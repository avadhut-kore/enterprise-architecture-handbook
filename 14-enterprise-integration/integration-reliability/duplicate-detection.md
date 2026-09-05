# Duplicate Message Detection and De-duplication

## 1. Origins of Duplicate Messages
Duplicates arise from normal distributed recovery protocols:
- Network ACK dropped after consumer has successfully committed database transaction.
- Consumer rebalance in Kafka occurs while processing is underway.
- Upstream retry triggered by conservative timeout threshold.

## 2. Sliding Window De-duplication Pattern

```
[Incoming Message] ──> [Extract Business Fingerprint] (Hash: SHA-256(tenant+account+tx_id))
                               │
                      [Query Redis Bloom Filter / Set]
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
             [Found in Set]           [Not Found]
                  │                         │
            Discard Message           1. Add to Redis (TTL = 24h)
            (Log DUPLICATE_DROP)      2. Forward to Business Pipeline
```
