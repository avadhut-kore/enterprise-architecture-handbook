# DATA-ECOM-001: Orders & Outbox PostgreSQL Schema
* `orders` table with UUIDv7 primary keys and optimistic locking `@Version` column.
* `outbox_events` table written atomically in the same database transaction.
