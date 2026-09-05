# Reconciliation Architecture: Bank Statement Reconciliation: Internal Ledger vs Bank

## 1. Architectural Purpose & Problem Context
Automated reconciliation of bank statement files (camt.053 / MT940 / BAI2) against internal treasury cash management accounts.

---

## 2. Reconciliation Engine & Exception Flow

```mermaid
flowchart TD
    Internal[(Internal Ledger / Orders)] --> IngestA[Ingest & Normalize]
    External[(PSP Gateway / Bank Reports)] --> IngestB[Ingest & Normalize]
    IngestA --> Matcher[Automated Matching Engine]
    IngestB --> Matcher
    Matcher -->|Matched Pairs| Balanced[(Reconciled Journal Store)]
    Matcher -->|Discrepancies| Exceptions[(Exception Triage Queue)]
    Exceptions --> Investigate[Investigation & Root Cause Analysis]
    Investigate --> Adjust[Adjustment Approval Workflow: 4-Eyes]
    Adjust --> Balanced
```

---

## 3. Production Invariants
- Never use fuzzy matching for financial transaction reconciliation; matching must be deterministic and rule-governed.
- All reconciliation exceptions must be tracked in an auditable exception queue with SLA-driven resolution targets.
- Adjustments and ledger write-offs must enforce strict four-eyes authorization controls.
