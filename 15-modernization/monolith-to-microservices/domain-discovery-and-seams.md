# Domain Discovery and Architectural Seams

## 1. Finding Architectural Seams
An **architectural seam** is a boundary in a codebase where behavior can be modified or extracted without editing the internal source code of surrounding modules (Michael Feathers).

```
Tangled Monolith Codebase
┌─────────────────────────────────────────────────────────────┐
│  OrderController                                            │
│    │                                                        │
│    ├──► Direct DB Query: SELECT * FROM customers...         │
│    ├──► In-Memory Call: PaymentManager.chargeCreditCard()   │
│    └──► Direct File Write: /var/log/audit.log               │
└─────────────────────────────────────────────────────────────┘
                               │
            Introduce Seam: Interface & Inversion of Control
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  OrderService ──► [IPaymentProcessor Interface]            │
│                         ▲                     ▲             │
│                         │ (Seam 1)            │ (Seam 2)    │
│        [Legacy In-Memory Adapter]   [Remote HTTP Adapter]   │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Domain-Driven Design (DDD) Bounded Contexts
1. **Event Storming Workshop**: Bring domain experts and developers together to plot all domain events on a chronological timeline.
2. **Context Mapping**: Identify Ubiquitous Language boundaries. For example, "Account" means something completely different to the Billing department (credit balance) vs. the Security department (login credentials). Each distinct meaning defines a candidate Bounded Context.
