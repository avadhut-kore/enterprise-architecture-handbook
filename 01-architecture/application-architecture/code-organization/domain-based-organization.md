# Domain-Based Organization

## 1. Aligning Code with DDD Bounded Contexts

```text
src/
├── Ordering/                   # Bounded Context 1
│   ├── Domain/                 # Pure Order aggregates, value objects
│   ├── Application/            # Order use cases
│   └── Infrastructure/         # Order persistence
├── Billing/                    # Bounded Context 2
│   ├── Domain/                 # Pure Billing entities
│   ├── Application/            # Invoice generation
│   └── Infrastructure/         # Payment gateway adapters
└── SharedKernel/               # Minimal shared primitives (Currency, Money)
```
