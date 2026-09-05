# Dual-Writes vs. The Transactional Outbox Pattern

## 1. Why Dual-Writes Invariably Fail
```java
// THE DUAL-WRITE DISASTER PATTERN
public void processOrder(Order order) {
    database.save(order);       // Step 1: Commits to local DB
    kafka.send("orders", order); // Step 2: Network drop! Kafka unreachable!
    // Result: Database has the order, but event bus never heard about it. Permanent data loss.
}
```

---

## 2. The Transactional Outbox Solution
Write both the domain mutation and the event record to the *same local database* within an atomic ACID transaction:
```sql
BEGIN;
  INSERT INTO orders (id, amount, status) VALUES ('ORD-1', 100, 'NEW');
  INSERT INTO outbox_events (id, aggregate_type, payload) VALUES (uuid(), 'ORDER', '{...}');
COMMIT;
-- Debezium CDC reads outbox_events table log and publishes to Kafka with zero dual-write risk
```
