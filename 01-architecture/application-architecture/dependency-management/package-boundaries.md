# Package Boundaries & Packaging Strategies

## 1. Package-by-Layer vs Package-by-Feature

```
Package-by-Layer (Weak Boundaries):
com.company.app
├── controllers (OrderController, UserController, BillingController)
├── services    (OrderService, UserService, BillingService)
└── repositories(OrderRepository, UserRepository, BillingRepository)
(Changes to 'Orders' touch every package; high risk of leaking internals)

Package-by-Feature / Component (Strong Boundaries):
com.company.app
├── orders
│   ├── OrderController
│   ├── internal (OrderService, OrderRepository, OrderEntity)
│   └── public   (IOrderFacade, OrderDto)
└── billing
```
Package-by-feature enables strong encapsulation and simplified modular monolith architecture.
