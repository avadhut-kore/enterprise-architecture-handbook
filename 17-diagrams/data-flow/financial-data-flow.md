# Financial Data Flow & Double-Entry Ledger Pipeline

Strict financial accounting architecture enforcing double-entry bookkeeping invariants, transactional idempotency, and immutable audit journals.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph TransactionIngress ["Payment Initiation Tier"]
        PayReq["Payment Instruction Payload<br/>(Idempotency-Key: uuid-v4)"]
        PayGW["Payment Ingress Controller"]
        PayReq --> PayGW
    end

    subgraph IdempotencyControl ["Deduplication & Distributed Lock"]
        RedisLock["Redis Distributed Lock / Idempotency Cache"]
        PayGW -->|"Verify Uniqueness"| RedisLock
    end

    subgraph LedgerExecution ["Core Ledger Engine (Atomic Multi-Leg)"]
        LedgerSvc["Double-Entry Accounting Service"]
        LedgerDB[("Immutable Ledger Journal (PostgreSQL)<br/>[WORM Table - Insert Only]")]

        PayGW -->|"Execute Balanced Posting"| LedgerSvc
        LedgerSvc -->|"Begin Transaction"| LedgerDB
        
        LedgerDB --> Debit["Leg 1: DEBIT Asset / Cash Account (-$100.00)"]
        LedgerDB --> Credit["Leg 2: CREDIT Customer Balance Account (+$100.00)"]
        Debit --- BalCheck["Invariant: SUM(Debits) == SUM(Credits)"]
        Credit --- BalCheck
        BalCheck -->|"Commit Transaction"| LedgerDB
    end

    subgraph AuditAndRecon ["Audit & Bank Reconciliation"]
        ReconEngine["Automated Bank Reconciliation Engine"]
        BankFeed["External Bank MT940 / BAI2 File Feed"]
        
        LedgerDB --> ReconEngine
        BankFeed --> ReconEngine
        ReconEngine -->|"Discrepancy Alerts"| OpsConsole["Finance Operations Console"]
    end

    classDef pay fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef ldg fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef rcn fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    class PayReq,PayGW,RedisLock pay;
    class LedgerSvc,LedgerDB,Debit,Credit,BalCheck ldg;
    class ReconEngine,BankFeed,OpsConsole rcn;
```

## PlantUML Specification

```plantuml
@startuml
autonumber
actor Client
participant "Payment Gateway" as gw
database "Idempotency Cache" as redis
participant "Ledger Engine" as ledger
database "Ledger Journal DB" as db
participant "Bank Feeds" as bank
component "Reconciliation" as recon

Client -> gw : POST /transfers (Idempotency-Key)
gw -> redis : Acquire Lock & Check Existing Key
redis -> gw : Lock Granted (New Transaction)
gw -> ledger : Post Double-Entry Transaction
ledger -> db : Insert Debit & Credit Legs (Zero-Sum Invariant)
db -> ledger : Commit Success
ledger -> redis : Cache Completed Result Payload
ledger -> Client : 201 Created (Transfer Confirmed)
recon -> db : Read Cleared Postings
bank -> recon : Ingest Daily Bank Statement
recon -> recon : Reconcile Settlement Accounts
@enduml
```

## Architectural Design Considerations

* **Strict Invariant Enforcement**: Every transaction must record at least two balanced entries; `SUM(Debits) - SUM(Credits) == 0` must be mathematically enforced via database constraints.
* **Append-Only Immutable Ledger**: Never execute `UPDATE` or `DELETE` on financial ledger entries; correct historical errors exclusively through explicit reversal and offsetting journal postings.
* **Idempotency Keys**: Mandate unique `Idempotency-Key` headers for all money movement APIs to guarantee safe retries across network timeouts.

## Related Documentation & Patterns

* [Sequence: Payment Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/sequence/payment.md)
* [PII Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/pii-flow.md)
* [Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md)
