# HLD-ECOM-001: Checkout Subsystem High-Level Design
* **Service Boundary**: Manages cart validation, promo codes, tax calculation, and payment capture.
* **Resilience**: Redis-backed distributed lock checking `Idempotency-Key` on all checkouts.
