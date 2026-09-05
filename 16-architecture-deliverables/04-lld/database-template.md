# LLD Database Interaction & DDL Specification

## 1. Table Schema (PostgreSQL DDL)
```sql
CREATE TABLE orders (
    order_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL,
    total_amount NUMERIC(12, 2) NOT NULL CHECK (total_amount >= 0),
    currency VARCHAR(3) NOT NULL,
    status VARCHAR(32) NOT NULL,
    version INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status) WHERE status = 'PENDING_PAYMENT';
```

## 2. Concurrency Locking Strategy
* Updates to order status use **Optimistic Locking** with an incrementing `version` column:
  `UPDATE orders SET status = :newStatus, version = version + 1 WHERE order_id = :id AND version = :currentVersion;`
* If rows affected == 0, raise `OptimisticLockException` and retry up to 3 times.
