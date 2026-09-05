# Data Ownership Extraction & Shared Database Decoupling

## 1. The Single Data Ownership Rule
In a microservices architecture, **a database table must be owned by exactly one service**. No external service may read or write to that table directly; all data access must occur through the owner service's authorized API or asynchronous events.

---

## 2. Decoupling Shared Tables: Foreign Key Breaking

```
Before Extraction: Monolithic Database
┌─────────────────────────────────────────────────────────────┐
│  ORDERS TABLE                                               │
│  order_id | customer_id (FK to CUSTOMERS) | total_amount    │
└─────────────────────────────────────────────────────────────┘
                               │
               Step 1: Drop Foreign Key Constraint
               Step 2: customer_id becomes an unconstrained Value Object
               Step 3: Move CUSTOMERS table to independent Customer DB
                               ▼
[Orders Service]                                    [Customer Service]
       │                                                    │
       ▼                                                    ▼
[Orders DB]                                         [Customer DB]
(Stores: customer_id = "CUST-101")                  (Owns: customer_id, name, address)
```

### Handling Cross-Domain Joins
When UI screens require order data joined with customer names:
1. **API Composition**: An edge gateway calls Orders Service, calls Customer Service, and merges the JSON payloads.
2. **Event-Carried State Transfer**: Orders Service listens to `customer.updated` events and caches customer names in a local read replica.
