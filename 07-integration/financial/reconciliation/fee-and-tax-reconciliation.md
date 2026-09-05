# Reconciliation Architecture: Fee & Tax Reconciliation Architecture

## 1. Architectural Purpose & Problem Context
Validating processor interchange-plus billing against contractual rate cards; identifying overbilled gateway transaction fees.

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
