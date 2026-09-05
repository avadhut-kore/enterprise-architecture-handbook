# Real-Time Fraud and Sanctions Screening Integration

## 1. Inline Fraud Interception Pattern
Card authorizations and payment transfers must be screened in real-time before transaction commitment:

```
[Payment Authorization Ingress] (Total SLA: 500ms)
              │
              ├─ Step 1: Pre-auth validation (20ms)
              ├─ Step 2: Inline Fraud Engine (POST /v1/eval, SLA: 80ms)
              │          ├── Device Fingerprint
              │          ├── Behavioral AI Risk Score (0 - 1000)
              │          └── OFAC / PEP Sanctions List Match
              │
              ▼
    (Risk Score > 750?)
              │
              ├── YES ──> [Reject / Step-Up MFA Required]
              └── NO  ──> [Forward to Core Ledger]
```
