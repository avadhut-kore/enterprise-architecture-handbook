# IBM MQ (MQSeries) to Apache Kafka Event Bridges

## 1. The MQ-Kafka Connector Topology
```
[Mainframe CICS Application] ──(Puts MQ Message)──> [IBM MQ Queue]
                                                           │
                                                           ▼
                                            [Kafka Connect MQ Source]
                                                           │
                                                           ▼
                                            [Kafka Topic: legacy.events]
```
