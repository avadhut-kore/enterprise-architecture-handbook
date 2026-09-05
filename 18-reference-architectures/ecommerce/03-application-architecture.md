# Application Architecture: E-Commerce Platform

## 1. Flash-Sale Inventory Reservation Pattern
To prevent database locking during high-concurrency checkout bursts:
1. When user clicks "Proceed to Checkout", the Cart Service executes an atomic **Lua Script** on Redis.
2. The script checks available stock and decrements the counter in-memory.
3. A temporary reservation key is created with a **10-minute Time-To-Live (TTL)**: `reservation:{user_id}:{sku_id}`.
4. If the customer completes payment within 10 minutes, the order is confirmed and the permanent warehouse ledger is updated asynchronously.
5. If the 10-minute TTL expires without payment, a Redis keyspace notification automatically increments the stock counter back, returning items to the pool without human intervention.
