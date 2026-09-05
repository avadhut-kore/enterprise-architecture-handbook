# System Design Interview: API Architecture

## 1. Expected Interface Deliverables

In Staff+ interviews, write out concrete HTTP / gRPC method signatures for the core features.

### Example: E-Commerce Order Placement
```http
POST /v1/orders
Headers:
  Authorization: Bearer <jwt_token>
  Idempotency-Key: 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d
  Content-Type: application/json

Request Body:
{
  "items": [
    {"product_id": "prod_123", "quantity": 2, "price_cents": 1999}
  ],
  "shipping_address_id": "addr_998",
  "currency": "USD"
}

Response (HTTP 201 Created):
{
  "order_id": "ord_8837194",
  "status": "PENDING_PAYMENT",
  "total_cents": 3998,
  "created_at": "2026-09-05T12:00:00Z"
}
```

---

## 2. Key Architecture Signals to Demonstrate

- Mention **Idempotency Keys** proactively for non-idempotent writes.
- Discuss **Cursor-based Pagination** (`limit` and `starting_after`) over offset-based pagination for large datasets.
- Address **Error Handling** adhering to RFC 7807 standards.
