# C4 Level 3: Component Diagram

The **Component Diagram** decomposes an individual container into its internal structural components (modules, controllers, service handlers, repository interfaces, adapters) and illustrates their dependencies.

## When to Use
- Detailed Technical Design Documents (TDDs) and team sprint planning.
- Enforcing Clean Architecture, Hexagonal (Ports & Adapters), or Modular Monolith boundaries.
- Refactoring complex services with high cyclomatic complexity.

---

## Architecture Example: Order Execution Service Components

```mermaid
flowchart TD
    subgraph Container["Order Execution Service (Container: Spring Boot)"]
        OrderController["Order REST Controller
[Component: Spring Web]
Exposes HTTP endpoints for order placement, cancellation, and status."]
        SecurityFilter["JWT Security Filter
[Component: Spring Security]
Validates Bearer tokens and extracts client principal/roles."]
        
        OrderCommandHandler["Order Command Handler
[Component: Application Service]
Coordinates order validation, idempotency checks, and state transitions."]
        RiskEngineAdapter["Pre-Trade Risk Evaluator
[Component: Domain Service]
Asserts purchasing power, margin limits, and sanctions compliance."]
        
        FixProtocolAdapter["FIX Exchange Gateway Adapter
[Component: Outbound Adapter]
Serializes orders to FIX 4.4 messages and handles socket connections."]
        EventPublisher["Kafka Event Publisher
[Component: Infrastructure Adapter]
Publishes transactional domain events to external Kafka topics."]
        OrderRepository["Order Repository Interface
[Component: Spring Data JPA]
Provides CRUD operations and optimistic locking on order entities."]
    end

    subgraph ExternalDeps["External Container Dependencies"]
        DB["PostgreSQL Order Store"]
        Kafka["Kafka Event Bus"]
        FIX["External Exchange FIX Engine"]
    end

    OrderController --> SecurityFilter
    SecurityFilter --> OrderCommandHandler
    OrderCommandHandler --> RiskEngineAdapter
    OrderCommandHandler --> FixProtocolAdapter
    OrderCommandHandler --> EventPublisher
    OrderCommandHandler --> OrderRepository

    OrderRepository -->|JDBC / SQL| DB
    EventPublisher -->|Kafka Producer API| Kafka
    FixProtocolAdapter -->|TCP / FIX Socket| FIX
```

---

## Related References
- [Component Template](./component-template.md)
- [Application Architecture Diagrams](../application/README.md)
