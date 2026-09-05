# PCI-DSS Zero-Scope Reference Architecture

## 1. Architectural Blueprint

```
                  [Customer Browser / Mobile App]
                                 │
           ┌─────────────────────┴─────────────────────┐
           ▼                                           ▼
[Non-CDE Application Server]                [PCI Level 1 Token Vault]
├── React / Next.js Web App                 ├── Hosted Iframe Fields
├── Product Catalog Service                 ├── Tokenization Engine
└── Shopping Cart Database                  └── HSM-Backed Storage
           │                                           │
           │ <────────── Returns Token ────────────────┘
           │      ("tok_visa_4111_9918")
           ▼
[Payment Orchestration Service]
           │ (Transmits Token + Amount)
           ▼
[Acquiring Bank / Payment Processor (Stripe/Adyen)]
```

## 2. Compliance Evaluation
Under this architecture, the merchant platform processes only surrogate tokens, reducing compliance obligations to SAQ A and eliminating application databases from PCI-DSS Level 1 scope.
