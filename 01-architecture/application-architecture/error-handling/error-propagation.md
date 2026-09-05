# Error Propagation Across Service Boundaries

## 1. Propagation Rules
- Contextual enrichment: As errors bubble up layers, enrich them with contextual metadata (e.g., `accountId`, `orderId`) without destroying the underlying root cause.
