# Core Reconciliation Architecture and Frameworks

## 1. The Four-Stage Reconciliation Pipeline

```
[System A Data Feed]    [System B Data Feed]
          │                       │
          └───────────┬───────────┘
                      ▼
            [Stage 1: Normalization]
            (Format conversion, currency alignment, timestamp UTC)
                      │
                      ▼
            [Stage 2: Matching Engine]
            (Exact key match, tolerance window, fuzzy rule execution)
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     [Matched]              [Breaks / Discrepancies]
                                  │
                                  ▼
                        [Stage 3: Auto-Resolution]
                        (Compensating entries, retries)
                                  │
                                  ▼
                        [Stage 4: Case Management]
                        (Human review for remaining breaks)
```
