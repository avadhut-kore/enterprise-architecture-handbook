# API Error Model: RFC 7807 Problem Details

## 1. Standard Error Payload
Standardize all HTTP API error responses using RFC 7807:
```json
{
  "type": "https://api.company.com/errors/insufficient-funds",
  "title": "Insufficient Funds",
  "status": 422,
  "detail": "Account balance $120.00 is insufficient for $500.00 withdrawal.",
  "instance": "/accounts/1234/withdrawals",
  "traceId": "00-4bf92f3577b34da6a3ce929d0e0e4736"
}
```
