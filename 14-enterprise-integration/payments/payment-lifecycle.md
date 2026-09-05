# End-to-End Payment Lifecycle and State Transitions

## 1. Payment Finite State Machine (FSM)

```
                     ┌──────────────────┐
                     │    INITIATED     │
                     └─────────┬────────┘
                               │
                 Authorize     ▼
                     ┌──────────────────┐
            ┌────────┤    AUTHORIZED    ├────────┐
            │        └─────────┬────────┘        │
      Void  │                  │ Capture         │ Expire / Cancel
            ▼                  ▼                 ▼
     ┌─────────────┐   ┌────────────────┐   ┌─────────────┐
     │   VOIDED    │   │    CAPTURED    │   │   EXPIRED   │
     └─────────────┘   └───────┬────────┘   └─────────────┘
                               │
                     Settle    ▼
                       ┌────────────────┐
                       │    SETTLED     │
                       └───────┬────────┘
                               │
                  Refund /     ▼
                Chargeback ┌────────────────┐
                           │    REFUNDED    │
                           └────────────────┘
```

## 2. Phase Operational Definitions
- **Authorization**: Places a temporary hold against the customer's available credit or funds. No money moves yet.
- **Capture**: Confirms the merchant's intent to collect the authorized funds (e.g., upon goods shipment).
- **Clearing**: Exchange of transaction details between acquirer and issuer through card network batch files.
- **Settlement**: The physical transfer of funds from the cardholder's bank to the merchant's bank account.
