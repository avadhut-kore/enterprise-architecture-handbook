# Payment Initiation and Ingress Gateway

## 1. Ingress Security & Idempotency
Payment initiation handles checkout requests originating from public internet clients. It enforces:
- WAF payload sanitization.
- Mandatory `Idempotency-Key` verification against Redis cluster.
- Rate limiting per API key / IP address.
- Decoupling payment initiation from asynchronous settlement.

## 2. Initiation Request Specification
```http
POST /v1/payments HTTP/1.1
Host: payments.enterprise.internal
Content-Type: application/json
Idempotency-Key: pay_req_9928172810
Authorization: Bearer eyJhbGciOiJ...

{
  "amount": 12500,
  "currency": "USD",
  "payment_method": {
    "type": "token",
    "token_id": "tok_visa_881928"
  },
  "customer_id": "cust_10928",
  "order_reference": "ORD-2026-9912",
  "capture_method": "AUTOMATIC"
}
```
