# Sequence Flows & Failure Recovery: Enterprise ERP

## 1. Procure-to-Pay Automated Three-Way Matching Flow

```mermaid
sequenceDiagram
    autonumber
    participant Vendor as Vendor Portal
    participant AP as Accounts Payable Engine
    participant Matcher as 3-Way Matching Worker
    participant DB as Universal Journal
    participant Bank as Corporate Bank

    Vendor->>AP: Submit Electronic Invoice (EDI 810 / XML)
    AP->>Matcher: Trigger Validation (PO #45001)
    Matcher->>DB: Query PO Details & Goods Receipt Quantities
    DB-->>Matcher: PO Line Items & GR Confirmation
    alt Match Successful (Price & Quantity Agree)
        Matcher->>DB: Commit Balancing Journal Document (DR Expense, CR AP)
        Matcher-->>Vendor: Invoice Approved (Scheduled for Payment)
        Note over DB,Bank: Payment run dispatches ISO 20022 pain.001 to Bank
    else Match Variance Exceeds Tolerance
        Matcher->>AP: Flag Variance Block; Route to Human Review Queue
    end
```
