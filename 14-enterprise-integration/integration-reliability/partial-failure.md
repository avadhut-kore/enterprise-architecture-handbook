# Partial Failure and Distributed Degradation

## 1. The Anatomy of Partial Failure
In multi-system integration pipelines, some components succeed while others fail. For example, in an e-commerce checkout orchestration:
- Inventory Reservation: **SUCCEEDED**
- Credit Card Charge: **SUCCEEDED**
- Loyalty Points Accrual: **FAILED (Timeout)**
- Email Confirmation: **FAILED (Service Down)**

Crashing the entire checkout transaction due to a failed loyalty point update is an architectural anti-pattern.

## 2. Tiers of Criticality Pattern
Categorize integration dependencies into strict criticality tiers:
- **Tier 1 (Hard Dependency)**: Critical path. If Inventory or Payment fails, rollback transaction immediately.
- **Tier 2 (Soft Dependency)**: Non-critical. If Loyalty Points fail, stash event in background outbox table and proceed with checkout completion.
- **Tier 3 (Informational)**: Fire-and-forget. If Email dispatch fails, write to async queue for best-effort retry.
