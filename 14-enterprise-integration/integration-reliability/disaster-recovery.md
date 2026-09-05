# Disaster Recovery and Multi-Region Integration

## 1. RPO and RTO in Enterprise Integration
- **Recovery Point Objective (RPO)**: The maximum acceptable data loss measured in time (e.g., RPO = 0 for core banking; RPO $\le 5$ min for analytics).
- **Recovery Time Objective (RTO)**: The maximum acceptable downtime before integration pipelines are restored (e.g., RTO $\le 1$ hour).

## 2. Multi-Region Active-Active vs. Active-Passive

| Pattern | Topology | Broker Replication | Failover Mechanics |
| :--- | :--- | :--- | :--- |
| **Active-Passive** | Primary in Region A, Hot Standby in Region B | Async MirrorMaker 2 / S3 replication | DNS routing switch, consumer group offset translation |
| **Active-Active** | Both regions process independent tenant traffic | Bi-directional topic replication | Global Anycast DNS, multi-region distributed locking |

## 3. The Kafka MirrorMaker Offset Gap
When failing over Kafka consumer groups to a secondary region, partition offsets will not match. Integration architectures must utilize tools like MirrorMaker 2 checkpoint topics (`__consumer_offsets`) to translate committed offsets across clusters during regional failover.
