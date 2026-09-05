# Chargebacks, Disputes, and Fraud Integration

## 1. The Dispute Lifecycle
```
[Customer Disputes Charge with Issuer]
                   │
                   ▼
       [Issuer Emits Chargeback Event] ──> [Acquirer Webhook]
                   │                              │
                   ▼                              ▼
      [Merchant Notified: Status DISPUTED] ◄──────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
   [Accept Dispute]      [Defend Dispute (Representment)]
   (Funds debited        (Submit proof of delivery, IP logs, signed receipts)
    plus dispute fee)
```
