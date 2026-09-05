# Mermaid Class Diagrams & Object Models

Class diagrams represent domain aggregate structures, design patterns, and entity relationships in Object-Oriented and Domain-Driven Design (DDD).

## Domain-Driven Design (DDD) Aggregate Model

```mermaid
classDiagram
    class OrderAggregate {
        +UUID orderId
        +CustomerId customerId
        +Money orderTotal
        +OrderStatus status
        +addItem(Item item, int qty)
        +cancelOrder(String reason)
        +markPaid()
    }

    class OrderItem {
        +UUID itemId
        +String sku
        +int quantity
        +Money unitPrice
    }

    class OrderStatus {
        <<enumeration>>
        PENDING
        PAID
        CANCELLED
        SHIPPED
    }

    class OrderRepository {
        <<interface>>
        +findById(UUID id) OrderAggregate
        +save(OrderAggregate order) void
    }

    OrderAggregate "1" *-- "many" OrderItem : Composition
    OrderAggregate --> OrderStatus : Has
    OrderRepository ..> OrderAggregate : Persists
```

## Visibility Modifiers
* `+` : Public
* `-` : Private
* `#` : Protected
* `~` : Package / Internal
