# PCI-DSS Trust Boundaries and Data Flow Diagrams

## 1. Data Flow Modeling (Requirement 1.2.4)
PCI-DSS requires up-to-date data flow diagrams showing all Cardholder Data ingestion, transmission, storage, and egress paths.

```
[Customer Browser] ──(PAN entered into Hosted Field)──> [Third-Party Gateway]
                                                              │
[Merchant Backend] ◄────── (Returns Surrogate Token) ─────────┘
        │
        ▼ (Stores Token in PostgreSQL DB)
[Out-of-Scope Merchant Database]
```
