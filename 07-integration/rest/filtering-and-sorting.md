# Filtering, Sorting & Field Selection

## 1. Filtering Syntax Standards
* Simple equality: `GET /v1/orders?status=shipped&customer_id=42`
* Range queries: `GET /v1/orders?created_at[gte]=2026-01-01&created_at[lte]=2026-03-31`
* Multiple values (IN clause): `GET /v1/orders?status=in:pending,processing,shipped`

---

## 2. Sorting & Sparse Fieldsets
* **Sorting**: Use `-` prefix for descending order:
  `GET /v1/products?sort=-price,rating` (Order by price DESC, then rating ASC).
* **Sparse Fieldsets (Field Projection)**: Allow clients to request only needed columns to minimize bandwidth:
  `GET /v1/users?fields=id,name,email`
