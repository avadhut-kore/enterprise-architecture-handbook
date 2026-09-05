# Reference Architecture: 05 Salesforce Enterprise Crm

## 1. Architectural Vision & Business Drivers
This reference architecture provides a comprehensive, production-grade blueprint for 05 salesforce enterprise crm. It balances low-latency runtime performance, high-availability guarantees, regulatory compliance, and non-blocking asynchronous event choreography.

## 2. End-to-End System Blueprint

```
                  [External Consumer Channels & Partner Networks]
                                         │
        ═════════════════════════════════▼═════════════════════════════════  [Edge WAF / mTLS Gateway]
                   Enterprise API Gateway & Ingress Layer
                   ├── OAuth 2.0 / OIDC Token Exchange
                   ├── Distributed Idempotency Key Verification
                   └── Token Bucket Rate Limiting
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
[Synchronous Domain Services]   [Enterprise Event Backbone]      [Batch & MFT Ingestion]
├── OpenAPI / gRPC Facades       ├── Apache Kafka Cluster         ├── Secure SFTP / AS2
└── Circuit Breakers & Retries   └── Schema Registry              └── Large File Chunking
        │                                │                                │
        └────────────────────────────────┼────────────────────────────────┘
                                         ▼
                     Core Business Systems & Ledgers of Record
                     ├── Core Databases & Anti-Corruption Layers
                     ├── Reconciliation & Audit Logs
                     └── Outbox CDC Streaming
```

## 3. Critical Architectural Decisions & Trade-Offs
- **Transport Protocol**: mTLS 1.3 enforced across all cross-system boundaries.
- **Delivery Guarantee**: At-least-once delivery coupled with persistent server-side idempotency tracking in Redis.
- **Failure Resilience**: Dead Letter Queues with automated diagnostic envelopes and operational replay runbooks.

## 4. Canonical Diagrams Reference
- Refer to [17-diagrams/c4/02-container-core-banking.md](../../17-diagrams/examples/core-banking.md) and [17-diagrams/sequence/01-order-fulfillment-saga.md](../../17-diagrams/sequence/saga.md).
