# API-PAY-001: Enterprise Payment Processing API Specification

---
**Metadata**:
* **Document ID**: API-PAY-001
* **Version**: 1.0.0
* **Status**: Approved
* **Base URL**: `https://api.enterprise.com/v1/payments`
---

## 1. Endpoint: Create Payment Charge
`POST /v1/payments/charges`

### Headers
* `Authorization`: `Bearer <OAuth2_Token>`
* `Idempotency-Key`: `7d4b6845-8c01-4475-b6d8-9472e38c5b08`
* `Content-Type`: `application/json`

### Request Body
```json
{
  "amount": 4999,
  "currency": "USD",
  "customer_id": "cust_12345",
  "payment_method": {
    "type": "card_token",
    "token": "tok_visa_4242"
  },
  "metadata": {
    "order_id": "ord_8877"
  }
}
```

### Response (201 Created)
```json
{
  "charge_id": "chg_99887766",
  "status": "succeeded",
  "amount": 4999,
  "currency": "USD",
  "created_at": "2026-03-15T18:00:00Z"
}
```
