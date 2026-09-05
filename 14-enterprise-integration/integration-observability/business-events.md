# Business Event Tracking and Activity Monitoring (BAM)

## 1. Technical Logs vs. Business Events
- **Technical Log**: "HTTP 200 POST /v1/settlements duration=120ms". Useful for site reliability engineers, useless for CFOs.
- **Business Event**: "Payment `$50,000` settled for Merchant `Acme Corp` via `SWIFT` with fee `$15.00`".

## 2. Business Activity Monitoring (BAM) Architecture

```
[Integration Pipeline] ──> [Emit CloudEvent: enterprise.payment.settled]
                                    │
                                    ▼
                         [Kafka Event Stream]
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
     [Real-Time Analytics / Flink]        [Data Lake / Iceberg]
                    │                               │
     [Executive Revenue Dashboard]        [Financial Audit Reports]
```

## 3. Canonical Business Event Envelope (CloudEvents Specification)
```json
{
  "specversion": "1.0",
  "type": "com.enterprise.banking.payment.settled",
  "source": "/core/settlement-engine",
  "id": "EVT-8819201",
  "time": "2026-09-05T12:45:00Z",
  "datacontenttype": "application/json",
  "data": {
    "transaction_id": "TX-109281",
    "amount": 50000.00,
    "currency": "USD",
    "sender_account": "ACC-99182",
    "recipient_account": "ACC-44129",
    "settlement_rail": "FEDNOW"
  }
}
```
