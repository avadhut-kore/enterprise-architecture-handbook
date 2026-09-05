# Distributed Design Principle: High Cohesion

## 1. Core Principle Definition

Cohesion refers to the degree to which elements within a single module or microservice belong together functionally and contextually.

**High Cohesion** dictates that a service should encapsulate closely related business responsibilities within a well-defined Domain-Driven Design (DDD) Bounded Context: things that change together must live together.

---

## 2. Cohesion Spectrum

```
Low Cohesion (Antipattern - "Utility" or "Generic" Services):
[ CommonHelperService ]
├── Generates User Invoices
├── Calculates Shipping Taxes
└── Crops Profile Images
(Changes for completely unrelated reasons; high churn and bug frequency)

High Cohesion (Target):
[ BillingService ]
├── Evaluates Invoices
├── Manages Subscriptions
└── Applies Discounts
(Dedicated solely to the financial billing bounded context)
```

---

## 3. Architectural Rules of Thumb

- If modifying a single business feature requires modifying and redeploying 5 different microservices, your architecture exhibits **low cohesion and high coupling** (a distributed monolith).
