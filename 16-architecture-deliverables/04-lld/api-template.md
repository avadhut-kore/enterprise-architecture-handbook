# LLD API Controller & DTO Specification

## 1. Endpoint Contract
* **HTTP Method & Path**: `POST /api/v1/orders`
* **Headers**:
  - `Content-Type: application/json`
  - `Idempotency-Key: <UUIDv4>`
  - `Authorization: Bearer <JWT>`

## 2. Request & Response Payload DTOs
```json
// POST /api/v1/orders Request Body
{
  "customer_id": "8f6b8b20-1b5e-4c3d-98e3-0d5b6e7a8f9c",
  "items": [
    {
      "sku": "SKU-PRO-001",
      "quantity": 2,
      "unit_price": 49.99
    }
  ]
}

// 201 Created Response Body
{
  "order_id": "a3f5e8d9-2c1b-4a5f-8e7d-9c8b7a6f5e4d",
  "status": "PENDING_PAYMENT",
  "total_amount": 99.98,
  "currency": "USD",
  "created_at": "2026-03-15T14:22:10Z"
}
```
