# LLD Service & Dependency Injection Specification

## 1. Service Wiring & Beans
```mermaid
classDiagram
    class OrderController {
        -OrderService orderService
        +createOrder(CreateOrderRequest) ResponseEntity
    }
    class OrderService {
        <<interface>>
        +create(OrderCommand) OrderResult
    }
    class OrderServiceImpl {
        -OrderRepository repo
        -EventPublisher publisher
        -PaymentClient paymentClient
        +create(OrderCommand) OrderResult
    }
    class OrderRepository {
        <<interface>>
        +save(Order) Order
        +findById(UUID) Optional~Order~
    }
    
    OrderController --> OrderService
    OrderServiceImpl ..|> OrderService
    OrderServiceImpl --> OrderRepository
```

## 2. Bean Lifecycles & Scopes
* All service implementations are stateless singletons managed by Spring or Guice.
* Scoped objects (UserContext) injected via RequestContextHolder / Go context.Context.
