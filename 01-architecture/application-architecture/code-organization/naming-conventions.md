# Architectural Naming Conventions & Ubiquitous Language

## 1. Naming Guidelines
- Use domain terms from the business Ubiquitous Language: name a class `UnderwritingPolicy`, not `PolicyDataProcessorManager`.
- DTOs should clearly convey purpose: `CreateOrderCommand`, `OrderSummaryResponse`.
- Interfaces should describe capabilities (`IOrderReader`, `IPaymentGateway`), not generic prefixes (`IOrderService`).
