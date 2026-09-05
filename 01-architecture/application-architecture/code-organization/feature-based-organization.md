# Feature-Based Code Organization (Screaming Architecture)

## 1. The Core Philosophy

Robert C. Martin coined the term **Screaming Architecture**:
> *When you look at the top-level directory of a codebase, it should scream what the business does (Orders, Invoices, Customers), not what technical framework it uses (Controllers, Views, Models).*

---

## 2. Directory Layout Comparison

```
Layer-Based (Technical):
controllers/
  OrderController.cs
  UserController.cs
services/
  OrderService.cs
  UserService.cs

Feature-Based (Business Domain):
features/
  orders/
    PlaceOrderEndpoint.cs
    PlaceOrderHandler.cs
    Order.cs
    OrderRepository.cs
  users/
    RegisterUserEndpoint.cs
    RegisterUserHandler.cs
    User.cs
```
In feature-based organization, an engineer working on "Orders" never has to hunt across 10 unrelated folders.
