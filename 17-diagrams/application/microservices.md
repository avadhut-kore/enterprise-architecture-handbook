# Microservices Architecture & Decentralized Data

Autonomous, loosely coupled microservices architecture featuring independent deployability, decentralized data ownership, and API gateway composition.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph ClientZone ["External Clients"]
        Web["Web Portal"]
        Mobile["Mobile App"]
    end

    subgraph GatewayZone ["Ingress & Routing"]
        APIGW["API Gateway (Routing, Rate Limiting, AuthN)"]
        Web --> APIGW
        Mobile --> APIGW
    end

    subgraph MicroservicesCluster ["Autonomous Microservices (EKS)"]
        subgraph UserContext ["User Bounded Context"]
            UserSvc["User Service"]
            UserDB[("User DB (Postgres)")]
            UserSvc --> UserDB
        end

        subgraph OrderContext ["Order Bounded Context"]
            OrderSvc["Order Service"]
            OrderDB[("Order DB (Postgres)")]
            OrderSvc --> OrderDB
        end

        subgraph InventoryContext ["Inventory Bounded Context"]
            InvSvc["Inventory Service"]
            InvDB[("Inventory DB (MongoDB)")]
            InvSvc --> InvDB
        end

        APIGW --> UserSvc
        APIGW --> OrderSvc
        APIGW --> InvSvc
    end

    subgraph AsyncEventBus ["Asynchronous Event Mesh"]
        Kafka["Kafka Event Broker<br/>(orders.v1, inventory.v1)"]
        OrderSvc -->|"Emit Events"| Kafka
        Kafka -->|"Consume Events"| InvSvc
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Clients" {
  [Web Client] --> [API Gateway]
}
package "Microservices" {
  [API Gateway] --> [User Service]
  [API Gateway] --> [Order Service]
  [API Gateway] --> [Inventory Service]
}
package "Decentralized Databases" {
  database "User DB" as db1
  database "Order DB" as db2
  database "Inventory DB" as db3
  [User Service] --> db1
  [Order Service] --> db2
  [Inventory Service] --> db3
}
queue "Kafka Bus" as kafka
[Order Service] --> kafka
kafka --> [Inventory Service]
@enduml
```

## Architectural Design Considerations

* **Database-per-Service**: Each microservice owns its private data store; direct cross-service database access is strictly prohibited.
* **Decoupled Deployments**: Any microservice can be built, tested, and deployed to production independently without synchronizing with other teams.
* **Distributed Governance**: Teams choose appropriate programming languages and database engines suited to their specific domain requirements.

## Related Documentation & Patterns

* [Modular Monolith](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/modular-monolith.md)
* [Event-Driven Application](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/event-driven.md)
* [C4 Container](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/c4/container.md)
