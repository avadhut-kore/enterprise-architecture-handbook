# Event-Driven Architecture (EDA) in Core Banking

## 1. Domain Event Topologies
Core banking state changes must be published as durable domain events using the Outbox pattern:
- `account.opened`
- `balance.debited`
- `fraud.alert.raised`
- `loan.defaulted`

## 2. Outbox CDC Pattern with Debezium
```sql
-- Transactional commit inside Core DB
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 'ACC-101';
  INSERT INTO outbox_events (id, aggregate_type, event_type, payload)
  VALUES (gen_random_uuid(), 'ACCOUNT', 'DEBIT_POSTED', '{"amount": 100}');
COMMIT;
-- Debezium CDC streams outbox_events row to Kafka topic: account.events
```
