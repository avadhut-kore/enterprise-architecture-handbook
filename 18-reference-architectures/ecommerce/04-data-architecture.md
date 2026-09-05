# Data Architecture: E-Commerce Platform

## 1. Polyglot Persistence Model
- **Product Catalog (OpenSearch)**: Full-text search, faceted navigation (color, size, brand), and real-time typo tolerance.
- **Inventory Counters (Redis Cluster)**: In-memory atomic counters partitioned by `sku_id` hash tags (`{sku_101}`).
- **Order System of Record (PostgreSQL Aurora)**: ACID transactional store managing orders, line items, shipping addresses, and payment tokens.

---

## 2. Order Database Schema (DDL Snippet)
```sql
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL,
    status VARCHAR(50) NOT NULL, -- PENDING_PAYMENT, PAID, FULFILLING, SHIPPED, CANCELLED
    subtotal NUMERIC(10, 2) NOT NULL,
    tax_amount NUMERIC(10, 2) NOT NULL,
    shipping_amount NUMERIC(10, 2) NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    created_at TIMESTAMPTZ DEFAULT clock_timestamp()
);

CREATE TABLE order_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL REFERENCES orders(id),
    sku VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL
);
```
