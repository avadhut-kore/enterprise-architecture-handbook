# System Design Interview: Data Modeling & Schema Design

## 1. Defining the Relational vs NoSQL Stance

When designing the storage tier, justify your selection based on access patterns:
- **Choose Relational (PostgreSQL, MySQL)**: When strong consistency, complex queries, foreign key guarantees, or financial ACID transactions are mandatory.
- **Choose NoSQL (Cassandra, DynamoDB, MongoDB)**: When data has simple key-value or wide-column access patterns, write throughput exceeds single-node limits, and eventual consistency is acceptable.

---

## 2. Schema Specification & Shard Key Selection

Always document:
1. **Table / Collection Schema**: Explicit data types and primary keys.
2. **Access Patterns**: What queries will be executed against these tables?
3. **Partition / Shard Key**: Which attribute guarantees uniform distribution without cross-partition joins?

```sql
-- PostgreSQL Example: User Orders
CREATE TABLE orders (
    order_id UUID PRIMARY KEY,
    user_id UUID NOT NULL,            -- Shard Key
    total_cents BIGINT NOT NULL,
    status VARCHAR(32) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL,
    version INT NOT NULL DEFAULT 1    -- Optimistic Locking
);

CREATE INDEX idx_orders_user_created ON orders (user_id, created_at DESC);
```
