# Order-to-Cash (O2C) Integration Architecture

## 1. End-to-End O2C Lifecycle

```
[E-Commerce / CRM] ──> 1. Sales Order Placed
                             │
                             ▼
     [ERP System]  ──> 2. Credit Check & Inventory Allocation
                             │
                             ▼
  [Warehouse / WMS]──> 3. Picking, Packing, & Goods Issue
                             │
                             ▼
     [ERP System]  ──> 4. Customer Invoice Generated (FI-AR)
                             │
                             ▼
 [Payment Gateway] ──> 5. Cash Collection & Auto-Clearing
```

## 2. Key Architectural Risks in O2C
- **Inventory Over-Allocation**: High-concurrency checkout requires distributed reservation locks in Redis prior to ERP order commitment.
- **Credit Limit Contention**: Multiple concurrent orders from a single corporate buyer must serialize credit exposure checks.
