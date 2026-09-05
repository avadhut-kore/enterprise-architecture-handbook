# Human Oversight & Maker-Checker Financial AI Patterns

## 1. The Maker-Checker Pattern for Generative AI

Under banking regulations (such as OCC Bulletin 2011-12 on Model Risk Management), automated systems must maintain strict segregation of duties:

```mermaid
sequenceDiagram
    autonumber
    actor Maker as Operations Specialist (Maker)
    participant AI as AI Reconciliation Assistant
    actor Checker as Senior Compliance Officer (Checker)
    participant Core as Core Settlement Ledger

    Maker->>AI: "Reconcile un-cleared batch transaction 941"
    Note over AI: AI analyzes ledger discrepancies;<br/>generates proposed balancing entry
    AI-->>Maker: Proposed Reconciliation Entry: Credit $14,200 to Account X
    Maker->>Maker: Verify rationale; click "Submit for Approval"
    Maker->>Checker: Dispatch Task to Checker Queue
    Checker->>Checker: Inspect AI rationale, original statement PDF & Maker audit trail
    Checker->>Core: Click "Approve & Settle" (Cryptographic Signature)
    Core-->>Core: Execute Immutable Ledger Settle
```
