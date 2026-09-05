# Salesforce Enterprise Integration Reference Architecture

## 1. Target Topology

```
                  [Customer Web / Mobile Channels]
                                 │
                                 ▼
                 [Salesforce Service & Sales Cloud]
                                 │
     ┌───────────────────────────┴───────────────────────────┐
     ▼                                                       ▼
[Pub/Sub gRPC Stream]                               [Composite REST API]
(Platform Events / CDC)                                      ▲
     │                                                       │
     ▼                                                       │
[Enterprise Event Mesh / Kafka] ──> [Enterprise Integration Layer]
                                             │
                                             ▼
                                  [ERP / Core Banking]
```
