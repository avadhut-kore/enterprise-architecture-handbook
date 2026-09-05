# Dependency Error Handling

## 1. Error Translation at Adapters
When an external service returns an error:
- Do not let AWS, Stripe, or Postgres exceptions leak into domain logic.
- Translate low-level exceptions into domain-meaningful errors inside the Infrastructure Adapter.
