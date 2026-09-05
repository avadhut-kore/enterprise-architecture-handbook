# Business Capability Decomposition

How to decompose macro enterprise domains into discrete, actionable Level-2 and Level-3 capabilities.

---

## 1. Deep Decomposition Example: Financial Institution

```text
1.0 CUSTOMER MANAGEMENT (Level 1)
├── 1.1 Customer Acquisition (Level 2)
│   ├── 1.1.1 Lead Ingestion & Qualification (Level 3)
│   ├── 1.1.2 Product Recommendation & Quoting (Level 3)
│   └── 1.1.3 Referral Tracking (Level 3)
├── 1.2 Customer Onboarding & KYC (Level 2)
│   ├── 1.2.1 Identity Document Verification (Level 3)
│   ├── 1.2.2 Anti-Money Laundering (AML) Screening (Level 3)
│   ├── 1.2.3 Credit Bureau Scoring (Level 3)
│   └── 1.2.4 Account Contract Signing (Level 3)
├── 1.3 Customer Servicing (Level 2)
│   ├── 1.3.1 Inbound Omnichannel Contact Routing (Level 3)
│   ├── 1.3.2 Dispute & Chargeback Intake (Level 3)
│   └── 1.3.3 Self-Service Profile Management (Level 3)
└── 1.4 Customer Insights & Loyalty (Level 2)
    ├── 1.4.1 Behavioral Churn Prediction (Level 3)
    └── 1.4.2 Loyalty Points Ledger Management (Level 3)
```

---

## 2. Capability Boundary Diagnostic Questions

When testing whether a capability has been properly isolated:
* Can this capability be completely outsourced to a third-party vendor without breaking our internal operating model? (If yes, it is an independent capability).
* Can we change the software supporting this capability without requiring changes to adjacent systems? (If no, the boundary may be leaky).
* Does this capability have a single identifiable executive business owner? (If multiple owners fight for control, it is likely two conflated capabilities).
