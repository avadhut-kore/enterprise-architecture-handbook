# Reference Architecture: Angular Enterprise Architecture (Nx Monorepo)

## 1. Architectural Vision & Enterprise Context
Enterprise workspace architecture organized into feature, ui, data-access, and util libraries using standalone components, Signals, and NgRx state management.

---

## 2. Component & Boundary Blueprint

```mermaid
flowchart TD
    subgraph Presentation / Interface
        API[API Controllers / UI Views]
        DTO[Input DTOs & Validation]
    end
    subgraph Application Layer
        Commands[Use Case / Command Handlers]
        Queries[Query Handlers]
    end
    subgraph Domain Layer
        Entities[Domain Entities & Aggregates]
        ValueObjects[Value Objects]
        Events[Domain Events]
    end
    subgraph Infrastructure Layer
        Persistence[Persistence / ORM Repositories]
        External[External System Clients]
    end

    API --> Commands
    API --> Queries
    Commands --> Entities
    Queries --> Persistence
    Persistence --> Entities
    Commands --> Infrastructure
    Commands --> External
```

---

## 3. Core Architectural Invariants
- Dependencies point inward toward the Domain Core.
- Framework dependencies are prohibited from polluting core business models.
- Verification rules and automated fitness functions enforce module boundaries on every commit.
