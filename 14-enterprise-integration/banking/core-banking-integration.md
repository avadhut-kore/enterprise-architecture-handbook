# Core Banking Integration Strategies and Patterns

## 1. Integration Topologies
Integrating third-party solutions (CRM, Fraud, Payment Rails) with core banking requires choosing between three architectural patterns:

| Strategy | Mechanism | Latency | Data Freshness | Blast Radius |
| :--- | :--- | :--- | :--- | :--- |
| **Direct Synchronous RPC** | SOAP/REST/MQ call during customer transaction | 100ms - 800ms | Immediate | High (Core latency impacts customer channel) |
| **Asynchronous Outbox** | Local DB commit + Debezium CDC to Kafka | 50ms - 2000ms | Near real-time | Low (Channel continues if core is delayed) |
| **Batch File Exchange** | SFTP transmission of ISO 20022 / NACHA files | Hours | End-of-Day | Zero (Decoupled batch window processing) |

## 2. Distributed Transaction Challenge: Dual-Write Mitigation
When customer balance must be deducted in Core Banking and loyalty points awarded in CRM, never use Two-Phase Commit (2PC / XA) across network boundaries. Deploy a **Saga Orchestrator with Compensating Transactions**:

```
[Saga Orchestrator] ──(1) Debit Core Ledger (POST /v1/accounts/{id}/debit)──> [Core Banking]
        │
        ├─ [SUCCESS] ──(2) Credit Points (POST /v1/points)──> [CRM]
        │
        └─ [FAILURE] ──(Compensate) Execute Credit Reversal ──> [Core Banking]
```
