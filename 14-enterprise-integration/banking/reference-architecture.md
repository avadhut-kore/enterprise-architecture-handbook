# Core Banking Modernization Reference Architecture

## 1. Target Topology Diagram

```
                 [Digital Channels: Web / Mobile / Branch]
                                    │
                                    ▼
                [API Gateway / WAF / OAuth2 Token Exchange]
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
[Real-Time Payment Orchestrator]                        [Customer Account Service]
    │                                                               │
    ├──────── (Real-time balance lookup) ──> [Redis Read Cache] ────┤
    │                                               ▲               │
    ▼                                               │               ▼
[Kafka Enterprise Event Backbone] ──────────────────┤   [Fraud Screening Engine]
    │                                               │
    ▼ (Debezium CDC Stream)                         │
[Core Banking Anti-Corruption Layer (ACL)] ─────────┘
    │
    ▼ (Mainframe MQ / SNA / CPYBOOK)
[Legacy Core Banking Ledger (IBM z/OS / DB2)]
```

## 2. Canonical Diagram Reference
See [17-diagrams/c4/02-container-core-banking.md](../../17-diagrams/examples/core-banking.md).
