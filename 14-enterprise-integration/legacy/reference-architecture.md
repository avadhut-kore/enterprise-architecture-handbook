# Legacy Mainframe Modernization Reference Architecture

## 1. Target Architecture Blueprint

```
                  [Modern Cloud Channels: Web / Mobile]
                                    │
                                    ▼
                 [API Gateway / Traffic Router (Strangler)]
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
[Modern Cloud Microservices]                            [Anti-Corruption Layer (ACL)]
    │                                                               │
    ├──────── (Async Events via Kafka) ─────────────────────────────┤
    │                                                               │
    ▼                                                               ▼
[Cloud Aurora DB]                                       [Mainframe Connectors (MQ/CTG)]
                                                                    │
                                                                    ▼
                                                 [Legacy Mainframe (IBM z/OS)]
                                                 ├── CICS / COBOL Transactions
                                                 └── DB2 / VSAM Datastores
```
