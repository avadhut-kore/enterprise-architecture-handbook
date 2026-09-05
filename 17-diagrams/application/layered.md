# Layered Architecture (N-Tier Structural Model)

Traditional enterprise layered architecture detailing strict separation of concerns across Presentation, Business Logic, Persistence, and Database tiers.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph PresentationTier ["1. Presentation / Ingress Layer"]
        Controllers["REST Controllers / GraphQL Resolvers"]
        DTOs["Request / Response DTOs & Validation"]
        Controllers --- DTOs
    end

    subgraph ApplicationTier ["2. Application / Business Logic Layer"]
        Services["Domain Services & Workflows"]
        BusinessRules["Business Invariants & Calculations"]
        Services --- BusinessRules
    end

    subgraph DataAccessTier ["3. Data Access / Persistence Layer"]
        DAOs["Data Access Objects (DAOs) / ORM Mappings"]
        Repositories["Spring Data / Entity Framework Repos"]
        DAOs --- Repositories
    end

    subgraph DatabaseTier ["4. Persistent Storage Layer"]
        RDBMS[(Relational Database / Postgres)]
    end

    Controllers -->|"Invokes Service Interface"| Services
    Services -->|"Queries / Persists Entities"| Repositories
    Repositories -->|"SQL Queries / JDBC"| RDBMS
```

## PlantUML Specification

```plantuml
@startuml
package "Presentation Layer" {
  [REST Controllers]
}
package "Business Layer" {
  [Domain Services]
}
package "Persistence Layer" {
  [Repositories / DAOs]
}
database "Relational DB" as db

[REST Controllers] --> [Domain Services] : Call
[Domain Services] --> [Repositories / DAOs] : Persist
[Repositories / DAOs] --> db : SQL
@enduml
```

## Architectural Design Considerations

* **Strict vs Relaxed Layering**: In strict layering, a layer can only call the layer immediately below it; relaxed layering permits calling deeper layers directly.
* **Leakage of Concerns**: Prevent persistence annotations and SQL semantics from leaking into presentation controllers.
* **Testing Simplicity**: Each layer can be mocked independently during unit and integration test suites.

## Related Documentation & Patterns

* [Clean Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/clean.md)
* [Hexagonal Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/hexagonal.md)
* [Modular Monolith](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/application/modular-monolith.md)
