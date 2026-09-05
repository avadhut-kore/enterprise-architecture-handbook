# API Error Model (RFC 7807 Problem Details)

All HTTP APIs MUST return standard RFC 7807 Problem Details on 4xx and 5xx responses:

```json
{
  "type": "https://api.enterprise.com/errors/insufficient-funds",
  "title": "Insufficient Funds",
  "status": 422,
  "detail": "Account acc-123 does not have sufficient available balance for this debit.",
  "instance": "/v1/transfers/txn-998",
  "code": "ACC_INSUFFICIENT_FUNDS",
  "timestamp": "2026-03-15T12:00:00Z",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "invalid_params": [
    {
      "name": "amount",
      "reason": "Requested amount 1500.00 exceeds balance 230.50"
    }
  ]
}
```
